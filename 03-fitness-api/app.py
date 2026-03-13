from flask import Flask, jsonify, request
from db_utils import get_schedule, new_booking, get_reservation

app = Flask(__name__)

@app.route('/activities', methods=['GET'])
def get_all_activities():
    """Endpoint: Get the full week schedule."""
    try:
        res = get_schedule()
        return jsonify(res), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/class_booking', methods=['POST'])
def add_booking():
    """Endpoint: Create a new class reservation."""
    booking_data = request.get_json()
    try:
        new_booking(
            person_id=booking_data['person_id'],
            activity=booking_data['activity'],
            day=booking_data['day']
        )
        return jsonify({"status": "Success", "message": "Booking created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/reservation', methods=['GET'])
def last_reservation():
    """Endpoint: Get confirmation of the last booking made."""
    try:
        res = get_reservation()
        return jsonify(res), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask server on port 5001
    app.run(debug=True, port=5001)