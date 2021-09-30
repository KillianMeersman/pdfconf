from flask import Flask, render_template, request, Response

from convert import pdf_to_string

app = Flask(__name__)

ALLOWED_EXTENSIONS = ("pdf",)


def allowed_file(file):
    filename = file.filename
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if "file" not in request.files:
            return "No file", 400

        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            return "No file", 400

        if file and allowed_file(file):
            return Response(
                pdf_to_string(file.read()), headers={"Content-Type": "text/plain"}
            )
