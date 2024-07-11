## Flask Application Design for 'GreenThread' Website

### HTML Files

**index.html** (Home Page):

- Header with 'GreenThread' logo and navigation menu
- Main content section showcasing featured products and sustainability initiatives
- Footer with contact information and social media links

**products.html** (Products Page):

- List of products with images, descriptions, and prices
- Filter and search options for easy navigation
- Product details page linked to each product image

**about.html** (About Us Page):

- Mission statement and values of GreenThread
- Team introduction and their commitment to sustainability
- Environmental impact and certifications

**contact.html** (Contact Page):

- Contact form for inquiries and customer support
- Email address, phone number, and social media links

**base.html** (Base Template):

- Includes common elements for all pages
- Header, footer, and navigation menu

### Routes

**main.py**

```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        return 'Submitted successfully!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation

- The Flask app is defined with template rendering and routing functionality.
- The index, products, about, and contact routes render the respective HTML files for each page.
- The contact route handles both GET (for form display) and POST (for form submission) requests.
- The base.html file acts as a template for all other pages, ensuring consistency in design and navigation.
- This application follows Flask conventions and provides a basic but functional website structure.