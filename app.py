from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        all_alphabets = []
        
        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                sum_numbers += num
            elif item.isalpha():
                alphabets.append(item.upper())
                all_alphabets.extend(list(item.lower()))
            else:
                special_characters.append(item)
        
        concat_string = ""
        for i, char in enumerate(reversed(all_alphabets)):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_numbers),
            "concat_string": concat_string
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)