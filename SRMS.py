import sqlite3
db = sqlite3.connect('SRMS.db')
cursor = db.cursor()


def main():
    userInput = -1
    while(userInput != "0"):
        print("\n Some options you may choose:")
        print("1: Print Players")
        print("2: Print Teachers")
        print("3: Print Matches")
        print("4: Insert Department")
        print("5: Update your Exam")
        print("6: Delete player")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printPlayers()
        if userInput == "2":
            printTeachers()
        if userInput == "3":
            printMatches()
        if userInput == "4":
            insertDepartment()
        if userInput == "5":
            UpdateExam()
        if userInput == "6":
            deletePlayer()
        if userInput == "0":
            print("Ending software...")
    db.close()
    return

############## Do not touch part ends ##############
####################################################


############## Please modify the following ##############
def printPlayers():
    print("Printing players")
    """
    Insert the correct Python and SQL commands
    to print all players
    """
    # Start your modifications after this comment

    return


def printTeachers():
    print("Printing Teachers")
    """
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    # Start your modifications after this comment

    cursor.execute("SELECT * FROM Teacher")
    print(cursor.fetchall())
    return


def printMatches():
    print("Printing matches")
    """ 
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    # Start your modifications after this comment

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
    db.close()

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
    db.close()

    return


def deletePlayer():
    playerID = input("What is the player's PlayerID? ")
    """ 
    Using the correct Python and SQL comands:
    Delete the Player and his Ranking information
    Additionally, set the playerid to NULL in ALL match-data it is found
    """
    # Start your modifications after this comment


main()
