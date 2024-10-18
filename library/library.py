from datetime import datetime

class LibraryBook:
    def __init__(self, book_id, due_date, return_date):
        self.book_id = book_id
        self.due_date = due_date
        self.return_date = return_date
        self.days_overdue = self.calculate_days_overdue()
        self.fine_rate = self.determine_fine_rate()
        self.fine_amount = self.calculate_fine_amount()

    def calculate_days_overdue(self):
        """Calculate the number of days a book is overdue."""
        return (self.return_date - self.due_date).days

    def determine_fine_rate(self):
        """Determine the fine rate based on overdue days."""
        if self.days_overdue <= 0:
            return 0  # No fine if not overdue
        elif self.days_overdue <= 7:
            return 20
        elif self.days_overdue <= 14:
            return 50
        else:
            return 100

    def calculate_fine_amount(self):
        """Calculate the total fine amount based on the fine rate."""
        return self.fine_rate * self.days_overdue if self.days_overdue > 0 else 0

    def display_info(self):
        """Display book information along with overdue details."""
        print(f"Book ID: {self.book_id}")
        print(f"Due Date: {self.due_date.date()}")
        print(f"Return Date: {self.return_date.date()}")
        print(f"Days Overdue: {self.days_overdue}")
        print(f"Fine Rate: Ksh {self.fine_rate} per day")
        print(f"Total Fine Amount: Ksh {self.fine_amount}")


def main():
    # User inputs
    book_id = input("Enter Book ID: ")
    due_date_input = input("Enter Due Date (YYYY-MM-DD): ")
    return_date_input = input("Enter Return Date (YYYY-MM-DD): ")

    # Convert string inputs to datetime objects
    due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
    return_date = datetime.strptime(return_date_input, "%Y-%m-%d")

    # Create a LibraryBook instance
    book = LibraryBook(book_id, due_date, return_date)

    # Display the book information
    book.display_info()


if __name__ == "__main__":
    main()
