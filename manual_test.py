#!/usr/bin/env python3
# Test logic without importing Flask app

def test_logic():
    """Test the core logic without Flask"""
    
    test_cases = [
        {
            "name": "Example A",
            "data": ["a","1","334","4","R", "$"]
        },
        {
            "name": "Example B", 
            "data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]
        },
        {
            "name": "Example C",
            "data": ["A","ABcD","DOE"]
        }
    ]
    
    for test_case in test_cases:
        print(f"\n--- Testing {test_case['name']} ---")
        data = test_case["data"]
        
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
        
        # Create concatenation string in reverse order with alternating caps
        concat_string = ""
        for i, char in enumerate(reversed(all_alphabets)):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
        
        print(f"Input: {data}")
        print(f"Odd numbers: {odd_numbers}")
        print(f"Even numbers: {even_numbers}")
        print(f"Alphabets: {alphabets}")
        print(f"Special characters: {special_characters}")
        print(f"Sum: {sum_numbers}")
        print(f"All alphabets collected: {all_alphabets}")
        print(f"Concat string: {concat_string}")

if __name__ == "__main__":
    test_logic()