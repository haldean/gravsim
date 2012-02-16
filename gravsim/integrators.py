from vec import vec
from consts import G

def force_function(masses):
  def force(m1):
    F = vec.zero()
    for m2 in masses:
      if m1 is not m2:
        f = m1.q - m2.q
        r = f.normalize()
        F -= f * (G * m1.mass * m2.mass / (r * r))
    return F
  return force

def explicit(masses, dt):
  force = force_function(masses)
  for mass in masses:
    mass.q     += mass.q_dot * dt
    mass.q_dot += force(mass) / mass.mass * dt
  return masses

def run_time(masses, dt, integrator, iters=None):
  if not iters:
    while True:
      yield masses
      integrator(masses, dt)
  else:
    for i in xrange(iters):
      yield masses
      integrator(masses, dt)
