# API Project

This project contains scripts to interact with a REST API.

## Requirements

- Recommended editor: Visual Studio Code
- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- Libraries imported in Python files must be organized in alphabetical order
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should follow PEP 8 style
- Length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary values by key
- Code should not execute when imported (`if __name__ == "__main__":`)

## Tasks

### 0. Gather data from an API

Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

NB: The endpoint for accessing specific TODO items for an employee with ID = 1 will be `https://jsonplaceholder.typicode.com/users/1/todos` and the endpoint to get specific employee details will be `https://jsonplaceholder.typicode.com/users/1`

Requirements:

- Use `urllib` or `requests` module
- The script must accept an integer as a parameter, which is the employee ID
- Display employee TODO list progress in the following format:
