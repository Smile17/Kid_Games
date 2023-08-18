# import required module
import os
import numpy as np

# assign directory
directory = 'input/audio'

# iterate over files in
# that directory
old_names = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        old_names.append(filename)

for i, filename in enumerate(old_names):
    f_old = os.path.join(directory, filename)
    f = str(i + 1)
    if i + 1 < 10:
        f = "0" + f
    f_new = os.path.join(directory, f + '.' + filename.split('.')[1])
    os.rename(f_old, f_new)

