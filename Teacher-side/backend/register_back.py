from database_handler import DatabaseHandler
import json

def register_btn_func(first_name, last_name, national_code, password):
    # checking that all fields are filled
    if not all([first_name, last_name, national_code, password]):
        return "Fill in all the fields"

    # db config
    db_handler = DatabaseHandler(
        host='185.4.28.110',
        user='root',
        port=5000, 
        password='sapprogram2583',
        database='sap'
    )

    try:
        classes_list = []
        classes = json.dumps(classes_list)
        
        # checking natoinal code exist or not
        if db_handler.national_code_exists(national_code):
            return "exist"

        # adding teacher
        if db_handler.add_teacher(first_name, last_name, national_code, password, str(classes)):
            return "registered"
        return "error"
    
    except Exception as e:
        return str(e)
    



print(register_btn_func('ali', 'sharifi', '093222', 'supsecpas'))