import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="mysql", database="chap9")
cur = db.cursor()

def fetchdata():
    cur.execute("select * from student;")
    result = cur.fetchall()
    for x in result:
        print(x)

def adddata():
    cur.execute("insert into student values('Ritu', 4000, 'Science', 345, 'B', 11)")
    cur.execute("insert into student values('Ankush', 6000, 'Commce', 445, 'A', 12)")
    cur.execute("insert into student values('Pihu', 3566, 'Humanis', 446, 'A', 11)")
    cur.execute("insert into student values('TInku', 8900, 'Science', 545, 'A+', 12)")
    db.commit()
    print("Records added")


    