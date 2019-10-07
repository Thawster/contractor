from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Flask is Cool!!')

# OUR MOCK ARRAY OF PROJECTS
stock = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

@app.route('/stock')
def stock_index():
    """Show all stock."""
    return render_template('stock_index.html', stock=stock)

if __name__ == '__main__':
    app.run(debug=True)