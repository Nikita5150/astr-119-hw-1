import numpy as np	#we use numpy for lots of things

def main():
	i = 0	#declare i equal to 0; integers can be declared with a number
	n = 10	#declare n = 10
	x = 119.0	#floating points nums are declared with a "."
	
	# we can use numpy to declare arrays quickly
	y = np.zeros(n,dtype=float)	#declares 10 zeros as floats using np
	
	#we can use for loops to iterate with a variable
	for i in range(n): 	#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.0	#set y = 2i+1 as floats
		
	#we can iterate through a varable
	for y_element in y:
		print(y_element)
		
#execute main function
if __name__ == "__main__":
	main()