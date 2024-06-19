import requests
import os

BASE_URL = "http://127.0.0.1:8000"
LANG = "eng"


def add_book(name, author, date, isbn):
    url = f"{BASE_URL}/api/books"

    book = {
        'name': name,
        'author': author,
        'published_date': date,
        'isbn': isbn
    }

    params = {'lan': LANG}

    response = requests.post(url, json=book, params=params)
    return response.json()


def read_all_books():
    url = f"{BASE_URL}/api/books"

    response = requests.get(url)
    return response.json()


def read_one_book(book_id):
    url = f"{BASE_URL}/api/books/{book_id}"

    params = {'lan': LANG}

    response = requests.get(url, params=params)
    return response.json()


def update_book(book_id, name, author, date, isbn):
    url = f"{BASE_URL}/api/books/{book_id}"

    book = {
        'name': name,
        'author': author,
        'published_date': date,
        'isbn': isbn
    }

    params = {"lan": LANG}

    response = requests.put(url, json=book, params=params)
    return response.json()


def delete_book(book_id):
    url = f"{BASE_URL}/api/books/{book_id}"

    params = {"lan": LANG}

    response = requests.delete(url, params=params)
    return response.json()


def main_menu():
    os.system("cls")
    print("*****\t\t\tLIBRARY MANAGEMENT API TEST\t\t\t*****\n")
    print("Choose:\n")
    print("1: Create a book (POST:/api/books")
    print("2: Book list (GET:/api/books")
    print("3: Read a book (GET:/api/books/{book_id}")
    print("4: Update a book (PUT:/api/books/{book_id}")
    print("5: Delete a book (DELETE:/api/books/{book_id}")
    print("6: Exit")
    print("****************************************************")
    choosen = int(input("Your Choice: "))

    return choosen


def add_menu():
    os.system("cls")
    print("*******************************")
    print("\tCREATE A BOOK")
    print("*******************************")
    name = input("Book name : ")
    author = input("Book author : ")
    published_date = input("Published Date : ")
    isbn = input("ISBN : ")

    book = add_book(name, author, published_date, isbn)
    print(book)
    print("*******************************\n")


def detail_menu():
    os.system("cls")
    print("*******************************")
    print("\tBOOK DETAIL")
    print("*******************************")
    book_id = input("The book ID: ")
    book = read_one_book(book_id)
    print(book)
    print("*******************************\n")


def update_menu():
    os.system("cls")
    print("*******************************")
    print("\tUPDATE A BOOK")
    print("*******************************")
    book_id = input("The book ID: ")
    book = read_one_book(book_id)
    print(book)
    print("*******************************")
    print("New infos (Put Nothing if you want same information)")
    print("*******************************")
    name = input("New book name : ")
    if name == "":
        name = book['name']

    author = input("Book author : ")
    if author == "":
        author = book['author']

    published_date = input("Published Date : ")
    if published_date == "":
        published_date = book['published_date']

    isbn = input("ISBN : ")
    if isbn == "":
        isbn = book['isbn']

    updated_book = update_book(book_id, name, author, published_date, isbn)
    print(updated_book)
    print("*******************************\n")


def list_menu():
    os.system("cls")
    print("*******************************")
    print("\tBOOK LIST")
    print("*******************************")
    book_list = read_all_books()
    for book in book_list:
        print(book)
    print("*******************************\n")


def delete_menu():
    os.system("cls")
    print("*******************************")
    print("\tDELETE A BOOK")
    print("*******************************")
    book_id = input("The book ID: ")
    book = read_one_book(book_id)
    print(book)
    print("*******************************")

    confirm = input("Are you sure to want delete the book ? (yes/no) ")
    if confirm == "yes" or confirm == "y":
        deleted_book = delete_book(book_id)
        print(deleted_book)
    else:
        print("Deleting cancelled")
    print("*******************************\n")


if __name__ == "__main__":
    choice = main_menu()
    while choice < 6:
        match choice:
            case 1:
                add_menu()
            case 2:
                list_menu()
            case 3:
                detail_menu()
            case 4:
                update_menu()
            case 5:
                delete_menu()
        input("Type Enter to continue")
        choice = main_menu()
