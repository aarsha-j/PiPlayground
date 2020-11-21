from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello_world.html')

@app.route('/about')
def index1():
    sports = ["Karate", "Dance", "Basketball"]
    languages = ["English", "Nepali", "ASL"]
    music = ["Underneath the Tree", "Can I Be Him", "Hey Joe"]
    code = ["HTML/CSS", "JavaScript", "Python"]
    return render_template('other_file.html', sports=sports, languages=languages, music=music, code=code)

@app.route('/dynamic')
def dynamic():
    greeting = "What's good"
    name = "Aarsha"
    movies = ["The Godfather", "Goodfellas", "The Princess Switch", "Cinderella", "Get Out"]
    return render_template("dynamic.html", greeting=greeting, name=name, movies=movies)

@app.errorhandler(404)
def error404(error):
    return "<h1>Sike, this page doesn't exist.</h1><h2>Get your life together</h2><h3>You're still here?</h3><h4>You're better than this</h4><h5>When an error page is more put together than you.</h5><h6>Imagine getting roasted by an error page...</h6>", 404
  
if __name__== '__main__' :
    app.run(debug=True, host='0.0.0.0') 