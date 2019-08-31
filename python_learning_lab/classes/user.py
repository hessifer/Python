class User:
    """A simple class for processing user information."""
    def __init__(self, first_name, last_name, username, email):
        """Initialize our user's information."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        """Process and display user data."""
        full_name = self.first_name + " " + self.last_name
        print(f"Name: {full_name.title()}\n\tUsername: {self.username}\n\tE-mail: {self.email}")

    def greet_user(self):
        """Display a greeting for the user."""
        print(f"Hello {self.first_name.title()}, it is nice to meet you.")


if __name__ == '__main__':
    user1 = User('charles', 'hessifer', 'nagalot', '12g@nodomain.com')
    user2 = User('smith', 'dude', 'hammer', 'hammer@nodomain.com')
    user3 = User('john', 'doe', 'jd', 'jd@nodomain.com')

    user1.describe_user()
    user2.describe_user()
    user3.describe_user()

    user1.greet_user()
    user2.greet_user()
    user3.greet_user()
