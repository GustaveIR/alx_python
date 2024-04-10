import sys
import requests

def fetch_employee_data(employee_id):
    # Fetching employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Fetching employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Counting completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    return employee_name, completed_tasks, todos

def display_progress(employee_name, completed_tasks, total_tasks):
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, completed_tasks, all_tasks = fetch_employee_data(employee_id)
    display_progress(employee_name, completed_tasks, len(all_tasks))
