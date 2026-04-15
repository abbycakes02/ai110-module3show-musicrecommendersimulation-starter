"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, taste_profile: dict, recommendations: list) -> None:
    """Pretty-print recommendations for a given profile."""
    print("\n" + "=" * 80)
    print(f"PROFILE: {profile_name}")
    print("=" * 80)
    print(f"User Preferences: {taste_profile}")
    print(f"\nTop 5 Recommendations:\n")
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{i}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f} | Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs('../data/songs.csv')
    print(f"\n🎵 Loaded {len(songs)} songs from catalog\n")

    # ============================================================================
    # STRESS TEST PROFILES
    # ============================================================================

    # Profile 1: High-Energy Pop Fan (Clear, well-represented preferences)
    profile_1 = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "favorite_artist": "Neon Echo",
        "target_energy": 0.85,
        "likes_acoustic": False
    }
    rec_1 = recommend_songs(profile_1, songs, k=5)
    print_recommendations("Profile 1: High-Energy Pop Fan", profile_1, rec_1)

    # Profile 2: Chill Lofi Lover (Low energy, acoustic preference)
    profile_2 = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "favorite_artist": "LoRoom",
        "target_energy": 0.38,
        "likes_acoustic": True
    }
    rec_2 = recommend_songs(profile_2, songs, k=5)
    print_recommendations("Profile 2: Chill Lofi Lover", profile_2, rec_2)

    # Profile 3: Intense Rock Enthusiast (High energy, specific mood)
    profile_3 = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "favorite_artist": "Voltline",
        "target_energy": 0.92,
        "likes_acoustic": False
    }
    rec_3 = recommend_songs(profile_3, songs, k=5)
    print_recommendations("Profile 3: Intense Rock Enthusiast", profile_3, rec_3)

    # ============================================================================
    # EDGE CASE & ADVERSARIAL PROFILES (designed to stress-test the algorithm)
    # ============================================================================

    # Edge Case 1: Conflicting Preferences (High energy + Sad mood)
    # This is "adversarial": these preferences rarely co-occur in real music
    profile_edge_1 = {
        "favorite_genre": "blues",
        "favorite_mood": "sad",
        "favorite_artist": None,
        "target_energy": 0.85,  # conflicting: sad songs are usually low-energy
        "likes_acoustic": True
    }
    rec_edge_1 = recommend_songs(profile_edge_1, songs, k=5)
    print_recommendations("EDGE CASE 1: Conflicting Preferences (High Energy + Sad Mood)", profile_edge_1, rec_edge_1)

    # Edge Case 2: Empty/Minimal Preferences (only energy)
    # Tests if the algorithm can still produce reasonable results without strong categorical matches
    profile_edge_2 = {
        "favorite_genre": None,
        "favorite_mood": None,
        "favorite_artist": None,
        "target_energy": 0.75,
        "likes_acoustic": False
    }
    rec_edge_2 = recommend_songs(profile_edge_2, songs, k=5)
    print_recommendations("EDGE CASE 2: Minimal Preferences (Only Energy)", profile_edge_2, rec_edge_2)

    # Edge Case 3: Underrepresented Genre + Highly Specific Mood
    # Tests if the algorithm handles rare preference combinations gracefully
    profile_edge_3 = {
        "favorite_genre": "classical",
        "favorite_mood": "relaxed",
        "favorite_artist": "Melody Masters",
        "target_energy": 0.25,
        "likes_acoustic": True
    }
    rec_edge_3 = recommend_songs(profile_edge_3, songs, k=5)
    print_recommendations("EDGE CASE 3: Underrepresented Genre (Classical + Relaxed)", profile_edge_3, rec_edge_3)

    # Edge Case 4: Extreme Energy Mismatch
    # User wants extremely high energy, but all their other preferences are from low-energy genres
    profile_edge_4 = {
        "favorite_genre": "ambient",
        "favorite_mood": "chill",
        "favorite_artist": "Orbit Bloom",
        "target_energy": 0.95,  # adversarial: ambient is rarely 0.95
        "likes_acoustic": True
    }
    rec_edge_4 = recommend_songs(profile_edge_4, songs, k=5)
    print_recommendations("EDGE CASE 4: Extreme Energy Mismatch (Ambient + 0.95 Energy)", profile_edge_4, rec_edge_4)

    # Edge Case 5: Contradictory Mood + Energy + Acoustic Profile
    # Tries to combine multiple conflicting signals (dreamy but energetic, acoustic but intense)
    profile_edge_5 = {
        "favorite_genre": "electronic",
        "favorite_mood": "dreamy",
        "favorite_artist": None,
        "target_energy": 0.88,
        "likes_acoustic": True
    }
    rec_edge_5 = recommend_songs(profile_edge_5, songs, k=5)
    print_recommendations("EDGE CASE 5: Multiple Contradictions (Dreamy + 0.88 Energy + Acoustic)", profile_edge_5, rec_edge_5)

    # Edge Case 6: Artist Preference with No Matching Artist
    # Tests graceful degradation when favorite artist doesn't exist in catalog
    profile_edge_6 = {
        "favorite_genre": "jazz",
        "favorite_mood": "relaxed",
        "favorite_artist": "Unknown Artist That Does Not Exist",
        "target_energy": 0.40,
        "likes_acoustic": True
    }
    rec_edge_6 = recommend_songs(profile_edge_6, songs, k=5)
    print_recommendations("EDGE CASE 6: Nonexistent Artist (Jazz + Relaxed)", profile_edge_6, rec_edge_6)

    print("\n" + "=" * 80)
    print("✅ STRESS TEST COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
