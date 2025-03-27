# with open("text.txt", "r") as file:
#     data = file.read()
#     print(data)

# with open("text.txt", "w") as file:        # "w" overwrites the text
#     file.write("I changed the text")

# with open("text.txt", "a") as file:        # "a" adds to the text
#     file.write("\n I am adding this line to the file")

import numpy as np

data = np.genfromtxt("data.csv", delimiter=",", skip_header=1, usecols=1)
print(data)