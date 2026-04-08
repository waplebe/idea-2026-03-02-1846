from flask import jsonify

def to_dict(task):
    """Convert a Task object to a dictionary."""
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'priority': task.priority,
        'due_date': task.due_date
    }