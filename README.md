# Probabilistic

Probabilistic is a Python library designed to facilitate the probabilistic execution of functions and the analysis of their outcome distributions. Whether you're simulating uncertain events, performing randomized experiments, or simply adding an element of chance to your applications, Probabilistic provides a straightforward and flexible toolkit to meet your needs.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
  - [API Reference](docs/API_Reference.md)
  - [Examples](docs/Examples.md)
  - [Contributing](docs/Contributing.md)
- [Support This Project](#support-this-project)


### Features

- [x] **Probabilistic Function Execution**: Execute functions based on specified probabilities using decorators.
- [x] **Batch Execution**: Execute multiple functions independently with individual probabilities.
- [x] **Distribution Analysis**: Assess the distribution of outcomes over multiple trials for single or multiple functions.

- [ ] Customizable Random Engines
- [ ] Conditional Probability-Based Execution
- [ ] Mutual Exclusivity Execution
- [ ] Dependent Function Execution
- [ ] Probability Chains
- [ ] Asynchronous Execution Support
- [ ] Integration with Popular Libraries like NumPy and Pandas for enhanced data handling and analysis.
## Quick Start

Here's a quick example to get you started with Probabilistic.

### Using the `function` Decorator

```python
import probabilistic

@probabilistic.function(0.5)
def greet():
    print("Hello, World!")

# Execute the function with a 50% chance
greet()
```

### Executing Multiple Functions with `execute`

```python
import probabilistic

def foo():
    print("Foo executed")

def bar():
    print("Bar executed")

# Execute `foo` and `bar` each with a 70% and 30% probability respectively
probabilistic.execute([foo, bar], p=[0.7, 0.3])
```

## Documentation
For documentation, please see the [API Reference](docs/API_Reference.md) and [Examples](docs/Examples.md).


## Support This Project
If you find this project helpful, please consider giving it a star on GitHub! 🌟

If you'd like to improve this project, feel free to submit a pull request or open an issue. Let's build something great together! 🚀

*Happy Probabilistic Coding!*