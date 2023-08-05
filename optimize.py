from scipy.optimize import rosen, differential_evolution
from stopping import calculate_stopping
import random

def fit_datapoints(datapoints:list, function, function_kwargs, initial_guess=None):
  def minimization_function(x, datapoints:list, function):
    '''
      x: a list of values which will be evaluated to (s, a0, a1, a2, a3)
    '''
    (s, a0, a1, a2, a3) = x
    error = 0
    for p_x, p_y in datapoints:
      simulated_y = function(E=p_x, amu=4, s=s, a0=a0, a1=a1, a2=a2, a3=a3, Zt=44)
      difference = (simulated_y - p_y)**2
      error += difference
    # print(error)
    return error

  # print(minimization_function(initial_guess, datapoints=datapoints, function=function))
  bounds = [(-1, 1) for _ in range(5)]
  result = differential_evolution(
    func=lambda x:minimization_function(x, datapoints=datapoints, function=function),
    bounds=bounds,
    maxiter=300,
    popsize=20,
    x0=initial_guess,
    seed=random.randint(0, 1000)
  )
  return result



