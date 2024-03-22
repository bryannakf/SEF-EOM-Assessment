import data

# Add a new valid supplier
def add_supplier():
    new_supplier = input("Enter the name of the new supplier: ")
    data.valid_suppliers.append(new_supplier)
    print(f"Supplier '{new_supplier}' added successfully.")

# Add a new valid department
def add_department():
    new_department = input("Enter the name of the new department: ")
    data.valid_departments.append(new_department)
    print(f"Department '{new_department}' added successfully.")

# Add a new valid description
def add_description():
    new_description = input("Enter the name of the new description: ")
    data.valid_description.append(new_description)
    print(f"Description '{new_description}' added successfully.")

# Add a new valid condition
def add_condition():
    new_condition = input("Enter the name of the new condition: ")
    data.valid_condition.append(new_condition)
    print(f"Condition '{new_condition}' added successfully.")

# View current valid suppliers
def view_valid_suppliers():
    print("\nCurrent Valid Suppliers:")
    for supplier in data.valid_suppliers:
        print("-", supplier)

# View current valid departments
def view_valid_departments():
    print("\nCurrent Valid Departments:")
    for department in data.valid_departments:
        print("-", department)

# View current valid descriptions
def view_valid_descriptions():
    print("\nCurrent Valid Descriptions:")
    for description in data.valid_description:
        print("-", description)

# View current valid conditions
def view_valid_conditions():
    print("\nCurrent Valid Conditions:")
    for condition in data.valid_condition:
        print("-", condition)

# Display admin menu options
def print_admin_menu():
    print("\nAdmin Menu")
    print("-----------")
    print("1. Add New Supplier")
    print("2. Add New Description")
    print("3. Add New Condition")
    print("4. Add New Department")
    print("5. View Valid Suppliers")
    print("6. View Valid Descriptions")
    print("7. View Valid Conditions")
    print("8. View Valid Departments")
    print("9. Exit")



# Main function 
def admin_menu():
    while True:
        print_admin_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_supplier()
        elif choice == '2':
            add_description()
        elif choice == '3':
            add_condition()
        elif choice == '4':
            add_department()
        elif choice == '5':
            view_valid_suppliers()
            input("Press Enter to continue...")
        elif choice == '6':
            view_valid_descriptions()
            input("Press Enter to continue...")
        elif choice == '7':
            view_valid_conditions()
            input("Press Enter to continue...")
        elif choice == '8':
            view_valid_departments()
            input("Press Enter to continue...")
        elif choice == '9':
            print("Exiting Admin Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    admin_menu()


