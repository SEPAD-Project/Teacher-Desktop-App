import mysql.connector
from mysql.connector import Error

def get_students_by_class_code(unic_class_code):
    """
    Retrieve national IDs of students in a specific class code from MySQL database.
    Returns list of national IDs or appropriate error message.
    """
    conn = None
    cursor = None
    try:
        # Connect to MySQL database (replace with your credentials)
        conn = mysql.connector.connect(
            host="185.4.28.110",
            database='sap',
            user='root',
            password='sapprogram2583',
            port=5000
        )
        
        cursor = conn.cursor()
        print(f'class code given in get students is {unic_class_code}')
        # Parameterized query to prevent SQL injection
        query = "SELECT student_national_code FROM students WHERE class_code = %s"
        cursor.execute(query, (unic_class_code,))
        
        # Fetch all results as list of tuples
        students = cursor.fetchall()
        print(students)
        
        # Return message if no students found
        if not students:
            return [False, "No students found in this class"]
            
        # Extract national IDs from tuples and return as list
        return [True, [student[0] for student in students]]
        
    except Error as e:
        # Handle MySQL specific errors
        return [False, f"Database Error: {str(e)}"]
    except Exception as e:
        # Handle other unexpected errors
        return [False, f"Unexpected Error: {str(e)}"]
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Example usage
if __name__ == "__main__":
    class_code = input("Enter class code: ")
    result = get_students_by_class_code(class_code)
    
    print("National IDs of students:")
    print(result)
