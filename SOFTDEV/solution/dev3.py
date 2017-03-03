class Pstruct (gdb.Command):
  """Returns content of a struct...
  """

  def __init__ (self):
	gdb.Command.__init__(self, "pstruct", gdb.COMMAND_NONE)

  def invoke (self,arg,bl):
	print "-------------"
	arg_list = gdb.string_to_argv(arg)
        next_addr = long(arg_list[0], 0)
        field = arg_list[1]
	for i in range(0,len(field)):
		char = field[i]
		if (cmp(char, "i") == 0):
	   		result = gdb.execute ("x/wu " + str(hex(next_addr)), False, True)
			next_addr = next_addr + 4
			print "> " + result.split()[1]
		if (cmp(char, "l") == 0):
           		result = gdb.execute ("x/gu " + str(hex(next_addr)), False, True)
			next_addr = next_addr + 8
			print "> " + result.split()[1]
		if (cmp(char, "f") == 0):
           		result = gdb.execute ("x/wf " + str(hex(next_addr)), False, True)
			next_addr = next_addr + 4
			print "> " + result.split()[1]
		if (cmp(char, "p") == 0):
			result = gdb.execute ("x/ga " + str(hex(next_addr)), False, True)
			next_addr = next_addr + 8
			print "> " + result.split()[1]
		if (cmp(char, "n") == 0):
                        result = gdb.execute ("x/ga " + str(hex(next_addr)), False, True)
			if(cmp(result.split()[1], "0x0") == 0):
				next_addr = next_addr + 8
			else:
				field1 = field[i+1:]
				field2 = field[:i]
                        	next_addr_n = next_addr
                        	next_addr_n2 = next_addr_n + 8
				new = gdb.execute("pstruct " + str(hex(next_addr_n2)) + " " + field1, False, True)
                        	print new[14:-15]
                        	tmp = gdb.execute ("x/ga " + str(hex(next_addr_n)), False, True)
                        	tmp_addr = str(tmp.split()[1])
				while (cmp(tmp_addr, "0x0") != 0):
					if(i != 0):
						next_addr_n1 = long(tmp_addr,0)
						for j in range (0,len(field2)):
							char = field2[j]
							if(cmp(char, "i") == 0 or cmp(char, "f") == 0 or cmp(char, ".") == 0):
								next_addr_n1 = next_addr_n1 - 4
							if(cmp(char, "l") == 0 or cmp(char, "p") == 0 or cmp(char, "s") == 0):
                                                        	next_addr_n1 = next_addr_n1 - 8
						before = gdb.execute("pstruct " + str(hex(next_addr_n1)) + " " + field2, False, True)
						print before[:-15]
					if(i != len(field) - 1):
                                		next_addr_n = long(tmp_addr,0)
                                		next_addr_n2 = next_addr_n + 8
                                		new = gdb.execute("pstruct " + str(hex(next_addr_n2)) + " " + field1, False, True)
                                		print new[:-15]
					tmp = gdb.execute ("x/ga " + str(hex(next_addr_n)), False, True)
                                        tmp_addr = str(tmp.split()[1])
                        	break

		if (cmp(char, "s") == 0):
           		tmp = gdb.execute ("x/ga " + str(hex(next_addr)), False, True)
			addr_tmp = long(tmp.split()[1],0)
	   		result = gdb.execute ("x/s " + str(hex(addr_tmp)), False, True)
			next_addr = next_addr + 8
			print "> " + result.split()[1]
		if (cmp(char, ".") == 0):
			next_addr = next_addr + 4
	print "-------------"
Pstruct()
Chat Conversation End
