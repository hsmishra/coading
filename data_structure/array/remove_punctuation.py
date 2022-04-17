def remove_punctuation(string):
 
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    return string
 
# Driver program
string = "Hello $World"
print(remove_punctuation(string))