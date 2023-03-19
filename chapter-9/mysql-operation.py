import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="mysql", db="chap9")
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

def updatedata():
    cur.execute("update student set stipend=5000 where name='Ritu'")
    print("Record updated")
    db.commit()

def deldata():
    cur.execute("delete from student where name='Ritu'")
    print("Record deleted")
    db.commit()

c = "y"
while c == "y":
    print("1. Add record")
    print("2. Update record")
    print("3. Delete record")
    print("4. Display record")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        adddata()
    elif ch == 2:
        updatedata()
    elif ch == 3:
        deldata()
    elif ch == 4:
        fetchdata()
    elif ch == 5:
        c = "n"
    else:
        print("Wrong input. Try again")

    
    