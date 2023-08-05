import matplotlib.pyplot as plt

def plot_measurement(datapoints, function_kwargs, stopping_func):
  plt.xscale('log')
  # PLOT SINGLE DATAPOINTS #

  datapoints_x = [p[0] for p in datapoints]
  datapoints_y = [p[1] for p in datapoints]
  plt.plot(datapoints_x, datapoints_y, 'ro')

  # PLOT FITTED FUNCTION #
  x_values = [x/1000 for x in range(30, 4000)]
  plt.plot(x_values, [stopping_func(E=x, **function_kwargs) for x in x_values])

  plt.show()