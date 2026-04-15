"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs('../data/songs.csv')
    print(f"Loaded {len(songs)} songs")  # Debug: Check if songs loaded

    # Starter example profile
    taste_profile = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "favorite_artist": "Neon Echo",
        "target_energy": 0.9,
        "likes_acoustic": False  # optional, if included in scoring
    }

    recommendations = recommend_songs(taste_profile, songs, k=5)
    print(f"Got {len(recommendations)} recommendations")  # Debug: Check if recommendations generated

    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
if __name__ == "__main__":
    main()
