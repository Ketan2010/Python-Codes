 # importing the module
import turtle 
#making a turtle object of Turtle class for drawing  
trtl = turtle.Turtle() 
#set colour of the pen red  
trtl.pencolor('red') 
#choosing the size of pen nib   
trtl.pensize(4)    
n=0   
#loop for 7 circles
while n<7:   
    n=n+1   
    trtl.penup()   
    trtl.setpos(0,-n*20)   
    trtl.pendown()   
    trtl.circle(20*n)   


input("Press any key to exit ...")