import math
import pygame

pygame.init()

global w, h

w,h = 1024,1024
screen = pygame.display.set_mode((w,h))

def main(a = 9.8, hdamp = 0.05, damp = 0.05):
    vo = input('enter initial velocity(m/s):>')
    theta = input('enter angle(degrees):>')
    vo = int(vo)
    theta = int(theta)
    #convert theta to radians
    theta = math.radians(theta)
    print(theta)
    #perform trig 
    costheta = math.cos(theta)
    sintheta = math.sin(theta)
    print(costheta, sintheta)
    #convert to degrees
    print(costheta, sintheta)
    #find x and y velocity
    vo = math.radians(vo)
    vox = vo * costheta 
    voy = vo * sintheta
    vox = math.degrees(vox)
    voy = math.degrees(voy)
    ball_x = 1018
    ball_y = 1018
    ball_x_v = int(vox)
    ball_y_v = int(voy)
    ball_y = int(ball_y)
    ball_x_v = int(ball_x_v)
    ball_y_v = int(ball_y_v)
    print('a =', a, 'm/s^2')
    print('Initial velocity =', vo, 'm/s')
    print('Vox = ', vox , 'm/s')
    print('Voy = ', voy , 'm/s')
    tt= voy * -2
    t = tt / a
    time = t * -1
    print(time)
    distance = vox * time
    print('projectile traveled', distance, 'meters')
    screen = pygame.display.set_mode((w,h))

    trail = []

    while True:

        screen.fill((0,0,0))


        if ball_x <= 0:

                ball_x_v = -ball_x_v*(1-damp)
                ball_x = 1
                print(ball_x)
        if ball_y <= 0:

            ball_y_v = -ball_y_v*(1-damp)
            
            ball_x_v = ball_x_v*(1-hdamp)
            
            ball_y = 1

        if ball_x >= w:

            ball_x_v = -ball_x_v*(1-damp)

            #ball_x = ball_x - ball_x

            #print(ball_x)
            
            

        if ball_y >=h:

            ball_y_v = -ball_y_v*(1-damp)
            
            ball_y = h - 1
            #print('landing coordinates: ', ball_x, ' ',  ball_y)
            #break

        ball_x += ball_x_v
        ball_y += ball_y_v
        ball_y_v += (a / 125)
        

        
        
        pygame.draw.circle(screen, (255,255,255), (int(ball_x), int(ball_y)), 5)

        pygame.display.update()

if __name__ == '__main__':

    main()
