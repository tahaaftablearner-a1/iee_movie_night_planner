"""
Main executable entry point for Movie Night Planner.
Handles file reading, user interactive loops, and exception handling.
"""

import csv
import os
from models import Movie, Watchlist


def load_movies_from_csv(file_path: str) -> list[Movie]:
    """Reads movies from an external CSV file with error recovery."""
    movies = []
    if not os.path.exists(file_path):
        print(f"[Error] File not found at path: {file_path}")
        return movies

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    movie = Movie(
                        title=row["title"].strip(),
                        genre=row["genre"].strip(),
                        rating=float(row["rating"]),
                        duration=int(row["duration"])
                    )
                    movies.append(movie)
                except (ValueError, KeyError) as e:
                    print(f"[Warning] Skipping malformed record {row}: {e}")
    except Exception as e:
        print(f"[Fatal Error] Failed to read dataset: {e}")

    return movies


def display_menu():
    print("\n" + "=" * 45)
    print("      IEEE MOVIE NIGHT PLANNER ")
    print("=" * 45)
    print("1. View All Movies")
    print("2. Search Movies by Genre")
    print("3. Filter Movies by Minimum Rating")
    print("4. Add Movie to Watchlist")
    print("5. Remove Movie from Watchlist")
    print("6. View Watchlist & Analytics")
    print("7. Exit")
    print("=" * 45)


def main():
    csv_path = os.path.join("data", "movies.csv")
    library = load_movies_from_csv(csv_path)
    watchlist = Watchlist()

    print(f"[System] Successfully loaded {len(library)} movies into the library.")

    while True:
        display_menu()
        choice = input("Enter option (1-7): ").strip()

        if choice == "1":
            print("\n--- Available Movie Library ---")
            for m in library:
                print(m)

        elif choice == "2":
            genre_input = input("Enter genre to search: ").strip()
            # List comprehension for filtering by genre (case-insensitive)
            results = [m for m in library if m.genre.lower() == genre_input.lower()]
            
            if results:
                print(f"\n--- Found {len(results)} movies matching '{genre_input}' ---")
                for m in results:
                    print(m)
            else:
                print(f"\n[Info] No movies found in genre: '{genre_input}'")

        elif choice == "3":
            try:
                min_rating = float(input("Enter minimum rating threshold (0.0 - 10.0): "))
                # List comprehension for filtering by rating threshold
                filtered = [m for m in library if m.rating >= min_rating]
                
                print(f"\n--- Movies with Rating >= {min_rating} ---")
                if filtered:
                    for m in filtered:
                        print(m)
                else:
                    print("[Info] No movies match or exceed that rating.")
            except ValueError:
                print("\n[Error] Invalid input! Please enter a numerical decimal value for rating.")

        elif choice == "4":
            title_input = input("Enter exact movie title to add: ").strip()
            match = next((m for m in library if m.title.lower() == title_input.lower()), None)
            
            if match:
                added = watchlist.add_movie(match)
                if added:
                    print(f"\n[Success] Added '{match.title}' to your watchlist!")
                else:
                    print(f"\n[Notice] '{match.title}' is already in your watchlist (Duplicates prevented).")
            else:
                print(f"\n[Error] Movie '{title_input}' not found in library.")

        elif choice == "5":
            title_input = input("Enter title to remove: ").strip()
            removed = watchlist.remove_movie(title_input)
            if removed:
                print(f"\n[Success] Removed '{title_input}' from watchlist.")
            else:
                print(f"\n[Error] '{title_input}' is not currently in your watchlist.")

        elif choice == "6":
            items = watchlist.get_all()
            print("\n--- Personal Watchlist ---")
            if not items:
                print("Your watchlist is currently empty.")
            else:
                for idx, m in enumerate(items, 1):
                    print(f"{idx}. {m}")
                print("-" * 45)
                print(f"Total Movies: {len(watchlist)}")
                print(f"Total Duration: {watchlist.total_duration()} minutes")
                print(f"Average Rating: {watchlist.average_rating():.2f} / 10")

        elif choice == "7":
            print("\nThank you for using Movie Night Planner! Goodbye.")
            break
        else:
            print("\n[Error] Invalid option selected. Please choose between 1 and 7.")


if __name__ == "__main__":
    main()
    
    