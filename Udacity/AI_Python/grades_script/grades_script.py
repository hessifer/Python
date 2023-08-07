names = input("Please enter a list of names separated by a comma: ").title().split(',')
assignments = input("Enter the number of assignments separated by a comma: ").split(',')
grades = input("Enter a list of grades seperated by a comma: ").split(',')

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
"""for i in range(len(names)):
    print(message.format(names[i].strip(), assignments[i].strip(), grades[i], int(grades[i]) + (int(assignments[i]) * 2)))
"""
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment) * 2))
