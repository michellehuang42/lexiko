import os, pytesseract, json, numpy, cv2
from PIL import Image, ImageFilter, ImageDraw
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from lab_data import load_lab_data

print(2+3)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello(name=None):
	return render_template('web-design.html', name=name)
	return url_for('static', filename='style.css')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			# return file.filename

			image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
			os.remove(UPLOAD_FOLDER+"/"+file.filename)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



			# return pytesseract.image_to_boxes(gray, config='--psm 6', nice=0)

			# check to see if we should apply thresholding to preprocess the image
			preprocess = request.form["preprocess"]
			if  preprocess == "thresh":
				gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

		   #  # make a check to see if median blurring should be done to remove
		   #  # noise

			elif preprocess == "blur":
				gray = cv2.medianBlur(gray, 3)
				print(preprocess)

			filename = "{}.png".format(os.getpid())
			cv2.imwrite(filename, gray)

			imagetext = pytesseract.image_to_string(filename)
			return imagetext

			imagetext = pytesseract.image_to_string(Image.open("./uploads/"+file.filename))
			# return imagetext 


@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/results")
def results(name=None):
	return render_template('results.html', name=name)
	return url_for('static', filename='results_style.css')

@app.route("/bye")
def bye():
	return "Goodbye World!!"

app.run(debug=True)

# need to import cv2