from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    filter_by = request.args.get('filter', 'all')
    tasks = load_tasks()
    if filter_by == 'completed':
        tasks = [t for t in tasks if t['completed']]
    elif filter_by == 'active':
        tasks = [t for t in tasks if not t['completed']]
    return render_template('index.html', tasks=tasks, filter_by=filter_by)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    priority = request.form.get('priority')
    due = request.form.get('due')

    if task_text:
        tasks = load_tasks()
        tasks.append({
            'text': task_text,
            'completed': False,
            'priority': priority or 'Medium',
            'due': due or ''
        })
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
