# API Reference

## Decorators

#### `function(p: float)`

**Description**:  
A decorator to conditionally execute a function based on a specified probability.

**Parameters**:
- `p` (`float`): Execution probability between 0 and 1.

**Usage**:

```python
import probabilistic

@probabilistic.function(0.5)
def maybe_execute():
    print("Executed with 50% probability")
```

**Raises**:
- `ValueError`: If `p` is not within the range [0, 1].

---

#### `distribution_function(n: int)`

**Description**:  
A decorator to assess the distribution of outcomes for a probabilistic function over multiple trials.

**Parameters**:
- `n` (`int`): Number of trials to perform for the distribution assessment.

**Usage**:

```python
import probabilistic

@probabilistic.distribution_function(n=1000)
def random_event():
    return "Success" if probabilistic.python_random() > 0.5 else "Failure"

distribution = random_event()
print(distribution)
```

**Raises**:
- `TypeError`: If the function returns an unhashable type.

---

## Execution Functions

#### `execute(funcs: List[Callable], p: List[float]) -> Dict[str, Any]`

**Description**:  
Executes a list of functions independently based on their respective probabilities.

**Parameters**:
- `funcs` (`List[Callable]`): List of functions to be executed.
- `p` (`List[float]`): List of probabilities corresponding to each function in `funcs`.

**Returns**:
- `Dict[str, Any]`: Dictionary mapping function names to their return values or error messages.

**Raises**:
- `ValueError`: If no functions are provided or if the lengths of `funcs` and `p` do not match.

**Usage**:

```python
import probabilistic

def task1():
    return "Task 1 Completed"

def task2():
    return "Task 2 Completed"

results = probabilistic.execute([task1, task2], p=[0.8, 0.3])
print(results)
```

---

#### `distribution_execute(func: List[Callable], n: List[int]) -> List[Dict[Any, float]]`

**Description**:  
Executes multiple functions a specified number of times each and returns their result distributions.

**Parameters**:
- `func` (`List[Callable]`): List of functions to be executed.
- `n` (`List[int]`): List of trial counts corresponding to each function in `func`.

**Returns**:
- `List[Dict[Any, float]]`: List of dictionaries, each representing the distribution of results for a function.

**Raises**:
- `TypeError`: If a function returns an unhashable type.

**Usage**:

```python
import probabilistic

def coin_flip():
    return "Heads" if probabilistic.python_random() > 0.5 else "Tails"

def dice_roll():
    return probabilistic.random.randint(1, 6)

distributions = probabilistic.distribution_execute([coin_flip, dice_roll], n=[1000, 1000])
print(distributions)
```
