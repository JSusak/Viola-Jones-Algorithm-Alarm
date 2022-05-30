import sqlite3


connection = sqlite3.connect("sqliteLogs/faceLogs.db")

cursor = connection.cursor()

# Define schema
c1 = """CREATE TABLE IF NOT EXISTS
faces(log_id INTEGER PRIMARY KEY, dateLogged DATE)"""

cursor.execute(c1)

c2 = """CREATE TABLE IF NOT EXISTS
facesLink(log_id INTEGER, picLink STRING, FOREIGN KEY(log_id) REFERENCES faces(log_id))"""

cursor.execute(c2)


def insertIntoFaces(log_id, dateLogged):
    cursor.execute("""INSERT INTO faces VALUES (?,?)""",(log_id, dateLogged))


def insertIntoFacesLink(log_id, stringLink):
    cursor.execute("""INSERT INTO facesLink VALUES (?,?)""",(log_id, stringLink))


# Getting the most recently inserted row: "SELECT * FROM TableName ORDER BY rowid DESC LIMIT 1;"


def getLastRowFaces():
    last_row = cursor.execute(
        "select * FROM faces ORDER BY log_id DESC LIMIT 1;"
    ).fetchone()
    print("The last row saved into the faces table @ faceLogs.db was: ", last_row) if (last_row != None) else print(
        "There is currently nothing inside the faces table - nothing has been printed."
    )


def getLastRowFacesLink():
    last_row = cursor.execute(
        "select * FROM facesLink ORDER BY log_id DESC LIMIT 1;"
    ).fetchone()

    print("The last row saved into the facesLink table @ faceLogs.db was: ", last_row) if (last_row != None) else print(
        "There is currently nothing inside the facesLink table - nothing has been printed."
    )
