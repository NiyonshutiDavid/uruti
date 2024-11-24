import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('uruti.db')
cursor = conn.cursor()

# Query to retrieve all users from the users table
cursor.execute("SELECT * FROM entrepreneurs")

# Fetch all results
entrepreneurs = cursor.fetchall()

# Display each user
for user in entrepreneurs:
    print(user)

# Close the connection
conn.close()
