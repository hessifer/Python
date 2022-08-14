"""
Write a function that accepts a list of lists that contain the name, age, and salary of specific employees
and also accepts a string representing the key to sort employees by. Your function should return a new list
that contains the lists representing each employee sorted in ascending order by the given key.
"""

def sort_employees(employees, sort_by):
    keys = ["name", "age", "salary"]
    sort_on = keys.index(sort_by)
    results = []

    while employees:
        min_index = 0
        for i in range(1, len(employees)):
            if employees[i][sort_on] < employees[min_index][sort_on]:
                min_index = i
        
        results.append(employees.pop(min_index))
    return results


def main():
    employees = [
        ["John", 33, 65000],
        ["Sarah", 24, 75000],
        ["Josie", 29, 100000]
    ]
    results = sort_employees(employees, "age")
    print(results)


if __name__ == "__main__":
    main()
