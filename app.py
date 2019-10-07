from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/')
def stock_index():
    """Show all stock."""
    return render_template('stock_index.html', stock=stock.find())

@app.route('/stock', methods=['POST'])
def stock_submit():
    """Submit a new item."""
    item = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
        'costs' : request.form.get('costs').split()
    }
    stock.insert_one(item)
    return redirect(url_for('stock_index'))

@app.route('/stock/new')
def stock_new():
    """Create a new item."""
    return render_template('stock_new.html')

if __name__ == '__main__':
    app.run(debug=True)