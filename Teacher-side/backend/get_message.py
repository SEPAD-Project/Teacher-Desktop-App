import requests

# server address
server_url = "http://185.4.28.110:5001"

# getting students message and show them
def fetch_messages(student, school_name, class_code):
    response = requests.post(f"{server_url}/get_last_message", json={
            "school_name": school_name,
            "class_code": class_code,
            "student_name": student
    }, timeout=3)
    if response.status_code == 200:
        data = response.json()
        return [True, data['message']]
    else:
        return [False, 'Error']
        