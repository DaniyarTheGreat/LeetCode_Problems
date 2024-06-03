"""
-- Library class that can register books
    - Book
    - Active or not
    - last page
    - size
-- Book class where new books can be registered
    - ID
    - Vin num
    - Author
    - Publish date
    - Total page num
-- User class where each user has one library
    - user_id
    - library
"""

class Book:
    def __init__(self, book_id, vin_num, author, publish_date, total_page):
        self.book_id = book_id
        self.vin_num = vin_num
        self.author = author
        self.publish_date = publish_date
        self.total_page = total_page
        self.book = {"book_id": self.book_id, "vin_num": self.vin_num, "author": self.author,
                     "publish_date": self.publish_date, "total_page": self.total_page}

class Library:
    def __init__(self):
        self.size = 0
        self.library = {}


    def add_book(self, book: dict):
        new_book = Book(**book)
        for key in self.library.keys:
            if key == new_book.book_id:
                pass
            else:
                self.library.update({key: {
                    f"{new_book.author}": new_book, 
                    "active": True, 
                    "last_page": 1}})
                

def lcs(arr1 : str,arr2 : str):
    curr_sub = 0
    max_sub = 0
    j = 0
    i = arr1.find(arr2[j])
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            curr_sub += 1
            max_sub = max(curr_sub, max_sub)
            i += 1
            j += 1
        else:
            curr_sub = 0
            
        

        