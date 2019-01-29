from flask import Flask, request, url_for, redirect
from flask import render_template
from database import create, delete, get_all_pics

app = Flask(__name__)
app.config['SECRET_KEY']= "hackerman"
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/emkay')
def emkay():
    return render_template("emkay.html")

@app.route('/liberstad')
def liberstad():
    pics=get_all_pics()
    return render_template("liberstad.html",pics=pics)
@app.route('/liberstad/upload',methods=['GET','POST'])
def upload():
    
    if request.method=='POST':
        if request.form['password']=="gipguy2019":
            print(request.form)
            print(request.files)
            f=request.files['pic']
            f.save("static/images/"+f.filename)
            title=request.form['title']
            create(f.filename,title)
            return redirect(url_for('liberstad'))
        else:
            return render_template('upload.html', error="wrong password")
    else:
        return render_template('upload.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
if __name__ == '__main__':
    app.run(debug=True)

