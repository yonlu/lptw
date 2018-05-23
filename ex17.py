from sys import argv
from os.path import exists

# One liner just for the laughs
script, from_file, to_file = argv; print(f"Copying from {from_file} to {to_file}"); indata = open(from_file).read(); input("Ready, hit RETURN to continue, CTRL-C to abort."); out_file = open(to_file, 'w').write(indata); print("All right, all done")
