import requests

# server address
server_url = "http://185.4.28.110:5001"

# getting students list
def get_students_list(school_name, class_code):
    '''
    Returns the list of students of the desired school name (school code)

    Args:
        school_name : school code to connect to directory of school
        class_code : class code to find class name and connect to direcctory of that class
    '''
    try:
        response = requests.post(f"{server_url}/get_students", json={"school_name": school_name, "class_code": class_code}, timeout=3)
        print(f'this is school path (school name) : {school_name}')
        print(f'this is class path (class code) : {class_code}')
        if response.status_code != 200:
            return [False, 'no school or class found'] # , response.json().get("error", "Unknown error")
        else:
            students = response.json().get("students", [])
            if not students:
                return [False, 'No Students found']
            else:
                return [True, students]
    except ConnectionError:
        return [False, 'ConnetionError']
    except Exception as e:
        return [False, e]

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
        

