import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for the landing page (index)
@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

# Route for the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Route for the SustainScore page
@app.route('/sustainscore')
def sustainscore():
    print('Request for SustainScore page received')
    return render_template('sustainscore.html')

# Route for the comparison page
@app.route('/compare')
def compare():
    print('Request for compare page received')
    return render_template('compare.html')

if __name__ == '__main__':
    app.run(debug=True)
