import mysql.connector

def get_values_by_username(value, person, host='localhost', user='root', password='ardbms', database='sap'):
    # connetcting to db
    db = mysql.connector.connect(
    host="185.4.28.110",  
    user="root",
    port=5000,   
    password="sapprogram2583",
    database=database
    )
    value = str(value)
    cursor = db.cursor()
    if person == 'student' :
        cursor.execute("SELECT COUNT(*) FROM students WHERE student_national_code = '{}'".format(value))
        result = cursor.fetchone()
        print(result)
        if result[0] > 0:
            cursor.execute('SELECT student_name, student_family, student_password, class_code, student_national_code, school_code class FROM students WHERE student_national_code = %s', (value,))

            udata = cursor.fetchone()
            cursor.close()
            db.close()

            if udata:
                print(udata)
                return(udata)
            else:
                return(False)
        else:
            cursor.close()
            db.close()
            return ('not found')
        
    elif person == 'teacher' :
        cursor.execute("SELECT COUNT(*) FROM teachers WHERE teacher_national_code = %s", (value,))
        result = cursor.fetchone()
        teacher_class_codes = []
        if result[0] > 0: # if user exist, return his/her information including password
            cursor.execute('SELECT teacher_name, teacher_family, teacher_password, id FROM teachers WHERE teacher_national_code = %s', (value,))
            result = cursor.fetchone()
            print('result is : {}'.format(result))
            # print(f'this is result : {[f"{i}:{result.index(i)}" for i in result]}')
            cursor.execute('SELECT class_id FROM teacher_class WHERE teacher_id = %s', (result[3],))
            class_ids = cursor.fetchall()
            class_id_list = [i[0] for i in class_ids]
            for i in class_id_list:
                cursor.execute('SELECT class_code FROM classes WHERE id = %s', (i,))
                class_code = cursor.fetchone()
                teacher_class_codes.append(class_code[0])
                print(f"class code index {i} is {class_code[0]}")
            for i in result :
                print(i)
            final_result = [i for i in result]
            final_result.append(teacher_class_codes)
            print(f"this is final result : {final_result}")
            print(class_ids)
            print(class_id_list)
            cursor.close()
            db.close()

            if result:
                return(final_result)
            else:
                return(False)
        else:
            cursor.close()
            db.close()
            return ('not found') # returning not found if user not exists

def get_class_name(school_code):
    '''Returns school name by its code'''
    db = mysql.connector.connect(
    host="185.4.28.110",  
    user="root", 
    port=5000,   
    password="sapprogram2583",
    database='sap'
    )
    cursor = db.cursor()
    cursor.execute(f'SELECT school_name FROM schools WHERE school_code = {school_code}')
    result = cursor.fetchone()
    print(f'school code is {school_code}')
    print(result)
    return result[0]

def get_students_name_by_national_code(national_code):
    print(national_code)
    db = mysql.connector.connect(
    host="185.4.28.110",  
    user="root", 
    port=5000,   
    password="sapprogram2583",
    database='sap'
    )
    cursor = db.cursor()
    cursor.execute(f'SELECT student_name, student_family FROM students WHERE student_national_code = {national_code}')
    result = cursor.fetchone()
    if result is not None:
        name = result[0] + ' ' + result[1]
        return name
    else:
        print(result)
        

if __name__ == '__main__' :
    get_students_name_by_national_code('09295')