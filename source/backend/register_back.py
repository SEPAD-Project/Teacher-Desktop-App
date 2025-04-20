from database_handler import DatabaseHandler
import json
import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
config = configparser.ConfigParser()
config.read(config_path)

ip_address = config['Database']['Host']
db_name = config['Database']['Database']
port = int(config['Database']['DB_port'])
user = config['Database']['User']
password = config['Database']['Password']

def register_btn_func(first_name, last_name, national_code, password, lesson):
    # checking that all fields are filled
    if not all([first_name, last_name, national_code, password, lesson]):
        return "Fill in all the fields"

    # db config
    db_handler = DatabaseHandler(
            host=ip_address,
            database=db_name,
            user=user,
            password='sapprogram2583',
            port=port
        )
    try:
        classes_list = []
        classes = json.dumps(classes_list)
        
        # checking natoinal code exist or not
        if db_handler.national_code_exists(national_code):
            return "exist"

        # adding teacher
        if db_handler.add_teacher(first_name, last_name, national_code, password, str(classes), lesson):
            return "registered"
        return "error"
    
    except Exception as e:
        print(str(e))
    


if __name__ == '__main__':
    print(register_btn_func('ali', 'sharifi', '093222', 'supsecpas'))