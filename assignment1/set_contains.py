myset = set()
if not 'val' in myset:
	print 'adding val to the set'
	myset.add('val')

if not 'val' in myset:
	print 'adding val for second time'
	myset.add('val')
elif 'givan' not in myset:
	print 'adding givan to set'
	myset.add('givan')
else:
	print 'both givan and val are in the set. no op'

print myset