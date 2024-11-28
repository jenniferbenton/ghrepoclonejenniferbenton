# Class Average Program

def main():
    grades = []

    while True:
        grade = input("Enter a grade (or type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

    if grades:
        average = sum(grades) / len(grades)
        print(f"\nThe average grade is: {average:.2f}")
    else:
        print("No grades entered.")


if __name__ == "__main__":
    main()