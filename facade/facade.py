class BookCatalog:
    def find_book(self, book_id):
        return f"Book ID {book_id}: Title, Description, Category, etc."

class UserAuthentication:
    def login(self, username, password):
        if username == "user2" and password == "password123":
            return True
        return False

class PaymentProcessing:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed successfully"

class BookReadingFacade:
    def __init__(self):
        self.book_catalog = BookCatalog()
        self.user_auth = UserAuthentication()
        self.payment_processor = PaymentProcessing()

    def read_book(self, book_id, username, password, amount):
        if self.user_auth.login(username, password):
            book_info = self.book_catalog.find_book(book_id)
            payment_status = self.payment_processor.process_payment(amount)
            return f"You are reading: {book_info}\n{payment_status}"
        return "Login failed. Please check your credentials."

def main():
    reading_service = BookReadingFacade()
    book_id = 123
    username = "user2"
    password = "password123"
    amount = 5.99
    result = reading_service.read_book(book_id, username, password, amount)

    print(result)

if __name__ == "__main__":
    main()
