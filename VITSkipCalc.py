##########
# EDIT THIS:
last_lab = "April 26 2024"
last_th = "May 3 2024"
##########

import datetime
import sys
import re
import math

import sqlite3

def main():
    sqliteConnection = sqlite3.connect("Calendar.db")
    cursor = sqliteConnection.cursor()

    # searching for exam dates
    q = "select name from sqlite_master where type='table';"
    cursor.execute(q)
    res = cursor.fetchall();
    months = [table[0] for table in res]
    
    cat1start, cat1end = examDateSearch(cursor, months, "CT1")
    cat2start, cat2end = examDateSearch(cursor, months, "CT2")
    labend = datetime.datetime.strptime(last_lab, '%B %d %Y')
    thend = datetime.datetime.strptime(last_th, '%B %d %Y')

    presentday = datetime.datetime.now()
    cat1status = False if not validDate(presentday, cat1start) else True
    cat2status = False if not validDate(presentday, cat2start) else True
    fatStatus = False if not validDate(presentday, thend) else True

    daycount_cat1 = daysBtwnDates(cursor, presentday, cat1start)
    daycount_cat2 = daysBtwnDates(cursor, presentday, cat2start)
    daycount_fat = daysBtwnDates(cursor, presentday, thend)
    
    schd = createSchd()

    unqCourse = getAttendance()
    for x in unqCourse:
        # tot = int(input("Number of classes held so far: "))
        # attn = int(input("Number of classes attended so far: "))
        attn = unqCourse[x][0]
        tot = unqCourse[x][1]
        print(f"{x} : {attn} out of {tot} class[es] attended".center(50,"-"))

    if(cat1status):
        calcSkips(schd, daycount_cat1, "CAT 1")
    if(cat2status):
        calcSkips(schd, daycount_cat2, "CAT 2")
    if(fatStatus):
        calcSkips(schd, daycount_fat, "FAT")

    #list of courses
    # unqCourse = []
    # for key in schd:
    #     day = schd[key]
    #     for x in day:
    #         if(x not in unqCourse):
    #             unqCourse.append(x)

def calcSkips(schd, daycount, examName):
    total = {}
    attnd = {}
    missed = {}

    unqCourse = getAttendance()
    for x in unqCourse:
        # tot = int(input("Number of classes held so far: "))
        # attn = int(input("Number of classes attended so far: "))
        attn = unqCourse[x][0]
        tot = unqCourse[x][1]

        curr_attn = attn
        curr_tot = tot

        #between present day and start of exam

        for i in range(len(daycount)):
            tot+=schd[i].count(x)*daycount[i]
            attn+=schd[i].count(x)*daycount[i]
        
        total[x]=tot
        attnd[x]=attn

        min_classes = math.ceil(0.75*tot)
        rem_classes = tot - curr_tot
        req_classes = min_classes - curr_attn
        miss = rem_classes - req_classes

        # print(f"{x} : {min_classes, rem_classes, req_classes, miss, attn, tot}")

        missed[x]=miss

    print(f"Available Skips until {examName}".center(50, "-"), "\n(1 lab class = 2 classes)")
    for key in total:
        # attndper = round((attnd[key]) / (total[key] + missed[key]) * 100, 2)
        print(key, str(missed[key]).rjust(50-len(key)-1, "."), " class[es]", sep="")      

def validDate(start, end):
    return False if start > end else True
    
def examDateSearch(cursor, months, exam):
    for month in months:
        q = f"select date from {month} where day='{exam}';"
        cursor.execute(q)
        dates = cursor.fetchall()
        
        if dates:
            start_str = f"{month} {dates[0][0]} 2024"
            start = datetime.datetime.strptime(start_str, '%B %d %Y')
            end_str = f"{month} {dates[-1][0]} 2024"
            end = datetime.datetime.strptime(end_str, '%B %d %Y')
    
    return start, end

def getDayCount(cursor, day, month, date):
    q = f"select count(*) from {month} where Date>={date} AND Day='{day}';"
    cursor.execute(q)
    res = cursor.fetchall()
    return res[0][0]

def getDayCountLast(cursor, day, month, date, enddate):
    q = f"select count(*) from {month} where Date>={date} AND Date<{enddate} AND Day='{day}';"
    cursor.execute(q)
    res = cursor.fetchall()
    return res[0][0]

