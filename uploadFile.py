from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from find_classes_and_interfaces import *
from g import *
from script import *
app = Flask(__name__,template_folder=os.path.dirname(__file__))
#app.config['UPLOAD_FOLDER']='uploads'
if 'uploads' not in os.listdir():
	os.mkdir('uploads')
@app.route('/upload')
def upload_Files():
   return render_template('upp.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)