# 🧪 Stress Test Output - Complete Results

## Test Execution

**Date:** April 14, 2026  
**System:** VibeMatcher 1.0  
**Dataset:** 17 songs from catalog  
**Test Type:** 6 distinct user profiles + edge cases  

---

## PROFILE 1: High-Energy Pop Fan

```
User Preferences: 
  - favorite_genre: 'pop'
  - favorite_mood: 'happy'
  - favorite_artist: 'Neon Echo'
  - target_energy: 0.85
  - likes_acoustic: False

Top 5 Recommendations:

1. Sunrise City - Neon Echo
   Score: 0.94 | Genre: pop | Mood: happy
   Because: favorite artist match, genre match, mood match, energy close (diff=0.03), 
            acousticness=0.18, danceability=0.79, valence=0.84

2. Gym Hero - Max Pulse
   Score: 0.61 | Genre: pop | Mood: intense
   Because: genre match, energy close (diff=0.08), acousticness=0.05, 
            danceability=0.88, valence=0.77

3. Night Drive Loop - Neon Echo
   Score: 0.59 | Genre: synthwave | Mood: moody
   Because: favorite artist match, energy close (diff=0.10), acousticness=0.22, 
            danceability=0.73, valence=0.49

4. Rooftop Lights - Indigo Parade
   Score: 0.54 | Genre: indie pop | Mood: happy
   Because: mood match, energy close (diff=0.09), acousticness=0.35, 
            danceability=0.82, valence=0.81

5. Urban Groove - Rhythm Kings
   Score: 0.45 | Genre: hip-hop | Mood: upbeat
   Because: energy close (diff=0.03), acousticness=0.12, danceability=0.85, valence=0.75
```

### Analysis
✅ **Excellent performance.** First recommendation has perfect alignment (artist + genre + mood + energy all match). This profile represents the "ideal case"—clear preferences from well-represented categories.

---

## PROFILE 2: Chill Lofi Lover

```
User Preferences:
  - favorite_genre: 'lofi'
  - favorite_mood: 'chill'
  - favorite_artist: 'LoRoom'
  - target_energy: 0.38
  - likes_acoustic: True

Top 5 Recommendations:

1. Midnight Coding - LoRoom
   Score: 0.88 | Genre: lofi | Mood: chill
   Because: favorite artist match, genre match, mood match, energy close (diff=0.04), 
            acousticness=0.71, danceability=0.62, valence=0.56

2. Focus Flow - LoRoom
   Score: 0.76 | Genre: lofi | Mood: focused
   Because: favorite artist match, genre match, energy close (diff=0.02), 
            acousticness=0.78, danceability=0.60, valence=0.59

3. Library Rain - Paper Lanterns
   Score: 0.70 | Genre: lofi | Mood: chill
   Because: genre match, mood match, energy close (diff=0.03), acousticness=0.86, 
            danceability=0.58, valence=0.60

4. Spacewalk Thoughts - Orbit Bloom
   Score: 0.53 | Genre: ambient | Mood: chill
   Because: mood match, energy close (diff=0.10), acousticness=0.92, 
            danceability=0.41, valence=0.65

5. Island Vibes - Tropical Beats
   Score: 0.51 | Genre: reggae | Mood: chill
   Because: mood match, energy close (diff=0.17), acousticness=0.60, 
            danceability=0.75, valence=0.80
```

### Analysis
✅ **Excellent performance.** Despite lofi being a niche genre, the system finds perfect matches because the artist is in the catalog. Top 3 are all by favorite artist or exactly match genre+mood+energy. The acoustic preference correctly weights high-acousticness songs higher.

---

## PROFILE 3: Intense Rock Enthusiast

