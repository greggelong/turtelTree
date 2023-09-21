import turtle
import random

def tree1(branchLen,t,n):
    # random two or three branches
    ex = random.uniform(1.1, 3.1)
    ln = random.uniform(0.5,0.8)
    #print(ex,ln)
    if n >0:
        t.forward(branchLen)
        t.right(20*ex)
        tree1(branchLen*ln,t,n-1)
         
        if random.choice([0,0,1])== 0:
            # three braches
            print("three branches")
            t.left(20*ex)
            tree1(branchLen*ln,t,n-1)
            t.left(20*ex)
            tree1(branchLen*ln,t,n-1)
        else:
            # two branches
            print("two branches")
            t.left(40*ex)
            tree1(branchLen*ln,t,n-1)
        t.right(20*ex) # moves back to center after either case
        t.backward(branchLen)
        
def tree3(branchLen,t,n):
    ex = random.uniform(1.1, 3.1)
    ln = random.uniform(0.5,0.8)
    choi = random.choice([0,1])
    #print(ex,ln)
    
    if n >0:
        ## go forward
        t.forward(branchLen)
        
        if choi == 0:
            print("only 1")
            onechoi = random.choice([0,1,2])
            # only one brach left or right
            if onechoi == 0:
                # to the right
                t.right(20*ex)
                tree3(branchLen*ln,t,n-1)
                t.left(20*ex)
            elif onechoi == 1:
                t.left(20*ex)
                tree3(branchLen*ln,t,n-1)
                t.right(20*ex)
            else:
                tree3(branchLen*ln,t,n-1)
         
        if choi== 1:
            print("tow or three")
            # two or three
            t.right(20*ex)
            tree3(branchLen*ln,t,n-1)
             
            if random.choice([0,0,1])== 0:

                t.left(20*ex)
                tree3(branchLen*ln,t,n-1)
                t.left(20*ex)
                tree3(branchLen*ln,t,n-1)
            else:
                t.left(40*ex)
                tree3(branchLen*ln,t,n-1)
            t.right(20*ex)
        t.backward(branchLen)
 
def tree2(branchLen,t,n):
    ex= 1
    ln =0.67
    if n >0:
        #go forwad
        t.forward(branchLen)
        # branch right
        t.right(20*ex)
        tree2(branchLen*ln,t,n-1)
        # branch left
        t.left(40*ex)
        tree2(branchLen*ln,t,n-1)
        # move angle back to center and go back warrds
        t.right(20*ex)
        t.backward(branchLen)
 
def tree4(branchLen,t,n):
     ## exit on level three branches
    ex= 3.7
    ln =0.67
    if n >0:
        #go forwad
        t.forward(branchLen)
        # branch right to right side
        t.right(20*ex)
        tree4(branchLen*ln,t,n-1)
        # branch left to center
        t.left(20*ex)
        tree4(branchLen*ln,t,n-1)
        # branch left to left side
        t.left(20*ex)
        tree4(branchLen*ln,t,n-1)
        # move angle back to center and go backwards
        t.right(20*ex)
        t.backward(branchLen)
        
def tree(branchLen,t):
    ## recursive tree with exit condition based on lengh
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    myWin = turtle.Screen()
    
    t.left(90)
    t2.left(90)
    t3.left(90)
    t.up()
    t2.up()
    t3.up()
    t.setpos(-300,0)
    t2.setpos(300,0)
    t3.setpos(0,0)
    t.backward(400)
    t2.backward(400)
    t3.backward(400)
    t2.down()
    t.down()
    t3.down()
    t.color("green")
    t2.color("red")
    t3.color("blue")
    
    # reg tree
    tree4(90,t2,5)
    # more random tree
    tree3(90,t,6)
    # les random tree
    tree1(90,t3,6)
    
    myWin.exitonclick()

main()
