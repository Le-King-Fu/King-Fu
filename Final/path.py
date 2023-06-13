import os

absolute_path = os.path.dirname(__file__)
relative_path = "Count_Me_One"
full_path = os.path.join(absolute_path, relative_path)
print(full_path)
