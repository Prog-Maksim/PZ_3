# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.


book_collections = {
    "Магистр": ["Лермонтов", "Достоевский", "Пушкин", "Тютчев"],
    "ДомКниги": ["Толстой", "Грибоедов", "Чехов", "Пушкин"],
    "БукМаркет": ["Пушкин", "Достоевский", "Маяковский"],
    "Галерея": ["Чехов", "Тютчев", "Пушкин"]
}
all_book = set()


def all_books():
    for books in book_collections.values():
        all_book.update(books)

    print("Полный список всех книг магазинов:")
    print(all_book)


def search_book_all_market() -> set:
    common_books = set(book_collections["Магистр"])
    for books in book_collections.values():
        common_books.intersection_update(books)

    return common_books


def search_first_book():
    unique_books = all_book.difference(search_book_all_market())
    print("Книга, которая есть не во всех магазинах:")
    print(next(iter(unique_books)))


if __name__ == "__main__":
    all_books()

    print("Книги, которые есть во всех магазинах:")
    print(search_first_book())

    search_first_book()