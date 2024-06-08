class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []

    def greeting(self):
        print("Welcome to Expense Tracker")

    def choose_task(self):
        while True:
            choose_task = input("Which task would you like to choose?\n"
                                "1. Add an expense\n"
                                "2. Remove an expense\n"
                                "3. Edit an expense\n"
                                "4. Add a category\n"
                                "5. Remove a category\n"
                                "6. Show all categories\n"
                                "7. Show all expenses\n"
                                "8. Exit\n"
                                "Enter the number of your choice: ")
            if choose_task == "1":
                self.add_expense()
            elif choose_task == "2":
                self.delete_expense()
            elif choose_task == "3":
                self.edit_expense()
            elif choose_task == "4":
                self.add_category()
            elif choose_task == "5":
                self.delete_category()
            elif choose_task == "6":
                self.show_all_categories()
            elif choose_task == "7":
                self.show_all_expenses()
            elif choose_task == "8":
                break
            else:
                print("Invalid option")

    def add_expense(self):
        try:
            amount = float(input("Enter the amount you spent: "))
            date = input("Enter the date of expense (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            if category not in self.categories:
                print("Category does not exist. Please add the category first.")
                return
            self.expenses.append({'amount': amount, 'date': date, 'category': category})
            print("Your expense has been added.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

    def delete_expense(self):
        try:
            index = int(input("Enter the index of the expense to delete: "))
            if 0 <= index < len(self.expenses):
                del self.expenses[index]
                print("Your expense has been deleted.")
            else:
                print("Invalid index")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the index.")

    def edit_expense(self):
        try:
            index = int(input("Enter the index of the expense to edit: "))
            if 0 <= index < len(self.expenses):
                amount = float(input("Enter the new amount: "))
                date = input("Enter the new date: ")
                category = input("Enter the new category: ")
                if category not in self.categories:
                    print("Category does not exist. Please add the category first.")
                    return
                self.expenses[index] = {'amount': amount, 'date': date, 'category': category}
                print("Your expense has been edited.")
            else:
                print("Invalid index")
        except ValueError:
            print("Invalid input. Please enter numeric values where appropriate.")

    def add_category(self):
        category = input("Enter the name of the new category: ")
        if category not in self.categories:
            self.categories.append(category)
            print("Category added.")
        else:
            print("Category already exists.")

    def delete_category(self):
        category = input("Enter the name of the category to delete: ")
        if category in self.categories:
            self.categories.remove(category)
            print("Category deleted.")
        else:
            print("Category does not exist.")

    def show_all_categories(self):
        print("Categories:", self.categories)

    def show_all_expenses(self):
        for i, expense in enumerate(self.expenses):
            print(f"{i}: Amount: {expense['amount']}, Date: {expense['date']}, Category: {expense['category']}")

def main():
    tracker = ExpenseTracker()
    tracker.greeting()
    tracker.choose_task()

if __name__ == "__main__":
    main()
