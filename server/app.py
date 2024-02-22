from flask import Flask, request, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route("/")
def hello_world():
    return "Hello, World!"

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods =["POST"])
def upload_image():
    if request.method == "POST":
        if 'image' not in request.files:
            return "error1"
        file = request.files['image']
        if file.filename == '':
            return "error2"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
    return "not_found"

if __name__ == '__main__':  
   app.run(debug=True, port=5000)