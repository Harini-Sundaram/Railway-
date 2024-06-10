import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

# def get_person_details():
#     try:
#         response = requests.get(f"{API_URL}/person_details")
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         st.error(f"Error fetching person details: {e}")
#         return []

def get_passengers():
    try:
        response = requests.get(f"{API_URL}/passengers")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching passengers: {e}")
        return []

# def create_person_detail(personid, email, age, ph_num, passengername):
#     person_data = {"personid": personid, "email": email, "age": age, "ph_num": ph_num, "passengername": passengername}
#     try:
#         response = requests.post(f"{API_URL}/person_details", json=person_data)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         st.error(f"Error creating person detail: {e}")
#         return {"error": "Failed to create person detail"}

def create_passenger(name, seatnumber, destination, foodpreference):
    passenger_data = {"name": name, "seatnumber": seatnumber, "destination": destination, "foodpreference": foodpreference}
    try:
        response = requests.post(f"{API_URL}/passengers", json=passenger_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error creating passenger: {e}")
        return {"error": "Failed to create passenger"}

st.title("Railway Management System")

# st.header("Create New Person Detail")
# person_id = st.number_input("Person ID", min_value=1, step=1)
# email = st.text_input("Email")
# age = st.number_input("Age", min_value=1, step=1)
# ph_num = st.text_input("Phone Number")
# person_passenger_name = st.text_input("Passenger Name (Person Detail)")

# if st.button("Create Person Detail"):
#     result = create_person_detail(person_id, email, age, ph_num, person_passenger_name)
#     st.write(result)

# st.header("List of Person Details")
# person_details = get_person_details()
# for person in person_details:
#     st.json(person)

st.header("Create New Passenger")
passenger_name = st.text_input("Passenger Name (Passenger)")
seat_number = st.number_input("Seat Number", min_value=1, step=1)
destination = st.text_input("Destination")
food_preference = st.selectbox("Food Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])

if st.button("Create Passenger"):
    result = create_passenger(passenger_name, seat_number, destination, food_preference)
    st.write(result)

st.header("List of Passengers")
passengers = get_passengers()
for passenger in passengers:
    st.json(passenger)
