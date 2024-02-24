import datetime
import sys
import re

def main():
    
    start = input("\nVacation start date (DDMMYYYY): ")
    end = input("Vacation end date (DDMMYYYY): ")

    if(datetime.datetime.strptime(start, '%d%m%Y') >= datetime.datetime.strptime(end, '%d%m%Y')):
        sys.exit("Incorrect dates. ")

    print("\nIs your school/university closed at any point within the above date range? (christmas holidays, etc.) ")
    x=2
    while(x!=1 and x!=0):
        x = int(input("(Enter 1 for yes, 0 for no): ")) 
    if(x==1):
        holstart = input("Holday start date (DDMMYYYY): ")
        holend = input("Holday end date (DDMMYYYY): ")
    else:
        holstart = "00000000"
        holend = "00000000"

    schd = createSchd()

    #list of courses
    unqCourse = []
    for key in schd:
        day = schd[key]
        for x in day:
            if(x not in unqCourse):
                unqCourse.append(x)

    total = {}
    attnd = {}
    missed = {}

    for x in unqCourse:
        print(x.center(50,"-"))
        tot = int(input("Number of classes held so far: "))
        attn = int(input("Number of classes attended so far: "))

        #between present day and start of vacation
        presentday = datetime.datetime.now().strftime('%d%m%Y')
        daycount = daysBtwnDates(presentday, start, holstart, holend)

        for i in range(len(daycount)):
            tot+=schd[str(i)].count(x)*daycount[i]
            attn+=schd[str(i)].count(x)*daycount[i]
        
        total[x]=tot
        attnd[x]=attn

        #between start of vacation and end of vacation
        miss=0
        daycount = daysBtwnDates(start, end, holstart, holend)
        
        for i in range(len(daycount)):
            miss+=(schd[str(i)].count(x))*daycount[i]

        missed[x]=miss

    print("Attendance %".center(50, "-"), "\n")
    for key in total:
        attndper = round((attnd[key]) / (total[key] + missed[key]) * 100, 2)
        print(key, str(attndper).rjust(50-len(key)-1, "."), "%", sep="")      
    
def daysBtwnDates(start, end, holstart, holend):
    cmon = 0
    ctue = 0
    cwed = 0
    cthur = 0
    cfri = 0
    hol = False

    startday = datetime.datetime.strptime(start, '%d%m%Y')
    endday = datetime.datetime.strptime(end, '%d%m%Y')

    #use this if you have no classes between two dates (christmas holidays, etc. )
    if(holstart != "00000000" and holend != "00000000"):
        hol = True
        holstartday = datetime.datetime.strptime(holstart, '%d%m%Y')
        holendday = datetime.datetime.strptime(holend, '%d%m%Y')
    
    while(startday <= endday):

        if(hol and holstartday <= startday and startday <=holendday):
            startday += datetime.timedelta(days=1)
            continue
    
        dayn = startday.strftime("%A")

        if(dayn=="Monday"):
            cmon+=1
        elif(dayn=="Tuesday"):
            ctue+=1
        elif(dayn=="Wednesday"):
            cwed+=1
        elif(dayn=="Thursday"):
            cthur+=1
        elif(dayn=="Friday"):
            cfri+=1

        startday += datetime.timedelta(days=1)
    
    return [cmon, ctue, cwed, cthur, cfri]

def createSchd():
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
    
    # print("Paste VTOP schedule: ")
    # input_lines = []
    # while(True):
    #     input_line = input()
    #     if input_line:
    #         input_lines.append(input_line)
    #     else:
    #         break
    
    # schd_str = '\n'.join(input_lines)

    with open("schedule.txt") as f:
        schd_str = f.read()

    schd = {}

    lines = schd_str.split('\n')
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day_count = 0
    lab = False
    
    for line in lines:
        if(day_count>6):
            print(schd)
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

            schd[str(day_count)] = courses

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
            
main()

print("\nhttps://github.com/d1by/\n")