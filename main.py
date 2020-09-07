# usr/bin/python3
# created: Sep 07, 2020
# by https://github.com/caocuong2404

from os import system,remove
from sys import argv
import re,argparse

class BashObf(object):
	def __init__(self,file,out):
		self.file = file
		self.out = out
		self.main()
	def main(self):
		try:
			_i = re.sub(r'eval','echo',open(self.file).read())
			with open('tmp.sh','w') as f:
				f.write(_i)
				f.close()
			system(f'sh tmp.sh > {self.out}')
			remove('tmp.sh')
			system('clear')
			print(f'[*] File saved as: {self.out}')
			_ = input('[*] Print output? (y/n) : ')
			if _.lower() == 'y':
				system(f'cat {self.out}')
			else:
				exit()
		except Exception as eror:
			exit(f'[*] Opps! Something went wrong: {str(eror)}')

try:
	arg = argparse.ArgumentParser(description='Scripts de-obfuscation bash shell',formatter_class=argparse.RawTextHelpFormatter)
	arg.add_argument('-i','--infile',help='File to de-obfuscation',metavar='')
	arg.add_argument('-o','--output',help='Output file save',metavar='')
	gc_ = arg.add_argument_group('Additional')
	gc_.add_argument('-c','--contact',help='Contact information',action='store_true')
	gc_.add_argument('-v','--version',help='Version script',action='store_true')
	oo_ = arg.parse_args()
	if oo_.infile and oo_.output:
		BashObf(oo_.infile,oo_.output)
	elif oo_.contact:
		system('xdg-open https://github.com/caocuong2404')
	elif oo_.version:
		print('1.0.0 Copyright © 2020')
	else:
		exit(f"""usage : python {argv[0]} <options>
or python {argv[0]} -h for show all options""")
except EOFError:
	pass
