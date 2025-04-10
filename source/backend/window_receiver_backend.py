import requests
import threading
import queue
import time
import os 
import configparser

config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
config = configparser.ConfigParser()
config.read(config_path)

ip_address = config['Server']['IP']
port = int(config['Server']['Open_window_port'])

class StudentMonitorBackend:
    def __init__(self, school, class_name, student_id):
        self.server_url = f'http://{ip_address}:{port}'
        self.school = school
        self.class_name = class_name
        self.student_id = student_id
        self.data_queue = queue.Queue()
        self.stop_event = threading.Event()
        
    def _fetch_data(self):
        """Fetch data from server with error handling"""
        try:
            params = {
                'school': self.school,
                'class': self.class_name,
                'student_id': self.student_id
            }
            
            response = requests.get(
                f'{self.server_url}/get',
                params=params,
                timeout=5
            )
            
            if response.status_code == 200:
                return response.json()
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"Network error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
        return None

    def _monitoring_loop(self):
        """Main data fetching loop"""
        while not self.stop_event.is_set():
            data = self._fetch_data()
            if data:
                self.data_queue.put(data)
            time.sleep(10)

    def start_monitoring(self):
        """Start background monitoring thread"""
        self.thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.thread.start()

    def stop_monitoring(self):
        """Stop monitoring thread"""
        self.stop_event.set()
        self.thread.join(timeout=1)

    def get_latest_data(self):
        """Get latest data from queue"""
        try:
            return self.data_queue.get_nowait()
        except queue.Empty:
            return None