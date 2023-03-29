# Connect to the database
import sqlite3

# Connect to the database
conn = sqlite3.connect('DatabaseName.db')
# ...
cursor = conn.cursor()

# SQL query execution
params = ('RUS', 0.5)
cursor.execute("""
    SELECT
        Language, Percentage
    FROM countrylanguage
    WHERE 
        CountryCode = %s AND
        Percentage > %s""", params)

rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()