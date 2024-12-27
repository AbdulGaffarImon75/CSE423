import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

###########################    Global Variables   ############################################

W_Width, W_Height = 500, 1000

shooter_x = 250
shooter_color = [0,1,1]
tem_shooter_color = shooter_color
shooter_y = 45
starting_shooter_y = -30
shooter_speed = 15
shooter_visibility = False

#### bullet = [ x, y, isLooping, isVisible ] ######             13 bullets per line, all have been written and kept in constant loop.
bullet_1 = [[shooter_x,shooter_y, True, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True],[shooter_x,shooter_y, False, True]]
bullet_2 = [[shooter_x-10,shooter_y, True, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True],[shooter_x-10,shooter_y, False, True]]
bullet_3 = [[shooter_x+10,shooter_y, True, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True],[shooter_x+10,shooter_y, False, True]]
bullet_4 = [[shooter_x-20,shooter_y, True, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True],[shooter_x-20,shooter_y, False, True]]
bullet_5 = [[shooter_x+20,shooter_y, True, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True],[shooter_x+20,shooter_y, False, True]]
bullet_speed = 9
bullet_r = 5
line_num = 1            # used later to increase the number of bullet lines
score = 0               # shooting alien gives points
lives = 3
isPlaying = False
gamestartStatus = "Game Started"
gameover = False
gameStart = False
exitGame = False
shootable = True
Won = False

### alien = [x,y,speed,hp,isVisible,color, direction] ########
alien_1 = [40, 590, 5, 100, False, [1,1,0], "right"]
alien_2 = [460, 590, 5, 100, False, [1,1,0], "left"]

##### alien bullet = [x,y,speed,isVisible] #########
bullet_a1 = [alien_1[0],alien_1[1]-10,5,False]
bullet_a2 = [alien_2[0],alien_2[1]-10,10,False]
bullet2_a1 = [alien_1[0],alien_1[1]-10,15,False]
bullet2_a2 = [alien_2[0],alien_2[1]-10,20,False]
bullet3_a1 = [alien_1[0],alien_1[1]-10,25,False]
bullet3_a2 = [alien_2[0],alien_2[1]-10,30,False]

###########################    Mid Point Line Drawing Algorithm Functions   #############################################
def originalZone(z, x, y, s):
    if z == 0:
        draw_points(x, y, s)
    elif z == 1:
        draw_points(y, x, s)
    elif z == 2:
        draw_points(-y, x, s)
    elif z == 3:
        draw_points(-x, y, s)
    elif z == 4:
        draw_points(-x, -y, s)
    elif z == 5:
        draw_points(-y, -x, s)
    elif z == 6:
        draw_points(y, -x, s)
    elif z == 7:
        draw_points(x, -y, s)
        
