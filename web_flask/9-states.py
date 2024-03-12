#!/usr/bin/python3

# Import necessary modules
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import State, City, storage # Import models and storage engine

# Configure the database connection
# Replace the connection string with your actual database credentials
DATABASE_URI = 'mysql+pymysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Initialize the Flask application
app = Flask(__name__)

# Route for displaying all states
@app.route('/states', methods=['GET'])
def states():
    # Create a new session
    session = Session()
    # Query all states, ordered by name
    states = session.query(State).order_by(State.name).all()
    # Close the session
    session.close()
    # Render the states template with the list of states
    return render_template('states.html', states=states)

# Route for displaying a specific state and its cities
@app.route('/states/<int:state_id>', methods=['GET'])
def state_detail(state_id):
    # Create a new session
    session = Session()
    # Query the state by its ID
    state = session.query(State).filter(State.id == state_id).first()
    if state:
        # If the state is found, get its cities
        cities = state.cities # Adjust based on your relationship setup
        # Render the state detail template with the state and its cities
        return render_template('state_detail.html', state=state, cities=cities)
    else:
        # If the state is not found, close the session and render a not found page
        session.close()
        return render_template('not_found.html')

# Teardown function to close the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
