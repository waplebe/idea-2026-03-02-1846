from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from utils import to_dict
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///tasks.db')
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.Enum('High', 'Medium', 'Low'), default='Medium')
    due_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Task {self.title}>'

    def to_dict(self):
        """Convert the task object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'due_date': str(self.due_date) if self.due_date else None
        }

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [task.to_dict() for task in tasks]
    return jsonify(task_list)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority')
    due_date_str = data.get('due_date')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    new_task = Task(title=title, description=description, priority=priority)

    if due_date_str:
        try:
            new_task.due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.priority = data.get('priority', task.priority)

    if data.get('due_date'):
        try:
            task.due_date = datetime.datetime.strptime(data['due_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    db.init_app(app)
    app.run(debug=True)