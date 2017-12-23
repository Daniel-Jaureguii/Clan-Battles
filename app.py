from flask import Flask, render_template, jsonify, request, session, url_for, redirect, flash


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/play')
def playOfTheWeek():
    return render_template('playOfTheWeek.html')
@app.route('/rankings')
def rankings():
    return render_template('rankings.html')
@app.route('/freeAgents')
def freeAgents():
    return render_template('freeAgents.html')
@app.route('/chat')
def chat():
    return render_template('chatRoom.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(8080), debug=True)