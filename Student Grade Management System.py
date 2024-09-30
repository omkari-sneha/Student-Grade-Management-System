def calculate_grade(total_score):
    if total_score >= 90:
        return 'A'
    elif total_score >= 80:
        return 'B'
    elif total_score >= 70:
        return 'C'
    elif total_score >= 60:
        return 'D'
    else:
        return 'F'


# Function to calculate total score
def calculate_total_score(scores):
    return sum(scores)


# Function to display student data
def display_students(students):
    print("\nStudent Data:")
    print("Name\t\tID\t\tTotal Score\tGrade")
    print("-" * 50)
    for student in students:
        total_score = calculate_total_score(student['scores'])
        grade = calculate_grade(total_score)
        print(f"{student['name']}\t\t{student['id']}\t\t{total_score}\t\t{grade}")


# Main function to manage the student grade system
def main():
    students = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        print(f"\nEntering data for student {i + 1}")
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        scores = []
        for j in range(3):
            score = float(input(f"Enter score for subject {j + 1}: "))
            scores.append(score)

        student = {
            'name': name,
            'id': student_id,
            'scores': scores
        }
        students.append(student)

    # Display all student details
    display_students(students)


# Run the main function
if __name__ == "__main__":
    main()
