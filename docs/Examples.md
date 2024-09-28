# Examples

## Probabilistic Function Execution

**File**: `function.py`

```python
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
```

**Output**:

```
=== Trial 1 ===
Hello
--------------------
=== Trial 2 ===
World!
--------------------
=== Trial 3 ===
Hello
World!
--------------------
...
```

## Batch Execution of Functions

**File**: `execute.py`

```python
import probabilistic

def hello():
    print("Hello")

def world():
    print("World!")

for i in range(1, 6):
    print(f"=== Trial {i} ===")
    probabilistic.execute([hello, world], p=[0.5, 0.5])
    print("-" * 20)
```

**Output**:

```
=== Trial 1 ===
Hello
--------------------
=== Trial 2 ===
World!
--------------------
=== Trial 3 ===
Hello
World!
--------------------
...
```

## Analyzing Outcome Distributions

**File**: `distribution_function.py`

```python
import probabilistic

@probabilistic.function(0.5)
def a():
    return 5

@probabilistic.function(0.5)
def b():
    return -5

@probabilistic.distribution_function(n=50000)
def probabilisticSum():
    value_sum = 0

    value_a = a()
    value_b = b()

    if value_a is not None:
        value_sum += value_a

    if value_b is not None:
        value_sum += value_b

    return value_sum

print(probabilisticSum())
```

**Sample Output**:

```python
{
    5: 0.2498,
    -5: 0.2512,
    0: 0.4990
}
```

This output indicates the probabilities of the sum being `5`, `-5`, or `0` based on the execution probabilities of functions `a` and `b`.

---

**File**: `distribution_execute.py`

```python
import probabilistic
import random

def toss_coin():
    """Simulates tossing a coin."""
    return "Heads" if random.choice([True, False]) else "Tails"

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

def get_color():
    """Randomly selects a color."""
    colors = ["Red", "Blue", "Green", "Yellow"]
    return random.choice(colors)

distributions = probabilistic.distribution_execute([toss_coin, roll_dice, get_color], n=[500, 1000, 5000])

for d in distributions:
    print(d)
```

**Sample Output**:

```python
{'Heads': 0.49, 'Tails': 0.51}
{1: 0.168, 2: 0.166, 3: 0.17, 4: 0.166, 5: 0.17, 6: 0.16}
{'Red': 0.25, 'Blue': 0.25, 'Green': 0.25, 'Yellow': 0.25}
```
