"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from app.forms import UploadForm
from flask import render_template, request, jsonify, send_file, flash
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

"""@app.route('/api/upload', methods=['POST'])
def upload():
    file_folder = app.config['UPLOAD_FOLDER']
    upload_form = UploadForm()
    print(request)
    if request.method == 'POST':
        if upload_form.validate_on_submit():
            print("Validated")
            file = upload_form.photo.data
            file_name = secure_filename(file.filename)
            file.save(os.path.join(file_folder, file_name))
            return jsonify(
            message = "File Upload Successful",
            filename = file_name,
            description = upload_form.description.data
            )
        
        print("Not validated")
        return jsonify(errors = form_errors(upload_form))"""

@app.route('/api/upload', methods=['POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit() == True:
            description = request.form['description']
            file = request.files['photo']

            #saves photos to uplaods folder
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File Uploaded Succesfully','sucessful')
            return jsonify({"message": "File Upload Successful", "filename": filename, "description": description})
    else:
        return jsonify({"errors":[{"filename": form_errors(form)}]})

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf_():
    return jsonify({'csrf_token': generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


"""@app.errorhandler(404)
def page_not_found(error):
    Custom 404 page.
    return render_template('404.html'), 404"""


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="5990")