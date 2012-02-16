class mass:
  def __init__(self, mass, position, velocity):
    self.mass = mass
    self.q = position
    self.q_dot = velocity

  def __str__(self):
    return '<mass m=%.3e, q=%s, q_dot=%s>' % (
        self.mass, self.q, self.q_dot)
  __repr__ = __str__
