from app import app, render_template

@app.route('/')
def index():
    name = 'Dan'
    return render_template('index.html', n=name)