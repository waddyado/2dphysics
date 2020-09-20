import math
import pygame

pygame.init()

global w, h

w,h = 2048,2048
screen = pygame.display.set_mode((w,h))

def main(a = 9.8, hdamp = 0.05, damp = 0.05):
    ball_x = 0
    ball_y = 0
    ball_x_v = input('enter initial velocity(m/s):>')
    ball_y_v = 0
    ball_y = int(ball_y)
    ball_x_v = int(ball_x_v)
    ball_y_v = int(ball_y_v)
    print('a(m/s^2) =', a)
    print('Vi(m/s) = ', ball_x_v)
    twoa =  9.8 * 2
    twoadeltad = twoa * ball_y
    Vf = math.sqrt(ball_x_v + twoadeltad)
    print('Vf(m/s) =', Vf)
    vfminusvi = Vf - ball_x_v
    time = vfminusvi / a
    print('Time(s) =', time)
    w,h = 1280,1280
    screen = pygame.display.set_mode((w,h))

    while True:

        screen.fill((0,0,0))
        ball_y_v += (a / 125)

        ball_x += ball_x_v
        ball_y += ball_y_v

        if ball_x <= 0:

                ball_x_v = -ball_x_v*(1-damp)
                ball_x = 1

        if ball_y <= 0:

            ball_y_v = -ball_y_v*(1-damp)
            
            ball_x_v = ball_x_v*(1-hdamp)
            
            ball_y = 1

        if ball_x >= w:

            ball_x_v = -ball_x_v*(1-damp)

            ball_x = w - 1 

        if ball_y >=h:

            ball_y_v = -ball_y_v*(1-damp)
            
            ball_y = h - 1
            
        
        pygame.draw.circle(screen, (255,255,255), (int(ball_x), int(ball_y)), 5)

        pygame.display.update()

if __name__ == '__main__':

    main()
