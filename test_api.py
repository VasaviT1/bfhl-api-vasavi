#!/usr/bin/env python3
import requests
import json

def test_api(base_url="http://localhost:5000"):
    """Test the BFHL API with all provided examples"""
    
    test_cases = [
        {
            "name": "Example A",
            "data": ["a","1","334","4","R", "$"],
            "expected": {
                "odd_numbers": ["1"],
                "even_numbers": ["334","4"],
                "alphabets": ["A","R"],
                "special_characters": ["$"],
                "sum": "339",
                "concat_string": "Ra"
            }
        },
        {
            "name": "Example B", 
            "data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"],
            "expected": {
                "odd_numbers": ["5"],
                "even_numbers": ["2","4","92"],
                "alphabets": ["A", "Y", "B"],
                "special_characters": ["&", "-", "*"],
                "sum": "103",
                "concat_string": "ByA"
            }
        },
        {
            "name": "Example C",
            "data": ["A","ABcD","DOE"],
            "expected": {
                "odd_numbers": [],
                "even_numbers": [],
                "alphabets": ["A","ABCD","DOE"],
                "special_characters": [],
                "sum": "0",
                "concat_string": "EoDdCbAa"
            }
        }
    ]
    
    for test_case in test_cases:
        print(f"\n--- Testing {test_case['name']} ---")
        payload = {"data": test_case["data"]}
        
        try:
            response = requests.post(f"{base_url}/bfhl", json=payload)
            result = response.json()
            
            print(f"Request: {json.dumps(payload)}")
            print(f"Response: {json.dumps(result, indent=2)}")
            
            # Validate response
            if response.status_code == 200:
                print("✅ Status Code: 200")
                
                # Check required fields
                required_fields = ["is_success", "user_id", "email", "roll_number", 
                                 "odd_numbers", "even_numbers", "alphabets", 
                                 "special_characters", "sum", "concat_string"]
                
                for field in required_fields:
                    if field in result:
                        print(f"✅ {field}: Present")
                    else:
                        print(f"❌ {field}: Missing")
                
                # Check expected values
                for key, expected_value in test_case["expected"].items():
                    if result.get(key) == expected_value:
                        print(f"✅ {key}: {result.get(key)} (Expected: {expected_value})")
                    else:
                        print(f"❌ {key}: {result.get(key)} (Expected: {expected_value})")
            else:
                print(f"❌ Status Code: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Testing BFHL API locally...")
    test_api()