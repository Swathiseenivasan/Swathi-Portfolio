from flask import Flask,render_template as render


app=Flask(__name__)

@app.route('/')
def home():
    return render('index.html')

if __name__=="__main__":
    app.run(debug=True)