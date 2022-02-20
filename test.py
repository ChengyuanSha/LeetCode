import re

txt = "The rain in Spain"
x = re.search("kkk", txt)

print("The first white-space character is located in position:", x.start()) 