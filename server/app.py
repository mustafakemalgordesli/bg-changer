from flask import Flask, request, jsonify
import uuid
import os
from werkzeug.utils import secure_filename
from remove_background import remove_background
from flask_cors import CORS

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
CORS(app=app, origins=["http://localhost:5173"])

@app.route("/")
def hello_world():
    return "Hello, World!"

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=["POST"])
def upload_image():
    if request.method == "POST":
        if 'image' not in request.files:
            return jsonify({ 
                "success": False
            }) 
        file = request.files['image']
        if file.filename == '':
            return jsonify({ 
                "success": False
            }) 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_name = uuid.uuid4().hex[:6].upper() + filename
            file_path = os.path.join(UPLOAD_FOLDER, file_name)
            file.save(file_path)
            return jsonify({ 
                "success": True,
                "data": file_name
            }) 
    return jsonify({ 
        "success": False
    }) 

@app.route("/remove", methods=["POST"])
def remove_bg():
    if request.method == "POST":
       filename = request.args.get('filename')
       if type(filename) == str and filename != "":
           path = remove_background("static/" + filename)
           return jsonify({ 
            "success": True,
            "data": path
           }) 
    return jsonify({ 
        "success": False
    }) 

if __name__ == '__main__':  
   app.run(debug=True, port=5000)