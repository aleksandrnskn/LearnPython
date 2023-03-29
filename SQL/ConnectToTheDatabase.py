import sqlite3

# Connect to the database
conn = sqlite3.connect('DatabaseName.db')
cursor = conn.cursor()

# SQL query execution
cursor.execute("SELECT * FROM tablename")

# Get the data
row = cursor.fetchone()
print(row)

# Close the connection
conn.close()