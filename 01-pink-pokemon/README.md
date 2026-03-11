# 🌸 Pink Pokemon Power!

An interactive console-based game that consumes real-time data from the **PokéAPI** to help users discover and "battle" with pink-colored Pokémon.

## 🚀 Features
* **Live Data Fetching:** Connects to the PokéAPI to retrieve a dynamic list of species categorized by color.
* **Interactive Mini-games:** * **Name Scramble:** Challenge yourself to guess the Pokémon name from a reversed string.
    * **Stat Battle:** Test your luck against the Pokémon's base attack stats fetched directly from the database.
* **Automated Logging:** The app generates a `pinkpokemon.txt` catalog and maintains a `log.txt` file to track player performance and history.

## 🛠️ Technical Implementation
This project demonstrates proficiency in:
* **REST API Integration:** Using the `requests` library to handle JSON responses.
* **File I/O:** Reading, writing, and appending data to local text files using context managers.
* **Modular Logic:** Structured with functions and a `main()` entry point for clean, maintainable code.
* **Data Manipulation:** Advanced use of lists, dictionaries, and string slicing.

## 📦 Installation & Setup
1. **Prerequisites:** Ensure you have Python 3.x installed.
2. **Install Dependencies:**
   ```bash
   pip install requests
