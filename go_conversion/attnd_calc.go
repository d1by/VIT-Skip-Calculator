package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strings"
	"time"
)

func main() {
	var start, end string
	fmt.Println("\nVacation start date (DDMMYYYY): ")
	fmt.Scanln(&start)
	fmt.Println("Vacation end date (DDMMYYYY): ")
	fmt.Scanln(&end)

	startday, _ := time.Parse("02012006", start)
	endday, _ := time.Parse("02012006", end)

	if startday.After(endday) {
		defer fmt.Println("ERROR: Start date must come before end date!")
		os.Exit(3)
	}

	schd := createSchd()

	// list of courses
	var unqCourse []string
	for _, day := range schd {
		for _, course := range day {
			if !slices.Contains(unqCourse, course) {
				unqCourse = append(unqCourse, course)
			}
		}
	}
}

func createSchd() map[uint8][]string {
	schd_in, err := os.ReadFile("schedule.txt")

	if err != nil {
		fmt.Print(err)
	}

	schd_str := string(schd_in)

	schd := make(map[uint8][]string)

	lines := strings.Split(schd_str, "\n")
	days := []string{"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"}
	var courses []string
	var day_count uint8 = 0
	lab := false

	for _, line := range lines {
		//if day_count >= 6 {
		//	fmt.Println(schd)
		//	break
		//}

		if lab {
			slots := strings.Split(line, "\t")
			lab_found, _ := regexp.MatchString(".*LAB.*", slots[0])
			if !lab_found {
				continue
			}

			for _, slot := range slots {
				re := regexp.MustCompile("[A-Z]+[0-9]+-([A-Z0-9]+)-.*")
				course := re.FindStringSubmatch(slot)
				if course != nil {
					// fmt.Println(course[1])
					courses = append(courses, course[1])
				}
			}

			schd[day_count] = courses
			day_count++
			lab = false
			continue
		}

		pattern := ".*" + days[day_count] + ".*"
		day, _ := regexp.MatchString(pattern, line)
		if day {
			courses = nil
			slots := strings.Split(line, "\t")
			for _, slot := range slots {
				re := regexp.MustCompile("[A-Z]+[0-9]+-([A-Z0-9]+)-.*")
				course := re.FindStringSubmatch(slot)
				if course != nil {
					// fmt.Println(course[1])
					courses = append(courses, course[1])
				}
			}

			lab = true
		}
	}

	return schd
}
