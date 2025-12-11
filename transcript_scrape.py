from flask import Flask, render_template, request
import json
import os
from dotenv import load_dotenv, dotenv_values
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app = Flask(__name__)
ytt_api = YouTubeTranscriptApi()

@app.route("/", methods=["POST", "GET"])
def link():
    transcript = None
    if request.method == "POST":
        link = request.form.get("link")
        try:
            video_id = link.replace("https://www.youtube.com/watch?v=","")
            transcript = ytt_api.fetch(video_id)
        except Exception as e:
            error = str(e)
        
        response = client.responses.create(
            model="gpt-5.1",
            input= f" Give a short but detailed summary of {transcript} however if the transcript is none then just greet and ask them to give a Youtube link with transcript use the word transcript enabled so that you can the provide a summary of the Youtube video"
        )
        summary = response.output_text
        print(response.output_text)
        return render_template("index.html", transcript=transcript, summary=summary, response=response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')