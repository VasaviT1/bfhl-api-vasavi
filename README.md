# BFHL REST API

A REST API that processes arrays and returns categorized data including numbers, alphabets, and special characters.

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

### Example A
**Input:** `["a","1","334","4","R", "$"]`
**Output:** `concat_string: "Ra"`, `sum: "339"`

### Example B
**Input:** `["2","a", "y", "4", "&", "-", "*", "5","92","b"]`
**Output:** `concat_string: "ByA"`, `sum: "103"`

### Example C
**Input:** `["A","ABcD","DOE"]`
**Output:** `concat_string: "EoDdCbAa"`, `sum: "0"`
```

## Tech Stack

- **Backend:** Python 3.9, Flask 2.3.3
- **Production Server:** Gunicorn 21.2.0
- **Hosting:** Render (with auto-deploy from GitHub)
- **Testing:** Requests library for HTTP testing