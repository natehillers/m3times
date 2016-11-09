## ((1 + 9*(m^3))^3)+((9*(m^4))^3)+((-9*(m*4)-(3*m))^3)
## where m is any number
## = 1

print "((1 + 9*(m^3))^3)+((9*(m^4))^3)+((-9*(m*4)-(3*m))^3) \nalways equals 1 \nwhen m is any positive number"
numberinput = raw_input("What do you want the max number to check? ")
maxnumber = int(numberinput)

linenumber = 0


with open('Results.txt','w') as a:
	def my_equation(m):
		return ((1 + (9*(m**3)))**3)+((9*(m**4))**3)+(((-9*(m**4))-(3*m))**3)
	for m in range(1,maxnumber):
		if my_equation(m) == 1:
			linenumber += 1
			a.write('PASS %d %s \n' % (linenumber, my_equation(m)))
			a.seek(0)
		else:
			a.write("ERROR " + str(m) + '\n')

print "Done! Check the 'results' file for final results"