```
User Preferences:
  - favorite_genre: 'rock'
  - favorite_mood: 'intense'
  - favorite_artist: 'Voltline'
  - target_energy: 0.92
  - likes_acoustic: False

Top 5 Recommendations:

1. Storm Runner - Voltline
   Score: 0.91 | Genre: rock | Mood: intense
   Because: favorite artist match, genre match, mood match, energy close (diff=0.01), 
            acousticness=0.10, danceability=0.66, valence=0.48

2. Gym Hero - Max Pulse
   Score: 0.60 | Genre: pop | Mood: intense
   Because: mood match, energy close (diff=0.01), acousticness=0.05, 
            danceability=0.88, valence=0.77

3. Electric Pulse - Tech Waves
   Score: 0.57 | Genre: electronic | Mood: intense
   Because: mood match, energy close (diff=0.03), acousticness=0.08, 
            danceability=0.90, valence=0.40

4. Urban Groove - Rhythm Kings
   Score: 0.45 | Genre: hip-hop | Mood: upbeat
   Because: energy close (diff=0.04), acousticness=0.12, danceability=0.85, valence=0.75

5. Sunrise City - Neon Echo
   Score: 0.43 | Genre: pop | Mood: happy
   Because: energy close (diff=0.10), acousticness=0.18, danceability=0.79, valence=0.84
```

### Analysis
✅ **Excellent performance.** First recommendation is near-perfect (0.91 score). The system correctly identifies high-energy, intense music and deprioritizes acoustic (dislikes acoustic = low score for high-acousticness songs). Note that position #2–5 include songs from other genres (pop, electronic, hip-hop) but match the intense mood and high energy target.

---

## 🚨 EDGE CASE 1: Conflicting Preferences (High Energy + Sad Mood)

```
User Preferences:
  - favorite_genre: 'blues'
  - favorite_mood: 'sad'
  - favorite_artist: None
  - target_energy: 0.85  ⚠️ CONTRADICTION: sad music is rarely high-energy
  - likes_acoustic: True

Top 5 Recommendations:

1. Blue Notes - Delta Blues
   Score: 0.58 | Genre: blues | Mood: sad
   Because: genre match, mood match, energy close (diff=0.40), acousticness=0.70, 
            danceability=0.55, valence=0.30

2. Rooftop Lights - Indigo Parade
   Score: 0.37 | Genre: indie pop | Mood: happy
   Because: energy close (diff=0.09), acousticness=0.35, danceability=0.82, valence=0.81

3. Sunrise City - Neon Echo
   Score: 0.36 | Genre: pop | Mood: happy
   Because: energy close (diff=0.03), acousticness=0.18, danceability=0.79, valence=0.84

4. Island Vibes - Tropical Beats
   Score: 0.35 | Genre: reggae | Mood: chill
   Because: energy close (diff=0.30), acousticness=0.60, danceability=0.75, valence=0.80

5. Urban Groove - Rhythm Kings
   Score: 0.35 | Genre: hip-hop | Mood: upbeat
   Because: energy close (diff=0.03), acousticness=0.12, danceability=0.85, valence=0.75
```

### Analysis
⚠️ **Algorithm handles contradiction by prioritizing category matches over energy.**

- **Top pick:** Blue Notes is the only sad blues song, so it wins despite energy mismatch (target 0.85, actual 0.45; diff=0.40)
- **Low scores:** All recommendations score poorly (0.58 max vs 0.88–0.94 for clear preferences)
- **Fallback behavior:** When no song satisfies all preferences, algorithm picks the best genre+mood match (Blue Notes) even though energy is far off
- **User experience:** User asked for sad music AND high energy, but the catalog doesn't offer a sad song that's 0.85 energy. The system correctly returns what it can find.

**Verdict:** ⚠️ System behavior is **reasonable but honest about the mismatch**. The explanation shows "energy close (diff=0.40)" so the user can see the contradiction. However, a user might be surprised that their "sad" preference overrode their "high energy" request.

---

## 🚨 EDGE CASE 2: Minimal Preferences (Only Energy)

```
User Preferences:
  - favorite_genre: None
  - favorite_mood: None
  - favorite_artist: None
  - target_energy: 0.75
  - likes_acoustic: False

Top 5 Recommendations:

1. Sunrise City - Neon Echo
   Score: 0.44 | Genre: pop | Mood: happy
   Because: energy close (diff=0.07), acousticness=0.18, danceability=0.79, valence=0.84

2. Gym Hero - Max Pulse
   Score: 0.43 | Genre: pop | Mood: intense
   Because: energy close (diff=0.18), acousticness=0.05, danceability=0.88, valence=0.77

3. Urban Groove - Rhythm Kings
   Score: 0.43 | Genre: hip-hop | Mood: upbeat
   Because: energy close (diff=0.13), acousticness=0.12, danceability=0.85, valence=0.75

4. Rooftop Lights - Indigo Parade
   Score: 0.43 | Genre: indie pop | Mood: happy
   Because: energy close (diff=0.01), acousticness=0.35, danceability=0.82, valence=0.81

5. Night Drive Loop - Neon Echo
   Score: 0.41 | Genre: synthwave | Mood: moody
   Because: energy close (diff=0.00), acousticness=0.22, danceability=0.73, valence=0.49
```

