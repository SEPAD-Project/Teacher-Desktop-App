from database_handler import DatabaseHandler
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



def get_class_id(class_name):
    db = DatabaseHandler(
            host=ip_address,
            database=db_name,
            user=user,
            password='sapprogram2583',
            port=port
        )
    print("class name received in 'get_class_school_id.py' is {}".format(class_name))
    class_id = db.get_class_id(class_name=class_name)
    return class_id

def get_school_id(school_code):
    db = DatabaseHandler(
            host=ip_address,
            database=db_name,
            user=user,
            password='sapprogram2583',
            port=port
        )
    print("school code received in 'get_class_school_id.py' is {}".format(school_code))
    school_id = db.get_school_id(school_code=school_code)
    return school_id

