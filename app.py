from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=host)
db = client.get_default_database()
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
        'description': request.form.get('description'),
        'cost': request.form.get('cost')
    }
    stock.insert_one(item)
    return redirect(url_for('stock_index'))

@app.route('/stock/<item_id>')
def stock_show(item_id):
    """Show a single item."""
    item = stock.find_one({'_id': ObjectId(item_id)})
    return render_template('stock_show.html', item=item)

@app.route('/stock/<item_id>', methods=['POST'])
def stock_update(item_id):
    """Submit an edited item."""
    updated_item = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    stock.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': updated_item})
    return redirect(url_for('stock_show', item_id=item_id))

@app.route('/stock/new')
def stock_new():
    """Create a new item."""
    return render_template('stock_new.html', item = {}, title = 'New Item')

@app.route('/stock/<item_id>/edit')
def stock_edit(item_id):
    """Show the edit form for a item."""
    item = stock.find_one({'_id': ObjectId(item_id)})
    return render_template('stock_edit.html', item=item, title = 'Edit Item')

@app.route('/stock/<item_id>/delete', methods=['POST'])
def stock_delete(item_id):
    """Delete one item."""
    stock.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('stock_index'))

if __name__ == '__main__':
    app.run(debug=True)