from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models.models import Item

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    # READ: Fetch all items from the database ordered by date
    items = Item.query.order_by(Item.date_created).all()
    return render_template('index.html', items=items)

@main.route('/add', methods=['POST'])
def add_item():
    # CREATE: Add a new item to the database
    content = request.form.get('content')
    if content:
        new_item = Item(content=content)
        try:
            db.session.add(new_item)
            db.session.commit()
        except Exception as e:
            return f"There was an issue adding your item: {e}"
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete_item(id):
    # DELETE: Remove an item by ID
    item_to_delete = Item.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect(url_for('main.index'))
    except Exception as e:
        return f"There was a problem deleting that item: {e}"