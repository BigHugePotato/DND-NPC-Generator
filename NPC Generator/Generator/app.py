from flask import Flask, render_template
from npc_generator import generate_npc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/npc_generator')
def npc_generator():
    npc = generate_npc()
    return render_template('npc.html', npc=npc)

if __name__ == '__main__':
    app.run(debug=True)
