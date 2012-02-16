from consts import *
from integrators import run_time, explicit
from vec import vec
import mass

def benchmark(integrator):
  m1 = mass.mass(m_SUN, vec(0, 0, 0), vec(0, 0, 0))
  m2 = mass.mass(m_SUN, vec(1, 0, 0), vec(0, 0, 0))
  def test():
    integrator([m1, m2])
  import timeit
  print(timeit.timeit(test, number=10000) / 10000)

def main():
  m1 = mass.mass(m_SUN, vec(0, 0, 0), vec(0, 0, 0))
  m2 = mass.mass(m_EARTH, vec(r_EARTH, 0, 0), vec(0, 107300, 0))

  initial_radius = m1.q.dist(m2.q)
  for masses in run_time([m1, m2], 0.01, explicit, iters=100000): pass
  final_radius = m1.q.dist(m2.q)

  print('delta_distance = %f (%.3f%%)' % (
    final_radius - initial_radius,
    (final_radius - initial_radius) * 100 / initial_radius))

if __name__ == '__main__':
  main()
