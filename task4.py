import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args        

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone number."
        except KeyError:
            return "Contact doesn't exist."
        except IndexError:
            return "Enter the argument for the command."
    return inner

#Errors mapping:
#add John          -> ValueError
#update John       -> ValueError
#show              -> IndexError
#show Unknown      -> KeyError
#all with no data  -> KeyError

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    save_contacts(contacts)
    return "Contact added."


@input_error
def update_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    save_contacts(contacts)
    return "Contact updated."


@input_error
def show_contact(args, contacts):
    name = args[0]

    if name not in contacts:
        raise KeyError

    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        raise KeyError

    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result

def main():
    contacts = load_contacts()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hi! I'm a bot who manages your contacts. I can add, update or show existing contacts. How can I help?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "update":
            print(update_contact(args, contacts))
        elif command == "show":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Bot supports 'add', 'update', 'show' and 'all' as commands")

if __name__ == "__main__":
    main()