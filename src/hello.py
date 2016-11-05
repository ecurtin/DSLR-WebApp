from flask import Flask, render_template
import gphoto2 as gp
app = Flask(__name__)

context = gp.Context()
camera = gp.Camera()

@app.route("/")
def hello():
    # return "Hello World!"
    return render_template('layout.html')

@app.route("/other")
def otherHello():
    return "this other thing"

@app.route("/init")
def initCamera():
    camera.init(context)
    text = camera.get_summary(context)
    return str(text)







if __name__ == "__main__":
    app.run()
