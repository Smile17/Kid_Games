# import required module
import os
import numpy as np

# assign directory
directory = 'input/alphabet'

# iterate over files in
# that directory
old_names = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        old_names.append(filename)

nums = [int(x.split('.')[0].split('_')[1]) for x in old_names]
print(nums)
idx = np.argsort(nums)
old_names = np.array(old_names)
old_names = old_names[idx]

for i, filename in enumerate(old_names):
    f_old = os.path.join(directory, filename)
    f = str(i + 1)
    if i + 1 < 10:
        f = "0" + f
    f_new = os.path.join(directory, f + ".png")
    os.rename(f_old, f_new)

