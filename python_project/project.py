def main():
    try:
        no_of_courses = int(input("What's the total number of courses? "))

        total_units = int(input("What's the total number of course units? "))

        preference = input("Would you like to input scores or grades?(return scores/grades) ").strip().lower()

        print("\n")

        compute(no_of_courses, total_units, preference)

    except ValueError:
        print("ValueError! check your input!")

def convert_scores_to_grades(score):

    if score < 0 or score > 100:
        return "Out of bounds"

    elif score >= 70:
        return "A"

    elif score >= 60:
        return "B"

    elif score >= 50:
        return "C"

    elif score >= 45:
        return "D"

    elif score >= 40:
        return "E"

    else:
       return "F"

def grade_weight(grade, units):
    if grade == "A":
        return 5 * units

    elif grade == "B":
        return 4 * units

    elif grade == "C":
        return 3 * units

    elif grade == "D":
        return 2 * units

    elif grade == "E":
        return 1 * units

    elif grade == "F":
        return 0

    else:
        raise ValueError("Invalid Grade!")

def grade_class(gp):
    if gp >= 4.50:
        return "YOU'RE IN FIRST CLASS! KEEP IT UP!"

    elif gp >= 3.50:
        return "YOU'RE IN SECOND CLASS UPPER! WORK HARDER!"

    elif gp >= 2.40:
        return "YOU'RE IN SECOND CLASS LOWER! YOU CAN DO BETTER!"

    elif gp >= 1.50:
        return "YOU'RE IN THIRD CLASS! DON'T GIVE UP, TRY HARDER!"

    elif gp >= 1.00:
        return "YOU'RE IN PASS! THIS IS NOT YOUR VERY BEST, BELIEVE ME!"

    else:
        return "SORRY, YOU FAILED!"


def compute(no_of_courses, total_units, preference):
    unit_counter = 0
    total_course_points = 0
    course_counter = 1

    if total_units != 0:
        try:
            while course_counter <= no_of_courses:
                if preference == "grades":
                    grade = input(f"Course_{course_counter}_grade: ").strip().upper()
                elif preference == "scores":
                    score = int(input(f"Course_{course_counter}_score: ").strip())
                    grade = convert_scores_to_grades(score)
                else:
                     raise ValueError("Please, enter the right input! scores/grades")

                units = int(input(f"Course_{course_counter}_unit: "))
                print("\n")

                course_counter += 1
                unit_counter += units
                total_course_points += grade_weight(grade, units)

            if total_units == unit_counter:
                gp = total_course_points / total_units
                print(f"Your grade point for this semester is: {gp:.2f}")
                print(grade_class(gp))
            else:
                print("Incomplete Units or Incorrect Total units inputted!")

        except ValueError:
            print("ValueError! check input again!")
        except UnboundLocalError:
            print("Please recheck your inputs!")





if __name__ == "__main__":
    main()
