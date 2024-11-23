import pytest
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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_init(self, books_collector):
        assert books_collector.books_genre == {}
        assert books_collector.favorites == []
        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book(self, books_collector):
        books_collector.add_new_book('Оно')
        assert 'Оно' in books_collector.books_genre

    def test_set_book_genre(self, books_collector):
        books_collector.add_new_book('Дюна')
        books_collector.set_book_genre('Дюна', 'Фантастика')
        assert books_collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('name, genre', [
        ['Загадка Эндхауза', 'Детективы'],
        ['Оно', 'Ужасы']
    ])
    def test_get_book_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book('Загадка Эндхауза')
        books_collector.set_book_genre('Загадка Эндхауза', 'Детективы')
        assert books_collector.get_books_with_specific_genre('Детективы') == ['Загадка Эндхауза']

    @pytest.mark.parametrize(
        'name, books_genre',
        [
            ("Оно", "Ужасы"),
            ("Дюна", "Фантастика"),
            ("Загадка Эндхауза", "Детективы"),
            ("Колобок", "Мультфильмы"),
            ("Ревизор", "Комедии"),
        ]
    )
    def test_get_books_genre(self, books_collector, name, books_genre):
        # Добавляем книги и устанавливаем им жанры
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, books_genre)

        # Получаем словарь жанров
        books_genre_dict = books_collector.get_books_genre()
        assert books_genre_dict[name] == books_genre

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        books_collector.add_new_book('Колобок')
        books_collector.set_book_genre('Колобок', 'Мультфильмы')
        assert (books_collector.get_books_for_children()) == (['Колобок'])

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book('Ревизор')
        books_collector.add_book_in_favorites('Ревизор')
        assert 'Ревизор' in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book('Ревизор')
        books_collector.add_book_in_favorites('Ревизор')
        books_collector.add_book_in_favorites('Ревизор')
        assert books_collector.get_list_of_favorites_books() == ['Ревизор']

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Ревизор')
        books_collector.add_book_in_favorites('Ревизор')
        books_collector.delete_book_from_favorites('Ревизор')
        assert 'Ревизор' not in books_collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name, genre', [
        ['Сказка о Попе Поповиче и работнике его Балде', 'Мультфильмы'],
        ['Песнь о вещем Олеге', 'Баллада']
    ])
    def test_set_book_genre_negative_case(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.set_book_genre(name, genre)
