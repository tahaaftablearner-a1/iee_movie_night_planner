class Movie:

    def __init__(self, title: str, genre: str, rating: float, duration: int):
        self.title = title
        self.genre = genre
        self.rating = float(rating)
        self.duration = int(duration)

    def __str__(self) -> str:
        return f"{self.title} | Genre: {self.genre} | Rating: {self.rating}/10 | Duration: {self.duration} mins"

    def __eq__(self, other) -> bool:
        if isinstance(other, Movie):
            return self.title.lower() == other.title.lower()
        return False

    def __hash__(self) -> int:
        return hash(self.title.lower())


class Watchlist:
    
    def __init__(self):
        self._movies: set[Movie] = set()

    def add_movie(self, movie: Movie) -> bool:
        if movie in self._movies:
            return False
        self._movies.add(movie)
        return True

    def remove_movie(self, title: str) -> bool:
        target = next((m for m in self._movies if m.title.lower() == title.lower()), None)
        if target:
            self._movies.remove(target)
            return True
        return False

    def get_all(self) -> list[Movie]:
        return list(self._movies)

    def total_duration(self) -> int:
        """Calculates total watchlist duration in minutes using sum()."""
        return sum(movie.duration for movie in self._movies)

    def average_rating(self) -> float:
        """Calculates average rating across all movies in the watchlist."""
        if not self._movies:
            return 0.0
        return sum(movie.rating for movie in self._movies) / len(self._movies)

    def __len__(self) -> int:
        return len(self._movies)