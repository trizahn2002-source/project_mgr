import argparse
from models.user import User
from utils.storage import save_users, load_users

def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )
    subparsers = parser.add_subparsers(dest="command")

    # add-user command
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    # list-users command
    subparsers.add_parser("list-users")

    args = parser.parse_args()

    if args.command == "add-user":
        users_data = load_users()
        users = [User(u["name"], u["email"]) for u in users_data]
        new_user = User(args.name, args.email)
        users.append(new_user)
        save_users(users)
        print(f"User '{args.name}' added!")

    elif args.command == "list-users":
        users = load_users()
        if not users:
            print("No users found.")
        for u in users:
            print(f"[User #{u['id']}] {u['name']} - {u['email']}")

if __name__ == "__main__":
    main()
            