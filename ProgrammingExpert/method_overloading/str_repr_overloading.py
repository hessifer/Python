class Page:
    def __init__(self, text, page_number):
        self.text = text
        self.page_number = page_number

    def __len__(self):
        return len(self.text)

    def __str__(self):
        return f"Page(text = {self.text}, page_number = {self.page_number})" 

    def __repr__(self):  #  internal representation of object
        return self.__str__()
        


class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number


    def __len__(self):
        return len(self.pages)

    def __str__(self):
        output =  f"Book(title = {self.title}, author = {self.author}, id = {self.id_number})"
        for page in self.pages:
            output += "\n" + str(page)
        
        return output

    def __repr__(self):
        # repr is useful to help debug and provide
        # useful information about the object
        return f"Book(id_number = {self.id_number})"


page1 = Page("Page 1!", 1)
page2 = Page("This is page 2.", 2)
book = Book("Tim is Great", "Tim", [page1, page2], 1)
print(len(page2))
print(len(book))
print(page1)
print(book)  # behind the scenes, Python specifically calls str() on the instance of a class
print(repr(book))