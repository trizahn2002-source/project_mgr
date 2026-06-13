# Python Project Management CLI Tool

## Setup
pip install -r requirements.txt

## How to Run Commands

### Users
python3 main.py add-user --name "Alex" --email "alex@gmail.com"
python3 main.py list-users

### Projects
python3 main.py add-project --user "Alex" --title "My Project" --desc "Description" --due 2025-12-31
python3 main.py list-projects

### Tasks
python3 main.py add-task --project "My Project" --title "Do something" --assign "Alex"
python3 main.py complete-task --project "My Project" --task-id 1

## Features
- Create and manage users, projects and tasks
- Data saved to JSON files
- Object-oriented design with inheritance