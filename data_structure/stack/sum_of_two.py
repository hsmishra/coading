name = "Hello this is python programing langauge system and design by satyam"

data = {}

for word in name.split(" "):
	if word[0] in data:
		data[word[0]].append(word)
	else:
		data[word[0]] = [word]

print(data)