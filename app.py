"""Flask app for Cupcakes"""
# from crypt import methods
from flask import Flask, request, render_template,  redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "cupcakesaregodsfood"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

#****************************
#Frontend Routes
#****************************

@app.route('/')
def home_page():
    return render_template('home.html')


#****************************
#RESTful JSON API 
#****************************

@app.route('/api/cupcakes')
def list_cupcakes():
    """Return JSON with all cupcakes in cupcakes database"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Get information regarding a specific cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a new cupcake and add to database"""
    #looked at solution for how to get the default image if nothing is entered
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], 
                rating=request.json["rating"], image=request.json["image"] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Update existing cupcake information"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.image = request.json.get('image', cupcake.image)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Delete an existing cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")