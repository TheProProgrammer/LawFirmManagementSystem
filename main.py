import sqlite3


def main():
    run = 1
    conn = sqlite3.connect('LawFirmDB.db')
    c = conn.cursor()
    while run == 1:
        entered_username = input("Username: ")
        entered_password = input("Password: ")
        if format_data(c.execute("SELECT username FROM users")).__contains__(entered_username) and format_data(c.execute("SELECT password FROM users WHERE username = '" + entered_username + "\'")).__contains__(entered_password):
            print("Login successful")
            user_type_query = "SELECT type FROM users WHERE username = '" + entered_username + "\'"
            if format_data(c.execute(user_type_query)).__contains__("client"):
                client_data = c.execute("SELECT * FROM clients_data WHERE name = '" + entered_username + "\'").fetchall()
                print("_________USER DATA_________")
                print("Name:", entered_username)
                print("CNIC:", client_data[0][1])
                print("City:", client_data[0][2])
                print("Phone: +92", client_data[0][3])
                print("")
                print("_________CASES DATA_________")
                cases_data = c.execute("SELECT * FROM cases_data WHERE client = '" + entered_username + "\'").fetchall()
                for case in cases_data:
                    print("Case Title:", entered_username, "versus", case[1])
                    print("Court:", case[2])
                    print("Judge:", case[3])
                    print("Status:", case[4])
                    print("Lawyer:", case[5])
                    print("")
                print("PLEASE CONTACT DBA IF DATA IS INVALID")
            elif format_data(c.execute(user_type_query)).__contains__("lawyer"):
                lawyer_data = c.execute("SELECT * FROM lawyers_data WHERE name = '" + entered_username + "\'").fetchall()
                print("_________USER DATA_________")
                print("Name:", entered_username)
                print("CNIC:", lawyer_data[0][1])
                print("Experience:", lawyer_data[0][2])
                print("Education:", lawyer_data[0][3])
                print("Speciality:", lawyer_data[0][4])
                print("")
                print("_________CASES DATA_________")
                cases_data = c.execute("SELECT * FROM cases_data WHERE lawyer = '" + entered_username + "\'").fetchall()
                for case in cases_data:
                    print("Case Title:", case[0], "versus", case[1])
                    print("Court:", case[2])
                    print("Judge:", case[3])
                    print("Status:", case[4])
                    print("")
                print("PLEASE CONTACT DBA IF DATA IS INVALID")
            elif format_data(c.execute(user_type_query)).__contains__("admin"):
                selection = eval(input("Which DataBase would you like edit:\n1.Clients\n2.Lawyers\n3.Cases\n4.Users\n"))
                if(selection == 1):
                    name = input("Enter Client Name:")
                    CNIC = input("Enter Cnic:")
                    City = input("Enter Enter City:")
                    phone = input("Enter Phone Number:")
                    c.execute("INSERT INTO clients_data VALUES (\'"+name+"\', \'"+CNIC+"\', \'"+City+"\', \'"+phone+"\')")
                elif (selection == 2):
                    name = input("Enter Lawyer Name:")
                    CNIC = input("Enter Cnic:")
                    Experience = input("Enter Experience:")
                    Education = input("Enter Education:")
                    Speciality = input("Enter Education:")
                    c.execute("INSERT INTO lawyers_data VALUES (\'" + name + "\', \'" + CNIC + "\', \'" + Experience + "\', \'" + Education + "\', \'" + Speciality + "\')")
                elif (selection == 3):
                    client = input("Enter Client Name:")
                    versus = input("Enter Versus:")
                    court = input("Enter court:")
                    judge = input("Enter Judge name:")
                    status = input("Enter status:")
                    lawyer = input("Enter lawyer Name:")
                    c.execute(
                        "INSERT INTO cases_data VALUES (\'" + client + "\', \'" + versus + "\', \'" + court + "\', \'" + judge + "\', \'" + status + "\', \'" + lawyer + "\')")
                elif (selection==4):
                    new_username = input("Enter new username:")
                    new_password = input("Enter new password:")
                    new_type = input("Enter new user type:")
                    c.execute("INSERT INTO users VALUES (\'"+new_username+"\',\'"+new_password+"\',\'"+new_type+"\')")
                else:
                    print("Invalid response")
        else:
            print("Invalid Credentials")

        if input("Run again? y/n: ") == 'y':
            run = 1
        else:
            run = 0
    print("Thank you for using LFDBMS!")
    conn.commit()
    conn.close()


def format_data(data):
    data2 = []
    for entry in data:
        data2.append(str(entry).replace("(", "").replace(")", "").replace(",", "").replace("\'", "").replace("[", "").replace("]", ""))
    return data2

main()
