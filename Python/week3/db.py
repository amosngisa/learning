import mysql.connector

from mysql.connector import Error

import pandas as pd

###############################################################################################################################################
# A function to connect to our mysql server
def create_connection(host_name,user_name,password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = password,
            database = db_name
        )
        # print("MySQL connection has been successful")
    except Error as error:
        print(f"Error: {error}")
        
    return connection

connection = create_connection("localhost", "root", "","school")

##################################################################################################################################################
# Creating database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
        
    except Error as error:
        print(f"Error: {error}")
        
# query = "CREATE database school"
# create_database(connection, query)

#####################################################################################################################################################
# Creating tables
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query succesful")
    except Error as error:
        print(f"Error: {error}")
        

create_table_teacher = """
CREATE TABLE teacher (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    dob DATE,
    phone_no VARCHAR(13)
);
"""
create_table_client = """
CREATE TABLE client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40),
    industry VARCHAR(20)
)
"""

create_table_course = """
CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(40),
    level VARCHAR(2),
    start_date DATE,
    teacher INT,
    cliennt INT
)
"""
#execute_query(connection, create_table_teacher)

###########################################################################################################################################################
# populating tables
pop_teacher = """
INSERT INTO teacher VALUES 
(1, 'Amos', 'Ngisa', '1998-10-10', '0707772715');

"""

pop_client = """
INSERT INTO client VALUES
(1, 'Allan Kioko', 'Software Development'),
(2, 'Joan Mwangi', 'Software Development'),
(3, 'Shawn Muriithi', 'Software Development'),
(4, 'Teddy Oloo', 'Software Development');
"""

pop_course = """
INSERT INTO course VALUES
(1, 'JavaScript', '05', '2024-05-20', 1, 1),
(2, 'JavaScript', '05', '2024-05-20', 1, 2),
(3, 'JavaScript', '05', '2024-05-20', 1, 3),
(4, 'JavaScript', '05', '2024-05-20', 1, 4),
(5, 'Python', '07', '2024-07-20', 1, 1),
(6, 'Python', '07', '2024-07-20', 1, 2)
"""
# execute_query(connection, pop_course)

##################################################################################################################################################################
# creating relationships
alter_course = """
ALTER TABLE course
ADD FOREIGN KEY(teacher)
REFERENCES teacher(teacher_id)
ON DELETE SET NULL;
"""

alter_course_again = """
ALTER TABLE course
ADD FOREIGN KEY(cliennt)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

#execute_query(connection, alter_course)

#######################################################################################################################################################################
# creating read query of data from db
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as error:
        print(f"Error: {error}")


q1 = """
SELECT *
FROM teacher;

"""

q2 = """
SELECT course.course_id, course.course_name, client.client_name
FROM course
JOIN client
ON course.cliennt = client.client_id

"""

results = read_query(connection, q1)

mylist = []

for result in results:
    result = list(result)
    mylist.append(result)
    
print(mylist)

########################################################################################################################################################
# formating output into pandas dataframe
# columns = ["Course Id", "Course Name", "Student Name"]
# data_f = pd.DataFrame(mylist, columns=columns)

# display(data_f)
# print(data_f)

#######################################################################################################################################################
# updating records
update = """
UPDATE teacher 
SET phone_no = '0781883760'
WHERE teacher_id = 1;

"""

execute_query(connection, update)