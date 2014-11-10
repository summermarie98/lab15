#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=0)
				
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Left", background= "purple")
		self.button2.grid(row=0,column=1)
		self.button2.bind("<Button-1>", self.button2Click)
		
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Down", background= "red")
		self.button3.grid(row=0,column=2)
		self.button3.bind("<Button-1>", self.button3Click)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Right", background= "yellow")
		self.button4.grid(row=0,column=3)	
		# "Bind" an action to the first button												
		self.button4.bind("<Button-1>", self.button4Click)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,-10)
                
        def button2Click(self, event):
                global player
		global drawpad
                drawpad.move(player,-10,0)
                
        def button3Click(self, event):
                global player
		global drawpad
                drawpad.move(player,0,10)
                
        def button4Click(self, event):
                global player
		global drawpad
                drawpad.move(player,10,0)
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    x1,y1,x2,y2= drawpad.coords(target)
	   # Insert the code here to make the target move, bouncing on the edges
	    drawpad.move(target,direction,0)    
	    if x2>drawpad.winfo_width():
	        direction = -3
	    if x1<0:
	        direction = 3
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            if didWeHit == True:
                drawpad.itemconfig(target, fill = "red")
            else:
                drawpad.itemconfig(target, fill = "blue")
                drawpad.after(10,self.animate)
                
            
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1,y1,x2,y2 = drawpad.coords(target)
                Px1,Py1,Px2,Py2 = drawpad.coords(player)
                if (Px1 >= x1 and Px2 <= x2) and (Py2 < y2 and Py1 > y1):
                        return True
                else:
                    return False             
                
myapp = MyApp(root)

root.mainloop()