class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.month = month
        self.birthday_month = month

    def birthday(self):
        self.age += 1


if __name__ == '__main__':
    def create_person_objects(person_names, person_ages, person_months):
        my_data = zip(person_names, person_ages, person_months)  # pairs items in names, ages, months together
        person_objects = []
        for item in my_data:
            person_objects.append(Person(*item))
        return person_objects

    def get_april_birthday(person_objects):
        # Increment age for all people with birthdays in April.
        # Return a dictionary "april_birthdays" with the names of
        # all people with an April birthday as keys, and their updated
        # ages as values.
        april_birthdays = {}
        for person in person_objects:
            if person.birthday_month == 'April':
                april_birthdays[person.name] = person.age + 1
        return april_birthdays


    def get_most_common_birthday_month(person_objects):
        # Use the "months" dictionary to record counts of birthday months
        # for persons in the "person_objects"
        # Return the month with the largest number of birthdays.
        calendar_months = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,
                           'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}
        max_month = ""
        max_count = 0

        for person in person_objects:
            calendar_months[person.birthday_month] += 1
        for key, value in calendar_months.items():
            if value > max_count:
                max_count = value
                max_month = key
        return max_month


    # Test Data
    names = ['Howard', 'Richard', 'Bob', 'John', 'David', 'Charles']
    ages = [31, 28, 31, 30, 31, 30]
    months = ['January', 'February', 'January', 'February', 'March', 'April']
    people = create_person_objects(names, ages, months)
    april_bdays = get_april_birthday(people)
    for n, b in april_bdays.items():
        print(n, b)
    print(get_most_common_birthday_month(people))


"""

def get_april_birthdays(people):
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age += 1
            april_birthdays[person.name] = person.age
            
    return april_birthdays
    


def get_most_common_month(people):
    months = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 
              'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
              'November':0, 'December':0}

    for person in people:
        months[person.birthday_month] += 1

    max_month = None
    max_value = 0
    for key in months.keys():
        if months[key] > max_value:
            max_value = months[key]
            max_month = key

    return max_month

"""
