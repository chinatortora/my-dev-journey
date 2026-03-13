-- =============================================
-- Fitness Center Reservation System Schema
-- Description: Handles class availability and user bookings.
-- =============================================

CREATE DATABASE IF NOT EXISTS fitness_reservations;
USE fitness_reservations;

-- Table: Weekly Class Schedule
CREATE TABLE IF NOT EXISTS classes_per_day (
    activity VARCHAR(50) NOT NULL,
    monday BOOLEAN NOT NULL DEFAULT 0,
    tuesday BOOLEAN NOT NULL DEFAULT 0,
    wednesday BOOLEAN NOT NULL DEFAULT 0,
    thursday BOOLEAN NOT NULL DEFAULT 0,
    friday BOOLEAN NOT NULL DEFAULT 0
);

-- Table: User Bookings
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    person_id INT NOT NULL,
    activity VARCHAR(50) NOT NULL,
    day VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Initial Data Seed
INSERT INTO classes_per_day (activity, monday, tuesday, wednesday, thursday, friday)
VALUES
('yoga', 1, 0, 1, 0, 1),
('pilates', 0, 1, 0, 1, 0);
 