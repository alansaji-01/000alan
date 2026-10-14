# Apply a 20 percent discount to a book priced above 1000.
class Book:
    def __init__(self, title, author, price):
        self.title, self.author, self.price = title, author, price
    def final_price(self):
        return self.price * 0.80 if self.price > 1000 else self.price

if __name__ == '__main__':
    book = Book('Python Programming', 'Guido', 1500)
    print('Title:', book.title)
    print('Author:', book.author)
    print('Final price:', book.final_price())
