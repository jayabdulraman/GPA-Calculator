"""GPA point calculator to aide tertiary institutions in calculating a student's GPA Point"""

counter = 0


def grade_in_letter(letter):
    """Converts grade in letters (A,B,C..) to their numbers according to the grading point rules"""

    global counter
    counter += 1
    letter = input("Enter Grade for Module " + str(counter) + " (eg A, B, C....F): ")

    if letter.upper() == 'A':
        return 5
    elif letter.upper() == 'B':
        return 4
    elif letter.upper() == 'C':
        return 3
    elif letter.upper() == 'D':
        return 2
    elif letter.upper() == 'E':
        return 1
    elif letter.upper() == 'F':
        return 0


def conditions(check):
    """Checks for different conditions and returns desired output"""

    if check >= 3.0 and check < 3.5:
        print("Congratulations! You just made it! However, check if you have no problem in any module! Good luck!")
    elif check >= 3.5 and check <= 4.0:
        print("Very Good! Congratulations! Keep it up!")
    elif check >= 4.0 and check <= 5.0:
        print("Brilliant Performance! Congratulations! Keep it up!")
    else:
        print("I'm sorry! Your GPA is short of the required passing point!")


def gpa_calculator():
    """GPA calculator that puts all functions together and run the calculator"""

    total_grade = []
    credit_hour = []
    try:
        totalmodule = int(input("Enter Total Number of Modules Offered: "))

        for module in range(totalmodule):
            letter = ' '
            grade = grade_in_letter(letter)
            hour = int(input("\tEnter Credit Hour for Module (eg 2,3,4..): "))
            credit_hour.append(hour)

            conversion = grade * hour

            total_grade.append(conversion)

        Total_credit_hour = sum(credit_hour)

        GPA = sum(total_grade) / Total_credit_hour

        print("==="*17)
        print("Output: ")
        print('Your total GPA Point is: {:.2f}'.format(GPA))

        condition = conditions(GPA)

        return condition

    except:
        print('Check to see if you made the correct inputs!')
    finally:
        print('==='*17)


print("===" * 17)
gpa_calculator()

