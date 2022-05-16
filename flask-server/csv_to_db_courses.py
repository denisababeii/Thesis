import pandas as pd
import mysql.connector

# Import CSV
data = pd.read_excel('courses.xlsx') 
df = pd.DataFrame(data)

# Connect to SQL Server
conn=mysql.connector.connect(host="localhost", user="root", password="", database="elective_recommender")
cursor = conn.cursor()

# Insert DataFrame to Table
for row in df.itertuples():
    record = (row.Name, row.Description, row.Type, row.Semester, row.Package, row.Link)
    cursor.execute(
                '''
                INSERT INTO courses (name, description, type, semester, package, link)
                VALUES (%s,%s,%s,%s,%s,%s)
                ''', record
    )
    conn.commit()
cursor.close()
conn.close()