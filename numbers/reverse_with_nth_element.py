"""
You have a list and the task is to reverse the
given list with 2nd elements of each worlds
"""

def reverse_string(name):
    return name.sort(key=lambda x: x[1])


name = ["satyam", "vivek", "rishabh", "aaditya", "abhi"]

reverse_string(name)

print(name)
