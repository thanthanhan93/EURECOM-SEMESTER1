# "pstruct" :that prints an area of memory according to the fields specified by the user.
# 2 args = memory address, format string specifying the fields. 
# Format:
	# i = integer (4 bytes)
	#l = long (8 bytes)
	#f = float (4 bytes)
	#s = pointer to a null-terminated string
	#p = pointer
	#n = a pointer to another element of the same type (print the same information for that address, recursively.)
	#. = skip one word

# https://sourceware.org/gdb/onlinedocs/gdb/Inferiors-In-Python.html

import gdb

class SHOW_INF(gdb.Command):

	def __init__ (self):
		super (SHOW_INF, self).__init__ ("pstruct",gdb.COMMAND_DATA)

	def normalcase(self,adress,i):
			if i == 'i':
				cmd = "x/1dw " + hex(adress)
				adress += 4
			if i == 'l':
				cmd = "x/1dg " + hex(adress)
				adress += 8
			if i == 'f':
				cmd = "x/1fw " + hex(adress)
				adress += 4
			if i == 's':
				cmd = "x/1ag " + hex(adress)
				adress += 8
				stradd = gdb.execute(cmd,False,True)
				cmd = "x/s " + stradd.split()[1]
			if i == 'p':
				cmd = "x/1ag " + hex(adress)
				adress += 8
			if i == '.':
				adress += 4
				return adress
			#print cmd
			value = gdb.execute(cmd,False,True)
			print ">", value.split()[1]
			return adress

	def printANS(self, address, field):
		# local var
		adress = int(address,0)
		cmd = ""
		print '-------------'
		if 'n' in field:
			currentnode = adress
			while(currentnode != 0):
				for i in field:
					if (i == 'n'):
						cmd = 'x/1ag' + hex(currentnode)
						nextnode = gdb.execute(cmd,False,True)
						nextnode = nextnode.split()[1]
						currentnode += 8
					else:
						currentnode = self.normalcase(currentnode,i)
						print '-------------'
				currentnode = int(nextnode,0)		
		else:
			for i in field:
				adress = self.normalcase(adress,i)
			print '-------------'

	def invoke(self, arg, from_ppy):
		# parse argument
		l_arg = gdb.string_to_argv(arg)
		# print answer
		self.printANS(l_arg[0],l_arg[1])

SHOW_INF()