import requests
import time

# آدرس سرور
server_url = "http://localhost:5001"

# school and class
school_name = input("Enter school name: ").strip()
class_code = input("Enter class code: ").strip()

# getting students list
response = requests.post(f"{server_url}/get_students", json={"school_name": school_name, "class_code": class_code})

if response.status_code != 200:
    print("Error while fetching students:", response.json().get("error", "Unknown error"))
    exit()

students = response.json().get("students", [])
print("Students in class:", students)

if not students:
    print("No students found in this class.")
    exit()

# getting students message and show them
def fetch_messages():
    while True:
        for student in students:
            response = requests.post(f"{server_url}/get_last_message", json={
                "school_name": school_name,
                "class_code": class_code,
                "student_name": student
            })
            if response.status_code == 200:
                data = response.json()
                print(f"{data['student']}: {data['message']}")
            else:
                print(f"Error fetching message for {student}")
        
        print("\n--- Waiting for next update ---\n")
        time.sleep(30)

fetch_messages()
