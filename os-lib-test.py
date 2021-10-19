import os

cur_dir = os.getcwd()
print(cur_dir)

split_zm = os.path.split(cur_dir)
print(split_zm)

dirname_zm = os.path.dirname(cur_dir)
print(dirname_zm)

basename_zm = os.path.basename(cur_dir)
print(basename_zm)

while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)