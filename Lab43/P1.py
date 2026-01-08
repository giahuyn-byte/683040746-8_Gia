"""
Gia Huy Nguyen 
683040746-8
P1
"""
from datetime import datetime
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self._checked_out = False


    def get_status(self):
        return "Checked out" if self._checked_out else "Available"
    
    
    def check_out(self):
        # if checked_out is False (item still in lib)
        if not self._checked_out:
            self._checked_out = True
            return True
        # can't check out if item not in lib
        return False
    def return_item(self):
        if self._checked_out:
            self._checked_out = False 
            return True
        return False
    def display_info(self):
        print(f"{self.title}")
        print(f"{self._id}")
        print(f"{self._checked_out}")
    

# implement 3 classes here
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self.pages_count = 0
    def display_info(self):
        print(f"{self.title}")
        print(f"Status: {self.get_status()}")
        print(f"Author: {self.author}")
        print(f"pages count: {self.pages_count}")

    def page_count(self,text):
        self.pages_count = text

class TextBook(Book):
    def __init__(self, title, item_id, author, subject, grade):
        super().__init__(title, item_id, author)
        self.subject = subject
        self.grade_level = grade
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Page_count: {self.pages_count}")
        print(f"Grade_level: {self.grade_level}")
        print(f"Status: {self.check_out()}")
        print(f"Subject: {self.subject}")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
       super().__init__(title, item_id)
       self.issue_number = issue_number
       now = datetime.now()
       self.month = now.month
       self.year = now.year

    
       
    def display_info(self):
       print(f"Title: {self.title}")
       print(f"item_id: {self._id}")
       print(f"issue_number: {self.issue_number}")
       print(f"Month: {self.month}")
       print(f"Year: {self.year}")
       print(f"Status: {self.check_out()}")


# Test your code:
# This is just an example. You should test a lot more than this.
book = Book("Harry Potter", "B001", "J.K. Rowling")
book.page_count(400)
book.display_info()
print()

book.check_out()
book.display_info()
print()

book.return_item()
book.display_info()
print("-" * 40)


textbook = TextBook("h", "b", "Habb", "P", 12)
textbook.page_count(900)
textbook.check_out()
textbook.display_info()
print("-" * 40)


magazine = Magazine("t", "a", 145)
magazine.display_info()



