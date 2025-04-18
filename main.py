"""
    passpy
    Simple program to manage your passwords

    Just a personal project, nothing serious...

    HOW IT WORKS
    passpy [email]

    Returns the password for the given email
"""
import argparse

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
