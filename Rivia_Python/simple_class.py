"""An illustration of a simple class."""

class Person:
    def __init__(self, fname, mname, lname, age):
        self.fname: str = fname
        self.mname: str = mname
        self.lname: str = lname
        self.age: int = age
    
    def get_full_name(self) -> str:
        full_name: str = f"{self.fname} {self.mname} {self.lname}"
        return full_name.title()
    
    def greet_person(self):
        """Greets a person with Hello followed by their first name."""
        msg: str = f"Hello, {self.fname.title()}"
        print(msg)


if __name__ == '__main__':
    first_name: str = "charles"
    middle_name: str = "anthony"
    last_name: str = "hessifer"
    age = 27

    person = Person(first_name, middle_name, last_name, age)
    print(f"Person: {person.get_full_name()}")
    print(f"Person's Age: {person.age}")
    person.greet_person()

