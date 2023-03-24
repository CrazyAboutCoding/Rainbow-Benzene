from turtle import*
colors=['violet','blue','green','yellow','orange','red']
speed(20)
bgcolor('black')
for i in range(200):
    pencolor(colors[i%6])
    width(i/100+1)
    forward(i)
    left(59)
forward(20)
