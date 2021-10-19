import subprocess
import sys
import os

print(sys.byteorder)
print(sys.getsizeof(1))
print(sys.platform)

print(os.getlogin())

cp = subprocess.run(['ls','-ltra'], capture_output = True, universal_newlines = True)
#print(cp.stdout)


cperror = subprocess.run(['ls','-ltra'], capture_output = True, universal_newlines = True,check=True)
print(cperror.stdout)