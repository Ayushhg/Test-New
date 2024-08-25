from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Parse JSON request
        data = request.json.get('data', [])
        
        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Find the highest lowercase alphabet
        lowercases = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercases) if lowercases else ""
        
        # Construct the response
        response = {
            "is_success": True,
            "user_id": "ayush_goel_01012000",  # Replace with actual birthdate
            "email": "ayush.goel2021@vitstudent.com",      
            "roll_number": "21BCE1115",      
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
