import sqlite3

def main():
    try:
        sqliteConnection = sqlite3.connect("Calendar.db")
        cursor = sqliteConnection.cursor()
        print("Connected to database.")

        print("---DATABASE EDITOR---\nCurrent academic calendar is set to UG Seniors.")
        print("Changing this database may lead to unexpected output.")

        q = "select name from sqlite_master where type='table';"
        cursor.execute(q)
        res = cursor.fetchall();
        print("Months in database: ", end='')
        for table in res:
            print(f"[{table[0]}] ", end='')
        print()

        while(True):
            ch = input("Exit? Y/N\n> ")
            if ch.lower() == 'y':
                break;
            month = input("Enter month: ")
            startday = int(input("Enter start day (0=MON, 1=TUE, etc.): "))
            totdays = int(input("Enter num of days in month: "))
            addMonth(cursor, month, startday, totdays)
            sqliteConnection.commit()
        
    except sqlite3.Error as error:
        print(f"Error: {error}")

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Connection terminated.")

def addMonth(cursor, month, startday, daytot):
    q = monthQuery(f"{month}")
    try:
        cursor.execute(q)
    except:
        q = f"select * from {month};"
        cursor.execute(q)
        res = cursor.fetchall();
        print(res)
        print(f"Data for {month} already exists. Override? Y/N")
        ch = input("> ")
        if ch.lower() != 'y':
            return
        else:
            print("Clear table? Y/N")
            ch = input("> ")
            if ch.lower() == 'y':
                q = f"drop table {month};"
                cursor.execute(q)
                addMonth(cursor, month, startday, daytot)
                return
            else:
                attemptUpdates(cursor, month)
                return

    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    dnum = startday # between 0 and 6

    for i in range(1, daytot+1):
        if days[dnum]=="SAT" or days[dnum] == "SUN":
            q = insertDate(month, i, "HOL")
        else:
            q = insertDate(month, i, days[dnum])
        
        cursor.execute(q)
        dnum = 0 if dnum==6 else dnum+1

    q = f"select * from {month};"
    cursor.execute(q)
    res = cursor.fetchall();
    print(res)
    attemptUpdates(cursor, month)
    return

def attemptUpdates(cursor, month):
    while(True):
        print("1.....Update day")
        print("2.....Exit")

        n = int(input("> "))

        if(n==2):
            break
        elif(n==1):
            date = int(input("Enter date: "))
            day = input("Enter val: ")
            q = updateDay(month, date, day)
            
            cursor.execute(q)

    q = f"select * from {month};"
    cursor.execute(q)
    res = cursor.fetchall();
    print(res)

    return

def monthQuery(month):
    return f"create table {month} (Date int primary key, Day varchar[3]);"
    
def insertDate(month, date, day):
    return f"insert into {month} (Date, Day) VALUES ({date}, '{day}');"

def updateDay(month, date, day):
    return f"update {month} set Day = '{day}' where date={date};"

if __name__ == "__main__":
    main()