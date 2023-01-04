from flask import Flask, make_response, request
import requests
from markupsafe import escape
import json
import version

app = Flask(__name__)


@app.route('/')
def index():
    return f'Index Page {version.get_version()}'


@app.route('/file', methods=['POST'])
def postfile():
    json_data = request.get_json()
    content = json_data.get("content")
    name = json_data.get("name")
    if len(content) >= 100:
        print("Content too long")
        return make_response("Content too long", 400)
    try:
        with open(f"{name}.txt", "w") as file:
            file.write(content)
            read_content = file.read()
            print(read_content)

    except Exception:
        return make_response("File couldn't be created", 500)
    return 'Post Success'


@app.route('/file')
def show_file_name():
    filename = request.args.to_dict()
    # show the user profile for that user
    if len(filename) <= 0:
        print("File not found")
        return make_response("File not found", 500)

    return f'File {escape(filename)}'
