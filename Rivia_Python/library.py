import random

class Library:
    library_name = "Bosh"
    library_phone = "123.456.7890"

    def __init__(self, member_id=None):
        if not member_id:
            self.member_id = self.register_member()
        else:
            self.member_id = member_id
    
    def register_member(self) -> int:
        """Used to register a new member."""
        self.fname = input("First Name: ")
        self.lname = input("Last Name: ")

        return random.randint(10000, 99999)

    def __repr__(self) -> str:
        """Provides a string representation of instance."""
        str_text = f"Library Name: {self.library_name}\n"
        str_text += f"Library Phone: {self.library_phone}"
        str_text += f"\nMember ID: {self.member_id}"

        return str_text
'''
    def __repr__(self):
        """Provides an object representation of the instance."""
        pass
'''

# library = Library()
library = Library(98989)
# print(library.member_id)
print(library)