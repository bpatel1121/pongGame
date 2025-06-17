Web VPython 3.2
#Brij
#
scene.bind('keydown', keydown_fun)    
scene.bind('click', click_fun)         
scene.background = 0.8*vec(1, 1, 1)    
scene.width = 640                     
scene.height = 480


ground = box(size = vec(20, 1, 20),
             pos = vec(0, -1, 0),
             color = 0*vec(1, 1, 1))


wallA = box(pos = vec(0, 0, -10),       #Creates wall A
            axis = vec(1, 0, 0),
            size = vec(20, 1, .2),
            color = vec(1.0, 0.7, 0.3)  # Amber
            )
wallB = box(pos = vec(-10, 0, 0),       #Creates wall B
            axis = vec(0, 0, 1),
            size = vec(20, 1, .2),
            color = color.blue          # Blue
            )
wallC = box(pos = vec(0, 0, 10),        #Creates Wall C
            axis = vec(1, 0, 0),
            size = vec(20, 1, .2),
            color = vec(1.0, 0.98, 0.314)
            )                           # Yellow 
            
wallD = box(pos = vec(10, 0, 0),        #Creates Wall D
            axis = vec(0, 0, 1),
            size = vec(20, 1, .2),
            color = color.green 
            )                           # Green 

PaddleA =   box(pos = vec(-8, 0, 0),    #Creating the body for PaddleA
            axis = vec(0, 0, 1),
            size = vec(5, 1, .2),
            color = color.red    
            )
            
PaddleB =   box(pos = vec(8, 0, 0),     #Creating the body for PaddleA
            axis = vec(0, 0, 1),
            size = vec(5, 1, .2),
            color = color.white    
            )
            
PaddleA.vel = vec(0, 0, 0)      #Creates Starting velocity of 0, for both PaddleA and B 
PaddleB.vel = vec(0, 0, 0)

#
ball = sphere(size = 1.0*vec(1, 1, 1),  
              color = vec(0.8, 0.5, 0.0)
              )
ball.vel =vec(randint(-9,9),0,randint(-9,9))

RATE = 30                               # The number of times the while loop runs each second  
dt = .5/(1*RATE)                        # The time step each time through the while loop
scene.autoscale = False                 # Avoids changing the view automatically
scene.forward = vec(0, -3, -2)          # Ask for a bird's-eye view of the scene...

while True:

    rate(RATE)                              # Maximum number of times per second
                                            # ..that the while loop runs
                                            
    
    PaddleA.pos = PaddleA.pos + PaddleA.vel*dt 
    PaddleB.pos = PaddleB.pos + PaddleB.vel*dt   
    ball.pos = ball.pos + ball.vel*dt
    
    #WALL ON PADDLE COLLISION
    if PaddleA.pos.z - 2.5 < wallA.pos.z:
        PaddleA.pos.z = wallA.pos.z + 2.5
        PaddleA.vel.z *= -.5
    if PaddleA.pos.z + 2.5 > wallC.pos.z:    
        PaddleA.pos.z = wallC.pos.z - 2.5
        PaddleA.vel.z *= -.5
    if PaddleB.pos.z - 2.5 < wallA.pos.z:           
        PaddleB.pos.z = wallA.pos.z + 2.5  
        PaddleB.vel.z *= -.5
    if PaddleB.pos.z + 2.5 > wallC.pos.z:           
        PaddleB.pos.z = wallC.pos.z - 2.5   
        PaddleB.vel.z *= -.5 
    #Ball on Wall Collision
    corral_collide(ball)
    #Ball on Paddle Collision
    if PaddleA.pos.z + 2.5 >= ball.pos.z >= PaddleA.pos.z -2.5 and ball.pos.x - .5 < PaddleA.pos.x:
            ball.vel.x *= -1.1
    if PaddleB.pos.z + 2.5 >= ball.pos.z >= PaddleB.pos.z -2.5 and ball.pos.x + .5 > PaddleB.pos.x:
            ball.vel.x *= -1.1

    
        #BALL ON WALL COLLISION
def corral_collide(ball):
    """Provides the physics for the collision of the ball and the walls
    """
    if ball.pos.z -.5 < wallA.pos.z:           
        ball.pos.z = wallA.pos.z + .5            
        ball.vel.z *= -1.0                 
    # If the ball hits wallB
    if ball.pos.x <= wallB.pos.x:          
        ball.pos.x = wallB.pos.x           
        ball.pos = vec(0,0,0)   
        ball.vel = vec(0,0,0)
        print("Right player has won!")

    #If the ball hits WallC
    if ball.pos.z + .5 > wallC.pos.z:
        ball.pos.z = wallC.pos.z - .5
        ball.vel.z *= -1.0
    
    #If the ball hits WallD
    if ball.pos.x >= wallD.pos.x:          
        ball.pos.x = wallD.pos.x          
        ball.pos = vec(0,0,0)
        ball.vel = vec(0,0,0)
        print("Left player has won!")
    
def keydown_fun(event):
    """This function is called each time a key is pressed."""
    key = event.key
    ri = randint(0, 10)           
    if key == 'up':
        PaddleB.vel = PaddleB.vel + vec(0, 0, -2)
    elif key == 'down':
        PaddleB.vel = PaddleB.vel + vec(0, 0, 2)
    elif key == 'w':
        PaddleA.vel = PaddleA.vel + vec(0, 0, -2)
    elif key == 's':
        PaddleA.vel = PaddleA.vel + vec(0, 0, 2)
    elif key == ' ':
        ball.pos = vec(0,0,0)
        ball.vel = vec(randint(-9,9), 0, randint(-9,9)) 

def click_fun(event):
    """This function is called each time the mouse is clicked."""
    print("event is", event.event, event.which)
 
def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low)      
    return int(randvalue)
