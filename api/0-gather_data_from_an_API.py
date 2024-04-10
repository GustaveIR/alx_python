import requests
import sys

USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

def check_first_line_formatting(user_id):
    """ Check student output formatting of the first line """

    try:
        # Fetch user's todos
        todos_response = requests.get(TODOS_URL).json()
        
        # Count total number of tasks and completed tasks for the user
        todos_count = sum(1 for todo in todos_response if todo['userId'] == user_id)
        todos_done = sum(1 for todo in todos_response if todo['userId'] == user_id and todo['completed'])

        # Fetch user details
        user_response = requests.get(USERS_URL).json()
        user_name = next((user['name'] for user in user_response if user['id'] == user_id), None)
        
        if user_name is None:
            raise ValueError("Invalid user ID")

        # Read first line from student's output
        with open('student_output', 'r') as f:
            first_line = f.readline().strip()

        # Compare with expected first line format
        expected_first_line = f"Employee {user_name} is done with tasks({todos_done}/{todos_count}):"
        if first_line == expected_first_line:
            print("First line formatting: OK")
        else:
            print("First line formatting: Incorrect")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")

def check_task_formatting(user_id):
    """ Check student output formatting of each task """

    try:
        # Read student output file
        with open('student_output', 'r') as f:
            next(f)  # Skip the first line
            for line_number, line in enumerate(f, start=1):
                if line.startswith('\t') and line[1:3] == '  ' and line.endswith('\n'):
                    print(f"Task {line_number} Formatting: OK")
                else:
                    print(f"Task {line_number} Formatting: Incorrect")
    except FileNotFoundError:
        print("Error: student_output file not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    check_first_line_formatting(user_id)
    check_task_formatting(user_id)
