from app import db

def to_dict(self):
    """Convert the task object to a dictionary."""
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description
    }