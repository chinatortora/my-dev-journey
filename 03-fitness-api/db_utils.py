import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    """Custom exception for database connection issues."""
    pass


def _connect_to_db(db_name):
    """Establishes a connection to the MySQL database."""
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return cnx
    except Exception as e:
        raise DbConnectionError(f"Error connecting to database: {e}")


def _map_values(schedule):
    """Transforms raw SQL schedule data into a readable dictionary format."""
    mapped = []
    for item in schedule:
        mapped.append({
            'Activity': item[0].capitalize(),
            'Monday': 'Available' if item[1] else 'Not Available',
            'Tuesday': 'Available' if item[2] else 'Not Available',
            'Wednesday': 'Available' if item[3] else 'Not Available',
            'Thursday': 'Available' if item[4] else 'Not Available',
            'Friday': 'Available' if item[5] else 'Not Available',
        })
    return mapped


def get_schedule():
    """Retrieves the weekly class availability from the database."""
    db_name = 'fitness_reservations'
    db_connection = None
    try:
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        query = "SELECT * FROM classes_per_day"
        cur.execute(query)
        result = cur.fetchall()
        return _map_values(result)
    except Exception:
        raise DbConnectionError("Failed to fetch schedule data")
    finally:
        if db_connection:
            db_connection.close()


def new_booking(person_id, activity, day):
    """Registers a new class reservation in the database."""
    db_name = 'fitness_reservations'
    db_connection = None
    try:
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        query = "INSERT INTO reservations (person_id, activity, day) VALUES (%s, %s, %s)"
        cur.execute(query, (person_id, activity, day))
        db_connection.commit()
    except Exception as e:
        raise DbConnectionError(f"Failed to create booking: {e}")
    finally:
        if db_connection:
            db_connection.close()


def get_reservation():
    """Retrieves the most recent reservation data for confirmation."""
    db_name = 'fitness_reservations'
    db_connection = None
    try:
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        query = "SELECT * FROM reservations ORDER BY reservation_id DESC LIMIT 1"
        cur.execute(query)
        result = cur.fetchone()

        if result:
            return [{
                'ID': result[0],
                'User_ID': result[1],
                'Activity': result[2].capitalize(),
                'Day': result[3].capitalize()
            }]
        return []
    except Exception:
        raise DbConnectionError("Failed to fetch reservation confirmation")
    finally:
        if db_connection:
            db_connection.close()