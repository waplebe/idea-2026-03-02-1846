# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks. The frontend provides a basic interface for interacting with the API.

**Why it's useful:**

A task manager is a fundamental tool for productivity. This API provides a foundation for building more complex task management applications or integrating task management functionality into existing systems.

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3.  **Set up the frontend:**
    ```bash
    npm install
    npm start
    ```

4.  **Set environment variables:**
    Create a `.env` file in the root directory and populate it with the following:
    ```
    DATABASE_URL=sqlite:///tasks.db
    ```

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `POST /tasks`: Creates a new task.  Request body: `{ "title": "Task Title", "description": "Task Description" }`
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `PUT /tasks/{id}`: Updates a specific task by ID. Request body: `{ "title": "New Task Title", "description": "New Task Description" }`
*   `DELETE /tasks/{id}`: Deletes a specific task by ID.

**Frontend:**

The frontend is a simple HTML page that uses JavaScript to interact with the API. It displays a list of tasks and provides forms for creating and updating tasks.

**Examples:**

*   **Create a task:**
    `POST /tasks` with a JSON body like `{"title": "Grocery Shopping", "description": "Buy milk, eggs, and bread"}`
*   **Get all tasks:**
    `GET /tasks`
*   **Update a task:**
    `PUT /tasks/1` with a JSON body like `{"title": "Grocery Shopping", "description": "Buy organic milk, free-range eggs, and sourdough bread"}`

**License:**

MIT License

**New Features:**

*   **Task Prioritization:** Added a `priority` field to the Task model and API endpoints.  Users can now assign a priority level (High, Medium, Low) to tasks.
*   **Task Due Dates:** Added a `due_date` field to the Task model and API endpoints. Users can specify a due date for each task.
*   **Frontend Updates:** Updated the frontend to display the priority and due date of each task.
*   **Testing:** Added unit tests for the Task model and API endpoints.

**Improvements:**

*   **Error Handling:** Improved error handling in the API endpoints.
*   **Documentation:** Updated the README file to include information about the new features and improvements.
*   **Code Style:** Improved the code style to follow PEP 8 guidelines.