from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2, "Должно добавится 2 книги"

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тень и кость')
        collector.add_new_book('Тень и кость')
        assert len(collector.get_books_rating()) == 1, "Должна обавится только 1 книга"

    def test_set_book_rating_more_than_11(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по галактике')
        collector.set_book_rating ('Автостопом по галактике', 12)
        assert collector.get_book_rating('Автостопом по галактике') == 1, "Рейтинг книги должен быть 1"

    def test_set_book_rating_less_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Свинка Пеппа')
        collector.set_book_rating('Свинка Пеппа', 0.5)
        assert collector.get_book_rating('Свинка Пеппа') == 1, "Рейтинг книги должен быть 1"

    def test_set_book_rating_7(self):
        collector = BooksCollector()
        collector.add_new_book('Жизнь взаймы')
        collector.set_book_rating('Жизнь взаймы', 7)
        assert 'Жизнь взаймы' in collector.get_books_with_specific_rating(7), '"Жизнь взаймы" в списке с рейтингом 7'

    def test_get_book_rating_not_in_list(self):
        collector = BooksCollector()
        collector.get_book_rating('Книга Келлс')
        assert collector.get_book_rating('Книга Келлс') == None, "У книги не из списка нет рейтинга"

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тень и кость')
        collector.add_new_book('Шестерка воронов')
        collector.add_book_in_favorites('Тень и кость')
        assert 'Тень и кость' in collector.get_list_of_favorites_books(), '"Тень и кость" есть в списке любимых книг'

    def test_delete_book_from_favorites_del_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шестерка воронов')
        collector.add_book_in_favorites('Шестерка Воронов')
        collector.delete_book_from_favorites('Шестерка Воронов')
        assert len(collector.get_list_of_favorites_books()) == 0, "Список любимых книг пустой"

    def test_add_book_in_favorites_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Разум и чувства')
        assert len(collector.get_list_of_favorites_books()) == 0, "Список любимых книг пустой"

    def test_get_books_with_specific_rating_book_with_rating_8(self):
        collector = BooksCollector()
        collector.add_new_book('Золушка')
        collector.set_book_rating ('Золушка', 8)
        collector.get_books_with_specific_rating(8)
        assert len(collector.get_books_with_specific_rating(8)) == 1, "В списке 1 книга с рейтингом 8"

    def test_get_books_with_specific_rating_book_not_such_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Тень и кость')
        collector.get_books_with_specific_rating(10)
        assert len(collector.get_books_with_specific_rating(10))== 0, "Список книг с ретингом 10 пустой"