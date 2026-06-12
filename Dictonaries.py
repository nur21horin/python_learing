numbers={
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5
}
print(numbers["three"])
print(numbers)
numbers["six"]=6
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial

print(planet_to_initial)