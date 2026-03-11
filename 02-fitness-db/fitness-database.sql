-- =============================================
-- Database Schema for Fitness Centre Management
-- Author: Antonella Tortora Picatto
-- Description: Management system for practitioners,
-- activities, memberships, and loyalty rewards.
-- =============================================

CREATE DATABASE IF NOT EXISTS fitness_centre;
USE fitness_centre;

-- 1. CORE TABLES
-- ---------------------------------------------

-- Base table for all individuals in the system
CREATE TABLE IF NOT EXISTS fitness_practitioners (
    person_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    telephone INT UNIQUE,
    email VARCHAR(100) UNIQUE
);

-- Tracks active membership status
CREATE TABLE IF NOT EXISTS members (
    person_id INTEGER NOT NULL,
    membership BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (person_id) REFERENCES fitness_practitioners(person_id)
);

-- Birthday tracking for marketing and loyalty campaigns
CREATE TABLE IF NOT EXISTS practitioners_birthday (
    person_id INTEGER,
    birthday DATE NOT NULL,
    FOREIGN KEY (person_id) REFERENCES fitness_practitioners(person_id)
);

-- Activity enrollment (Supports up to 2 concurrent activities)
CREATE TABLE IF NOT EXISTS fitness_activities (
    person_id INTEGER,
    first_activity VARCHAR(50) NOT NULL,
    second_activity VARCHAR(50),
    CONSTRAINT FK_activity_person FOREIGN KEY(person_id) REFERENCES fitness_practitioners(person_id)
);

-- 2. MOCK DATA INJECTION
-- ---------------------------------------------

INSERT INTO fitness_practitioners (person_id, name, surname, telephone, email) VALUES
(1, 'Mary', 'Jones', 1234567, 'mary.j@example.com'),
(2, 'Marta', 'Perez', 7834567, 'marta.p@example.com'),
(3, 'Santina', 'Siracusa', 0934567, 'santina.s@example.com'),
(4, 'Tamara', 'Bianchini', 6734567, 'tamara.b@example.com'),
(5, 'Lucia', 'Siracusa', 5674567, 'lucia.s@example.com'),
(6, 'Lucia', 'Barrero', 9384567, 'lucia.b@example.com'),
(7, 'Marta', 'Escriva', 9864567, 'marta.e@example.com'),
(8, 'Adriana', 'Picatto', 1554567, 'adriana.p@example.com');

INSERT INTO members (person_id, membership) VALUES
(1, 0), (2, 0), (3, 1), (4, 1), (5, 0), (6, 1), (7, 0), (8, 1);

INSERT INTO practitioners_birthday (person_id, birthday) VALUES
(1, '1989-12-07'), (2, '1989-06-22'), (3, '2002-09-11'), (4, '1990-10-27'),
(5, '1984-07-17'), (6, '1983-11-02'), (7, '1989-11-15'), (8, '1970-03-01');

INSERT INTO fitness_activities (person_id, first_activity, second_activity) VALUES
(1, 'yoga', 'pilates'), (2, 'yoga', NULL), (3, 'pilates', NULL), (4, 'pilates', 'yoga'),
(5, 'yoga', NULL), (6, 'pilates', 'yoga'), (7, 'pilates', NULL), (8, 'yoga', 'pilates');

-- 3. BUSINESS LOGIC & AUTOMATION
-- ---------------------------------------------

-- Procedure to streamline new practitioner onboarding
DELIMITER //
CREATE PROCEDURE InsertValuefitness_practitioners(
    IN p_id INTEGER, IN p_name VARCHAR(50), IN p_surname VARCHAR(50),
    IN p_tel INT, IN p_email VARCHAR(100)
)
BEGIN
    INSERT INTO fitness_practitioners (person_id, name, surname, telephone, email)
    VALUES (p_id, p_name, p_surname, p_tel, p_email);
END //
DELIMITER ;

-- Function: Calculate multi-activity discount
DELIMITER //
CREATE FUNCTION have_discount (second_activity VARCHAR(50))
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    RETURN IF(second_activity IS NOT NULL, 'Eligible for Discount', 'Standard Rate');
END//
DELIMITER ;

-- Function: Loyalty Reward - Free Birthday Class
DELIMITER //
CREATE FUNCTION have_freeclass (birthday DATE)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    RETURN IF(MONTH(NOW()) = MONTH(birthday), 'Free Class Available', 'No Reward This Month');
END//
DELIMITER ;

-- 4. ANALYTICS & REPORTING QUERIES
-- ---------------------------------------------

-- Complex View: Members enrolled in multiple activities
SELECT t1.name, t2.first_activity, t2.second_activity, t3.membership
FROM fitness_practitioners t1
LEFT JOIN fitness_activities t2 ON t1.person_id = t2.person_id
LEFT JOIN members t3 ON t2.person_id = t3.person_id
WHERE t2.second_activity IS NOT NULL AND t3.membership = 0;