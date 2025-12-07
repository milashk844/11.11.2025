import uuid
from typing import Self

class Book:
    def __init__(self, author: str, title: str, book_id: int):
        self.author = author
        self.title = title
        self.book_id = book_id

    def __str__(self):
        return f"ID: {self.book_id}, '{self.title}' — {self.author}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        """Додає книгу до фондів бібліотеки"""
        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки '{self.name}'.")

    def remove_book(self, book_id: int):
        """Видаляє книгу за її унікальним ідентифікатором"""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Книга '{book.title}' видалена з бібліотеки '{self.name}'.")
                return
        print(f"Книгу з ID {book_id} не знайдено у бібліотеці '{self.name}'.")

    def show_books(self):
        """Виводить список усіх книг у бібліотеці"""
        if not self.books:
            print(f"У бібліотеці '{self.name}' немає книг.")
        else:
            print(f"Книги у бібліотеці '{self.name}':")
            for book in self.books:
                print(book)


# Приклад використання:
library = Library("Центральна бібліотека")

book1 = Book("Тарас Шевченко", "Кобзар", 1)
book2 = Book("Леся Українка", "Лісова пісня", 2)

library.add_book(book1)
library.add_book(book2)

library.show_books()

library.remove_book(1)
library.show_books()
