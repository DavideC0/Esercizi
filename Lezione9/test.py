def anagram(s: str, t: str) -> bool:
    string_s: str = sorted(s)
    string_t: str = sorted(t)
    if string_s == string_t:
        return True
    else:
        return False

print(anagram("NeurIPS","UniReps"))


"""Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""

class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def get_balance(self) -> float:
        return self.balance
    
class Bank:
    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}
    
    def create_account(self, account_id: str):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")   
        self.accounts[account_id] = Account(account_id, 0)
        return self.accounts[account_id]
        
    def deposit(self, account_id: str, amount: float):
        self.accounts[account_id].balance += amount
    
    def get_balance(self, account_id: str) -> float:
        return self.accounts[account_id].get_balance()

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

def is_valid_sudoku(board):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
    
    def is_valid_sudoku_helper(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(square):
                    return False
        
        return True
    
    return is_valid_sudoku_helper(board)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"{self.val}"
        
def reverse_list(head: ListNode) -> list[int]:
    prev = None
    current = head
    lista: list = []
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        lista.append(prev.val)
    return list(reversed(lista))

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))


"""
    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.
"""

class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
    def borrow(self):
        if self.is_borrowed:
            return 0
        else:
            self.is_borrowed = True
    
    def get(self):
        return self.is_borrowed
            
    def return_book(self):
        self.is_borrowed = False
    
    def __str__(self):
        return f"{self.title}"

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book):
        if book.get():
            raise ValueError("Book is already borrowed")
        else:
            self.borrowed_books.append(book)
            book.borrow()
            
    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by this member")
        book.return_book()
        self.borrowed_books.remove(book)
        
        
class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.member: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str):
        self.books[book_id] = Book(book_id, title, author, False)
    
    def register_member(self, member_id: str, name: str):
        self.member[member_id] = Member(member_id, name)
        
    def borrow_book(self, member_id: str, book_id: str):
        if book_id not in self.books:
            raise ValueError("Book not found")
        if member_id not in self.member:
            raise ValueError("Member not found")
        self.member[member_id].borrow_book(self.books[book_id])
        
    def return_book(self, member_id: str, book_id: str):
        self.member[member_id].return_book(self.books[book_id])
        
    def get_borrowed_books(self, member_id: str):
        lista: list[Book] = []
        for i in range(len(self.member[member_id].borrowed_books)):
            if self.member[member_id].borrowed_books[i].is_borrowed:
                lista.append(self.member[member_id].borrowed_books[i].title)
        return lista
    

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']
            
        
"""Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Methodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro."""

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    if not tree:
        return True
    stack = []
    stack.append(tree.left)
    stack.append(tree.right)
         
    while stack:
        node1 = stack.pop()
        node2 = stack.pop()
             
        if not node1 and not node2:
            continue
             
        if not node1 or not node2:
            return False
             
        if node1.key != node2.key:
             return False
             
        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)
         
        return True
    
print(symmetric([1,2,2,3,4,4,3]))