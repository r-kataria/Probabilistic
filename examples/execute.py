# Example with run function

import probabilistic

def hello():
    print("Hello")

def world():
    print("World!")

for i in range(1, 6):
    print(f"=== Trial {i} ===")
    
    probabilistic.execute([hello, world], p=[0.5,0.5])
    
    print("-" * 20)