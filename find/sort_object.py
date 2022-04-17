class Solution:

    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age

    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'


if __name__ == '__main__':

    Solutions = [
        Solution('John', 'IT', 28),
        Solution('Sam', 'Banking', 20),
        Solution('Joe', 'Finance', 25)
    ]

    sortedByName = sorted(Solutions, key=lambda x: x.name)

    # output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
    print(sortedByName)
