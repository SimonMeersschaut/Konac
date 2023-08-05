import stopping
import random
import plot
import optimize
import json
# output = calculate_stopping(E=0.4/4, s=5.142*(10**-1), a0=7.421*(10**-3), a1=-1.199*(10**-4), a2=3.350*(10**-3), a3=1.109*(10**-1), Zt=10.297)
# output = calculate_stopping(E=4/4, s=5.142*(10**-1), a0=7.421*(10**-3), a1=-1.199*(10**-4), a2=3.350*(10**-3), a3=1.109*(10**-1), Zt=10.297)

kwargs = {
  's':5.142*(10**-1),
  'a0':7.421*(10**-3),
  'a1':-1.199*(10**-4),
  'a2':3.350*(10**-3),
  'a3':1.109*(10**-1),
  'Zt': 44#10.297
}

with open('data.json', 'r') as f:
  datapoints = json.load(f)

# calculate datapoints
# datapoints = []
# for E in range(30, 3000, 50):
#   output = stopping.calculate_stopping(E=E/1000, **kwargs)
#   output += random.random()*2*(-1 if random.randint(0, 1)==0 else 1)
#   datapoints.append((E,output))

# print(datapoints)

fit_results = []
for i in range(5):
  result = optimize.fit_datapoints(
    datapoints=datapoints,
    function=stopping.calculate_stopping,
    function_kwargs=kwargs,
    # initial_guess = [5.142*(10**-1), 7.421*(10**-3), -1.199*(10**-4), 3.350*(10**-3), 1.109*(10**-1)]
  )
  print(result)
  fit_results.append(result)

optimal_fit = sorted(fit_results, key=lambda fit:fit.fun)[0]
print()
print(optimal_fit)
# plot
kwargs.update({
  's':optimal_fit.x[0],
  'a0':optimal_fit.x[1],
  'a1':optimal_fit.x[2],
  'a2':optimal_fit.x[3],
  'a3':optimal_fit.x[4],
})
plot.plot_measurement(datapoints, kwargs, stopping_func=stopping.calculate_stopping)