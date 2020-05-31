# bounce.py
#
# Exercise 1.5

height = 100
bounces = 0

while bounces < 10:
    bounces += 1
    height *= (3/5)
    print(bounces, round(height, 4)) 