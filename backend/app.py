# app.py - Flask backend API that receives a message via POST and returns a response

from flask import Flask, request, jsonify  # Import Flask core, request handler, and JSON response
from flask_cors import CORS                # Import CORS to allow communication with frontend

# Create a new Flask application instance
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) so React (on a different port) can talk to this API
CORS(app)

# Define a route that accepts POST requests at /api/message
@app.route('/api/message', methods=['POST'])
def get_message():
    # Get JSON data from the request body
    data = request.get_json()

    # Extract the "text" field from the data (default to empty string if missing)
    user_input = data.get('text', '')

    # Create and return a JSON response
    return jsonify({"response": f"Flask received: {user_input}"})

# Run the app only if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the development server with debug mode on
    app.run(debug=True)