### Analysis
⚠️ **Graceful degradation, but limited utility.**

- **Behavior:** With no genre, mood, or artist preferences, the algorithm falls back to energy matching + danceability + valence
- **Scores:** All recommendations score low (~0.40–0.44) because there are no categorical matches
- **Diversity:** Results include multiple genres (pop, hip-hop, indie pop, synthwave), which is good for discovery but not personalized
- **Surprising choice:** Top 5 includes songs with energy varying from 0.75 (exact) to 0.82 (diff=0.07), showing energy matching works

**Verdict:** ⚠️ Algorithm **doesn't fail**, but recommendations lack personality. For a user who only specifies energy, the system should probably ask "any other preferences?" This reveals a UX issue: the system works but feels generic.

---

## 🚨 EDGE CASE 3: Underrepresented Genre (Classical + Relaxed)

```
User Preferences:
  - favorite_genre: 'classical'
  - favorite_mood: 'relaxed'
  - favorite_artist: 'Melody Masters'
  - target_energy: 0.25
  - likes_acoustic: True

Top 5 Recommendations:

1. Serenade in G - Melody Masters
   Score: 0.90 | Genre: classical | Mood: relaxed
   Because: favorite artist match, genre match, mood match, energy close (diff=0.00), 
            acousticness=0.95, danceability=0.30, valence=0.60

2. Coffee Shop Stories - Slow Stereo
   Score: 0.54 | Genre: jazz | Mood: relaxed
   Because: mood match, energy close (diff=0.12), acousticness=0.89, 
            danceability=0.54, valence=0.71

3. Spacewalk Thoughts - Orbit Bloom
   Score: 0.41 | Genre: ambient | Mood: chill
   Because: energy close (diff=0.03), acousticness=0.92, danceability=0.41, valence=0.65

4. Library Rain - Paper Lanterns
   Score: 0.40 | Genre: lofi | Mood: chill
   Because: energy close (diff=0.10), acousticness=0.86, danceability=0.58, valence=0.60

5. Focus Flow - LoRoom
   Score: 0.38 | Genre: lofi | Mood: focused
   Because: energy close (diff=0.15), acousticness=0.78, danceability=0.60, valence=0.59
```

### Analysis
✅ **Perfect match for available data.**

- **Top pick:** The system correctly identifies "Serenade in G" as a perfect match (0.90 score) because it's the only classical + relaxed song in the catalog
- **Fallback:** After the perfect match, the system gracefully falls back to other relaxed/acoustic songs (jazz, ambient, lofi) with lower scores
- **Representation:** Classical music has only 1 song, so there's no diversity within genre. But the system handles this honestly.
- **Acoustic preference:** Successfully boosts songs with high acousticness (0.95, 0.89, 0.92, 0.86, 0.78)

**Verdict:** ✅ System works well **for underrepresented genres IF the exact match exists**. However, this reveals a limitation: a classical fan will get Serenade (0.90) and then 4 non-classical songs. A real catalog would have more classical options.

---

## 🚨 EDGE CASE 4: Extreme Energy Mismatch (Ambient + 0.95 Energy)

```
User Preferences:
  - favorite_genre: 'ambient'
  - favorite_mood: 'chill'
  - favorite_artist: 'Orbit Bloom'
  - target_energy: 0.95  ⚠️ EXTREME MISMATCH: ambient is typically 0.25–0.35 energy
  - likes_acoustic: True

Top 5 Recommendations:

1. Spacewalk Thoughts - Orbit Bloom
   Score: 0.77 | Genre: ambient | Mood: chill
   Because: favorite artist match, genre match, mood match, energy close (diff=0.67), 
            acousticness=0.92, danceability=0.41, valence=0.65

2. Island Vibes - Tropical Beats
   Score: 0.47 | Genre: reggae | Mood: chill
   Because: mood match, energy close (diff=0.40), acousticness=0.60, 
            danceability=0.75, valence=0.80

3. Library Rain - Paper Lanterns
   Score: 0.43 | Genre: lofi | Mood: chill
   Because: mood match, energy close (diff=0.60), acousticness=0.86, 
            danceability=0.58, valence=0.60

4. Midnight Coding - LoRoom
   Score: 0.42 | Genre: lofi | Mood: chill
   Because: mood match, energy close (diff=0.53), acousticness=0.71, 
            danceability=0.62, valence=0.56

5. Rooftop Lights - Indigo Parade
   Score: 0.35 | Genre: indie pop | Mood: happy
   Because: energy close (diff=0.19), acousticness=0.35, danceability=0.82, valence=0.81
```

