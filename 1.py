      **PROGRAM_1**
     # A Program to read a name and print Hello <name>
     name = input("Please Enter Your Name Here:\n")
     print("Hello " + name)


	# A Program to read two numbers and display sum, difference, product and division
	print("Enter First Number")
	num1 = input()
	print("Enter Second Number")
	num2 = input()
	print("************************************")
	print("Sum of Given numbers is : "+str(int(num1)+int(num2)))
	print("Difference of Given numbers is : "+str(int(num1)-int(num2)))
	print("Product of Given numbers is : "+str(int(num1)*int(num2)))
	print("Division of Given numbers is : "+str(int(num1)/int(num2)))
	print("************************************")


     A Program to calculate number of words and characters of a given string
	print("Enter a sentence ")
	sentence = input()
	words = sentence.split()
	word_count = 0
	character_count = 0
	for word in words:
	     word_count += 1
	     character_count += len(word)
	print("Total Numbers of Words in the sentence are : ",word_count)
	print("Total Numbers of characters in the sentence excluding spaces are :
	",character_count)
	print("Total Numbers of characters in the sentence including spaces are :
	",character_count+word_count-1)



	# A Program to get Area of a selected shape.
	while True:
	      print("*****************************************")
	      print("Select the Shape that you want to calculate Area")
	      print("""
	           1. Rectangle
	           2. Triangle
	           3. Circle
	           4. Exit """)
	     choice = input()
	     if(choice == '1'):
	          print("Enter the Width of the Rectangle in meters")
	          width = int(input())
	          print("Enter the height of the Rectangle in meters")
	          height = int(input())
	          print("The area of a Given Rectangle is ", width*height , " squaremeters")
	          continue
	     elif(choice == '2'):
	          print("Enter the Base value of the Triangle in meters")
	          base = int(input())
	          print("Enter the height of the Triangle in meters")
	          height = int(input())
	          print("The area of a Given Rectangle is ", 0.5*base*height , " squaremeters")
	          continue
	     elif(choice == '3'):
	          print("Enter the Radius of the Circle in meters")
	          radius = int(input())
	          print("The area of a Given Circle is ", 3.14*radius*radius , " squaremeters")
	          continue
	     elif(choice == '4'):
	          break
          else:
               
              print("Please enter a valid number from the menu") 
              continue
         print("")

	

 # A Program to print a name n times where name and n values has to be input from
	standard input

	print("Enter Your name : ")
	name = input()
	print("Enter How many times you want to print your name")
	n = int(input())
	for i in range(n):
	    print(name)
	print("")



 
 	# A Program to Handle Divide By Zero Exception
	print("Enter Numerator Value : ")
	num1 = int(input())
	print("Enter Denominator value : ")
	num2 = int(input())
	try:
	     result = num1/num2
	     print("The Division of Given Numbers is : ", result)
	except ZeroDivisionError:
	     print("Divide By zero Error. The Denominator should not be Zero")
	print("")



	# A Program to print current time with an interval of 10 seconds
	import time
	for i in range(10):
	     seconds = time.time()
          local_time  =  time.ctime(seconds)	
	    print("Local time:", local_time)	
	    time.sleep(10)	
	print("")	



	# A Program to Read a file and print No	of Words in each Line
	file1 = open('myfile.txt', 'r')	
	Lines = file1.readlines()	
	i=0	
	for line in Lines:	
	      i += 1	
	      count = len(line.split())	
	      print("Line ", i, "No of Words ", count)
	print("")	




