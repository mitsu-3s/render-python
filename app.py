from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/list')
def show_list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)