import requests
import os 
import configparser

config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
config = configparser.ConfigParser()
config.read(config_path)

ip_address = config['Server']['IP']
port = int(config['Server']['Open_window_port'])

def get_active_window_from_server(school, class_name, student_id):
    """
    Get the active window from the server.

    Parameters:
    school (str): School name
    class_name (str): Class name
    student_id (str): Student ID

    Returns:
    str: Active window title or error message
    """
    try:
        # Prepare query parameters
        params = {
            'school': school,
            'class': class_name,
            'student_id': student_id
        }
        
        # Send GET request to the server
        response = requests.get(
            f"http://{ip_address}:{port}/get",
            params=params,
            timeout=5
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data.get('active', 'No active window found')
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"
            
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return f"Connection failed: {str(e)}"
    except Exception as e:
        # Handle unexpected errors
        return f"Unexpected error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    SCHOOL = "Test School"                # School name
    CLASS = "Class A"                     # Class name
    STUDENT_ID = "STD123"                 # Student ID
    
    # Fetch and display the active window
    active_window = get_active_window_from_server(SCHOOL, CLASS, STUDENT_ID)
