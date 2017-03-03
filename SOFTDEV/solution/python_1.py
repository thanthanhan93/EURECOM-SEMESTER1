import sys
import re

n = int(sys.argv[1])

text = sys.stdin.read();
d = [];

for line in text.split('\n'):
	num = re.findall('\d+',line)
	if num:
		d.append([int(num[0]), line.rstrip()]);
		d = sorted(d, key=lambda x: x[0],reverse=True)
currentnum = -1;
for i in range(0,len(d)):
	if i<n:
		currentnum = d[i][0]
	else:
		if d[i][0]!=currentnum:
			break;
	print d[i][1]


