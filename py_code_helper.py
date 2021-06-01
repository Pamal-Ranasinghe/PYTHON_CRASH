import sqlite3 as lite



#functions are starting
class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print('unabled to craete a db')

    # TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return False

    # TODO: create data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall();
        except Exception:
            return False

    # TODO: create data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False
    




# TODO:provide interface to user

def main():
    print("*"*40)
    print("\n::COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\nPress 1. Insert a new Course\n')
    print('Press 2. show all courses\n')
    print('Press 3. Delete a course (NEED ID OF COURSES)\n')  
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice : ")

    if choice == "1":
        name = input("\n Enter course name : ")
        description = input("\n Enter course description : ")
        price = input("\n Enter course price : ")
        private = input("\n Is this course private (0/1): ")

        if db.insert_data([name, description, price, private]):
            print('Course was inserted successfully')
        else:
            print("OOPS something went wrong")

    elif choice == "2":
        print("\n :: Course List :: ")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("\n Course ID no : " + str(item[0]))
            print("\n Course Name : " + str(item[1]))
            print("\n Course Descriptiom : " + str(item[2]))
            print("\n Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Is private : " + private)
            print("\n")

    elif choice == "3":
        record_id = input("Enter the course ID : ")
        
        if db.delete_data(record_id):
            print("Course deleted")
        else:
            print("OOPS went something went wrong")

    else:
        print("\n BAD CHOICE")

            
if __name__ == '__main__' : 
    main()