import sqlite3
db = sqlite3.connect('SRMS.db')
cursor = db.cursor()


def main():
    userInput = -1
    while(userInput != "0"):
        print("\n Some options you may choose:")
        print("1: Print Students ")
        print("2: Delete Teachers ")
        print("3: Print Marks ")
        print("4: Filtering Students ")
        print("5: Average Marks ")
        print("6: Insert Department ")
        print("7: Update your Exam ")
        print("8: Visualization ")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printStudents()
        if userInput == "2":
            deleteTeachers()
        if userInput == "3":
            printMarks()
        if userInput == "4":
            filterStudents()   
        if userInput == "5":
            averageMarks()    
        if userInput == "6":
            insertDepartment()
        if userInput == "7":
            UpdateExam()
        if userInput == "8":
            visualization()
        if userInput == "0":
            print("Ending software...")
    db.close()
    return

############## Do not touch part ends ##############
####################################################


############## Please modify the following ##############
def printStudents():
    print("Printing Students who took Chemistry in this semester")
    
    cursor.execute("SELECT S_Name, S_Mail FROM student JOIN Course WHERE Title  = 'Chemistry' GROUP BY S_Address_PostalCode")
    print(cursor.fetchall())
    
    db.commit()
    return
     

def deleteTeachers():
    print("Delete Teachers who has gmails. ")
    
    cursor.execute("DELETE FROM Teacher WHERE T_Mail LIKE '%l'")
    print(cursor.fetchall())

    print("Congratulation!Successfully Deleted. ")
    
    db.commit()
    return
   


def printMarks():
    print("Printing Marks and Department who lives in Helsinki")
    """ 
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    # Start your modifications after this comment

    cursor.execute(" SELECT ExamDesc, Marks, Dept_Name, S_Address_City, S_Mail FROM Exam JOIN Department JOIN student WHERE S_Address_City = 'helsinki' GROUP BY Marks ")
    print(cursor.fetchall())


    db.commit()
    return


def filterStudents():
    print("Delete Teachers who has gmails. ")
    
    cursor.execute("Select S_Name, S_Address_City, S_Address_Street, S_Phone, S_Mail, S_DOB, S_Address_PostalCode FROM student WHERE  S_Mail LIKE '%gmail' AND S_Address_City = 'helsinki' ORDER by S_Address_PostalCode ASC")
    print(cursor.fetchall())

    
    db.commit()
    return

def averageMarks():
    print(" The Average marks of the final exam is: ")
    
    cursor.execute("SELECT AVG(Marks) FROM Exam JOIN Department WHERE ExamDesc = 'FINAL'")
    print(cursor.fetchall())

    
    db.commit()
    return


   



def insertDepartment():
    print(" Please Insert a Department: ")
    

    departmentId = input('Department ID: ')
    departmentName = input('Department Name: ')
    studentId = input('Student ID: ')
    cursor.execute("""INSERT INTO Department(Dept_ID, Dept_Name, Stu_ID) VALUES (?,?,?) """,
                   (departmentId, departmentName, studentId))

    db.commit()
    print('Data entered successfully.')

    return


def UpdateExam():
    print(" Please Update the exam if your course ID is between 600 to 603 : ")
    #newMatchDate = input("What is the new matchdate you want to set?")

    
    # Start your modifications after this comment
    # #Course_ID = input('Course ID: ')
    #regID = input('Registration ID: ')
    #examDesc = input('Exam Description: ')

    print("Insert course ID between 600 to 603. ")

    courseID = input('Course ID: ')
    marks = input('Marks: ')
    #deptID = input('Dept_ID: ')
    

    #cursor.execute("""Update Exam SET Reg_No = , Marks = marks, 
    #Dept_ID = deptID, Course_ID = courseID  where Marks > 50 """)

    cursor.execute('UPDATE Exam SET Marks = ? WHERE  Course_ID = ? ', (marks,courseID))
    


    db.commit()
    print('Data Updated successfully.')

    return


def visualization():
    #playerID = input("What is the player's PlayerID? ")
    """ 
    Using the correct Python and SQL comands:
    Delete the Player and his Ranking information
    Additionally, set the playerid to NULL in ALL match-data it is found
    """
    # Start your modifications after this comment


main()
