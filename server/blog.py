from flask import Flask, render_template, abort, request, render_template_string
 
app = Flask(__name__)
 
PRODUCTS = {
    'iphone': {
        'name': 'iPhone 5S',
        'category': 'Phones',
        'price': 699,
    },
    'galaxy': {
        'name': 'Samsung Galaxy 5',
        'category': 'Phones',
        'price': 649,
    },
    'ipad-air': {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649,
    },
    'ipad-mini': {
        'name': 'iPad Mini',
        'category': 'Tablets',
        'price': 549
    }
}
 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)
 
@app.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

@app.route('/query', methods=['POST'])
def create_user():
    # print (request.form)
    foo = request.form['foo']
    # return render_template('query.html', val = foo)
    template = '''
    {%% extends 'base.html' %%}
    
    {%% block container %%}
    <div class="top-pad">
        <h1>%s</h1>
    </div>
    {%% endblock %%}
    ''' % (str(foo))
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
