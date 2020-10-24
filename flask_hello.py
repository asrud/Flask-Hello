from flask import Flask, render_template #, request
from dotenv import load_dotenv
load_dotenv('.flaskenv')

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or '--'
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=80)
