from flask import Flask, render_template, redirect, request,send_file,url_for
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
      print(f.filename)
      ####### WHILE FINAL TESTING UNCOMMENT THIS LINE TO GENERATE LINE DIRECTLY FROM API#############
      #payLoad=generateResponse(zip_to_result(os.path.join(os.path.dirname(__file__),f.filename)))
      #with open("output.json","w") as f:
      	#json.dumps(payLoad,f)
      ####################################################
      generatePythonFiles()
      zf = zipfile.ZipFile("FlaskFiles.zip", "w")
      for diir,subdir,fil in os.walk("Dirs"):
      	zf.write(diir)
      	for fname in fil:
      		zf.write(os.path.join(diir,fname))
      zf.close()
      return redirect('/download')
@app.route('/download')
def downloadFile ():
    path = "FlaskFiles.zip"
    return send_file(path, as_attachment=True)
		
if __name__ == '__main__':
   app.run(debug = True)