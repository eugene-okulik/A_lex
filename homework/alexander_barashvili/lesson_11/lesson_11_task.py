class Book:
    material = 'бумага'
    is_text = True


    def __init__(self, book_name, autor, count_pages, isbn, is_reserved):
        self.book_name = book_name
        self.autor = autor
        self.count_pages = count_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


    def check_reserve_book(self):
        print(f'Название: {self.book_name}, Автор: {self.autor}, страниц: {self.count_pages}, '
              f'материал: {self.material}{', зарезервирована' if self.is_reserved else ''}')


class SchoolBooks(Book):
    def __init__(self, book_name, autor, count_pages, subject, pupils_class, is_exercise, isbn, is_reserved):
        super().__init__(book_name, autor, count_pages, isbn, is_reserved)
        self.subject = subject
        self.pupils_class = pupils_class
        self.is_exercise = is_exercise


    def check_reserve_book(self):
        if self.is_reserved:
            self.is_reserved = ', зарезервирована'
        else:
            self.is_reserved = ''
        print(f'Название: {self.book_name}, Автор: {self.autor}, страниц: {self.count_pages}, '
              f'предмет: {self.subject}, класс: {self.pupils_class}{', зарезервирована' if self.is_reserved else ''}')


book1 = Book('Идиот', 'Достоевский', 500, 501512, None)
book2 = Book('Изучаем Python', 'Марк Лутц', 1272, 12345, True)
book3 = Book('Простой Python', 'Билл Любанович', 476, 64586, False)
book4 = Book('Чистый код', 'Роберт Мартин', 459, 5125112, True)
book5 = Book('Знакомство с Python', 'Бейдер Дэн', 512, 6431512, True)
book1.check_reserve_book()
book2.check_reserve_book()
book3.check_reserve_book()
book4.check_reserve_book()
book5.check_reserve_book()
print()
pupil_book1 = SchoolBooks('Алгебра', 'Какой-то автор', 100, 'Матемаика', 9, True, 1241, None)
pupil_book2 = SchoolBooks('Всеобщая история', ' Ирина Свенцицкая', 100, 'История', 5, True, 1241, True)
pupil_book3 = SchoolBooks('География. 10 класс', 'В. В. Николина', 200, 'Георгафия', 10, True, 1241, False)
pupil_book1.check_reserve_book()
pupil_book2.check_reserve_book()
pupil_book3.check_reserve_book()
