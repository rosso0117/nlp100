# coding: utf-8

def make_str(x, y, z):
    return "{x}時の{y}は{z}".format(x=x, y=y, z=z)

print(make_str(x=12, z=22.4, y="気温"))
