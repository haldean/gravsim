import math

class vec3:
  @classmethod
  def zero(cls):
    return cls(0, 0, 0)

  def __init__(self, *el):
    if len(el) != 3:
      raise Exception(
          'Vectors must have 3 elements (tried to make vector of %s)' % el)
    self.el = list(el)

  def __neg__(self):
    return vec(-self.el[0], -self.el[1], -self.el[2])

  def __add__(self, other):
    return vec(
        self.el[0] + other.el[0],
        self.el[1] + other.el[1],
        self.el[2] + other.el[2])

  def __iadd__(self, other):
    self.el[0] += other.el[0]
    self.el[1] += other.el[1]
    self.el[2] += other.el[2]
    return self

  def __sub__(self, other):
    return vec(
        self.el[0] - other.el[0],
        self.el[1] - other.el[1],
        self.el[2] - other.el[2])

  def __isub__(self, other):
    self.el[0] -= other.el[0]
    self.el[1] -= other.el[1]
    self.el[2] -= other.el[2]
    return self

  def __mul__(self, other):
    if isinstance(other, vec):
      return (
          self.el[0] * other.el[0] +
          self.el[1] * other.el[1] +
          self.el[2] * other.el[2])
    else:
      try:
        return vec(
            other * self.el[0],
            other * self.el[1],
            other * self.el[2])
      except:
        return NotImplemented
  __rmul__ = __mul__

  def __imul__(self, other):
    self.el[0] *= other
    self.el[1] *= other
    self.el[2] *= other
    return self

  def __div__(self, other):
    return vec(
        self.el[0] / other,
        self.el[1] / other,
        self.el[2] / other)

  def __idiv__(self, other):
    self.el[0] /= other
    self.el[1] /= other
    self.el[2] /= other
    return self

  def dot(self, other):
    return self * other

  def norm(self):
    return math.sqrt(self.el[0] ** 2 + self.el[1] ** 2 + self.el[2])

  def normalize(self):
    n = self.norm()
    self.el[0] /= n
    self.el[1] /= n
    self.el[2] /= n
    return n

  def dist(self, other):
    return (self - other).norm()

  def __len__(self):
    return 3

  def __getitem__(self, key):
    return self.el[key]

  def __setitem__(self, key, value):
    self.el[key] = value

  def __delitem__(self, key):
    self.el[key] = 0

  def __iter__(self):
    return iter(self.el)

  def __str__(self):
    return '[%s]' % ', '.join(map(lambda x: '%.3e' % x, self))
  __repr__ = __str__
vec = vec3
