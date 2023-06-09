from flask import Flask, render_template, request, redirect, url_for


app = Flask(name)
"""
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(60), nullable=False)
    price = db.Column(db.String(12), nullable=False)
    image = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()
"""

products=[]
clothing_list , electronics_list ,  kitchenware_list , miscellaneous_list = [] , [] , [] , [] 


@app.route('/AddItemPage', methods=['GET' , 'POST'])
def AddItemPage():
    if request.method == 'POST':
        # Get the submitted form data
        item_name = request.form['item-name']
        item_description = request.form['item-description']
        item_price_IRR = request.form['item-price']
        item_id = request.form['item-id']
        #item_price_USD = ""
        item_image = request.form['item-image']
        item_category = request.form['item-category']
        product = {'name': item_name, 'description' : item_description,'price_IRR': item_price_IRR ,'product_id' :item_id , 'category':item_category, 'image': item_image}
        products.append(product)

        # Create a new item dictionary
        new_item = {
            'name': item_name,
            'description': item_description,
            'price_IRR': item_price_IRR,
            #'price_USD': item_price_USD,
            'image': item_image,
            'category': item_category
        }

        # Add the new item to the appropriate list based on its category
        if item_category == 'clothing':
            clothing_list.append(new_item)
        elif item_category == 'electronics':
            electronics_list.append(new_item)
        elif item_category == 'kitchenware':
            kitchenware_list.append(new_item)
        elif item_category == 'miscellaneous':
            miscellaneous_list.append(new_item)

        # Redirect to the index page
        return redirect(url_for('index'))

    return render_template('AddItemPage.html')


if name == 'main':
    app.run(debug=True)