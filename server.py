from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', firstName="Joe")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/form")
def formpage():
    return render_template('formpage.html')


@app.post("/create")
def create():
    fn = request.form.get("firstName")
    ln = request.form.get("lastName")
    return render_template('created.html', firstName=fn, lastName=ln)


if __name__ == "__main__":
    app.run(debug=True)