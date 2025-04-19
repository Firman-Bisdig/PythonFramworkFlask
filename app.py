from flask import Flask, render_template

app = Flask(__name__)


app_name = "My aplication name is : Firman and Man"

#1 App Route di flask "hello world"
@app.route("/")
def hello_world():
    return f"<p>Hello, semuanya, apa kabar! {app_name} </p>"

#2 App Route di flask
@app.route("/Aplikasi")
def Aplikasi():
    return f"<h1> Selamat datang di Aplikasi Man </h1>"

#3 App Route dengan HTML
@app.route("/about")
def about():
    return render_template('about.html')

#4 App Route 
@app.route("/about-bostrapp/")
def about_bostrapp():
    return render_template('about.html')

#4 App Route Dinamis
@app.route('/profile/<username>')
def profile(username):
    return "nama anda adalah {}".format(username)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya Menggunakan Angka
def user(user_id):
    return f"User ID: {user_id}!"

#7 App Route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
    return f"Welcome to {app_name}!"

@app.route('/data')
def data():
    user = {"name": "Firman", "age": 19, "city": "Pangkep"}
    return render_template('data.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)