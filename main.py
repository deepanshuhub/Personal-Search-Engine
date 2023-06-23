from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "#use your refrence key"
model_engine = "#use your text-davinci"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    prompt = request.form["prompt"]
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
    resp = completion.choices[0].text
    return render_template("result.html", response=resp)

if __name__ == "__main__":
    app.run(debug=True)
