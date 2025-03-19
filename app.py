# flask server application
from flask import Flask, jsonify, render_template, request,send_file,session





app = Flask(__name__, static_folder='static')




# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)