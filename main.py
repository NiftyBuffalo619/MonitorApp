import logging
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='ui', static_url_path='', static_folder='ui')
app.logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
app.logger.addHandler(file_handler)



@app.route('/')
def index():
    logging.info('Serving index')
    return render_template('index.html')
@app.route('/ui')
def send_report():
    return send_from_directory('ui')

if __name__ == '__main__':
    app.run()