### Analysis
⚠️ **Category matches override energy mismatch.**

- **Top pick:** "Spacewalk Thoughts" wins with score 0.77 despite massive energy mismatch (target 0.95, actual 0.28; diff=0.67)
- **Why it wins:** Artist match (1.5) + genre match (1.2) + mood match (1.0) = 3.7 weight total >> energy mismatch penalty
- **Explanation honesty:** System shows "energy close (diff=0.67)" so user can see the huge mismatch
- **Irony:** The system recommends a 0.28-energy song to a user who asked for 0.95 energy, because they matched on artist/genre/mood
- **Fallback behavior:** Remaining songs (#2–5) also favor low-energy matches that are chill/acoustic

**Verdict:** ⚠️ **Algorithm reveals a design limitation: categorical preferences are weighted higher than numeric ones.** A user who says "I want ambient" gets ambient, even if they also said "energy 0.95" (which contradicts ambient). This could be a feature (respecting explicit genre preference) or a bug (ignoring energy request).

**UX Problem:** The system should probably ask "Did you mean high-energy ambient (which doesn't exist) or did you want to explore high-energy songs in general?" but it doesn't.

---

## 🚨 EDGE CASE 5: Multiple Contradictions (Dreamy + 0.88 Energy + Acoustic)

```
User Preferences:
  - favorite_genre: 'electronic'
  - favorite_mood: 'dreamy'
  - favorite_artist: None
  - target_energy: 0.88  ⚠️ CONTRADICTION: dreamy is usually low-energy
  - likes_acoustic: True  ⚠️ CONTRADICTION: electronic is rarely acoustic

Top 5 Recommendations:

1. Electric Pulse - Tech Waves
   Score: 0.47 | Genre: electronic | Mood: intense
   Because: genre match, energy close (diff=0.07), acousticness=0.08, 
            danceability=0.90, valence=0.40

2. Folk Tales - Storytellers
   Score: 0.47 | Genre: folk | Mood: dreamy
   Because: mood match, energy close (diff=0.38), acousticness=0.80, 
            danceability=0.60, valence=0.65

3. Rooftop Lights - Indigo Parade
   Score: 0.36 | Genre: indie pop | Mood: happy
   Because: energy close (diff=0.12), acousticness=0.35, danceability=0.82, valence=0.81

4. Urban Groove - Rhythm Kings
   Score: 0.36 | Genre: hip-hop | Mood: upbeat
   Because: energy close (diff=0.00), acousticness=0.12, danceability=0.85, valence=0.75

5. Sunrise City - Neon Echo
   Score: 0.36 | Genre: pop | Mood: happy
   Because: energy close (diff=0.06), acousticness=0.18, danceability=0.79, valence=0.84
```

### Analysis
⚠️ **Algorithm splits between contradictory preferences.**

- **Top picks tied at 0.47:**
  - "Electric Pulse" matches electronic + energy, but not dreamy (intense instead) and not acoustic (0.08)
  - "Folk Tales" matches dreamy + acoustic, but not electronic and energy mismatch (diff=0.38)
- **Algorithm behavior:** There's no "electronic + dreamy + 0.88 energy + acoustic" song, so the system returns two different compromises
- **Score collapse:** All recommendations score in the 0.36–0.47 range (poor compared to 0.88+ for clear preferences)
- **Honest explanation:** Each song's explanation shows what matched and what didn't

**Verdict:** ⚠️ **System handles multiple contradictions by returning multiple imperfect options.** The score reflects the contradiction (low 0.47) so it's honest. However, a user might feel like nothing satisfies them, which is true—the preferences are inherently contradictory.

**Design insight:** The user really needs to clarify priorities. "I want electronic music (priority 1) that's dreamy (priority 2) or I want dreamy music (priority 1) that's as energetic as possible (priority 2)?" The current system has no way to express priority order.

---

## 🚨 EDGE CASE 6: Nonexistent Artist (Jazz + Relaxed)

```
User Preferences:
  - favorite_genre: 'jazz'
  - favorite_mood: 'relaxed'
  - favorite_artist: 'Unknown Artist That Does Not Exist'
  - target_energy: 0.40
  - likes_acoustic: True

Top 5 Recommendations:

1. Coffee Shop Stories - Slow Stereo
   Score: 0.71 | Genre: jazz | Mood: relaxed
   Because: genre match, mood match, energy close (diff=0.03), acousticness=0.89, 
            danceability=0.54, valence=0.71

2. Serenade in G - Melody Masters
   Score: 0.51 | Genre: classical | Mood: relaxed
   Because: mood match, energy close (diff=0.15), acousticness=0.95, 
            danceability=0.30, valence=0.60

3. Focus Flow - LoRoom
   Score: 0.41 | Genre: lofi | Mood: focused
   Because: energy close (diff=0.00), acousticness=0.78, danceability=0.60, valence=0.59

4. Library Rain - Paper Lanterns
   Score: 0.41 | Genre: lofi | Mood: chill
   Because: energy close (diff=0.05), acousticness=0.86, danceability=0.58, valence=0.60

5. Folk Tales - Storytellers
   Score: 0.39 | Genre: folk | Mood: dreamy
   Because: energy close (diff=0.10), acousticness=0.80, danceability=0.60, valence=0.65
```

### Analysis
✅ **Graceful fallback when artist doesn't exist.**

- **Algorithm behavior:** Favorite artist = "Unknown Artist That Does Not Exist" → artist_score = 0.0 for all songs, but algorithm doesn't break
- **Top pick:** "Coffee Shop Stories" (jazz + relaxed) wins with 0.71 score (good despite missing artist match)
- **Robust degradation:** Algorithm simply ignores the nonexistent artist and relies on genre + mood + energy
- **Score impact:** Loses ~0.15–0.20 points compared to an artist match (e.g., Profile 2 had 0.88 for artist+genre+mood+energy vs 0.71 here for just genre+mood+energy)

**Verdict:** ✅ **System is robust to missing data.** This is excellent defensive programming. A missing favorite artist doesn't crash the system or return garbage; it just gives slightly lower scores and relies on other features. Real recommenders need this robustness.

---

## Summary Table

| Profile | Top Score | Genre Match | Mood Match | Artist Match | Energy Match | Key Finding |
|---------|-----------|-------------|-----------|--------------|--------------|------------|
| Profile 1: Pop Fan | 0.94 | ✅ | ✅ | ✅ | ✅ | All preferences align; system excels |
| Profile 2: Lofi Lover | 0.88 | ✅ | ✅ | ✅ | ✅ | Niche genre works if artist exists |
| Profile 3: Rock Fan | 0.91 | ✅ | ✅ | ✅ | ✅ | High-energy moods are well-served |
| Edge Case 1 | 0.58 | ✅ | ✅ | ❌ | ❌ | Conflicting preferences lower score |
| Edge Case 2 | 0.44 | ❌ | ❌ | ❌ | ✅ | Minimal preferences = generic recs |
| Edge Case 3 | 0.90 | ✅ | ✅ | ✅ | ✅ | Underrep. genre works if exists |
| Edge Case 4 | 0.77 | ✅ | ✅ | ✅ | ❌ | Category > energy; huge mismatch shown |
| Edge Case 5 | 0.47 | ⚠️ | ⚠️ | ❌ | ⚠️ | Multiple contradictions = split decision |
| Edge Case 6 | 0.71 | ✅ | ✅ | ❌ | ✅ | Missing artist handled gracefully |

---

## Recommendations for Improvement

1. **Priority system:** Let users specify which preferences matter most (genre > energy > mood) to resolve conflicts
2. **Better explanations for contradictions:** "You asked for high-energy + sad, but sad songs are usually low-energy. Here's the best match I found…"
3. **Diversity enforcement:** Limit to 2 recommendations per artist, force at least 2 different genres in top 5
4. **Explore-exploit:** 70% recommendations match preferences, 30% are "wild cards" from underexplored genres
5. **User feedback loop:** Track skips/likes to learn whether the user really wanted high energy OR sad music more
