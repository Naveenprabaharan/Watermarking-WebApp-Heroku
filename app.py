from flask import Flask, render_template, request
import model as m

# Author Naveenprabaharan S - GCT[1918L12]

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello():
    if request.method == "POST":
        Water_Mark_image = request.files['Water_Mark_image']
        Water_Mark_Text = request.form['Water_Mark_Text']
        Water_Mark_Position = request.form['Water_Mark_Position']
        Water_Mark_Text_size = request.form['Water_Mark_Text_size']
        print(Water_Mark_Text, Water_Mark_Position,Water_Mark_Text_size)
        t_picname = m.Water_Mark(Water_Mark_image,Water_Mark_Text,Water_Mark_Position,Water_Mark_Text_size)

        #dcp = Document_Tampering_Detection
        dcp = f'static/final/{t_picname}.jpg'

    return render_template("index.html", pred=dcp)


@app.route("/")
def submit():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

