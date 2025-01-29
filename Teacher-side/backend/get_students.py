import requests
import time

# server address
server_url = "http://localhost:5001"


# getting students list
def get_students_list(school_name, class_code):
    try:
        response = requests.post(f"{server_url}/get_students", json={"school_name": school_name, "class_code": class_code})

        if response.status_code != 200:
            return [False, 'no school or class found'] # , response.json().get("error", "Unknown error")
        else:
            students = response.json().get("students", [])
            if not students:
                return [False, 'No Students found']
            else:
                return [True, students]
    except Exception:
        return [False, 'Error']

# print(get_students_list('hn1', '1052'))


# getting students message and show them
def fetch_messages(student, school_name, class_code):
    response = requests.post(f"{server_url}/get_last_message", json={
            "school_name": school_name,
            "class_code": class_code,
            "student_name": student
    })
    if response.status_code == 200:
        data = response.json()
        return [True, data['message']]
    else:
        return [False, 'Error']
        
fetch_messages('Reza', 'hn1', '1052')

# fetch_messages()
