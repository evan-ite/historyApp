from flask import Flask, render_template, request, jsonify
import requests, os, json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

HISTORY_API_URL = 'https://api.api-ninjas.com/v1/historicalevents'

# Initialize Flask app with the custom template folder path
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'app', 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history', methods=['GET'])
def history():
    year = request.args.get('year')
    
    if not year:
        return jsonify({"error": "Year is required"}), 400

    api_url = f'{HISTORY_API_URL}?year={year}'

    print("API URL:", api_url)

    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error fetching data"}), 500

    # response_data = [
    # {
    #     "year": "-45",
    #     "month": "01",
    #     "day": "01",
    #     "event": "The Julian calendar takes effect..."
    # },
    # # ... more events
    # ]
    # return jsonify(response_data)

# Run the Flask app (127.0.0.1:5000 by default).
app.run(debug=True)