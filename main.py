import argparse
import json
from models.user import User
from models.project import Project
from utils.storage import save_users, load_users

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("add-user")
    p1.add_argument("--name", required=True)
    p1.add_argument("--email", required=True)

    sub.add_parser("list-users")

    p2 = sub.add_parser("add-project")
    p2.add_argument("--user", required=True)
    p2.add_argument("--title", required=True)
    p2.add_argument("--desc", default="")
    p2.add_argument("--due", default="")

    sub.add_parser("list-projects")

    args = parser.parse_args()

    if args.command == "add-user":
        users_data = load_users()
        users = [User(u["name"], u["email"]) for u in users_data]
        users.append(User(args.name, args.email))
        save_users(users)
        print(f"User '{args.name}' added!")

    elif args.command == "list-users":
        users = load_users()
        if not users:
            print("No users found.")
        for u in users:
            print(f"[User #{u['id']}] {u['name']} - {u['email']}")

    elif args.command == "add-project":
        projects_data = load_projects_raw()
        project = Project(args.title, args.user, args.desc, args.due)
        projects_data.append(project.to_dict())
        with open("data/projects.json", "w") as f:
            json.dump(projects_data, f, indent=2)
        print(f"Project '{args.title}' added for {args.user}!")

    elif args.command == "list-projects":
        projects = load_projects_raw()
        if not projects:
            print("No projects found.")
        for p in projects:
            print(f"[Project #{p['id']}] {p['title']} - owner: {p['owner_name']}")

def load_projects_raw():
    import os
    if not os.path.exists("data/projects.json"):
        return []
    with open("data/projects.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    main()