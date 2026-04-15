from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_artist: str
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    songs = []
    with open(csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            song_dict = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            }
            songs.append(song_dict)

    print(f"Loading songs from {csv_path}...")
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Simple scoring:
      - categorical matches (artist, genre, mood) are binary (1.0 / 0.0)
      - energy closeness is 1 - abs(diff) assuming energy in [0,1]
      - acousticness honors likes_acoustic: high acousticness preferred if True, low otherwise
      - danceability & valence used as-is (already in [0,1])
    Returns top-k as (song_dict, score, explanation).
    """
    # helper to keep numeric features in the [0,1] range
    def clamp(x, a=0.0, b=1.0):
        return max(a, min(b, x))

    # weights for each feature. Higher weight => more influence on final score.
    weights = {
        "artist": 1.5,
        "genre": 1.2,
        "mood": 1.0,
        "energy": 1.5,
        "acoustic": 1.0,
        "danceability": 0.7,
        "valence": 0.6
    }
    total_weight = sum(weights.values())  # used to normalize final score to ~[0,1]

    # Pull user preferences and normalize to lowercase where comparing strings
    fav_artist = (user_prefs.get("favorite_artist") or "").strip().lower()
    fav_genre = (user_prefs.get("favorite_genre") or "").strip().lower()
    fav_mood = (user_prefs.get("favorite_mood") or "").strip().lower()
    target_energy = user_prefs.get("target_energy", None)  # expected numeric in [0,1] or None
    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))

    # Define a "judge" function that scores a single song and returns (score, explanation).
    # This isolates the scoring logic so it can be reused (and tested) independently.
    def score_song(song: Dict) -> Tuple[float, str]:
        """
        Score a single song dict against the user preferences.
        Returns a tuple of (score, explanation).
        """
        # normalize song categorical fields for comparison
        artist = (song.get("artist") or "").lower()
        genre = (song.get("genre") or "").lower()
        mood = (song.get("mood") or "").lower()

        # categorical/binary matches:
        # - artist: partial match (substring) gives 1.0, else 0.0
        # - genre and mood: require exact match to count
        artist_score = 1.0 if fav_artist and fav_artist in artist else 0.0
        genre_score = 1.0 if fav_genre and fav_genre == genre else 0.0
        mood_score = 1.0 if fav_mood and fav_mood == mood else 0.0

        # numeric features (assume in [0,1] except tempo)
        energy = clamp(float(song.get("energy", 0.0)))
        # if user provided a target energy, score by closeness: 1 - abs(diff)
        if target_energy is not None:
            energy_score = clamp(1.0 - abs(energy - float(target_energy)))
        else:
            # if no target, use the song's energy directly as its contribution
            energy_score = energy

        acousticness = clamp(float(song.get("acousticness", 0.0)))
        # prefer high acousticness if user likes acoustic, otherwise prefer low acousticness
        acoustic_score = acousticness if likes_acoustic else (1.0 - acousticness)

        danceability_score = clamp(float(song.get("danceability", 0.0)))
        valence_score = clamp(float(song.get("valence", 0.0)))

        # weighted linear combination of feature scores, then normalize
        score = (
            weights["artist"] * artist_score +
            weights["genre"] * genre_score +
            weights["mood"] * mood_score +
            weights["energy"] * energy_score +
            weights["acoustic"] * acoustic_score +
            weights["danceability"] * danceability_score +
            weights["valence"] * valence_score
        ) / total_weight

        # build short, human-readable explanation for why this song scored as it did
        reasons = []
        if artist_score > 0:
            reasons.append("favorite artist match")
        if genre_score > 0:
            reasons.append("genre match")
        if mood_score > 0:
            reasons.append("mood match")

        # explain energy contribution: either closeness to target or raw energy value
        if target_energy is not None:
            diff = abs(energy - float(target_energy))
            reasons.append(f"energy close (diff={diff:.2f})")
        else:
            reasons.append(f"energy={energy:.2f}")

        # include acousticness/danceability/valence for transparency
        reasons.append(f"acousticness={acousticness:.2f}")
        reasons.append(f"danceability={danceability_score:.2f}")
        reasons.append(f"valence={valence_score:.2f}")

        explanation = ", ".join(reasons)
        return score, explanation

    # Score every song in the catalog using the judge (score_song), collect and sort.
    scored = []
    for s in songs:
        score, explanation = score_song(s)
        scored.append((s, score, explanation))

    # sort songs by score descending and return top-k
    scored.sort(key=lambda t: t[1], reverse=True)
    return scored[:k]
