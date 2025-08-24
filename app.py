from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Shikha")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None
    error = None
    if request.method == "POST":
        age_str = request.form.get("age", "").strip()
        try:
            age = int(age_str)
            result = "Adult ✅" if age >= 18 else "Minor ❌"
        except ValueError:
            error = "Please enter a valid whole number for age."
    return render_template("predict.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
