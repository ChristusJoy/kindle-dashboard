from flask import Flask, Response, render_template, jsonify, request
from flask_cors import CORS
import subprocess
TASK_FILE = 'todo.txt'
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('index.html')


#Playback stats and controls

@app.route('/data')
def media_info():
    try:
        # Get playback status (Playing or Paused)
        status = subprocess.check_output(
            ['playerctl', 'status'], universal_newlines=True
        ).strip()

        # Get media metadata
        title = subprocess.check_output(
            ['playerctl', 'metadata', 'xesam:title'], universal_newlines=True
        ).strip()
        artist = subprocess.check_output(
            ['playerctl', 'metadata', 'xesam:artist'], universal_newlines=True
        ).strip()
        art_url = subprocess.check_output(
            ['playerctl', 'metadata', 'mpris:artUrl'], universal_newlines=True
        ).strip()

        return jsonify({
            'title': title,
            'artist': artist,
            'art_url': art_url,
            'status': status
        })
    except subprocess.CalledProcessError:
        return jsonify({
            'title': '',
            'artist': '',
            'art_url': '',
            'status': 'Stopped'
        })

@app.route('/playpause')
def play_pause():
    try:
        subprocess.run(['playerctl', 'play-pause'])
        return Response("Toggled play/pause", mimetype='text/plain')
    except subprocess.CalledProcessError:
        return Response("Error toggling play/pause", mimetype='text/plain')
    
@app.route('/next')
def next_track():
    try:
        subprocess.run(['playerctl', 'next'])
        return Response("Next track", mimetype='text/plain')
    except subprocess.CalledProcessError:
        return Response("Error skipping to next track", mimetype='text/plain')
    
@app.route('/prev')
def prev_track():
    try:
        subprocess.run(['playerctl', 'previous'])
        return Response("Previous track", mimetype='text/plain')
    except subprocess.CalledProcessError:
        return Response("Error skipping to previous track", mimetype='text/plain')
    

# Todo list that sync with a text file

def read_tasks():
    unfinished = []
    completed = []
    current = None

    with open(TASK_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '[unfinished]':
                current = unfinished
            elif line == '[completed]':
                current = completed
            elif line and current is not None:
                current.append(line)

    return {'unfinished': unfinished, 'completed': completed}


def write_tasks(data):
    with open(TASK_FILE, 'w') as f:
        f.write('[unfinished]\n')
        for task in data['unfinished']:
            f.write(task + '\n')
        f.write('[completed]\n')
        for task in data['completed']:
            f.write(task + '\n')


@app.route('/todo', methods=['GET'])
def get_tasks():
    return jsonify(read_tasks())


@app.route('/toggle', methods=['POST'])
def toggle_task():
    task = request.json.get('task')
    data = read_tasks()

    if task in data['unfinished']:
        data['unfinished'].remove(task)
        data['completed'].append(task)
    elif task in data['completed']:
        data['completed'].remove(task)
        data['unfinished'].append(task)

    write_tasks(data)
    return jsonify(success=True)


@app.route('/reset', methods=['POST'])
def reset_tasks():
    data = read_tasks()
    all_tasks = data['unfinished'] + data['completed']
    write_tasks({'unfinished': all_tasks, 'completed': []})
    return jsonify(success=True)   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
