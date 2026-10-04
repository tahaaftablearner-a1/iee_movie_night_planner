 1. Project Overview
The **Movie Night Planner** is a modular Python application designed to load external movie datasets, search/filter movies dynamically, and curate a personal watchlist. It demonstrates clean software architecture, robust input validation, duplicate prevention using sets, and automated runtime analytics.

---

## 2. Concepts Implemented
- **Object-Oriented Programming (OOP):** Custom `Movie` class and `Watchlist` container encapsulating state and behavioral methods (`__str__`, `__eq__`, `__hash__`).
- **File Handling:** Dynamic `.csv` parsing using `csv.DictReader` and context managers (`with` statement).
- **Error & Exception Handling:** Graceful `try/except` wrappers around numerical parsing and invalid user menu selections.
- **Data Structures & Comprehensions:** Sets (`set()`) for duplicate prevention; list comprehensions for high-performance genre/rating filtering.

---

## 3. How to Run the Program
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/ieee-movie-night-planner.git
   cd ieee-movie-night-planner
