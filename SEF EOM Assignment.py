import data
from data import valid_description, valid_condition, valid_departments, valid_suppliers
import admin
from datetime import timedelta, date, datetime



# Print welcome message
def print_welcome():
    print("\nIT Asset Management Application")
    print("-----------------------------------\n")

# Print asset details
def print_asset_details():
    print("ID  Description           Serial Number    Supplier      Date Acquired   Purchase Price   Current Value   Condition  Department  Next Maintenance")
    for key, asset in data.asset_dictionary.items(): 
        date_acquired = asset['Date Acquired'].strftime("%Y-%m-%d")  # Formatting datw
        next_maintenance = asset['Next Scheduled maintenance'].strftime("%Y-%m-%d") if asset['Next Scheduled maintenance'] is not None else "None"  # Format next maintenance or handle None case
        print(f"{key:<4} {asset['Description']:<20} {asset['Serial Number']:<15} {asset['Supplier']:<13} {date_acquired:<15} {asset['Purchase price']:<15} {asset['Current Value']:<15} {asset['Condition']:<10} {asset['Department']:<12} {next_maintenance:<}")



# Print menu options
def print_menu_options():
    print("\nEnter your option from the list ")
    print("--------------------------------------------")
    print("Enter A  - Add Asset")
    print("Enter B  - Update Current Value")
    print("Enter C  - Add Condition")
    print("Enter D  - Add Department")
    print("Enter E  - Delete Asset")
    print("Enter F  - Quit")
    print("Enter G  - Admin Menu")

# Get valid menu choice
def get_valid_menu_choice():
    valid_options = {'A', 'B', 'C', 'D', 'E', 'F','G'}
    while True:
        menu_choice = input("\nPlease enter your option > ").upper()
        if menu_choice not in valid_options:
            print("Sorry, this is not a valid option.")
            continue
        return menu_choice

# Add a new asset
def add_asset():
    while True:
        description = input("Please enter description: ")
        if description not in data.valid_description:
            print("Invalid description. Please choose from the following descriptions:", data.valid_description)
            continue
        
        while True:
            serial_number = input("Please enter serial number (15 digits): ")
            if not serial_number.isdigit() or len(serial_number) != 15:
                print("Invalid serial number. Please enter a unique 15-digit integer.")
                continue
            # Check if the serial number is already in use
            if any(asset['Serial Number'] == int(serial_number) for asset in data.asset_dictionary.values()):
                print("Serial number already exists. Please enter a unique serial number.")
                continue
            break
    
        while True:
            supplier = input("Please enter supplier: ")
            if supplier not in data.valid_suppliers:
                print("Invalid supplier. Please choose from the following suppliers:", data.valid_suppliers)
                continue
            break
        
        while True:
            date_acquired = input("Please enter date acquired (YYYY-MM-DD): ")
            try:
                date_acquired = datetime.strptime(date_acquired, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")
                continue
            break

        while True:
            purchase_price = input("Please enter purchase price: ")
            try:
                purchase_price = float(purchase_price)
            except ValueError:
                print("Invalid purchase price. Please enter a float value.")
                continue
            break

        while True:
            current_value = input("Please enter current value: ")
            try:
                current_value = float(current_value)
            except ValueError:
                print("Invalid current value. Please enter a float value.")
                continue
            break
        
        while True:
            condition = input("Please enter condition: ")
            if condition not in data.valid_condition:
                print("Invalid condition. Please choose from the following conditions:", data.valid_condition)
                continue
            break
        
        while True:
            department = input("Please enter department: ")
            if department not in data.valid_departments:
                print("Invalid department. Please choose from the following departments:", data.valid_departments)
                continue
            break
        
        while True:
            next_maintenance = input("Please enter next maintenance (YYYY-MM-DD): ")
            try:
                next_maintenance = datetime.strptime(next_maintenance, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")
                continue
            break
        

        # Adding asset to dictionary
        data.add_asset_to_dictionary(description, serial_number, supplier, date_acquired, purchase_price, current_value, condition, department, next_maintenance)
        print("Asset added successfully.")
        break


#Update a current value of an asset
def add_current_value():
    while True:
        asset_id_input = input("Please enter the ID of the asset you want to update: ")
        
        # Checking if the input is a valid integer
        try:
            asset_id = int(asset_id_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer ID.")
            continue
        
        # Checking if the asset ID exists
        if asset_id not in data.asset_dictionary:
            print("Asset ID not found.")
            continue

        # Retrieving the asset
        asset = data.asset_dictionary[asset_id]

        new_current_value_input = input("Please enter the new current value: ")
        
        # input for current value as float
        try:
            new_current_value = float(new_current_value_input)
        except ValueError:
            print("Invalid input. Please enter a valid float value for the current value.")
            continue

        # Updating the current value of the asset
        asset['Current Value'] = new_current_value

        print("Current value updated successfully.")
        break
    
# Add condition for an asset
def add_condition():
    while True:
        asset_id = input("Please enter the ID of the asset you want to update: ")
        
        # Checkinf if the asset ID is a valid integer
        if not asset_id.isdigit():
            print("Invalid input. Please enter a valid integer ID.")
            continue
        
        asset_id = int(asset_id)
        
        # Checking if the asset ID exists
        if asset_id not in data.asset_dictionary:
            print("Asset ID not found.")
            continue

        # Retrieving the asset
        asset = data.asset_dictionary[asset_id]

        new_condition = input("Please enter the new condition: ")
        
        # Checking if the entered condition is in the predefined list
        if new_condition not in data.valid_condition:
            print("Invalid condition. Please choose from the following conditions:", data.valid_condition)
            continue
        
        # Update the condition of the asset
        asset['Condition'] = new_condition

        print("Condition updated successfully.")
        break


# Add department for an asset
def add_department():
    while True:
        asset_id = input("Please enter the ID of the asset you want to update: ")
        
        if not asset_id.isdigit():
            print("Invalid input. Please enter a valid integer ID.")
            continue
        
        asset_id = int(asset_id)
        
        if asset_id not in data.asset_dictionary:
            print("Asset ID not found.")
            continue

        asset = data.asset_dictionary[asset_id]

        new_department = input("Please enter the new department: ")
        
        # Checking if the entered department is in the predefined list
        if new_department not in data.valid_departments:
            print("Invalid department. Please choose from the following departments:", data.valid_departments)
            continue
        
        # Updating the department of the asset
        asset['Department'] = new_department

        print("Department updated successfully.")
        break


# Delete an asset
def delete_asset():
    asset_id = int(input("Please enter the ID of the asset you want to delete: "))
    
    # Checking if the asset ID exists
    if asset_id not in data.asset_dictionary:
        print("Asset ID not found.")
        return

    # Deleting the asset from the dictionary
    del data.asset_dictionary[asset_id]

    print("Asset deleted successfully.")

# Main function
def main():
    while True:
        print_welcome()
        print_asset_details()
        print_menu_options()
        option = get_valid_menu_choice()
        if option == 'A':
            add_asset()
        elif option == 'B':
            add_current_value()
        elif option == 'C':
            add_condition()
        elif option == 'D':
            add_department()
        elif option == 'E':
            delete_asset()
        elif option == 'F':
            print("Exiting...")
            break
        elif option == 'G':
            admin.admin_menu()
        

if __name__ == "__main__":
    main()