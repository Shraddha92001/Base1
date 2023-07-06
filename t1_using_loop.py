from turtle import*

speed('slowest')

distance =100
sides = 6

for i in  range (sides):
    pencolor('red')
    fd(distance)
    rt(360/sides)

hideturtle()
mainloop()