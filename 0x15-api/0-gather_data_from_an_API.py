#!/usr/bin/python3
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            
                # Get TODO list for the employee
                    response = requests.get(url)
                        todos = response.json()
                            
                                # Get user details
                                    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
                                        user = user_response.json()
                                            
                                                # Extract employee name
                                                    employee_name = user['name']
                                                        
                                                            # Initialize variables
                                                                total_tasks = len(todos)
                                                                    completed_tasks = 0
                                                                        completed_task_titles = []
                                                                            
                                                                                # Count completed tasks and collect titles
                                                                                    for todo in todos:
                                                                                                if todo['completed']:
                                                                                                                completed_tasks += 1
                                                                                                                            completed_task_titles.append(todo['title'])
                                                                                                                                
                                                                                                                                    # Display progress
                                                                                                                                        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
                                                                                                                                            for title in completed_task_titles:
                                                                                                                                                        print(f"\t{title}")

                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                if len(sys.argv) != 2:
                                                                                                                                                                            print("Usage: python script.py employee_id")
                                                                                                                                                                                    sys.exit(1)
                                                                                                                                                                                        
                                                                                                                                                                                            try:
                                                                                                                                                                                                        employee_id = int(sys.argv[1])
                                                                                                                                                                                                            except ValueError:
                                                                                                                                                                                                                        print("Employee ID must be an integer.")
                                                                                                                                                                                                                                sys.exit(1)
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                        get_employee_todo_progress(employee_id)

