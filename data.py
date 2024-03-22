from datetime import timedelta, date, datetime

valid_description =['Desktop Computer','Laptop Computer', 'Printer', 'Projector', 'Mobile Phone', 'TV', 'Server','Router','Network switch', 'Firewall']
valid_suppliers = ['PC Computers', 'CF Technology', 'YH Tech', 'PL Technology', 'RF Servers']
valid_condition =['New', 'Good', 'Moderate', 'Old']
valid_departments = ['HR', 'IT', 'HR', 'Finance', 'Sales', 'Marketing','Operations']




# Defining IT assets
asset1 = {
    "Description": "Desktop Computer",
    "Serial Number": 123456789012345,
    "Supplier": "PC Computers",
    "Date Acquired": datetime(2020, 2, 6),
    "Purchase price": 1000.00,
    "Current Value": 700.00,
    "Condition": "Moderate",
    "Department": "HR",
    "Next Scheduled maintenance": date.today() + timedelta(days=10)
}

asset2 = {
    "Description": "Laptop Computer",
    "Serial Number": 123456789012346,
    "Supplier": "CF Technology",
    "Date Acquired": datetime(2023, 4, 16),
    "Purchase price": 400.00,
    "Current Value": 300.00,
    "Condition": "Good",
    "Department": "IT",
    "Next Scheduled maintenance": date.today() + timedelta(days=50)
}

asset3 = {
    "Description": "Printer",
    "Serial Number": 123456789012347,
    "Supplier": "YH Tech",
    "Date Acquired": datetime(2024, 2, 6),
    "Purchase price": 1000.00,
    "Current Value": 1000.00,
    "Condition": "New",
    "Department": "Finance",
    "Next Scheduled maintenance": date.today() + timedelta(days=90)
}

asset4 = {
    "Description": "Projector",
    "Serial Number": 123456789012348,
    "Supplier": "CF Technology",
    "Date Acquired": datetime(2015, 12, 9),
    "Purchase price": 500.00,
    "Current Value": 100.00,
    "Condition": "Old",
    "Department": "Sales",
    "Next Scheduled maintenance": date.today() + timedelta(days=270)
}

asset5 = {
    "Description": "Mobile phone",
    "Serial Number": 123456789012349,
    "Supplier": "PC Computers",
    "Date Acquired": datetime(2022, 10, 3),
    "Purchase price": 1000.00,
    "Current Value": 800.00,
    "Condition": "Good",
    "Department": "Marketing",
    "Next Scheduled maintenance": date.today() + timedelta(days=56)
}

asset6 = {
    "Description": "TV",
    "Serial Number": 123456789012340,
    "Supplier": "PL Technology",
    "Date Acquired": datetime(2020, 5, 17),
    "Purchase price": 300.00,
    "Current Value": 200.00,
    "Condition": "Moderate",
    "Department": "Operations",
    "Next Scheduled maintenance": date.today() + timedelta(days=6)
}

asset7 = {
    "Description": "Server",
    "Serial Number": 123456789012341,
    "Supplier": "RF Servers",
    "Date Acquired": datetime(2016, 8, 26),
    "Purchase price": 3000.00,
    "Current Value": 2000.00,
    "Condition": "Old",
    "Department": "IT",
    "Next Scheduled maintenance": date.today() + timedelta(days=260)
}

asset8 = {
    "Description": "Router",
    "Serial Number": 123456789012342,
    "Supplier": "PC Computers",
    "Date Acquired": datetime(2019, 9, 30),
    "Purchase price": 100.00,
    "Current Value": 60.0,
    "Condition": "Moderate",
    "Department": "IT",
    "Next Scheduled maintenance": date.today() + timedelta(days=45)
}

asset9 = {
    "Description": "Network switch",
    "Serial Number": 123456789012343,
    "Supplier": "YH Tech",
    "Date Acquired": datetime(2018, 3, 10),
    "Purchase price": 100.00,
    "Current Value": 60.00,
    "Condition": "Moderate",
    "Department": "IT",
    "Next Scheduled maintenance": date.today() + timedelta(days=5)
}

asset10 = {
    "Description": "Firewall",
    "Serial Number": 123456789012345,
    "Supplier": "PC Computers",
    "Date Acquired": datetime(2014, 7, 21),
    "Purchase price": 4000.00,
    "Current Value": 2700.00,
    "Condition": "Old",
    "Department": "IT",
    "Next Scheduled maintenance": date.today() + timedelta(days=60)
}

# Defining IT asset dictionary
asset_dictionary = {
    1: asset1,
    2: asset2,
    3: asset3,
    4: asset4,
    5: asset5,
    6: asset6,
    7: asset7,
    8: asset8,
    9: asset9,
    10: asset10
}

# Add new IT asset to dictionary
def add_asset_to_dictionary(description, serial_number, supplier, date_acquired, purchase_price, current_value, condition, department, next_maintenance):
    asset_dictionary[max(asset_dictionary.keys()) + 1] = {
        "Description": description,
        "Serial Number": serial_number,
        "Supplier": supplier,
        "Date Acquired": date_acquired,
        "Purchase price": purchase_price,
        "Current Value": current_value,
        "Condition": condition,
        "Department": department,
        "Next Scheduled maintenance": next_maintenance
    }

# Delete an IT asset from the dictionary
def delete_asset(key):
    del asset_dictionary[key]

#add_asset_to_dictionary("New Server", 123456789012350, "PC Computers", datetime(2023, 1, 15), 4000, 3500, "Good", "IT", date.today() + timedelta(days=90))

#delete_asset(10)
