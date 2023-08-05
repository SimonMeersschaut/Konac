import math

def calculate_stopping(E, amu, s, a0, a1, a2, a3, Zt):
  '''
  E: energy (in MeV)
  returns stopping (in eV/(10^15 amu/cm^2))
  '''
  E = E/amu
  Beta = 219.49/Zt
  # print(E)
  top = (E**s)*math.log(math.exp(1) + Beta*E)
  bottom = a0 + a1*(E**.5) + a2*E + a3*(E**(1+s))
  return top/bottom