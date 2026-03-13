# 📅 Fitness Booking API System

A Full-stack internal tool designed to manage gym class schedules and automate the reservation process. This project demonstrates a complete **N-Tier Architecture**: Client -> API -> Database.

## 🏗️ System Architecture
The application is decoupled into four specialized modules to ensure maintainability:

* **`main.py` (Client Layer):** A command-line interface (CLI) that handles user interactions and data visualization.
* **`app.py` (Server Layer):** A Flask-based REST API that exposes endpoints for scheduling and bookings.
* **`db_utils.py` (Data Access Layer):** Manages all SQL transactions, including complex mapping and exception handling.
* **`config.py` (Security):** Isolates sensitive database credentials.

## 🌟 Key Features
* **Dynamic Scheduling:** Fetches real-time class availability from a MySQL backend.
* **Automated Booking:** Allows users to register for specific slots with instant database persistence.
* **Custom Data Mapping:** Transforms raw SQL tuples into readable JSON formats for the frontend.
* **Error Handling:** Implements custom exception classes (`DbConnectionError`) to manage database downtime gracefully.

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Flask.
* **Database:** MySQL.
* **Communication:** RESTful API (JSON).

## 🚀 Setup & Execution
1.  **Database:** Run `fitness_reservations.sql` in your MySQL environment.
2.  **Config:** Update `config.py` with your local DB credentials.
3.  **Launch API:**
    ```bash
    python app.py
    ```
4.  **Launch Client:**
    ```bash
    python main.py
    ```

---
*Status: Functional Prototype - Evolution from core Python to API Integration.*