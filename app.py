from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("103-index.html")

# if we have server/ip and port 
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)