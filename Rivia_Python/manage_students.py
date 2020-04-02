# Now in our main module or the program where we need to use the functionality
# provided in the above module 'registration.py' we use the keyword import
# followed by a space and the file name minus the extenion from which we
# are importing funcitonality


import registration


def main():
    """Main entry of our program."""
    first_name = "Student"
    last_name = "Smith"
    email = "students@mynonexistingschool.edu"

    # Register our user.
    student_smith_uid = registration.register_user(first_name, last_name, email)

    # Student Smith got married changes last name.
    registration.update_user(student_smith_uid, last_name='Fitoniche')

    # Display information for a given uid.
    registration.display_user_info(student_smith_uid)


if __name__ == '__main__':
    main()
