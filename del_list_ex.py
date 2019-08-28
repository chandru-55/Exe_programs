'''
 By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
​
Hints:
Use list comprehension to delete a bunch of element from a list.'''
try:
	y = [12,24,35,70,88,120,155]
	d = [x for x in y if x%5!=0 and x%7!=0]
	print(d)

except SyntaxError:
	print("this program syntax is not correct")

except ValueError:
	#if x/5==0 or x/7 == 0:
	#	y.remove(d)
	#	print(y)
	#else:
		print("ValueError")
except TypeError:
	print("TypeError")