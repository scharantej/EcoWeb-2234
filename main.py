
from flask import Flask, render_template, request
app = Flask(__name__)

products = [
    {'name': 'Eco-Friendly T-Shirt', 'price': 25, 'image': 'tshirt.jpg'},
    {'name': 'Sustainable Jeans', 'price': 40, 'image': 'jeans.jpg'},
    {'name': 'Organic Cotton Hoodie', 'price': 30, 'image': 'hoodie.jpg'}
]

@app.route('/')
def index():
    """Render the home page."""
    featured_products = products[:3]  # Get the first 3 products for featured section
    return render_template('index.html', products=featured_products)

@app.route('/products')
def products_page():
    """Render the products page."""
    return render_template('products.html', products=products)

@app.route('/about')
def about_page():
    """Render the about page."""
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    """Render the contact page and handle form submission."""
    if request.method == 'POST':
        # Handle form submission
        return 'Submitted successfully!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
