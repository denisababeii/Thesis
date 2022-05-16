import pandas as pd
import mysql.connector

# Import CSV
data = pd.read_excel('grades.xlsx') 
df = pd.DataFrame(data)

# Connect to SQL Server
conn=mysql.connector.connect(host="localhost", user="root", password="", database="elective_recommender")
cursor = conn.cursor()

count=0
# Insert DataFrame to Table
for row in df.itertuples():
    record = (row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])
    cursor.execute(
                '''
                INSERT INTO `grades`(`Object_oriented_programming`, `Data_structures_and_algorithms`, `Database_management_systems`, `Computer_systems_architecture`, `Functional_and_logic_programming`, `Artificial_intelligence`, `Formal_languages_and_compiler_design`, `Operating_systems`, `Mobile_application_programming`, `Computer_networks`, `Elective_1`, `Elective_2`, `Elective_3`, `Elective_1_Mark`, `Elective_2_Mark`, `Elective_3_Mark`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''', record
    )
    conn.commit()
cursor.close()
conn.close()