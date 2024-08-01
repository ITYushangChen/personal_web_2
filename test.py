from flask import Flask, request, send_file,render_template
import subprocess
import os
from werkzeug.utils import secure_filename
import logging
from logging.handlers import RotatingFileHandler



app = Flask(__name__)
app.secret_key = 'somerandomshitsecretkey18265920'
# if not app.debug:
#     file_handler = RotatingFileHandler('server.log', maxBytes=10240, backupCount=10)
#     file_handler.setFormatter(logging.Formatter(
#         '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
#     ))
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.setLevel(logging.INFO)
#     app.logger.info('Video compression startup')

# UPLOAD_FOLDER = 'uploads'
# COMPRESSED_FOLDER = 'compressed'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER

# # Ensure the upload and compressed directories exist
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

# @app.route('/')
# def index():
#     return '''
    # <!doctype html>
    # <title>Video Compressor</title>
    # <h1>Upload a video to compress</h1>
    # <form method=post enctype=multipart/form-data action="/compress">
    #   <input type=file name=video>
    #   <input type=submit value=Compress>
    # </form>
    # '''

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/compress', methods=['POST'])
# def compress_video():
#     if 'video' not in request.files:
#         return 'No file part'
#     file = request.files['video']
#     if file.filename == '':
#         return 'No selected file'

#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#         # Define compressed video file path
#         compressed_filename = f"compressed_{filename}"
#         # compressed_filepath = os.path.join(app.config['COMPRESSED_FOLDER'], compressed_filename)
#         compressed_filepath = os.path.join('/home/YushangChen/compressed/', compressed_filename)
#         # Compress video using ffmpeg
#         command = f"ffmpeg -i {filepath} -vcodec h264 -acodec mp2 {compressed_filepath}"
#         subprocess.run(command, shell=True)

#         # Send the compressed video file as a response
#         return send_file(compressed_filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
