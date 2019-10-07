from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Contractor
stock = db.stock

app = Flask(__name__)

#@app.route('/')
#def index():
#    """Return homepage."""
#    return render_template('home.html', msg='Flask is Cool!!')

# OUR MOCK ARRAY OF PROJECTS
stock = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

@app.route('/')
def stock_index():
    """Show all stock."""
    return render_template('stock_index.html', stock=stock.find())

if __name__ == '__main__':
    app.run(debug=True)