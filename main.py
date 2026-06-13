import argparse
import json
import os
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import save_users, load_users

def load_projects_raw():
    if not os.path.exists("data/projects.json"):
        return []
    with open("data/projects.json", "r") as f:
        return json.load(f)

def save_projects_raw(projects):
    os.makedirs("data", exist_ok=True)
    with open("data/projects.json", "w") as f:
        json.dump(projects, f, indent=2)

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

    p3 = sub.add_parser("add-task")
    p3.add_argument("--project", required=True)
    p3.add_argument("--title", required=True)
    p3.add_argument("--assign", default="")

    p4 = sub.add_parser("complete-task")
    p4.add_argument("--project", required=True)
    p4.add_argument("--task-id", dest="task_id", required=True, type=int)

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
        projects = load_projects_raw()
        project = Project(args.title, args.user, args.desc, args.due)
        projects.append(project.to_dict())
        save_projects_raw(projects)
        print(f"Project '{args.title}' added for {args.user}!")

    elif args.command == "list-projects":
        projects = load_projects_raw()
        if not projects:
            print("No projects found.")
        for p in projects:
            print(f"[Project #{p['id']}] {p['title']} - owner: {p['owner_name']}")

    elif args.command == "add-task":
        projects = load_projects_raw()
        for p in projects:
            if p["title"].lower() == args.project.lower():
                task = Task(args.title, args.assign)
                p["tasks"].append(task.to_dict())
                save_projects_raw(projects)
                print(f"Task '{args.title}' added to '{args.project}'!")
                return
        print(f"Project '{args.project}' not found.")

    elif args.command == "complete-task":
        projects = load_projects_raw()
        for p in projects:
            if p["title"].lower() == args.project.lower():
                for t in p["tasks"]:
                    if t["id"] == args.task_id:
                        t["status"] = "complete"
                        save_projects_raw(projects)
                        print(f"Task #{args.task_id} marked complete!")
                        return
        print("Task not found.")

if __name__ == "__main__":
    main()