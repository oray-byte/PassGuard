from numpy import void
from pathlib import Path
from hashlib import pbkdf2_hmac as pb
from os import mkdir, urandom, access, chdir, stat, chmod, walk

def login() -> bool:
    # TEMP |
    #      v
    password: str = "temp"
    
    entered_password = input("Enter master password: ")
    
    if (entered_password == password):
        print("Login successful...")
        return True
    else:
        print("Login unsuccessful...")
        return False
    
def add_login() -> void:
    if (not login()):
        return # Login unsuccessful
    # TODO: Implement add_login
    return

def delete_login() -> void:
    if (not login()):
        return # Login unsuccessful
    # TODO: Implement delete_login
    return

def view_login() -> void:
    if (not login()):
        return # Login unsuccessful
    table = open("C:/passwords/passwords.csv", "r")

    for row in table:
        data = row.split(',')[0:4]
        print(data)
        
    # TODO: Implement view_login()
    table.close()
    return

pass_folder = Path("C:/passwords")

if not pass_folder.exists():
    pass_folder.mkdir()

while (True):
    print("[0] Add login information\n[1] Delete login information\n[2] View login information\n[3] Exit")
    u_input: int = int(input("Option: "))
    if (u_input == 0):
        add_login()
    elif (u_input == 1):
        delete_login()
    elif (u_input == 2):
        view_login()
    elif (u_input == 3):
        break
    else:
        continue