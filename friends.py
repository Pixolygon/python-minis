import sqlite3
# OPEN CONNECTION
con = sqlite3.connect("friends.db")

# CREATE CURSOR OBJECT
c = con.cursor()

# CREATE TABLES
# creation_query = '''
#     CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);
#     '''
# c.execute(creation_query)

# INSERT DATA INTO TABLES
# insert_query = '''
#     INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7);
#     '''
# c.execute(insert_query)

# INSERT SINGLE PIECE OF FULL DATA
# form_first = "Mary-Todd"
# query = '''
#     INSERT INTO friends (first_name) VALUES (?)
#     '''
# c.execute(query, (form_first,))

# INSERT FULL DATA
# form_data = ("Steve", "Irwin", 9)
# query = '''
#     INSERT INTO friends VALUES (?,?,?);
#     '''
# c.execute(query, form_data)

# BULK INSERT
# people = [
#     ("Roald", "Amundsen", 5),
#     ("Rosa", "Parks", 8),
#     ("Henry", "Hudson", 7),
#     ("Neil", "Armstrong", 7),
#     ("Daniel", "Boone", 3),
# ]
# # c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print(f"Inserting {person}.")

# SELECTING FROM THE DB
# c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
# for result in c:
#     print(result)
# print(c.fetchall())  # prints single list of all data
# print(c.fetchone())

# COMMIT CHANGES
con.commit()

# CLOSE CONNECTION
con.close()
