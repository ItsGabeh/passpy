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

# Analyze arguments
args = parser.parse_args()
print(args.email, args.add)
