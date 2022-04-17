"""
Write a Python program to sort a list of dictionaries using Lambda.
"""

models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

print(sorted(models, key=lambda x: x['model']))
