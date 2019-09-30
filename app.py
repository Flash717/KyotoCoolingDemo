from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Kyoto Cooling Demo'

@app.route('/user/<user_id>')
def getUser(user_id = None):
    return 'You requested user ' + user_id

@app.route('/user/<user_id>/connections')
def getUserConnections(user_id):
    degree = request.args.get('degree', '1')

    return 'You requested connections for user ' + user_id + ' with degree ' + degree

if __name__ == '__main__':
    app.run(port=8081)