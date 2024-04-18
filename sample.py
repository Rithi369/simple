import sqlite3
con = sqlite3.connect('student.db')
cursor = con.cursor()

def student_exist(regno):
    sql = ''' create table if not exists student(regno integer primary key,name varchar(10), mark1 int, mark2 int, mark3 int)'''
    cursor.execute(sql)
    data = (regno,)
    sql = "select * from student where regno=?"
    cursor.execute(sql, data)
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False

def add_student():
    regno=int(input("Enter Student Register Number:"))
    if (student_exist(regno) == True):
        print("Student Already Exists \n Try Again\n")
    else:
        name=input("Enter Student Name:")
        mark1=int(input("Enter Mark in Subject1:"))
        mark2= int(input("Enter Mark in Subject2:"))
        mark3= int(input("Enter Mark in Subject3:"))
        data = (regno,name,mark1,mark2,mark3)
        sql="Insert into student values(?,?,?,?,?)"
        cursor.execute(sql,data)
        con.commit()
        print("Student Added Succecfully")

def dispaly_student():
    cursor.execute("select * from student")
    result = cursor.fetchall()
    if len(result) > 0 :
        for i in result :
            print("Student Regno:", i[0])
            print("Student Name:", i[1])
            print("Mark in Subject1:", i[2])
            print("Mark in Subject2:", i[3])
            print("Mark in Subject3:", i[4])
            print('_______________________________________')
    else:
            print("No Record Exists")


def remove_student():
    regno = input("Enter the register number of student to be removed:")
    if (student_exist(regno) == False):
        print("Student does not exist\n Try again")

    else:
        sql = "Delete from student where regno=?"
        data = (regno,)
        cursor.execute(sql, data)
        con.commit()
        print("student removed")


def menu():
    print("Select")
    print("1 To Add new student")
    print("2 To dispaly all student details")
    print("3. To remove particular student")
    print("4. To exit")
    ch = int(input("Enter your choice:"))
    if (ch == 1):
        add_student()
    elif ch == 2:
        dispaly_student()
    elif ch == 3:
        remove_student()
    elif ch == 4:
        exit()
    else:
        print("Invalid choice")
    menu()
menu()