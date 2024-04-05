import requests
import sys

def fetch_employee_data(employee_id):
    try:
        # Fetch employee details
        employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        employee_data = employee_response.json()
        employee_name = employee_data.get('name')

        # Fetch employee TODO list
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        todos_data = todos_response.json()

        # Calculate number of completed tasks
        completed_tasks = [task for task in todos_data if task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Display employee TODO list progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{len(todos_data)}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_data(employee_id)