def draw_Line(x0, y0, x1, y1, c=[1,1,1]):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = convert_n_to_0(zone, x0, y0)
    x1, y1 = convert_n_to_0(zone, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    d0 = 2 * dy - dx
    de = 2 * dy
    dne = 2 * (dy - dx)
    x, y = x0, y0

    while (x < x1):
        originalZone(zone, x, y, c)
        if d0 < 0:
            x += 1
            d0 += de
        else:
            x += 1
            y += 1
            d0 += dne
        
def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        else:
            zone = 7
    else:
        if dx >= 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx <= 0 and dy < 0:
            zone = 5
        else:
            zone = 6
    return zone

def convert_n_to_0(zone, x, y):
    if zone == 0:
        return (x, y)
    else:
        if zone == 1:
            return (y, x)
        elif zone == 2:
            return (y, -x)
        elif zone == 3:
            return (-x, y)
        elif zone == 4:
            return (-x, -y)
        elif zone == 5:
            return (-y, -x)
        elif zone == 6:
            return (-y, x)
        else:
            return (x, -y)
        
###########################    Mid Point Circle Drawing Algorithm Functions   #############################################
def circlePoints(x, y, x0, y0, color):
    draw_points(x + x0, y + y0, color)
    draw_points(y + x0, x + y0, color)
    draw_points(y + x0, -x + y0, color)
    draw_points(x + x0, -y + y0, color)
    draw_points(-x + x0, -y + y0, color)
    draw_points(-y + x0, -x + y0, color)
    draw_points(-y + x0, x + y0, color)
    draw_points(-x + x0, y + y0, color)
    
def midpointLine(radius, x0, y0, color):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints(x, y, x0, y0, color)

    while x < y:
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints(x, y, x0, y0, color)
        
def draw_circle(radius, x0, y0, color=[1,1,1]):
    midpointLine(radius, x0, y0, color)        # outer circle
    
def draw_points(x, y, color=[1,1,1]):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel  # glVertex2f only used once
    glEnd()
    
    
###################### Play, Pause, Exit, Restart and Convert Coordinate Drawing Functions #################################
def restart_img():
    draw_Line(30,700,80,700,[0,1,0])
    draw_Line(50, 720, 30, 700, [0, 1, 0])
    draw_Line(50, 680, 30, 700, [0, 1, 0])
def exit_img():
    draw_Line(470, 680, 430,720, [1, 0, 0])
    draw_Line(470, 720, 430, 680, [1, 0, 0])
def play_img():
    draw_Line(130, 680, 130, 720, [0, 0, 1])
    draw_Line(130, 680, 170, 700, [0, 0, 1])
    draw_Line(130, 720, 170, 700, [0, 0, 1])
def pause_img():
    draw_Line(140, 680, 140, 720, [1, 1, 0])
    draw_Line(160, 680, 160, 720, [1, 1, 0])
    

####################################  All Drawing Functions ################
def line():
    draw_Line(0,650,500,650)
    
def main_shooter(shooter_x, shooter_y, shooter_color):
    color = shooter_color
    
    bf = 0              # bigger fin
    while bf < 20:
        draw_Line(shooter_x - 15, shooter_y + 10 - bf, shooter_x - 35, shooter_y - 10 - bf)     # left big fin
        draw_Line(shooter_x + 15, shooter_y + 10 - bf, shooter_x + 35, shooter_y - 10 - bf)     # right big fin
        bf += 1
        
    sf = 0              # smaller fin
    while sf < 10:
        draw_Line(shooter_x - 10, shooter_y - 20 - sf, shooter_x - 20, shooter_y - 30 - sf)   # bottom left small fin
        draw_Line(shooter_x + 10, shooter_y - 20 - sf, shooter_x + 20, shooter_y - 30 - sf)   # bottom right small fin
        draw_Line(shooter_x + 5, shooter_y + 15 - sf, shooter_x + 15, shooter_y + 25 - sf)    # upper right small fin
        draw_Line(shooter_x - 5, shooter_y + 15 - sf, shooter_x - 15, shooter_y + 25 - sf)    # bottom right small fin
        sf += 1
        
    bc_r = 0            # bigger circle radius
    while bc_r < 20:
        draw_circle(bc_r, shooter_x, shooter_y, color)
        bc_r += 1
        
    sc_r = 0            # smaller circle radius
    while sc_r < 11:
        draw_circle(sc_r, shooter_x, shooter_y - 23, color)
        sc_r += 1
        
def starting_shooter():     # shooter appearing in screen
    global shooter_x, starting_shooter_y, shooter_color
    color = shooter_color
    if starting_shooter_y < 600:
        main_shooter(shooter_x, starting_shooter_y, shooter_color)
               
            
def bullet1():          # line 1
    global bullet_1, bullet_r, shooter_color, line_num
    for i in bullet_1:
        if i[3]:            # if bullet visible
            count = 0
            while count <= bullet_r:
                draw_circle(count, i[0], i[1], shooter_color)   # drawing bullet
                count += 1
                
def bullet2():          # line 2
    global bullet_2, bullet_r, shooter_color, line_num
    for i in bullet_2:
        if i[3]:            # if bullet visible
            count = 0
            while count <= bullet_r:
                draw_circle(count, i[0], i[1], shooter_color)   # drawing bullet
                count += 1
                
def bullet3():          # line 3
    global bullet_3, bullet_r, shooter_color, line_num
    for i in bullet_3:
        if i[3]:            # if bullet visible
            count = 0
            while count <= bullet_r:
                draw_circle(count, i[0], i[1], shooter_color)   # drawing bullet
                count += 1
                
def bullet4():          # line 4
    global bullet_4, bullet_r, shooter_color, line_num
    for i in bullet_4:
        if i[3]:            # if bullet visible
            count = 0
            while count <= bullet_r:
                draw_circle(count, i[0], i[1], shooter_color)   # drawing bullet
                count += 1
                
def bullet5():          # line 5
    global bullet_5, bullet_r, shooter_color, line_num
    for i in bullet_5:
        if i[3]:            # if bullet visible
            count = 0
            while count <= bullet_r:
                draw_circle(count, i[0], i[1], shooter_color)   # drawing bullet
                count += 1
                
def themes():
    mode_change_r = 0
    while mode_change_r <= 11:
        draw_circle(mode_change_r, 250, 680, [0, 1, 1])
        draw_circle(mode_change_r, 350, 680, [0, 1, 0])
        draw_circle(mode_change_r, 300, 680, [1, 0, 1])
        mode_change_r += 1
        
def heart(): 
    if lives > 2:
        
        cir_r = 0
        while cir_r <= 8:
            draw_circle(cir_r, 243, 730, [1, 0, 0])
            draw_circle(cir_r, 257, 730, [1,0,0])
            cir_r += 1
            
        ln = 0
        while ln < 15:
            draw_Line(235+ln,728-ln,266-ln,728-ln,[1,0,0])
            ln += 1
            
    if lives > 1:
        
        cir_r = 0
        while cir_r <= 8:
            draw_circle(cir_r, 243+50, 730, [1, 0, 0])
            draw_circle(cir_r, 257+50, 730, [1, 0, 0])
            cir_r += 1
            
        ln = 0
        while ln < 15:
            draw_Line(235+50 + ln, 728 - ln, 266+50 - ln, 728 - ln, [1, 0, 0])
            ln += 1
            
    if lives > 0:
        
        cir_r = 0
        while cir_r <= 8:
            draw_circle(cir_r, 243+100, 730, [1, 0, 0])
            draw_circle(cir_r, 257+100, 730, [1, 0, 0])
            cir_r += 1
            
        ln = 0
        while ln < 15:
            draw_Line(235+100 + ln, 728 - ln, 266+100 - ln, 728 - ln, [1, 0, 0])
            ln += 1
            
def alien1():
    global alien_1
    if alien_1[4]:          # if alien visible
        
        count2 = 0
        while count2 <= 20:
            draw_Line(alien_1[0]-25 + count2, alien_1[1]+45 - count2, alien_1[0]-25 + count2, alien_1[1] - count2, [1, 1, 1])
            draw_Line(alien_1[0] + 5 + count2, alien_1[1] + 25 + count2, alien_1[0] + 5 + count2, alien_1[1] - 20 + count2,[1, 1, 1])
            count2 += 1
            
        count3 = 0
        while count3 <= 5:
            draw_circle(count3, alien_1[0] - 7, alien_1[1] - 20, [1,1,1])
            draw_circle(count3, alien_1[0] + 7, alien_1[1] - 20, [1,1,1])
            count3 += 1
            
        count = 0
        while count <= 20:
            draw_circle(count, alien_1[0], alien_1[1], alien_1[5])
            count += 1
            
def alien2():
    global alien_2
    if alien_2[4]:          # if alien visible
        
        count2 = 0
        while count2 <= 20:
            draw_Line(alien_2[0]-25 + count2, alien_2[1]+45 - count2, alien_2[0]-25 + count2, alien_2[1] - count2, [1, 1, 1])
            draw_Line(alien_2[0] + 5 + count2, alien_2[1] + 25 + count2, alien_2[0] + 5 + count2, alien_2[1] - 20 + count2,[1, 1, 1])
            count2 += 1
            
        count3 = 0
        while count3 <= 5:
            draw_circle(count3, alien_2[0] - 7, alien_2[1] - 20, [1,1,1])
            draw_circle(count3, alien_2[0] + 7, alien_2[1] - 20, [1,1,1])
            count3 += 1
            
        count = 0
        while count <= 20:
            draw_circle(count, alien_2[0], alien_2[1], alien_2[5])
            count += 1
            
def bulletOfAlien():
    if bullet_a1[3] and alien_1[3]:         # if bullet visible and alien still has hp
        count = 0
        while count <= 8:
            if count < 5:
                draw_circle(count, bullet_a1[0], bullet_a1[1], [1,0,1])
            else:
                draw_circle(count, bullet_a1[0], bullet_a1[1], [1,1,0])
            count += 1
            
    if bullet_a2[3] and alien_2[3]:         # if bullet visible and alien still has hp
        count = 0
        while count <= 8:
            if count < 5:
                draw_circle(count, bullet_a2[0], bullet_a2[1], [1,0,1])
            else:
                draw_circle(count, bullet_a2[0], bullet_a2[1], [1,1,0])
            count += 1

    if line_num > 2 and Won == False:
        if bullet2_a1[3] and alien_1[3]:         # if bullet visible and alien still has hp
            count = 0
            while count <= 8:
                if count < 5:
                    draw_circle(count, bullet2_a1[0], bullet2_a1[1], [1, 0, 1])
                else:
                    draw_circle(count, bullet2_a1[0], bullet2_a1[1], [1, 1, 0])
                count += 1
                
        if bullet2_a2[3] and alien_2[3]:         # if bullet visible and alien still has hp
            count = 0
            while count <= 8:
                if count < 5:
                    draw_circle(count, bullet2_a2[0], bullet2_a2[1], [1, 0, 1])
                else:
                    draw_circle(count, bullet2_a2[0], bullet2_a2[1], [1, 1, 0])
                count += 1
                
    if line_num > 4 and Won == False:
        if bullet3_a1[3] and alien_1[3]:         # if bullet visible and alien still has hp
            count = 0
            while count <= 8:
                if count < 5:
                    draw_circle(count, bullet3_a1[0], bullet3_a1[1], [1, 0, 1])
                else:
                    draw_circle(count, bullet3_a1[0], bullet3_a1[1], [1, 1, 0])
                count += 1
                
        if bullet3_a2[3] and alien_2[3]:         # if bullet visible and alien still has hp
            count = 0
            while count <= 8:
                if count < 5:
                    draw_circle(count, bullet3_a2[0], bullet3_a2[1], [1, 0, 1])
                else:
                    draw_circle(count, bullet3_a2[0], bullet3_a2[1], [1, 1, 0])
                count += 1
                

def reset():
    global isPlaying, gameStart, bullet_a1, tem_shooter_color,bullet2_a1,bullet3_a1,bullet3_a2, bullet2_a2, Won,bullet_2,bullet_1,starting_shooter_y, shooter_visibility, gameover, bullet_3,exitGame,shootable, bullet_4, bullet_5, gameover,shooter_speed, gameStart,lives,tem_shooter_color,gamestartStatus, bullet_a2, bullet_1 ,bullet_speed, shooter_x, shooter_y, shooter_color, alien_1, alien_2, score, line_num
    shooter_x = 250
    shooter_color = [0, 1, 1]
    tem_shooter_color = shooter_color
    shooter_y = 45
    shooter_visibility = False
    starting_shooter_y = -30
    shooter_speed = 15
    bullet_1 = [[shooter_x, shooter_y, True, True], [shooter_x, shooter_y, False, True],
                [shooter_x, shooter_y, False, True], [shooter_x, shooter_y, False, True],
                [shooter_x, shooter_y, False, True], [shooter_x, shooter_y, False, True],
                [shooter_x, shooter_y, False, True], [shooter_x, shooter_y, False, True],
                [shooter_x, shooter_y, False, True], [shooter_x, shooter_y, False, True],
                [shooter_x, shooter_y, False, True], [shooter_x, shooter_y, False, True],
                [shooter_x, shooter_y, False, True]]
    bullet_2 = [[shooter_x - 10, shooter_y, True, True], [shooter_x - 10, shooter_y, False, True],
                [shooter_x - 10, shooter_y, False, True], [shooter_x - 10, shooter_y, False, True],
                [shooter_x - 10, shooter_y, False, True], [shooter_x - 10, shooter_y, False, True],
                [shooter_x - 10, shooter_y, False, True], [shooter_x - 10, shooter_y, False, True],
                [shooter_x - 10, shooter_y, False, True], [shooter_x - 10, shooter_y, False, True],
                [shooter_x - 10, shooter_y, False, True], [shooter_x - 10, shooter_y, False, True],
                [shooter_x - 10, shooter_y, False, True]]
    bullet_3 = [[shooter_x + 10, shooter_y, True, True], [shooter_x + 10, shooter_y, False, True],
                [shooter_x + 10, shooter_y, False, True], [shooter_x + 10, shooter_y, False, True],
                [shooter_x + 10, shooter_y, False, True], [shooter_x + 10, shooter_y, False, True],
                [shooter_x + 10, shooter_y, False, True], [shooter_x + 10, shooter_y, False, True],
                [shooter_x + 10, shooter_y, False, True], [shooter_x + 10, shooter_y, False, True],
                [shooter_x + 10, shooter_y, False, True], [shooter_x + 10, shooter_y, False, True],
                [shooter_x + 10, shooter_y, False, True]]
    bullet_4 = [[shooter_x - 20, shooter_y, True, True], [shooter_x - 20, shooter_y, False, True],
                [shooter_x - 20, shooter_y, False, True], [shooter_x - 20, shooter_y, False, True],
                [shooter_x - 20, shooter_y, False, True], [shooter_x - 20, shooter_y, False, True],
                [shooter_x - 20, shooter_y, False, True], [shooter_x - 20, shooter_y, False, True],
                [shooter_x - 20, shooter_y, False, True], [shooter_x - 20, shooter_y, False, True],
                [shooter_x - 20, shooter_y, False, True], [shooter_x - 20, shooter_y, False, True],
                [shooter_x - 20, shooter_y, False, True]]
    bullet_5 = [[shooter_x + 20, shooter_y, True, True], [shooter_x + 20, shooter_y, False, True],
                [shooter_x + 20, shooter_y, False, True], [shooter_x + 20, shooter_y, False, True],
                [shooter_x + 20, shooter_y, False, True], [shooter_x + 20, shooter_y, False, True],
                [shooter_x + 20, shooter_y, False, True], [shooter_x + 20, shooter_y, False, True],
                [shooter_x + 20, shooter_y, False, True], [shooter_x + 20, shooter_y, False, True],
                [shooter_x + 20, shooter_y, False, True], [shooter_x + 20, shooter_y, False, True],
                [shooter_x + 20, shooter_y, False, True]]
    bullet_speed = 9
    line_num = 1
    isPlaying = False
    gameStart = False
    exitGame = False
    shootable = True
    alien_1 = [40, 590, 5, 100, False, [1, 1, 0], "right"]
    alien_2 = [460, 590, 5, 100, False, [1, 1, 0], "left"]
    bullet_a1 = [alien_1[0], alien_1[1] - 10, 5, False]
    bullet_a2 = [alien_2[0], alien_2[1] - 10, 10, False]
    bullet2_a1 = [alien_1[0], alien_1[1] - 10, 15, False]
    bullet2_a2 = [alien_2[0], alien_2[1] - 10, 20, False]
    bullet3_a1 = [alien_1[0], alien_1[1] - 10, 25, False]
    bullet3_a2 = [alien_2[0], alien_2[1] - 10, 30, False]


                
############# Looping ##########################
def animate():
    global isPlaying, gameStart, bullet_a1, tem_shooter_color,bullet2_a1,bullet3_a1,bullet3_a2, bullet2_a2, Won,bullet_2,bullet_1,starting_shooter_y, shooter_visibility, gameover, bullet_3,exitGame,shootable, bullet_4, bullet_5, gameover,shooter_speed, gameStart,lives,tem_shooter_color,gamestartStatus, bullet_a2, bullet_1 ,bullet_speed, shooter_x, shooter_y, shooter_color, alien_1, alien_2, score, line_num
    glutPostRedisplay()
    
    ################## After Game over Reset all ##################################################
    if gameover == True:
        reset()

    if gameStart == True and isPlaying == True:
        ############ starting Shooter entry and win leave #############################
        if shooter_visibility == False:
            if starting_shooter_y < 45:
                starting_shooter_y += 5
            if starting_shooter_y == 45:
                shooter_visibility = True
                
        if Won:                                 # check if all the bullets are stored at shooter_y point
            
            check = 'ok'
            for i in bullet_1:
                if i[1] != shooter_y:
                    check = 'not ok'
                    
            if check == 'ok':
                for i in bullet_2:
                    if i[1] != shooter_y:
                        check = 'not ok'
                        
            if check == 'ok':
                for i in bullet_3:
                    if i[1] != shooter_y:
                        check = 'not ok'
                        
            if check == 'ok':
                for i in bullet_4:
                    if i[1] != shooter_y:
                        check = 'not ok'
                        
            if check == 'ok':
                for i in bullet_5:
                    if i[1] != shooter_y:
                        check = 'not ok'
                        
            if check == 'ok':
                shooter_visibility = False
                starting_shooter_y += 20
                isPlaying = False

    if (gameStart == True and isPlaying == True) and shooter_visibility:
        ############# alien destroyed ####################################
        if alien_1[3] <= 0:         # hp zero
            alien_1[4] = False      # invisible
            bullet_a1[3] = False    # invisible
        if alien_2[3] <= 0:
            alien_2[4] = False
            bullet_a2[3] = False
        if alien_1[3] <= 0 and alien_2[3] <= 0:     # both hp zero
            if Won == False:
                Won = True
                print(".....................................................")
                print("Yaayyyy!! You Won!!")
                print("Score:",score)
                
        ##### bullet number,bullet speed, Difficulties change according to score ##############
        if score > 10 and score < 20:
            line_num = 3
            bullet_speed = 12
            shooter_speed = 18
            alien_1[2] = 8              # alien speed = 8
            alien_2[2] = 8
            
        if score > 50:
            line_num = 5
            bullet_speed = 15
            shooter_speed = 20
            alien_1[2] = 12
            alien_2[2] = 12
            
        ########## shooter and alien color auto change after got shot ###################
        if alien_1[5] == [1,0,0]:
            alien_1[5] = [1,1,0]
            
        if alien_2[5] == [1,0,0]:
            alien_2[5] = [1,1,0]
            
        if shooter_color == [1,0,0]:
            shooter_color = tem_shooter_color
            
        #### alien moving #######################
        if alien_1[4] == True:                      # if visible
            #------------------------------------------------------
            if alien_1[6] == "right":
                alien_1[0] += alien_1[2]
                if alien_1[0] >= 460:               # if more than 460, then alien is out of screen
                    alien_1[6] = "left"
                                                    #constant movement from right to left, same for alien2
            if alien_1[6] == "left":
                alien_1[0] -= alien_1[2]
                if alien_1[0] <= 40:
                    alien_1[6] = "right"
            #------------------------------------------------------        
        if alien_2[4] == True:
            
            if alien_2[6] == "right":
                alien_2[0] += alien_2[2]
                if alien_2[0] >= 460:
                    alien_2[6] = "left"
                    
            if alien_2[6] == "left":
                alien_2[0] -= alien_2[2]
                if alien_2[0] <= 40:
                    alien_2[6] = "right"
                    
                    
        ######## alien bullet looping #######################
        if gamestartStatus == "Game Running" and Won == False:
            
            if alien_1[4] == True:                  # if visible
                bullet_a1[1] -= bullet_a1[2]
                if bullet_a1[1] <= 0:
                    bullet_a1[1] = alien_1[1]-10
                    bullet_a1[0] = alien_1[0]
                    bullet_a1[3] = True
                    
            if alien_2[4] == True:
                bullet_a2[1] -= bullet_a2[2]
                if bullet_a2[1] <= 0:
                    bullet_a2[1] = alien_2[1] - 10
                    bullet_a2[0] = alien_2[0]
                    bullet_a2[3] = True
                    
            if line_num > 2:
                
                if alien_1[4] == True:
                    bullet2_a1[1] -= bullet2_a1[2]
                    if bullet2_a1[1] > 400:                    # sudden change in direction occurs here
                        if bullet2_a1[0] < shooter_x:          # if alienx < shooterx, meaning alien is left of shooter, then alienx + speed. falls closer to shooter
                            bullet2_a1[0] += bullet2_a1[2]
                        if bullet2_a1[0] > shooter_x:          # if alienx > shooterx, meaning alien is right of shooter, then alienx - speed. falls closer to shooter
                            bullet2_a1[0] -= bullet2_a1[2]
                    if bullet2_a1[1] <= 0:
                        bullet2_a1[1] = alien_1[1] - 10
                        bullet2_a1[0] = alien_1[0]
                        bullet2_a1[3] = True
                        
                if alien_2[4] == True:
                    bullet2_a2[1] -= bullet2_a2[2]
                    if bullet2_a2[1] > 400:
                        if bullet2_a2[0] < shooter_x:
                            bullet2_a2[0] += bullet2_a2[2]
                        if bullet2_a2[0] > shooter_x:
                            bullet2_a2[0] -= bullet2_a2[2]
                    if bullet2_a2[1] <= 0:
                        bullet2_a2[1] = alien_2[1] - 10
                        bullet2_a2[0] = alien_2[0]
                        bullet2_a2[3] = True
                        
            if line_num > 4:
                
                if alien_1[4] == True:
                    bullet3_a1[1] -= bullet3_a1[2]
                    if bullet3_a1[1] > 500:
                        if bullet3_a1[0] < shooter_x:
                            bullet3_a1[0] += bullet3_a1[2]
                        if bullet3_a1[0] > shooter_x:
                            bullet3_a1[0] -= bullet3_a1[2]
                    if bullet3_a1[1] <= 0:
                        bullet3_a1[1] = alien_1[1] - 10
                        bullet3_a1[0] = alien_1[0]
                        bullet3_a1[3] = True
                        
                if alien_2[4] == True:
                    bullet3_a2[1] -= bullet3_a2[2]
                    if bullet3_a2[1] > 500:
                        if bullet3_a2[0] < shooter_x:
                            bullet3_a2[0] += bullet3_a2[2]
                        if bullet3_a2[0] > shooter_x:
                            bullet3_a2[0] -= bullet3_a2[2]
                    if bullet3_a2[1] <= 0:
                        bullet3_a2[1] = alien_2[1] - 10
                        bullet3_a2[0] = alien_2[0]
                        bullet3_a2[3] = True
                        
                        
        ###### losing life ##########################
        if bullet_a1[3] == True:            # if visible
            d1 = math.sqrt((bullet_a1[0] - shooter_x) ** 2 + (bullet_a1[1] - shooter_y) ** 2)     # distance between two points
            if d1 <= 28:
                bullet_a1[3] = False
                tem_shooter_color = shooter_color
                shooter_color = [1, 0, 0]
                if lives > 0:
                    print("Got Shot")
                    lives -= 1
                if lives == 0:
                    gameStart = False
                    gameover = True
                    print("...............................................")
                    print("Game Over")
                    shooter_speed = 0
                    print("Score:", score)
                print("Lives:",lives)
                
        if bullet_a2[3] == True:
            d1 = math.sqrt((bullet_a2[0] - shooter_x) ** 2 + (bullet_a2[1] - shooter_y) ** 2)     # distance between two points
            if d1 <= 28:
                bullet_a2[3] = False
                tem_shooter_color = shooter_color
                shooter_color = [1, 0, 0]
                if lives > 0:
                    print("Got Shot")
                    lives -= 1
                if lives == 0:
                    gameStart = False
                    gameover = True
                    print('...................................................')
                    print("Game Over")
                    shooter_speed = 0
                    print("Score:", score)
                print("Lives:",lives)
                
        if bullet2_a1[3] == True:
            d1 = math.sqrt((bullet2_a1[0] - shooter_x) ** 2 + (bullet2_a1[1] - shooter_y) ** 2)     # distance between two points
            if d1 <= 28:
                bullet2_a1[3] = False
                tem_shooter_color = shooter_color
                shooter_color = [1, 0, 0]
                if lives > 0:
                    print("Got Shot")
                    lives -= 1
                if lives == 0:
                    gameStart = False
                    gameover = True
                    print('...................................................')
                    print("Game Over")
                    shooter_speed = 0
                    print("Score:", score)
                print("Lives:",lives)
                
        if bullet2_a2[3] == True:
            d1 = math.sqrt((bullet2_a2[0] - shooter_x) ** 2 + (bullet2_a2[1] - shooter_y) ** 2)     # distance between two points
            if d1 <= 28:
                bullet2_a2[3] = False
                tem_shooter_color = shooter_color
                shooter_color = [1, 0, 0]
                if lives > 0:
                    print("Got Shot")
                    lives -= 1
                if lives == 0:
                    gameStart = False
                    gameover = True
                    print('...................................................')
                    print("Game Over")
                    shooter_speed = 0
                    print("Score:", score)
                print("Lives:",lives)
                
        if bullet3_a1[3] == True:
            d1 = math.sqrt((bullet3_a1[0] - shooter_x) ** 2 + (bullet3_a1[1] - shooter_y) ** 2)     # distance between two points
            if d1 <= 28:
                bullet3_a1[3] = False
                tem_shooter_color = shooter_color
                shooter_color = [1, 0, 0]
                if lives > 0:
                    print("Got Shot")
                    lives -= 1
                if lives == 0:
                    gameStart = False
                    gameover = True
                    print('...................................................')
                    print("Game Over")
                    shooter_speed = 0
                    print("Score:", score)
                print("Lives:",lives)
                
        if bullet3_a2[3] == True:
            d1 = math.sqrt((bullet3_a2[0] - shooter_x) ** 2 + (bullet3_a2[1] - shooter_y) ** 2)     # distance between two points
            if d1 <= 28:
                bullet3_a2[3] = False
                tem_shooter_color = shooter_color
                shooter_color = [1, 0, 0]
                if lives > 0:
                    print("Got Shooted")
                    lives -= 1
                if lives == 0:
                    gameStart = False
                    gameover = True
                    print('...................................................')
                    print("Game Over")
                    shooter_speed = 0
                    print("Score:", score)
                print("Lives:",lives)
                
        ############# bullet_1 looping ##################################################################
        for i in range(len(bullet_1)):
            
            if bullet_1[-1][2] == True:         # intially if the second last bullet of the array is visible, the aliens appear.
                if gamestartStatus == "Game Started" or gamestartStatus == "Game Restarted":
                    if Won == False:
                        alien_1[4] = True
                        alien_2[4] = True
                        bullet_a1[3] = True
                        bullet_a2[3] = True
                    gamestartStatus = "Game Running"
                    
            if bullet_1[i][2] == True:
                if Won == True:
                    if bullet_1[i][1] != shooter_y:
                        bullet_1[i][1] = (bullet_1[i][1] + bullet_speed)
                    else:
                        bullet_1[i][1] = shooter_y
                else:
                    bullet_1[i][1] = (bullet_1[i][1] + bullet_speed)
                if bullet_1[i][1] > shooter_y + 50 and bullet_1[i][1] < shooter_y + 70:
                    if i < len(bullet_1) - 1:
                        bullet_1[i+1][2] = True
                if bullet_1[i][1] > 650:
                    bullet_1[i][1] = shooter_y
                    bullet_1[i][0] = shooter_x
                    bullet_1[i][3] = True
                    
            ###### While shooter bullet clashing with alien #############
            if bullet_1[i][3] == True:                  # if visible
                d1 = math.sqrt((bullet_1[i][0] - alien_1[0]) ** 2 + (bullet_1[i][1] - alien_1[1]) ** 2)     # distance between two points
                if d1 < 25:
                    if alien_1[4] == True:
                        bullet_1[i][3] = False
                        alien_1[5] = [1,0,0]        # red
                        alien_1[3] -= 1
                        score += 1
                d2 = math.sqrt((bullet_1[i][0] - alien_2[0]) ** 2 + (bullet_1[i][1] - alien_2[1]) ** 2)     # distance between two points
                if d2 < 25:
                    if alien_2[4] == True:
                        bullet_1[i][3] = False
                        alien_2[5] = [1, 0, 0]
                        alien_2[3] -= 1
                        score += 1
                        
        ############# bullet_2 looping ##################################################################
        for i in range(len(bullet_2)):
            if bullet_2[i][2] == True:
                if Won == True:
                    if bullet_2[i][1] != shooter_y:
                        bullet_2[i][1] = (bullet_2[i][1] + bullet_speed)
                        if shooter_color == [0, 1, 1]:
                            bullet_2[i][0] = (bullet_2[i][0] - 0.5)
                        if shooter_color == [1, 0, 1]:
                            bullet_2[i][0] = (bullet_2[i][0] - 1)
                        if shooter_color == [0, 1, 0]:
                            bullet_2[i][0] = (bullet_2[i][0] - 2)
                        if bullet_2[i][1] > shooter_y + 50 and bullet_2[i][1] < shooter_y + 70:
                            if i < len(bullet_2) - 1:
                                bullet_2[i + 1][2] = True
                        if bullet_2[i][1] > 650:
                            bullet_2[i][1] = shooter_y
                            bullet_2[i][0] = shooter_x - 10
                            bullet_2[i][3] = True
                    else:
                        bullet_2[i][1] = shooter_y
                else:
                    bullet_2[i][1] = (bullet_2[i][1] + bullet_speed)
                    if shooter_color == [0,1,1]:
                        bullet_2[i][0] = (bullet_2[i][0] - 0.5)
                    if shooter_color == [1,0,1]:
                        bullet_2[i][0] = (bullet_2[i][0] - 1)
                    if shooter_color == [0,1,0]:
                        bullet_2[i][0] = (bullet_2[i][0] - 2)
                    if bullet_2[i][1] > shooter_y + 50 and bullet_2[i][1] < shooter_y + 70:
                        if i < len(bullet_2) - 1:
                            bullet_2[i + 1][2] = True
                    if bullet_2[i][1] > 650:
                        bullet_2[i][1] = shooter_y
                        bullet_2[i][0] = shooter_x - 10
                        bullet_2[i][3] = True
                        
            ###### While clashing with alien #############
            if bullet_2[i][3] == True and line_num > 2:
                d1 = math.sqrt((bullet_2[i][0] - alien_1[0]) ** 2 + (bullet_2[i][1] - alien_1[1]) ** 2)
                if d1 < 25:
                    if alien_1[4] == True:
                        bullet_2[i][3] = False
                        alien_1[5] = [1,0,0]
                        alien_1[3] -= 1
                        score += 1
                d2 = math.sqrt((bullet_2[i][0] - alien_2[0]) ** 2 + (bullet_2[i][1] - alien_2[1]) ** 2)
                if d2 < 25:
                    if alien_2[4] == True:
                        bullet_2[i][3] = False
                        alien_2[5] = [1, 0, 0]
                        alien_2[3] -= 1
                        score += 1
        ############# bullet_3 looping ##################################################################
        for i in range(len(bullet_3)):
            if bullet_3[i][2] == True:
                if Won == True:
                    if bullet_3[i][1] != shooter_y:
                        bullet_3[i][1] = (bullet_3[i][1] + bullet_speed)
                        if shooter_color == [0, 1, 1]:
                            bullet_3[i][0] = (bullet_3[i][0] + 0.5)
                        if shooter_color == [1, 0, 1]:
                            bullet_3[i][0] = (bullet_3[i][0] + 1)
                        if shooter_color == [0, 1, 0]:
                            bullet_3[i][0] = (bullet_3[i][0] + 2)
                        if bullet_3[i][1] > shooter_y + 50 and bullet_3[i][1] < shooter_y + 70:
                            if i < len(bullet_3) - 1:
                                bullet_3[i + 1][2] = True
                        if bullet_3[i][1] > 650:
                            bullet_3[i][1] = shooter_y
                            bullet_3[i][0] = shooter_x + 10
                            bullet_3[i][3] = True
                    else:
                        bullet_3[i][1] = shooter_y
                else:
                    bullet_3[i][1] = (bullet_3[i][1] + bullet_speed)
                    if shooter_color == [0, 1, 1]:
                        bullet_3[i][0] = (bullet_3[i][0] + 0.5)
                    if shooter_color == [1,0,1]:
                        bullet_3[i][0] = (bullet_3[i][0] + 1)
                    if shooter_color == [0,1,0]:
                        bullet_3[i][0] = (bullet_3[i][0] + 2)
                    if bullet_3[i][1] > shooter_y + 50 and bullet_3[i][1] < shooter_y + 70:
                        if i < len(bullet_3) - 1:
                            bullet_3[i + 1][2] = True
                    if bullet_3[i][1] > 650:
                        bullet_3[i][1] = shooter_y
                        bullet_3[i][0] = shooter_x + 10
                        bullet_3[i][3] = True
                        
            ###### While clashing with alien #############
            if bullet_3[i][3] == True and line_num > 2:
                d1 = math.sqrt((bullet_3[i][0] - alien_1[0]) ** 2 + (bullet_3[i][1] - alien_1[1]) ** 2)
                if d1 < 25:
                    if alien_1[4] == True:
                        bullet_3[i][3] = False
                        alien_1[5] = [1,0,0]
                        alien_1[3] -= 1
                        score += 1
                d2 = math.sqrt((bullet_3[i][0] - alien_2[0]) ** 2 + (bullet_3[i][1] - alien_2[1]) ** 2)
                if d2 < 25:
                    if alien_2[4] == True:
                        bullet_3[i][3] = False
                        alien_2[5] = [1, 0, 0]
                        alien_2[3] -= 1
                        score += 1
                        
        ############# bullet_4 looping ##################################################################
        for i in range(len(bullet_4)):
            if bullet_4[i][2] == True:
                if Won == True:
                    if bullet_4[i][1] != shooter_y:
                        bullet_4[i][1] = (bullet_4[i][1] + bullet_speed)
                        if shooter_color == [0, 1, 1]:
                            bullet_4[i][0] = (bullet_4[i][0] - 1)
                        if shooter_color == [1, 0, 1]:
                            bullet_4[i][0] = (bullet_4[i][0] - 2)
                        if shooter_color == [0, 1, 0]:
                            bullet_4[i][0] = (bullet_4[i][0] - 4)
                        if bullet_4[i][1] > shooter_y + 50 and bullet_4[i][1] < shooter_y + 70:
                            if i < len(bullet_4) - 1:
                                bullet_4[i + 1][2] = True
                        if bullet_4[i][1] > 650:
                            bullet_4[i][1] = shooter_y
                            bullet_4[i][0] = shooter_x - 20
                            bullet_4[i][3] = True
                    else:
                        bullet_4[i][1] = shooter_y
                else:
                    bullet_4[i][1] = (bullet_4[i][1] + bullet_speed)
                    if shooter_color == [0, 1, 1]:
                        bullet_4[i][0] = (bullet_4[i][0] - 1)
                    if shooter_color == [1,0,1]:
                        bullet_4[i][0] = (bullet_4[i][0] - 2)
                    if shooter_color == [0,1,0]:
                        bullet_4[i][0] = (bullet_4[i][0] - 4)
                    if bullet_4[i][1] > shooter_y + 50 and bullet_4[i][1] < shooter_y + 70:
                        if i < len(bullet_4) - 1:
                            bullet_4[i + 1][2] = True
                    if bullet_4[i][1] > 650:
                        bullet_4[i][1] = shooter_y
                        bullet_4[i][0] = shooter_x - 20
                        bullet_4[i][3] = True
                        
            ###### While clashing with alien #############
            if bullet_4[i][3] == True and line_num > 4:
                d1 = math.sqrt((bullet_4[i][0] - alien_1[0]) ** 2 + (bullet_4[i][1] - alien_1[1]) ** 2)
                if d1 < 25:
                    if alien_1[4] == True:
                        bullet_4[i][3] = False
                        alien_1[5] = [1,0,0]
                        alien_1[3] -= 1
                        score += 1
                d2 = math.sqrt((bullet_4[i][0] - alien_2[0]) ** 2 + (bullet_4[i][1] - alien_2[1]) ** 2)
                if d2 < 25:
                    if alien_2[4] == True:
                        bullet_4[i][3] = False
                        alien_2[5] = [1, 0, 0]
                        alien_2[3] -= 1
                        score += 1
                        
        ############# bullet_5 looping ##################################################################
        for i in range(len(bullet_5)):
            if bullet_5[i][2] == True:
                if Won == True:
                    if bullet_5[i][1] != shooter_y:
                        bullet_5[i][1] = (bullet_5[i][1] + bullet_speed)
                        if shooter_color == [0, 1, 1]:
                            bullet_5[i][0] = (bullet_5[i][0] + 1)
                        if shooter_color == [1, 0, 1]:
                            bullet_5[i][0] = (bullet_5[i][0] + 2)
                        if shooter_color == [0, 1, 0]:
                            bullet_5[i][0] = (bullet_5[i][0] + 4)
                        if bullet_5[i][1] > shooter_y + 50 and bullet_5[i][1] < shooter_y + 70:
                            if i < len(bullet_5) - 1:
                                bullet_5[i + 1][2] = True
                        if bullet_5[i][1] > 650:
                            bullet_5[i][1] = shooter_y
                            bullet_5[i][0] = shooter_x + 20
                            bullet_5[i][3] = True
                    else:
                        bullet_5[i][1] = shooter_y
                else:
                    bullet_5[i][1] = (bullet_5[i][1] + bullet_speed)
                    if shooter_color == [0, 1, 1]:
                        bullet_5[i][0] = (bullet_5[i][0] + 1)
                    if shooter_color == [1,0,1]:
                        bullet_5[i][0] = (bullet_5[i][0] + 2)
                    if shooter_color == [0,1,0]:
                        bullet_5[i][0] = (bullet_5[i][0] + 4)
                    if bullet_5[i][1] > shooter_y + 50 and bullet_5[i][1] < shooter_y + 70:
                        if i < len(bullet_5) - 1:
                            bullet_5[i + 1][2] = True
                    if bullet_5[i][1] > 650:
                        bullet_5[i][1] = shooter_y
                        bullet_5[i][0] = shooter_x + 20
                        bullet_5[i][3] = True
                        
            ###### While clashing with alien #############
            if bullet_5[i][3] == True and line_num > 4:
                d1 = math.sqrt((bullet_5[i][0] - alien_1[0]) ** 2 + (bullet_5[i][1] - alien_1[1]) ** 2)
                if d1 < 25:
                    if alien_1[4] == True:
                        bullet_5[i][3] = False
                        alien_1[5] = [1,0,0]
                        alien_1[3] -= 1
                        score += 1
                d2 = math.sqrt((bullet_5[i][0] - alien_2[0]) ** 2 + (bullet_5[i][1] - alien_2[1]) ** 2)
                if d2 < 25:
                    if alien_2[4] == True:
                        bullet_5[i][3] = False
                        alien_2[5] = [1, 0, 0]
                        alien_2[3] -= 1
                        score += 1

def mouseListener(button, state, x, y):
    global isPlaying, exitGame, gameStart, shooter_color, alien_1, alien_2,bullet2_a1,bullet3_a1,bullet3_a2, bullet2_a2, Won,starting_shooter_y, bullet_1,shooter_visibility, tem_shooter_color,bullet_2,bullet_3,bullet_4,bullet_5,line_num,bullet_a1,bullet_a2, score, shooter_speed,bullet_r,shootable, bullet_speed,shooter_y, shooter_x, lives, gameover, gamestartStatus
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN: 
            ################ Theme Change ############ THESE ARE THE BUTTONS FOR CHANGING MODES
            if y >= 55 and y <= 75:
                if x >= 235 and x <= 265:
                    shooter_color = [0,1,1]
                if x >= 285 and x <= 315:
                    shooter_color = [1,0,1]
                if x >= 335 and x <= 365:
                    shooter_color = [0,1,0]

            ##### Pause and Play ##################
            if x >= 130 and x <= 170:
                if y >= 35 and y <= 75:
                    if gameover == False and shootable:
                        if isPlaying == True:
                            isPlaying = False
                            shooter_speed = 0
                        else:
                            isPlaying = True
                            shooter_speed = 10
                            if gameStart == False:
                                print("..........................................................")
                                print(gamestartStatus)
                                print("Lives:",lives)
                                print("Score:",score)
                            gameStart = True
                            
            ##### Exit #############
            if x >= 430 and x <= 470:
                if y >= 35 and y <= 75:
                    print(".............................................................")
                    print("Good bye! Total Score:",score)
                    glutLeaveMainLoop()

            ##### Restart #############
            if x >= 30 and x <= 70:
                if y >= 35 and y <= 75:
                    exitGame = True
                    isPlaying = False
                    if gameStart:
                        if Won == False:
                            print(".............................................................")
                            print("Game Ended. Score:",score)
                            print("Lives:", lives)
                    
                    Won = False
                    bullet_r = 5
                    score = 0
                    lives = 3
                    gamestartStatus = "Game Restarted"
                    gameover = False
                    
                    reset()


def keyboardListener(key, x, y):
    global shooter_x, shooter_speed, gameStart,alien_1, alien_2,Won, isPlaying, shootable, shooter_y, bullet_1, gameover, gamestartStatus
    if isPlaying == True:
        if bullet_1[-1][2] and Won==False:
            if key == b'a' or key == b'A':
                if shooter_x > 30:
                    shooter_x -= shooter_speed
            if key == b'd' or key == b'D':
                if shooter_x < 470:
                    shooter_x += shooter_speed
        if key == b'w' or key == b'W':
            if shooter_y < 620:
                shooter_y = shooter_y
        if key == b's' or key == b'S':
            if shooter_y > 40:
                shooter_y = shooter_y

    if key == b' ':
        if gameover == False and shootable == True:
            if isPlaying == True:
                isPlaying = False
                shooter_speed = 0
            else:
                isPlaying = True
                shooter_speed = 10
                if gameStart == False:
                    print(gamestartStatus)
                    print("Lives:", lives)
                gameStart = True

def specialKeyListener1(key, x, y):
    global shooter_x, shooter_speed, gameStart, isPlaying, shootable, shooter_y, bullet_1
    if isPlaying == True:
        if bullet_1[-1][2] == True and Won==False:
            if key == GLUT_KEY_LEFT:
                if shooter_x > 30:
                    shooter_x -= shooter_speed
            if key == GLUT_KEY_RIGHT:
                if shooter_x < 470:
                    shooter_x += shooter_speed


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def show_screen(): #Gl DisPlaying Screen Function
    global isPlaying
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if shooter_visibility == True:
        main_shooter(shooter_x, shooter_y, shooter_color)
        bullet1()
        if line_num > 2:
            bullet2()
            bullet3()
        if line_num > 4:
            bullet4()
            bullet5()
    else:
        starting_shooter()
    restart_img()
    line()
    themes()
    heart()
    bulletOfAlien()
    alien1()
    alien2()

    if isPlaying == True:
        pause_img()
    else:
        play_img()
    exit_img()
    glutSwapBuffers()

# GL Driver Codes
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 750)
glutInitWindowPosition(400, 0)
wind = glutCreateWindow(b"Alien Shooter Game")
glutDisplayFunc(show_screen)
glutIdleFunc(show_screen)
glutSpecialFunc(specialKeyListener1)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()