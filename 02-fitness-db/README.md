# 🏋️‍♂️ Fitness Centre Database Management

This project provides a complete **MySQL Relational Schema** designed to manage the operations of a boutique fitness center. It focuses on practitioner tracking, activity enrollment, and automated loyalty programs.

## 📊 Database Architecture
The schema consists of four interconnected tables:
* **`fitness_practitioners`**: Master table with unique contact information.
* **`members`**: Tracks subscription statuses.
* **`practitioners_birthday`**: Stores date of birth for loyalty marketing.
* **`fitness_activities`**: Manages class enrollments and multi-activity logic.



## 🛠️ Key SQL Features
* **Relational Integrity:** Implements `FOREIGN KEY` constraints and `UNIQUE` indexes to ensure data consistency.
* **Stored Procedures:** Includes `InsertValuefitness_practitioners` to standardize the onboarding of new clients.
* **Custom Functions:** * `have_discount`: Automatically identifies clients eligible for multi-class pricing.
    * `have_freeclass`: Logic to flag active birthday rewards based on the current month.
* **Advanced Queries:** Utilization of `LEFT JOINs`, `Subqueries`, and `Aggregate Functions` (MAX/MIN) for demographic reporting.

## 🚀 How to Setup
1. Open your MySQL client (e.g., MySQL Workbench).
2. Create the database: `CREATE DATABASE fitness_centre;`.
3. Run the provided script: `SOURCE database_setup.sql;`.
4. Test the business logic by calling the custom functions or procedures.

---
*Focus: Data Modeling & Business Intelligence.*
