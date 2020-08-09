from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('test.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['textt']
    text2 = request.form['text2']
    if text=="admin" and text2=="admin":
        return render_template("tempp.html")
    else:
    	return "NONO"
if __name__ == '__main__':
    app.run(debug=True)
