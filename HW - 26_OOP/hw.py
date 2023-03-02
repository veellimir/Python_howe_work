from math import pi

class Sphere:
    def __init__(self, radius=1.0, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_radius(self):
        return self.radius

    def get_volume(self):
        return 4 / 3 * (pi * self.radius ** 3)

    def get_square(self):
        return 4 * pi * self.radius ** 2

    def get_center(self):
        return self.x, self.y, self.z

    def is_point_inside(self, x, y, z):
        if ((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.radius ** 2:
            return True
        else:
            return False

    def set_radius(self, r):
        self.radius = r

sp = Sphere(0.6)

print('get_radius:', sp.get_radius())

print('get_volume:', sp.get_volume())

print('get_square:', sp.get_square())

print('get_center:', sp.get_center())

print('is_point_inside:', sp.is_point_inside(0, -1.5, 0))

print('set_radius:', sp.set_radius(1.6))

print('is_point_inside:', sp.is_point_inside(0, -1.5, 0))