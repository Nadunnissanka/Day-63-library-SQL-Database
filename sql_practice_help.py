import sqlite3

# create a database
database = sqlite3.connect("books-collection.db")

# create a cursor to interact with SQLite database
cursor = database.cursor()

# create a table inside database
# inside the brackets there is a sql create table syntax
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# SQL docs - https://www.w3schools.com/sql/sql_ref_create_table.asp

# to add data to created table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
database.commit()

# use SQL alchemy for SQL database integration

