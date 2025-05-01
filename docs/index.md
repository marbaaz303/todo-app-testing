# Smart To-Do App

Welcome to the documentation for the **Smart To-Do App** built for the Software Testing and Automation course.

## Features

- Add, delete, and complete tasks
- Set task priority (Low, Medium, High)
- Assign due dates
- Filter and view tasks

## Live Demo

Access the deployed app here: [todo-app-testing-1.onrender.com](https://todo-app-testing-1.onrender.com)

## Data Model

Each task has the following fields:
- `text`: Description of the task
- `completed`: Boolean status
- `priority`: Task priority (Low, Medium, High)
- `due`: Optional due date

## Testing

Unit testing includes:
- White-box: Functional route logic
- Black-box: BVA, ECP test cases

## CI/CD

CI/CD pipeline is implemented using GitHub Actions. Tests are automatically run on push.

## Deployment

The app is deployed on Render with Gunicorn as the WSGI server.
