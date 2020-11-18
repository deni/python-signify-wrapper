import os
import tempfile
import subprocess

signify_binary = os.getenv('SIGNIFY_BINARY')

def signed(data, publickey, signature):
	returncode = int()

	with tempfile.TemporaryDirectory() as tmpdir:
		with open(tmpdir + '/data', 'w+b') as f:
			f.write(data)

		with open(tmpdir + '/key.pub', 'w') as f:
			# Define signify template
			template = 'untrusted comment: signify public key\n{publickey}\n'
			f.write(template.format(publickey = publickey))

		with open(tmpdir + '/data.sig', 'w') as f:
			# Define signify template
			template = 'untrusted comment: verify with key.pub\n{signature}\n'
			f.write(template.format(signature = signature))

		signifyCommand = ('{signify_binary} -V '
			'-m {data} -p {publickey}')
		signifyCommand = signifyCommand.format(
			signify_binary = signify_binary,
			data = tmpdir + '/data',
			publickey = tmpdir + '/key.pub',
		)

		result = subprocess.run(
			signifyCommand.split(),
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL,
		)
		returncode = result.returncode

	if returncode == 0:
		return True
	else:
		return False

def sign(data, privatekey):
	signature = str()

	with tempfile.TemporaryDirectory() as tmpdir:
		with open(tmpdir + '/data', 'w+b') as f:
			f.write(data)

		with open(tmpdir + '/key.sec', 'w') as f:
			# Define signify template
			template = 'untrusted comment: signify secret key\n{privatekey}\n'
			f.write(template.format(privatekey = privatekey))

		signifyCommand = ('{signify_binary} -S '
			'-m {data} -s {privatekey} -x {signature}')
		signifyCommand = signifyCommand.format(
			signify_binary = signify_binary,
			data = tmpdir + '/data',
			privatekey = tmpdir + '/key.sec',
			signature = tmpdir + '/data.sig',
		)

		result = subprocess.run(
			signifyCommand.split(),
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL,
		)

		with open(tmpdir + '/data.sig') as f:
			lines = f.read().splitlines()
			signature = lines[2-1]

	if signature:
		return signature
	else:
		return None
