import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Environment variables for database credentials
DB_NAME = os.getenv("DB_NAME", "railway")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5473")

# Database connection
conn = psycopg2.connect(
    database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
cur = conn.cursor()

# @app.route('/person_details', methods=['POST'])
# def create_person_detail():
#     try:
#         data = request.get_json()
#         cur.execute(
#             "INSERT INTO PersonDetails (PersonID, email, Age, ph_num, PassengerName) VALUES (%s, %s, %s, %s, %s) RETURNING PersonID",
#             (data['personid'], data['email'], data['age'], data['ph_num'], data['passengername'])
#         )
#         conn.commit()
#         return jsonify({"PersonID": cur.fetchone()[0]})
#     except Exception as e:
#         conn.rollback()
#         app.logger.error(f"Error creating person detail: {e}")
#         return jsonify({"error": "Failed to create person detail"}), 500

# @app.route('/person_details', methods=['GET'])
# def list_person_details():
#     try:
#         cur.execute("SELECT * FROM PersonDetails")
#         return jsonify(cur.fetchall())
#     except Exception as e:
#         app.logger.error(f"Error fetching person details: {e}")
#         return jsonify({"error": "Failed to fetch person details"}), 500

@app.route('/passengers', methods=['POST'])
def create_passenger():
    try:
        data = request.get_json()
        cur.execute(
            "INSERT INTO RailwayPassengers (Name, SeatNumber, Destination, FoodPreference) VALUES (%s, %s, %s, %s) RETURNING Name",
            (data['name'], data['seatnumber'], data['destination'], data['foodpreference'])
        )
        conn.commit()
        return jsonify({"Name": cur.fetchone()[0]})
    except Exception as e:
        conn.rollback()
        app.logger.error(f"Error creating passenger: {e}")
        return jsonify({"error": "Failed to create passenger"}), 500

@app.route('/passengers', methods=['GET'])
def list_passengers():
    try:
        cur.execute("SELECT * FROM RailwayPassengers")
        return jsonify(cur.fetchall())
    except Exception as e:
        app.logger.error(f"Error fetching passengers: {e}")
        return jsonify({"error": "Failed to fetch passengers"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
