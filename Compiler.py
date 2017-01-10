import re

cSource = '''def z():
 global n,f
 n,f=f,n
 return 0
def r(x):
 a=0
 x=re.sub('"','\\"',x)
 while n and n[-1]:a+=eval(x)
 return a
p=lambda x:n.append(x)or 0
'''+re.sub('[>\]]',')',
	re.sub('}','")',
		re.sub('{','+r("',
			re.sub('\[','-(',
				re.sub('<','+0*(',
					re.sub('\[]','+len(n)',
						re.sub('{}','+(len(n)and n.pop())',
							re.sub('<>','+z()',
								re.sub('\(','+p(',
									re.sub('\(\)','+1',
										raw_input()
									)
								)
							)
						)
					)
				)
			)
		)
	)
)[1:]+"\nprint '\\n'.join(n)"

while re.search("(\+1){2,}",cSource):
	size = (lambda x:(x[1]-x[0])/2)(re.search("(\+1){2,}",cSource).span())
	cSource = re.sub("(\+1){2,}",str(size),cSource,1)
 
print cSource
