# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatcher 1.0**

---

## 2. Intended Use  

VibeMatcher is a content-based music recommendation system designed for classroom exploration and learning how AI systems make choices. It's **not** a real product—it's a sandbox to understand recommendation algorithms.

**What it does:** Given a user's musical taste (favorite artist, genre, mood, and desired energy level), it scores every song in the catalog and returns the top 5 best matches.

**Who it's for:** Students learning about AI, recommendation systems, and algorithm design.

**Key assumption:** The system assumes that similarity in genre, artist, mood, and energy level predicts what a user will like. It doesn't learn from user behavior or feedback—it only matches profiles to song features.

---

## 3. How the Model Works  

Imagine you tell a DJ your favorite artist, genre, mood, and energy level. The DJ then scores each song by checking:
- "Is it by my favorite artist?" (strong signal)
- "Is it in my favorite genre?" (strong signal)  
- "Does it match my mood?" (medium signal)
- "Is the energy close to what I want?" (strong signal)
- "Is it as acoustic/loud/happy as I like?" (weaker signals)

The DJ combines all these signals into a single score (0–1) for each song, sorts them, and plays the top 5.

**Features we use:**
- From songs: `artist`, `genre`, `mood`, `energy`, `acousticness`, `danceability`, `valence`
- From user: `favorite_artist`, `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

**Scoring formula (in plain language):**
1. Check exact matches for artist (partial substring), genre, and mood (yes/no → 1.0 or 0.0)
2. For energy, calculate how close the song's energy is to the user's target (closer = higher score)
3. For acousticness, reward high values if the user likes acoustic, low values if they don't
4. Include danceability and valence (happyness) as bonus signals
5. Combine all signals with weights (some matter more than others) into a final score
6. Rank by score, highest first

**Weights we use:**
- Artist match: 1.5 (most important)
- Genre match: 1.2
- Energy match: 1.5 (most important)
- Mood match: 1.0
- Acousticness: 1.0
- Danceability: 0.7
- Valence: 0.6

---

## 4. Data  

**Dataset size:** 17 songs in the catalog.

**Genres represented:** pop, rock, lofi, ambient, synthwave, jazz, indie pop, hip-hop, country, classical, electronic, reggae, blues, folk.

**Moods represented:** happy, chill, intense, focused, relaxed, moody, upbeat, nostalgic, sad, dreamy.

**Features captured:**
- Song metadata (title, artist)
- Genre and mood tags
- Numeric attributes: energy (0–1), tempo (50–160 BPM), valence/happiness (0–1), danceability (0–1), acousticness (0–1)

**Limitations of the dataset:**
- Very small (only 17 songs—a real catalog has millions)
- Uneven representation: some genres well-covered (pop, rock, lofi), others scarce (country, blues, folk)
- No temporal metadata (release date, popularity trends)
- No user interaction data (streams, likes, skips)
- No cultural or regional context
- Limited diversity in artist representation (artists appear 1–2 times each)

**Changes made:** Used the provided dataset as-is. No songs added or removed.

---

## 5. Strengths  

**Works well for:**
- Users with strong, clear preferences (e.g., "I love pop and energy level 0.8")
- Matching songs within the same genre/mood cluster
- Finding songs by favorite artists (if they exist in the catalog)
- Balancing multiple preferences (doesn't just pick genre OR mood, it weighs both)

**Patterns it captures correctly:**
- High-energy users get upbeat songs (e.g., "Gym Hero," "Electric Pulse")
- Acoustic lovers get instrumental-heavy tracks (e.g., "Serenade in G," "Coffee Shop Stories")
- Mood matching (chill users get lofi/ambient, intense users get rock/electronic)
- Artist loyalty (if your favorite artist has multiple songs, they score high)

**Intuition-matching moments:**
- A rock + intense + high-energy profile correctly ranks "Storm Runner" high
- An ambient + chill + low-energy profile correctly prioritizes "Spacewalk Thoughts" and "Library Rain"
- An acoustic + relaxed user gets jazz and folk over electronic

---

## 6. Limitations and Bias

**Major limitations:**

1. **No discovery outside preferences:** If you love indie pop, you'll never see classical music—even if it might match your energy and mood. The system locks onto genre.

2. **Artist over-weighting:** Because artist match has high weight (1.5), users get stuck recommending the same artists. If your favorite artist only has 2 songs, you get those 2 immediately.

3. **Tiny, skewed dataset:** With only 17 songs and uneven genre representation, the system can't fairly serve users who like underrepresented genres (country, blues, classical).

4. **Binary categorical matching:** The system treats "liked your favorite artist" as a hard yes/no. A song by a *similar* artist scores 0, even if it might be a great match.

5. **No user feedback loop:** The system can't learn that you actually skip the danceability recommendations. It will keep suggesting them.

6. **Assumes independence:** The model treats each feature independently. It doesn't know that "happy + acoustic" often go together in the real world, or that "intense + relaxed" might be contradictory.

**Biases and unfairness (Discovered During Experiments):**
The overarching problem with VibeMatcher is that its scoring calculation strictly penalizes user experimentation due to the exact matching rules (e.g., `genre_score` is explicitly restricted to 1.0 or 0.0). During the "Small Data Experiment," the system punished related genres; a user who requested Country music was entirely blocked from receiving overlapping Folk recommendations simply because the genre string ("country" vs. "folk") wasn't mathematically identical. This binary rigidity forces users into extreme "Filter Bubbles" where they only receive literal matches. 

Additionally, because the "energy gap" calculation strongly prioritizes closeness (`1.0 - abs(diff)`), users who don't manually set a target energy inherit the song's native energy as their score. This inherently biases the fallback algorithm to recommend aggressively high-energy, high-danceability Pop/Hip-hop tracks to any "undecided" users, completely alienating users of slower genres like Ambient or Blues simply because their base features are naturally lower scores.

**Genre & Artist bias:** Users of underrepresented genres (country, blues) get fewer good recommendations because there aren't enough songs to choose from. Meanwhile, pop fans are spoiled for choice.
- **Mood bias:** The system might over-recommend happy, upbeat songs because valence and danceability are always included in scoring. Sadder moods could be undervalued.
- **Feature bias:** The model treats mood and energy as user-specifiable, but some users might not know their target energy level. Missing this preference means their recommendations are less personalized.

**Unexpected failures:**

- A user who likes both "chill" and "intense" music (e.g., peaceful rain sounds + workout beats) can only get one at a time.
- A song might score high for having high danceability even if the user never expressed interest in dancing.

---

## 7. Evaluation  

**User profiles tested:**

1. **High-Energy Pop Fan** (`favorite_genre: pop`, `favorite_mood: happy`, `favorite_artist: Neon Echo`, `target_energy: 0.85`)
   - Expected: Upbeat pop songs
   - Got: "Sunrise City", "Gym Hero", "Night Drive Loop"
   - Observation: Artist and genre matching works perfectly.

2. **Chill Lofi Lover** (`favorite_genre: lofi`, `favorite_mood: chill`, `target_energy: 0.38`, `likes_acoustic: True`)
   - Expected: Low-energy, acoustic, lofi songs
   - Got: "Midnight Coding," "Library Rain," "Focus Flow"
   - Observation: Matching genre + mood + energy + acousticness perfectly isolates the soft, instrumental tracks.

3. **Intense Rock Enthusiast** (`favorite_genre: rock`, `favorite_mood: intense`, `favorite_artist: Voltline`, `target_energy: 0.92`)
   - Expected: Fast, loud rock
   - Got: "Storm Runner" (correct), then fell back to "Gym Hero" (pop) and "Electric Pulse" (electronic)
   - Observation: Once it runs out of rock songs, it strictly grabs other high-energy tracks.

4. **Conflicting Preferences** (`favorite_genre: blues`, `favorite_mood: sad`, `target_energy: 0.85`)
   - Expected: High-energy sad music (which barely exists)
   - Got: "Blue Notes" (low energy, but sad blues)
   - Observation: The system prioritizes the genre category over the mathematical energy target.

**What surprised us:**

- **The "Gym Hero" Effect:** We noticed that the song "Gym Hero" (which is an *intense* pop song) kept showing up for users who just wanted *happy* pop. Surprising, but mathematically logical: because "Gym Hero" shares the "pop" genre tag and has a massive energy score (0.93), the algorithm awards it huge points. This combined score overrules the fact that the mood ("intense" vs "happy") isn't a perfect match!
- **Fallback Behavior:** A user with no favorite artist still gets good recommendations by falling back on danceability + valence.
- **Strict Boundaries:** A user asking for "ambient" music with "0.95 energy" still gets sleepy ambient music. The algorithm refuses to break genre boundaries just to meet an energy target.

---

## 8. Future Work  

**If we kept developing VibeMatcher, we'd add:**

1. **Diversity enforcement:** Ensure top 5 has at least 3 different artists and 2 different genres. This prevents the boring "all the same artist" problem.

2. **User interaction feedback:** Track which recommendations the user clicks, skips, or loves. Use that to adjust weights over time. (This is collaborative filtering—the real power move.)

3. **Better explanation for non-matches:** When a song doesn't match your favorite genre but scores high anyway, explain *why* (e.g., "Your target energy is 0.9 and this song nails it, even though it's electronic not rock").

4. **Explore-exploit balance:** 70% of recommendations match your preferences tightly, 30% are "wild cards" from other genres at the same energy/mood level. This helps users discover new music without abandoning their taste.

5. **Larger, balanced dataset:** Add more songs, especially in underrepresented genres. Better data = fairer recommendations.

6. **Temporal features:** Track which songs are trending, which are classics, which are new. Some users like new releases; others prefer timeless tracks.

7. **Allow combined preferences:** Let users say "I want something like Artist X *and* Artist Y" or "genre A OR genre B" instead of just one of each. More expressive, more useful.

8. **A/B testing:** Compare different weight sets (original vs. genre-heavy vs. energy-heavy) with real users to see which feels best.

---

## 9. Personal Reflection

**Biggest learning moment:**

I realized how *simple* algorithms can feel intelligent and personal. When I tested the recommender, it genuinely felt like it "understood" my taste—just by checking a few features and multiplying numbers. That's humbling. It showed me that the "magic" of AI is often just good engineering, not mystique. A weighted sum of features, sorted well, feels like magic to the user.

**How AI tools helped (and where I double-checked):**

- **Good:** AI tools helped me design the scoring logic quickly. They suggested weighting schemes and feature combinations that made sense.
- **Double-check:** I manually tested a few user profiles because the tool's first suggestions sometimes over-weighted one feature (e.g., artist match drowning out mood). I adjusted weights by hand based on *my intuition*, then ran experiments to see if it felt right.
- **Validation:** When the tool suggested "no duplicates in top 5," I built that into the ranking logic and tested it. It worked, but I had to verify it didn't break other cases.

**What surprised me:**

- How much the dataset *mattered*. With only 17 songs, some user tastes couldn't be served fairly. This isn't the algorithm's fault—it's the data's fault. Real recommendation systems struggle with the same problem at scale (e.g., a tiny genre on Spotify gets fewer good recommendations).
- How *weights* shape the world. Changing the weight on genre from 1.2 to 0.5 completely changed which songs appeared at the top. This showed me that design choices aren't neutral—they have taste baked in.

**If I extended this project, I'd:**

- Add real user data: Simulate 100 profiles with listening history, see which recommendations they actually liked, then tune weights based on that.
- Build a UI: Let users drag sliders for preference strength, see explanations for *every* recommendation, hide songs the algorithm gives low scores to.
- Compare algorithms: Test content-based (what we built) vs. collaborative filtering (find similar users, recommend their favorite songs) vs. a hybrid. Which feels more surprising and delightful?
- Study the "discovery problem": Can we recommend a Beethoven symphony to someone who only likes hip-hop, in a way that doesn't feel random? Or is that a design choice—should recommendations be predictable or surprising?
- Deploy it and watch it fail: Real users would probably hate this. Understanding why it fails on real people is where the hard learning begins.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
