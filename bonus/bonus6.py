contents = ['Carrots sliced the long way.', 'Are the carrots sliced?', "Carrots, what carrots!"]
filenames = ['ok.txt', 'great.txt', 'oops.txt']

for index, filename in enumerate(filenames):
    filepath = f"bonus6/{filename}"
    file = open(filepath, 'w')
    file.write(contents[index])
