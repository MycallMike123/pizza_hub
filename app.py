from flask import Flask, render_template

app = Flask(__name__)

RESTAURANTS = [
  {
  'id': 1,
  'name': 'Crust & Crave Pizzeria',
  'description': 'An Italian-inspired eatery that celebrates the good life.',
  'location': '123 Main St',
  'cuisine': 'pizza',
  'price': 'Ksh. 1000',
  'rating': 4.5,
  },
  {
    'id': 2,
    'name': 'Bella Vita Bistro',
    'description': 'An Italian-inspired eatery that celebrates the good life.',
    'location': 'Kiambu',
    'cuisine': 'pizza',
    'price': 'Ksh. 1200',
    'rating': 4.5,
  },
  {
    'id': 3,
    'name': 'Urban Spice Kitchen',
    'description': 'A modern restaurant offering a vibrant fusion of flavors.',
    'location': 'Nairobi',
    'cuisine': 'pizza',
    'price': 'Ksh. 1500',
    'rating': 4.5,
  },
  {
    'id': 4,
    'name': 'Harvest & Hearth',
    'description': 'A cozy spot focusing on farm-to-table, comfort food.',
    'location': 'Kakamega',
    'cuisine': 'pizza',
    'price': 'Ksh. 1200',
    'rating': 4.3,
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html", restaurants = RESTAURANTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)