# BFHL REST API

A REST API that processes arrays and returns categorized data including numbers, alphabets, and special characters.

## ✅ Requirements Verification

This implementation meets ALL specified requirements:

1. ✅ **Status** - Returns `is_success: true/false`
2. ✅ **User ID** - Format: `john_doe_17091999` (full_name_ddmmyyyy)
3. ✅ **Email ID** - Returns email address
4. ✅ **College Roll Number** - Returns roll number
5. ✅ **Even Numbers Array** - Separates and returns even numbers as strings
6. ✅ **Odd Numbers Array** - Separates and returns odd numbers as strings
7. ✅ **Alphabets Array** - Converts to uppercase, handles multi-character strings
8. ✅ **Special Characters Array** - Identifies non-alphanumeric characters
9. ✅ **Sum of Numbers** - Returns sum as string
10. ✅ **Concatenation String** - Alphabets in reverse order with alternating caps

## API Endpoints

### POST /bfhl
Processes input data array and returns categorized results.

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

### GET /bfhl
Returns operation code for verification.

## Verified Test Cases

### Example A ✅
**Input:** `["a","1","334","4","R", "$"]`
**Output:** `concat_string: "Ra"`, `sum: "339"`

### Example B ✅
**Input:** `["2","a", "y", "4", "&", "-", "*", "5","92","b"]`
**Output:** `concat_string: "ByA"`, `sum: "103"`

### Example C ✅
**Input:** `["A","ABcD","DOE"]`
**Output:** `concat_string: "EoDdCbAa"`, `sum: "0"`

## Local Development

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
python main.py
```

3. **Test the logic:**
```bash
python manual_test.py
```

4. **Test with HTTP requests:**
```bash
python test_api.py
```

The API will be available at `http://localhost:5000/bfhl`

## Testing Methods

### 1. Manual Logic Test
```bash
python manual_test.py
```

### 2. HTTP API Test
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R","$"]}'
```

### 3. Automated Test Suite
```bash
python test_api.py
```

## Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

### Quick Deploy to Render
1. Push code to GitHub
2. Connect GitHub repo to Render
3. Deploy as Web Service
4. Use the provided `render.yaml` configuration

## Files Structure

```
bfhl-api/
├── main.py               # Main Flask application
├── app.py                # Backup Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment config
├── manual_test.py        # Logic verification
├── test_api.py          # HTTP API testing
├── DEPLOYMENT_GUIDE.md  # Detailed deployment steps
├── README.md            # This file
└── .gitignore          # Git ignore rules
```

## Tech Stack

- **Backend:** Python 3.9, Flask 2.3.3
- **Production Server:** Gunicorn 21.2.0
- **Hosting:** Render (with auto-deploy from GitHub)
- **Testing:** Requests library for HTTP testing

## Error Handling

- Graceful exception handling with proper HTTP status codes
- Returns `is_success: false` with error details on failure
- Input validation for malformed requests