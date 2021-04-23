import pygame
import numpy as np

#Change the colors of the lines and points here
point_color = (249, 127, 81)
hull_color = (27, 156, 252)
line_color = (37, 204, 247)

def direction(a, b, c):
    #(b-a) x (c-a)
    #The points are according to python, hence check for negative
    return (((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])) < 0)



def main():    
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Convex Hull")
    #n is the number of points
    n = 20
    points = np.random.randint(25, 455, size=2*n)
    
    #Arrys for the coordinates
    coords = []
    hull = []
    
    #Plotting the plane
    for i in range(0, len(points)-1, 2):
        pygame.draw.circle(win, point_color, (points[i], points[i+1]), 4)
        coords.append([points[i], points[i+1]])
    pygame.display.update()

    
    #find leftmost point, considering only x coord
    leftmost_x = min([xcoord[0] for xcoord in coords])
    leftmost_point = [t for t in coords if leftmost_x is t[0]][0]
    pygame.draw.circle(win, hull_color, leftmost_point, 4)
    pygame.display.update()
    
    #The first point in the hull
    current_point = leftmost_point
    
    
    while(True):
        hull.append(current_point)
        next_point = coords[(coords.index(current_point) + 1)%n]
        for check_point in coords:
            #Check all points for the next boundary point.
            #The most counter-clockwise point is selected
            #Uncomment below  line to view the cheking process
            pygame.draw.line(win, (255,0,0), current_point,check_point, 1)
            clock.tick(20)
            pygame.display.update()
            if(direction(current_point, next_point, check_point)):
                next_point = check_point
                
        pygame.draw.line(win, line_color, current_point,next_point, 4)
        #Here current point is the point we already have stored in the hull 
        #while next point is the incoming hull point
        pygame.display.update()
        current_point = next_point  
        
        if(current_point == hull[0]):
            break
        
    
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
   
main()