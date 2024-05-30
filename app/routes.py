from flask import Blueprint, render_template, request
from .models import Restaurant, Pizza, db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)

@bp.route('/restaurant/<int:restaurant_id>')
def restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    pizzas = Pizza.query.filter_by(restaurant_id=restaurant_id).all()
    return render_template('restaurant.html', restaurant=restaurant, pizzas=pizzas)
