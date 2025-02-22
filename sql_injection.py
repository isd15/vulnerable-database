import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# BAD: SQL Injection Vulnerable
user_input = input("Enter username: ")
query = f"SELECT * FROM users WHERE username = '{user_input}'"

cursor.execute(query)
print(cursor.fetchall())
