from flask import *
import os
from werkzeug.utils import secure_filename

app=Flask(__name__,template_folder=os.path.dirname(__file__))

app.secret_key = "secret_key12345"
path = os.getcwd()
if 'uploads' not in os.listdir():
	os.mkdir("uploads")
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['zip','rar'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def upload_form():
    return render_template('upp.html')
@app.route('/', methods=['POST'])
def upload_file():    
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)  
		file=request.files["file"]
		if file.filename=='':
			flash("No file selected for uploading")
			return redirect(request.url)
    	'''if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/')'''
	    if file and allowed_file(file.filename):
	    	filename=secure_filename(file.filename)
	    	file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
	    	flash('File successfully uploaded')
	    	return redirect('/')
    else:
        return redirect(request.url)


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=3000)