# Python allows the programmer to split their coding
# logic into smaller more maintainable files called modules.

# Functionality from a module can be 'import'ed into other modules
# such as the main module that we have been working with.

# Modules are just other python src files that adhere
# to the same Pythonic principles.

# let's say we wanted to write code specifically for handling
# registration for example. Our code might look something like
# stored in registration.py


def register_user(first_name: str, last_name: str, email: str) -> int:
    """Registers a given user.

    Parameters:
    first_name (str) - The first name of the user.
    last_name (str) - The last name of the user.
    email (str) - The email address of the user being registered.

    Return:
    uid (int) - Unique identifier of registered user.
    """
    pass


def deregister_user(uid: int):
    """Removes a registered user from the system.

    Parameters:
    uid (int) - The unique identifier of the registered user.
    """
    pass


def update_user(uid: int, **kwargs: dict):
    """Updates user information in system.

    Parameters:
    **kwargs (dict) - Key / Value pair of user attributes requiring update.
    """
    pass


def display_user_info(uid: int):
    """Displays to terminal user information."""
    print(f"{uid}\n\tFirst Name: ...\n\tLast Name: ...\n\tEmail: ...")
