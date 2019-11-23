import os
from uuid import uuid4
from flask import Flask, render_template, request, jsonify, send_from_directory
from subprocess import TimeoutExpired
from common.config import cfg as config
from common.docx2pdf import LibreOfficeError, convert_to
from common.errors import RestAPIError, InternalServerErrorError
from common.files import uploads_url, save_to
import boto3

app = Flask(__name__, static_url_path='')


@app.route('/')
def hello():
    # return render_template('home.html')
    return 'hello'


@app.route('/upload', methods=['POST'])
def upload_file():
    upload_id = str(uuid4())
    source = save_to(os.path.join(
        config['uploads_dir'], 'source', upload_id), request.files['file'])

    try:
        result = convert_to(os.path.join(
            config['uploads_dir'], 'pdf', upload_id), source, timeout=15)

        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(result[1:], 'dqdkbi8zxasp', result)

    except LibreOfficeError:
        raise InternalServerErrorError(
            {'message': 'Error when converting file to PDF'})
    except TimeoutExpired:
        raise InternalServerErrorError(
            {'message': 'Timeout when converting file to PDF'})

    return jsonify({'result': {'source': uploads_url(source), 'pdf': uploads_url(result)}})


@app.route('/uploads/<path:path>', methods=['GET'])
def serve_uploads(path):
    return send_from_directory(config['uploads_dir'], path)


@app.errorhandler(500)
def handle_500_error():
    return InternalServerErrorError().to_response()


@app.errorhandler(RestAPIError)
def handle_rest_api_error(error):
    return error.to_response()


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
