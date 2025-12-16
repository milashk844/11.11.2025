import unittest
from io import StringIO
import sys
from library import Book, Library

class TestBook(unittest.TestCase):
    def setUp(self):
        """Фікстура: створює книгу перед кожним тестом"""
        self.book = Book("Тарас Шевченко", "Кобзар", 1)

    def test_book_attributes(self):
        self.assertEqual(self.book.author, "Тарас Шевченко")
        self.assertEqual(self.book.title, "Кобзар")
        self.assertEqual(self.book.book_id, 1)

        def test_book_str(self):
            expected = "ID: 1, 'Кобзар' — Тарас Шевченко"
            self.assertEqual(str(self.book), expected)

    class TestLibrary(unittest.TestCase):
        def setUp(self):
            """Фікстура: створює бібліотеку та дві книги"""
            self.library = Library("Центральна бібліотека")
            self.book1 = Book("Тарас Шевченко", "Кобзар", 1)
            self.book2 = Book("Леся Українка", "Лісова пісня", 2)

        def test_add_book(self):
            self.library.add_book(self.book1)
            self.assertIn(self.book1, self.library.books)

        def test_remove_book(self):
            self.library.add_book(self.book1)
            self.library.add_book(self.book2)
            self.library.remove_book(1)
            self.assertNotIn(self.book1, self.library.books)
            self.assertIn(self.book2, self.library.books)

        def test_remove_nonexistent_book(self):
            self.library.add_book(self.book1)
            # Перевіримо, що книга з ID=99 не видаляється
            captured_output = StringIO()
            sys.stdout = captured_output
            self.library.remove_book(99)
            sys.stdout = sys.__stdout__
            self.assertIn("не знайдено", captured_output.getvalue())

        def test_show_books_empty(self):
            captured_output = StringIO()
            sys.stdout = captured_output
            self.library.show_books()
            sys.stdout = sys.__stdout__
            self.assertIn("немає книг", captured_output.getvalue())

        def test_show_books_with_books(self):
            self.library.add_book(self.book1)
            self.library.add_book(self.book2)
            captured_output = StringIO()
            sys.stdout = captured_output
            self.library.show_books()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            self.assertIn("Кобзар", output)
            self.assertIn("Лісова пісня", output)

            if __name__ == "__main__":
                unittest.main()