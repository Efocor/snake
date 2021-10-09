# -*- coding: utf-8 -*-

import pygame, sys, time, random


# Window size
frame_size_x = 720
frame_size_y = 480

#Difficulty
difficulty = input("Ingresa nivel de dificultad (1:Fácil, 2:Medio, 3:Difícil): ")
assert difficulty.isdigit(), "El valor ingresado debe ser un número entre 1 y 3"
difficulty = int(difficulty)
assert difficulty in [1,2,3,4], "El valor ingresado debe ser un número entre 1 y 3"
difficulty = (difficulty**2)*10
#difficulty = 200

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')
    
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

#Ganar el juego
def victoria():
    my_font = pygame.font.SysFont('times new roman', 50) #Copia de lo hecho en game_over
    game_over_surface = my_font.render('Ganaste', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'consolas', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#Pausa
def pausar(): #Función
    pausado = True #Variable que define el proceso pausa
    while pausado: #Mientras este pausado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()#Para salir
            if event.type == pygame.KEYDOWN: #Pulsar P para volver a jugar
                if event.key == pygame.K_p:
                    pausado = False #Reflejo
                elif event.key == pygame.K_q: #Pulsar Q para salir
                    pygame.quit()
                    quit() #Salir	
        game_window.fill(black) #Te tira la pantalla a negro
        my_font = pygame.font.SysFont('arial', 50) #La fuente de letra
        show_msg(0, yellow, 'consolas', 20)	#Llamar a  funcion Submensaje
        font_msg = my_font.render('JUEGO EN PAUSA', True, blue) #Leyenda de aviso
        game_window.blit(font_msg, (frame_size_x/4, frame_size_y/4))
        pygame.display.update() #Mostar cambios en pantalla
        time.sleep(0.1)	#Pausa antes de volver

# Game Over
def game_over():
    global snake_pos, snake_body, food_pos, food_spawn, direction, change_to, score #Global para trabajar variables fuera de la función
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('GAME OVER', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'consolas', 20)	
    show_restart(0, blue, 'consolas', 15)	
    pygame.display.flip()
    while True: #Condición
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == ord('c'): #Si se pulsa C ocurre lo siguiente
                snake_pos = [100, 50] #Varibles en global, la posicion
                snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]] #Variable cuerpo serpiente
                food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10] #La comida
                food_spawn = True #Aparecer
                direction = 'RIGHT'
                change_to = direction
                score = 0#Reinicio de la puntuacion
                return					
            if event.type == pygame.KEYDOWN and event.key == ord('q'): #Si se pulsa Q ocurre lo siguiente.
                pygame.quit() #Se termina el juego
                sys.exit()
    time.sleep(5)
    pygame.quit()
    sys.exit()	

# Mensaje
def show_msg(choice, color, font, size):
    msg_font = pygame.font.SysFont(font, size)
    msg_surface = msg_font.render('Pulse Q para salir', True, color)
    msg_rect = msg_surface.get_rect()
    if choice == 1:
        msg_rect.midtop = (frame_size_x/10, 15)
    else:
        msg_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(msg_surface, msg_rect)
    # pygame.display.flip()
    
# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Puntaje : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()

# Reinicio
def show_restart(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Pulsa C si deseas reiniciar, presiona Q para terminar ', True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()    

# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Cerrar juego
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_p:
                pausar()				

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

	#Si se consiguen 10 puntos
    if score==10:
        victoria()	
		
    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)