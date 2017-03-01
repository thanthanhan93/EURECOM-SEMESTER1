import sys
import re

path = sys.argv[1];
#print path

with open(path) as f:
    lines = f.readlines()

lines = lines[:len(lines)-1]
row = len(lines)
col = len(lines[0])-1
map = []
for line in lines:
	r = line.replace('\n','')
	map.append(r)

#print ''.join(lines)

def possible_path():
	map_logical = [[2] * col for i in range(row)]
	#print str(len(map_logical)) + "," + str(len(map))
	#print str(len(map_logical[0])) + "," + str(len(map[0]))
	#print map
	for i in range(0,row):
		for j in range(0,col):
			#print i,j
			if (map[i][j] == "#"):
				if (i-1>=0 and map[i-1][j]=="O"):
					map_logical[i][j] = 0;
				else:
					map_logical[i][j] = 1
			if (map[i][j] == "E"):
				map_logical[i][j] = 9
			if (map[i][j] == "S"):
				map_logical[i][j] = 0
			if (map[i][j] == "O"):
				map_logical[i][j] = 0
	return map_logical

def find_BEpoint(text):
	for i in range(0,row):
		for j in range(0,col):
			if(map[i][j] == text):
				return [i, j]
	return 0;

def solution_path(map,S):
	for line in map:
		print str(line)
	print ''

	if (map[S[0]][S[1]] == 9):
		return ''
	map[S[0]][S[1]] = 0;
	if (S[0]-1 >= 0 and map[S[0]-1][S[1]] != 0):
		map_n = map
		re = solution_path(map_n,[S[0]-1,S[1]])
		if (re != 0):
			return "U"+re
	if (S[1]+1 <= col-1 and map[S[0]][S[1]+1] != 0):
		map_n = map
		re = solution_path(map_n,[S[0],S[1]+1])
		if (re != 0):
			return "R"+re 
	if (S[0]+1 <= row-1 and map[S[0]+1][S[1]] != 0):
		map_n = map
		re = solution_path(map_n,[S[0]+1,S[1]])
		if (re != 0):
			return "D"+re
	if (S[1]-1 >= 0 and map[S[0]][S[1]-1] != 0):
		map_n = map
		re = solution_path(map_n,[S[0],S[1]-1])
		if (re != 0):
			return "L"+re
	return 0;

p_start = find_BEpoint('S');
p_end = find_BEpoint("E");
map_l = possible_path();
#for line in map_l:
#	print str(line)

print solution_path(map_l,p_start)
#print p_start
#for line in map_l:
#	print str(line)




