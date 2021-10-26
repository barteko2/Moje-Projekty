"""Aby wyeliminować konieczność jawnego wywoływania python w wierszu polecenia podczas uruchamiania
skryptu, można dodać na początku skryptu linię "#!/usr/bin/env python" jak poniżej'''"""
#!/usr/bin/env python
import subprocess
import sys
import os
"""
print(sys.byteorder)
print(sys.getsizeof(1))
print(sys.platform)

print(os.getlogin())

cp = subprocess.run(['ls','-ltra'], capture_output = True, universal_newlines = True)
#print(cp.stdout)


cperror = subprocess.run(['ls','-ltra'], capture_output = True, universal_newlines = True,check=True)
print(cperror.stdout)
"""

#!!!!!!!!!!!!!!!!sysargv
if __name__ == '__main__':
    print(f"Pierwszy argument: '{sys.argv[0]}'")
    print(f"drugi argument: '{sys.argv[1]}'")
    print(f"trzeci argument: '{sys.argv[2]}'")
    print(f"czwarty argument: '{sys.argv[3]}'")
