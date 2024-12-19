# Dynamic expense tracker
def a():
    expenses = {"Food": 0.0, "Transport": 0.0, "Entertainment": 0.0, "Clothes": 0.0, "Others": 0.0}

    while True:
        print("\n 1.Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option:")

        if choice == "1":
            category = input("Category (Food, Transport,  Entertainment, Clothes, Others): ").strip().title()
            if category not in expenses: #if we don't have any category so we can put any word for eg- like Watch,phones etc.
                category = "Others"#it will direct to Others Category
            amount = float(input("Enter the Amount:"))#Amount will be taken in float because in real world due to GST
            #sometimes we are charged in paisa 0.50Rs so we use float
            expenses[category] += amount
        elif choice == "2":
            total =  sum(expenses.values())
            print(" Total Expense Summary:")# final display or View Summary
            for category, amount in expenses.items():
                percentage = (amount / total * 100) if total > 0 else 0 #percentage logic
                print(f"{category}: ₹{amount:.2f} \tin percentage:({percentage:.2f}%)")
            print(f"Total: ₹{total:.2f}")
        elif choice == "3":
            print("Thankyou :) See you Again!")
            break
        else:
            print("Invalid Option. Please Check Again!")


if __name__ == "__main__":
        a()



