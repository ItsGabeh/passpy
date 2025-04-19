"""
    passpy
    Simple program to manage your passwords

    Just a personal project, nothing serious...

    HOW IT WORKS
    passpy [email]

    Returns the password for the given email
"""
import argparse
import pathlib
import os
import json
from cryptography.fernet import Fernet

# Create the program directory if not exists
# Get the user home directory
home = pathlib.Path.home()

# program's directory
passpy_dir = ".passpy"

# path to passpy dir
passpy_dir_path = pathlib.Path(home / passpy_dir)

# check if the passpy dir exists
if not passpy_dir_path.exists():
    print(f"passpy dir does not exists: {passpy_dir_path}")
    print(f"creating passpy dir at {passpy_dir_path}")

    # create the directory
    # exists_ok prevents error if in any case the dir exists
    passpy_dir_path.mkdir(exist_ok=True)

    # change permissions: only owner can read, write and execute
    os.chmod(passpy_dir_path, 0o700)

# Add specifications to the parser
parser = argparse.ArgumentParser(
    prog="passpy",
    description="Simple program to manage your passwords"
)

# Add argument for the email
parser.add_argument("email", help="Your email")
# Add argument to store an email
parser.add_argument("-a", "--add", help="Add your email", action="store_true")
# Add argument to store the password of the email
parser.add_argument("-p", "--pwd", help="Store your password")

# Analyze arguments
args = parser.parse_args()
print(args.email, args.add, args.pwd)

passpy_pwd_file = "passpy_pwd"


# check if the passpy file exists, otherwise it will create a new one
passpy_pwd_file_path = pathlib.Path(passpy_dir_path, passpy_pwd_file)
if not passpy_pwd_file_path.exists():
    passpy_pwd_file_path.touch(exist_ok=True)

# create Fernet key
# the key is stored in a file, but if os not it will create a new one
passpy_key_file = "passpy_key"
passpy_key_file_path = pathlib.Path(passpy_dir_path, passpy_key_file)
if not passpy_key_file_path.exists():
    passpy_key_file_path.touch(exist_ok=True)

    # this key must be stored in a file to recover
    key = Fernet.generate_key()

    # write the key to the file
    with passpy_key_file_path.open("wb") as key_file:
        key_file.write(key)

# if there is a passpy key then load the key
with passpy_key_file_path.open("rb") as key_file:
    key = key_file.read()

# load the fernet key
f = Fernet(key)

data = {}

with passpy_pwd_file_path.open("r", encoding="utf-8") as file:
    content = file.read()
    if content != "":
        data = json.loads(content)

# Save the mail and password to a file in passpy dir
if args.add and args.pwd is not None:

    # encrypt the password
    password = f.encrypt(args.pwd.encode())

    with passpy_pwd_file_path.open("w", encoding="utf-8") as file:
        # f.write(f"{args.email},{args.pwd}\n")
        data[args.email] = str(password)
        json.dump(data, file, indent=4)

# Base case, pass only the email
# return the email and password
elif args.email is not None:
    print(f"email: {args.email}: password: {data[args.email]}")