document.addEventListener('DOMContentLoaded', function() {
    const taskList = document.getElementById('task-list');
    const newTaskForm = document.getElementById('new-task-form');

    // Fetch tasks from the API
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            taskList.innerHTML = '';
            tasks.forEach(task => {
                const listItem = document.createElement('li');
                listItem.textContent = `${task.title} - Priority: ${task.priority.value}, Due Date: ${task.due_date}`;
                taskList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching tasks:', error));

    // Add new task
    newTaskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const priority = document.getElementById('priority').value;
        const dueDate = document.getElementById('due_date').value;

        if (!title) {
            alert('Title is required');
            return;
        }

        const data = {
            title: title,
            description: description,
            priority: priority,
            due_date: dueDate
        };

        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(newTask => {
            taskList.innerHTML = '';
            fetch('/tasks')
                .then(response => response.json())
                .then(tasks => {
                    tasks.forEach(task => {
                        const listItem = document.createElement('li');
                        listItem.textContent = `${task.title} - Priority: ${task.priority.value}, Due Date: ${task.due_date}`;
                        taskList.appendChild(listItem);
                    });
                });
        })
        .catch(error => console.error('Error creating task:', error));
    });
});