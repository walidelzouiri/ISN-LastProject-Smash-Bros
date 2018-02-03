from turtle import*

ch00 = input("Enter a number for the size of the square : ")
size = int(ch00)

ch01 = input("Enter the number of stick you want : ")
stick = int(ch01)

def draw_motif(size):
    fd(60)
    rt(40)
    i = 0
    while i < 4:
        fd(size)
        lt(90)
        i = i + 1
    rt(140)
    fd(60)
    rt(180)
 

def Number_of_stick(stick):
    k = 0
    while k < stick:
        draw_motif(size)
        k = k + 1
        rt(360 //stick)

        
pendown()
Number_of_stick(stick)
mainloop()