def daysBtwnDates(cursor, start, end):
    cmon = 0
    ctue = 0
    cwed = 0
    cthur = 0
    cfri = 0
    hol = False

    while(start.month != end.month):
        startday = start.strftime('%B %d %Y')
        startmonth = startday.split(' ', 1)[0]
        startdate = startday.split(' ', 1)[1].split(' ', 1)[0]

        # print(f"{startmonth, startdate}")
        # q = f"select * from {startmonth} where Date>={startdate} AND Day = 'THU';"
        # cursor.execute(q)
        # res = cursor.fetchall()
        # print(res)

        cmon += getDayCount(cursor, 'MON', startmonth, startdate)
        ctue += getDayCount(cursor, 'TUE', startmonth, startdate)
        cwed += getDayCount(cursor, 'WED', startmonth, startdate)
        cthur += getDayCount(cursor, 'THU', startmonth, startdate)
        cfri += getDayCount(cursor, 'FRI', startmonth, startdate)

        # print(f"{startmonth} count: {cmon, ctue, cwed, cthur, cfri}")

        q = f"select count(*) from {startmonth} where Date>={startdate};"
        cursor.execute(q)
        res = cursor.fetchall()
        start += datetime.timedelta(days=res[0][0])

    startday = start.strftime('%B %d %Y')
    startmonth = startday.split(' ', 1)[0]
    startdate = startday.split(' ', 1)[1].split(' ', 1)[0]

    endday = end.strftime('%B %d %Y')
    enddate = endday.split(' ', 1)[1].split(' ', 1)[0]

    cmon += getDayCountLast(cursor, 'MON', startmonth, startdate, enddate)
    ctue += getDayCountLast(cursor, 'TUE', startmonth, startdate, enddate)
    cwed += getDayCountLast(cursor, 'WED', startmonth, startdate, enddate)
    cthur += getDayCountLast(cursor, 'THU', startmonth, startdate, enddate)
    cfri += getDayCountLast(cursor, 'FRI', startmonth, startdate, enddate)

    # print(f"{startmonth} count: {cmon, ctue, cwed, cthur, cfri}")

    return [cmon, ctue, cwed, cthur, cfri]

def createSchd():
    # MANUAL 
    # print("\nEnter course names: ")
    # print("*** Enter course twice if it counts as 2 classes, etc. ***")
    # schd = {}
    # weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # for i in range(5):
    #     courses = []
    #     print(weekdays[i].center(50, "-"))
    #     cont = True
    #     count = 1
    #     print("Type \"STOP\" to proceed to the next day. ")
    #     while(cont):
    #         print(count, ": ", end="")
    #         x = input()

    #         if(x.lower()=="stop"):
    #             cont = False
    #             continue
            
    #         count+=1
    #         courses.append(x)
        
    #     schd[str(i)] = courses
    
    # COPY AND PASTE
    # print("Paste VTOP schedule: ")
    # input_lines = []
    # while(True):
    #     input_line = input()
    #     if input_line:
    #         input_lines.append(input_line)
    #     else:
    #         break
    
    # schd_str = '\n'.join(input_lines)

    # VIA TEXT FILE
    with open("schedule.txt") as f:
        schd_str = f.read()

    schd = {}

    lines = schd_str.split('\n')
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day_count = 0
    lab = False
    
    for line in lines:
        if(day_count>6):
            # print(schd)
            break
        
        if(lab):
            slots = line.split('\t')
            lab_found = re.search(".*LAB.*", slots[0])
            if(not lab_found):
               continue

            for slot in slots[1:]:
                course = re.search("[A-Z]+[0-9]+-([A-Z0-9]+)-.*", slot)
                if(course):
                    # print(course.group(1))
                    courses.append(course.group(1))

            schd[day_count] = courses

            day_count+=1
            lab = False
            continue

        day = re.search(f".*{days[day_count]}.*", line)
        if(day):
            # print("\n", days[day_count], "\n")
            courses = []
            slots = line.split('\t')
            for slot in slots[2:]:
                course = re.search("[A-Z]+[0-9]+-([A-Z0-9]+)-.*", slot)
                if(course):
                    # print(course.group(1))
                    courses.append(course.group(1))
            
            lab = True
            continue
        

    return schd

def getAttendance():
    with open("attendance.txt") as f:
        attendance_str = f.read()
    
    attendance_vals = re.findall(r'.*([A-Z]{4}\d{3}[A-Z])\s.*?(\d+)\s+(\d+)(?!\s*%)', attendance_str)
    
    # print(attendance_vals)
    attendance = {}
    for course in attendance_vals:
        if(course[0] not in attendance):
            attendance[course[0]] = [int(course[1]), int(course[2])]
        else:
            attendance[str(course[0] + '(2)')] = [int(course[1]), int(course[2])]
 
    return attendance


            
if __name__ == '__main__':
    main()
    print("\nhttps://github.com/d1by/\n")