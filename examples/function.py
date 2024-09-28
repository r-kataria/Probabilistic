import probabilistic

@probabilistic.function(0.5)
def hello():
    print("Hello")

@probabilistic.function(0.5)
def world():
    print("World!")

for i in range(1, 6):
    print(f"=== Trial {i} ===")
    
    hello()
    world()
    
    print("-" * 20)  # Separator for clarity
