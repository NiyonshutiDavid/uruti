import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('uruti.db')
cursor = conn.cursor()

# Query to retrieve all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Fetch all results
tables = cursor.fetchall()

# Display each table name
for table in tables:
    print(table[0])

# Close the connection
conn.close()
