import requests
import sys

def fetch_employee_data(employee_id):
    """
    Fetch employee data from the given employee ID and display their TODO list progress.

    Args:
        employee_id (int): The ID of the employee to fetch data for.

    Returns:
        None
    """
    try:
        # Fetch employee details
        employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        employee_response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        employee_data = employee_response.json()
        employee_name = employee_data.get('name')

        # Fetch employee TODO list
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        todos_response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        todos_data = todos_response.json()

        # Calculate number of completed tasks
        completed_tasks = [task for task in todos_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos_data)

        # Display employee TODO list progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")  # Format tasks with 1 tabulation and 1 space

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
try:
    employee_id = int(employee_id)
except ValueError:
    print("Employee ID must be an integer.")
    sys.exit(1)


    fetch_employee_data(employee_id)
