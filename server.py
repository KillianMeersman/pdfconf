import logging

from flask import Flask, Response, render_template, request

from convert import pdf_to_string

logging.basicConfig(level=logging.INFO)

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
            text = ""
            try:
                for i, page in enumerate(
                    pdf_to_string(file, password=request.form.get("password"))
                ):
                    text += f"\n\n{'=' * 25} PAGE {i + 1} {'=' * 25}\n\n"
                    text += page
            except ValueError as e:
                return Response(
                    str(e), status=400, headers={"Content-Type": "text/plain"}
                )

            return Response(text.strip(), headers={"Content-Type": "text/plain"})
