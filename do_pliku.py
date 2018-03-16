import subprocess

bash = ['python', 'skrypt.py']
with open('output.txt', 'w') as out:
	return_code = subprocess.call(bash, stdout=out)
