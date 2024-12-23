from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return f'Welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form.get('nm')
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name=user))

@app.route("/")
def index():
   return render_template("index.html")  

if __name__ == '__main__':
   app.run(debug=True)

