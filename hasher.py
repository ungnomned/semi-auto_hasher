import os
import subprocess
import time
os.system('color')

file_path = input("enter the path to the file you wish to hash: ")
Algorithm = input("enter the desired algorith (MD5/SHA1/SHA256): ")
Hash_beta = input("Enter the trusted hash from the downloaded website: ")
Hash = Hash_beta.upper()

command = f"certutil -hashfile {file_path} {Algorithm}"

subprocess.run(["powershell", command], capture_output=True, text=True)

L1 = subprocess.run(["powershell", command], capture_output=True, text=True)
L2 = L1.stdout

if L2.__contains__(Hash) or L2.__contains__(Hash_beta):
    print('\x1b[6;30;42m' + 'IT IS A MATCH' + '\x1b[0m')

else:
    print('\x1b[6;30;41m' + 'NOT A MATCH' + '\x1b[0m')
time.sleep(5)
