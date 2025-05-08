from flask import Flask, render_template, request, send_file
from caption_generator import generate_caption
from hashtag_generator import generate_hashtags
from image_generator import create_branded_image
import os

app = Flask(__name__)

# Ensure downloads directory exists
DOWNLOADS_DIR = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        keywords = request.form.get("keywords")
        tone = request.form.get("tone")
        platform = request.form.get("platform")

        # Generate content
        caption = generate_caption(keywords, tone, platform)
        hashtags = generate_hashtags(keywords)
        image_path = create_branded_image(keywords, DOWNLOADS_DIR)

        # Pass results to template
        return render_template(
            "index.html",
            caption=caption,
            hashtags=hashtags,
            image_path=os.path.basename(image_path),
        )

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(DOWNLOADS_DIR, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)