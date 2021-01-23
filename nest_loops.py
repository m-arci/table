#Assignment 6: Advanced Loop


#Create a function that takes in two parameters: rows, and columns, both of which are integers. 
#The function should then proceed to draw a playing board (as in the examples from the lectures) 
#the same number of rows and columns as specified. 
#After drawing the board, your function should return True.

# def table(x,y):
#     for row in range(x):
# 	     if row%2 == 0:
# 	     	for column in range(1,6):
# 	     		if column%2 == 1:
# 	     			if column != 5:
# 	     				print(" ",end="")
# 	     			else:
# 	     				print(" ")
# 	     		else:
# 	     			print("|",end="")
# 	     else:
# 	     	print("-------")
#     return(True)



# table(5,5)


def table(x,y):
    for row in range(x):
	     if row%2 == 0:
	     	for column in range(1,y+1):
	     		if column%2 == 1:
	     			if column != y:
	     				print(" ",end="")
	     			else:
	     				print(" ")
	     		else:
	     			print("|",end="")
	     else:
	     	print("-------")
    return(True)



table(4,9)