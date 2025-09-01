import os
import signal
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/launch_teleop', methods=['POST'])
def launch_teleop():
    try:
        subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "echo $$ > /tmp/teleop.pid; ros2 run omorobot_teleop teleop_keyboard; exec bash"
        ])
        return "teleop launched", 200
    except Exception as e:
        return str(e), 500

@app.route('/cancel_teleop', methods=['POST'])
def cancel_teleop():
    try:
        with open('/tmp/teleop.pid', 'r') as f:
            pid = int(f.read().strip())
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        os.remove('/tmp/teleop.pid')
        return "teleop finished", 200
    except Exception as e:
        return str(e), 400
        

@app.route('/launch_cartographer_rviz', methods=['POST'])
def launch_cartographer_rviz():
    try:
        subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "echo $$ > /tmp/cartographer_rviz.pid; ros2 launch omorobot_cartographer cartographer_rviz_launch.py; exec bash"
        ])
        return "cartographer_rviz launched", 200
    except Exception as e:
        return str(e), 500

@app.route('/cancel_cartographer_rviz', methods=['POST'])
def cancel_cartographer_rviz():
    try:
        with open('/tmp/cartographer_rviz.pid', 'r') as f:
            pid = int(f.read().strip())
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        os.remove('/tmp/cartographer_rviz.pid')
        return "cartographer_rviz finished", 200
    except Exception as e:
        return str(e), 400

@app.route('/launch_navigation_rviz', methods=['POST'])
def launch_navigation_rviz():
    try:
        subprocess.Popen([
            "gnome-terminal", "--",
            "bash", "-c",
            "echo $$ > /tmp/navigation_rviz.pid; ros2 launch omorobot_navigation2 navigation2_rviz_launch.py; exec bash"
        ])
        return "navigation_rviz launched", 200
    except Exception as e:
        return str(e), 500

@app.route('/cancel_navigation_rviz', methods=['POST'])
def cancel_navigation_rviz():
    try:
        with open('/tmp/navigation_rviz.pid', 'r') as f:
            pid = int(f.read().strip())
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        os.remove('/tmp/navigation_rviz.pid')
        return "navigation_rviz finished", 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
