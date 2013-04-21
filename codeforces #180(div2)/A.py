import sys
n = input()
st = raw_input()
s = st.find('R')
t = st.find('L')
if s == -1:
	s = st.find('.',t) - 1
if t == -1:
	t = st.find('.',s) + 1
print s+1,t
