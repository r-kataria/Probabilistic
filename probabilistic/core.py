from typing import Callable, Optional, List, Dict, Any
from functools import wraps
import math

from .random_engines import python_random

def function(p: float):
    """
    Decorator to conditionally execute a function based on a specified probability.

    Probability Formula:
    P(func) = p

    :param p: Execution probability between 0 and 1.
    :raises ValueError: If p is not within the range [0, 1].
    :return: Decorator that wraps the target function with probabilistic execution logic.
    """

    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            rand_val = python_random()
            if rand_val <= p:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator


def execute(funcs: List[Callable], p: List[float]) -> Dict[str, Any]:
    """
    Execute a list of functions independently based on their respective probabilities.

    :param funcs: List of functions to be executed.
    :param p: List of probabilities corresponding to each function in `funcs`.
    :return: Dictionary mapping function names to their return values or error messages.
    :raises ValueError: If no functions are provided or if the length of `p` does not match `funcs`.
    """
    
    if not funcs:
        raise ValueError("No functions provided to execute.")

    results = []

    # Execute each function independently
    for i in range(len(funcs)):
        prob = p[i]
        
        rand_val = python_random()
        
        if rand_val <= prob:
            try:
                result = funcs[i]()
                
                reuslts.append(result)
                
            except Exception as e:
                result = f"Error: {e}"
                
                results.append(result)
        else:
            results.append(None)

    return results


def distribution_function(n: int):
    """
    Decorator to assess the distribution of outcomes for a probabilistic function over multiple trials.

    Probability Formulas:
    - For each expected outcome, P(outcome) = count / n
    - P(None) = 1 - sum(count of all outcomes / n)

    :param n: Number of trials to perform for the distribution assessment.
    :return: Decorator that wraps the target function to compute its outcome distribution.
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results_count = {}
            results_count['_None'] = 0  # To account for non-executions
            for _ in range(n):
                result = func(*args, **kwargs)
                if isinstance(result, dict):
                    # If the function returns a dict, iterate over its values
                    for res in result.values():
                        if res is None:
                            results_count['_None'] += 1
                        else:
                            if not isinstance(res, (str, int, float, tuple, frozenset, bool)):
                                raise TypeError(f"Unhashable type returned: {type(res)}")
                            results_count[res] = results_count.get(res, 0) + 1
                else:
                    if result is None:
                        results_count['_None'] += 1
                    else:
                        if not isinstance(result, (str, int, float, tuple, frozenset, bool)):
                            raise TypeError(f"Unhashable type returned: {type(result)}")
                        results_count[result] = results_count.get(result, 0) + 1
            # Calculate actual distribution
            actual_distribution = {k: v / n for k, v in results_count.items()}
            return actual_distribution
        return wrapper
    return decorator


def distribution_execute(func: List[Callable], n: List[int]) -> List[Dict[Any, float]]:
    """
    Execute multiple functions a specified number of times each and return their result distributions.

    :param func: List of functions to be executed.
    :param n: List of trial counts corresponding to each function in `func`.
    :return: List of dictionaries, each representing the distribution of results for a function.
    :raises TypeError: If a function returns an unhashable type.
    """
    
    all_results = []
    for value in range(len(n)):
        results_count = {}
        results_count['_None'] = 0  # To account for non-executions

        for _ in range(n[value]):
            result = func[value]()
            if isinstance(result, dict):
                # If the function returns a dict, iterate over its values
                for res in result.values():
                    if res is None:
                        results_count['_None'] += 1
                    else:
                        if not isinstance(res, (str, int, float, tuple, frozenset, bool)):
                            raise TypeError(f"Unhashable type returned: {type(res)}")
                        results_count[res] = results_count.get(res, 0) + 1
            else:
                if result is None:
                    results_count['_None'] += 1
                else:
                    if not isinstance(result, (str, int, float, tuple, frozenset, bool)):
                        raise TypeError(f"Unhashable type returned: {type(result)}")
                    results_count[result] = results_count.get(result, 0) + 1

        # Calculate actual distribution
        actual_distribution = {k: v / n[value] for k, v in results_count.items()}
        
        all_results.append(actual_distribution)
        
    return all_results
