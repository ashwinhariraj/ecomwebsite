from flask import Flask, render_template

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Shirts', 'price': 10.00},
    {'id': 2, 'name': 'Jeans', 'price': 15.00},
    {'id': 3, 'name': 'Hoodies', 'price': 20.00},
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)