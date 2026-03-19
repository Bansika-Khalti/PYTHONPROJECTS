# Library System

library = {}  # dictionary

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    
    # tuple (book info)
    info = (title, author)
    
    # set (genres)
    genres = set(input("Enter genres (comma separated): ").split(","))
    
    library[book_id] = {
        "info": info,
        "genres": genres
    }
    
    print("Book added!\n")


def view_books():
    if not library:
        print("No books available\n")
    else:
        for bid, data in library.items():
            info = data["info"]
            genres = data["genres"]
            
            print(f"ID: {bid}, Title: {info[0]}, Author: {info[1]}")
            print(f"Genres: {', '.join(genres)}")
            print("-" * 20)


def search_book():
    bid = input("Enter Book ID: ")
    
    if bid in library:
        info = library[bid]["info"]
        print(f"Found: {info[0]} by {info[1]}\n")
    else:
        print("Book not found\n")


def main():
    while True:
        print("1.Add 2.View 3.Search 4.Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

main()