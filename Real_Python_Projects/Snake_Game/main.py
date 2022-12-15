import pygame
from pygame.locals import *
from pprint import pprint
import random
import threading
import time


def move_snake(_event, block_x, block_y, row, column, direction):
    if _event.key == K_UP:
        new_block_x = block_x
        new_block_y = block_y - 1
        direction = "up"
    elif _event.key == K_DOWN:
        new_block_x = block_x
        new_block_y = block_y + 1
        direction = "down"
    elif _event.key == K_RIGHT:
        new_block_x = block_x + 1
        new_block_y = block_y
        direction = "right"
    elif _event.key == K_LEFT:
        new_block_x = block_x - 1
        new_block_y = block_y
        direction = "left"


    row -= 1
    column -= 1
    if new_block_x > row:
        new_block_x = row
    if new_block_x < 0:
        new_block_x = 0
    if new_block_y > column:
        new_block_y = column
    if new_block_y < 0:
        new_block_y = 0

    return new_block_x, new_block_y, direction

def move_snake_no_event(block_x, block_y, row, column, direction):
    if direction == "up":
        new_block_x = block_x
        new_block_y = block_y - 1
        direction = "up"
    elif direction == "down":
        new_block_x = block_x
        new_block_y = block_y + 1
        direction = "down"
    elif direction == "right":
        new_block_x = block_x + 1
        new_block_y = block_y
        direction = "right"
    elif direction == "left":
        new_block_x = block_x - 1
        new_block_y = block_y
        direction = "left"

    '''
    row -= 1
    column -= 1
    if new_block_x > row:
        new_block_x = row
    if new_block_x < 0:
        new_block_x = 0
    if new_block_y > column:
        new_block_y = column
    if new_block_y < 0:
        new_block_y = 0
    ''' 

    return new_block_x, new_block_y, direction

def create_grid(row, column):
    print("create_grid")
    grid = []
    rows = ["X"]*row
    for i in range(column):
        grid.append(list(rows)) 
    return grid

def initalize_grid(grid, row, column):
    print("initalize_grid")
    #create snake
    grid[0][0] == "S"
    #create apple
    row_middle = round(row/2)
    column_middle = round(column/2)
    grid[row_middle][column_middle] = "A"
    snake = [[0, 0]]
    apple = [row_middle, column_middle]
    return snake, apple

def create_snake(grid):
    print("create_snake")
    snake_parts = []
    for i_row in range(len(grid)):
        for i_col in range(len(grid[0])):
            if grid[i_row][i_col] == "S":
                snake_parts.append([i_row, i_col])
    return snake_parts

def create_apple(grid):
    print("create_apple")
    apple_location = []
    for i_row in range(len(grid)):
        for i_col in range(len(grid[0])):
            if grid[i_row][i_col] == "A":
                apple_location.append([i_row, i_col])
    return apple_location

def did_snake_eat_apple(snake, apple):
    print("did_snake_eat_apple")
    #print(snake)
    #print(apple)
    if snake[-1][0] == apple[0] and snake[-1][1] == apple[1]:
        return True
    return False

def new_apple_location(grid, snake, rows, columns):
    print("new_apple_location")
    locations_for_random = (columns * rows) - len(snake)
    random_number = random.randint(0, locations_for_random)
    print(random_number)
    
    count = 0
    for i in range(rows):
        for j in range(columns):
                if [i, j] in snake:
                    #print("hey made it to snake")
                    count == count
                else:
                    if count == random_number:
                        return [i, j]
                    count += 1

def update_grid(grid, snake, apple):
    print("update_grid")
    #clear grid
    '''
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            grid[row][column] = "X" 
    '''

    #create snake
    for loc in snake:
        #grid[loc[0]][loc[1]] == "S"
        surface.blit(snake_image,(loc[0]*40, loc[1]*40))

    #create apple
    grid[apple[0]][apple[1]] == "A"
    surface.blit(apple_image, (apple[0]*40, apple[1]*40))

def check_if_snake_died(snake, row, column):
    row -= 1
    column -= 1
    print("this is the snake", snake)
    if snake[-1][1] > row:
        return True
    if snake[-1][1] < 0:
        return True
    if snake[-1][0] > column:
        return True
    if snake[-1][0] < 0:
        return True
    
    print("this is the snake: ", snake)

    for i in range(len(snake) - 1):
        if snake[i][0] == snake[-1][0] and snake[i][1] == snake[-1][1]:
            print('snake ate its self whoops')
            return True


    return False
    



first_apple_flag = True

if __name__ == "__main__":
    pygame.init()

    rows = 10
    columns = 10

    surface = pygame.display.set_mode((rows*40, columns*40))
    surface.fill((92, 25, 84))

    snake_image = pygame.image.load("snake_game_images/block.jpg").convert()
    apple_image = pygame.image.load("snake_game_images/apple.jpg").convert()

    #create grid
    grid = create_grid(rows, columns)

    #initalize grid with snake and apple
    snake, apple = initalize_grid(grid, rows, columns)

    #adds apple and snake to screen from grid
    update_grid(grid, snake, apple)

    #bring initalized items to screen
    pygame.display.flip()
    head_x = 0
    head_y = 0

    print("snake: ", snake)

    running = True

    mutex = threading.Lock()

    direction = "down"

    while running:
        print("beginning of while loop")
        mutex.acquire()
        time.sleep(.1)
        mutex.release()

        key_press_flag = False

        for event in pygame.event.get():
            #print(pygame.event.event_name(event.type))
            #print(event.type)
            #move the block
            if event.type == KEYDOWN:
                print("---------------------------------------------------------------------")
                print("some key was pushed")

                #refresh screen
                surface.fill((92, 25, 84))

                #remove end of snake unless snake ate apple


                #move snake
                head_x, head_y, direction = move_snake(event, head_x, head_y, rows, columns, direction)
                snake.append([head_x, head_y])
                
                #check to see if snake bumped into wall or its self
                check_if_snake_died(snake, rows, columns)
                print(check_if_snake_died(snake, rows, columns))
                if check_if_snake_died(snake, rows, columns) == True:
                    print("snake ran into a wall and the game has ended")
                    running = False
                    break
                print('-=-=-=-=-=-=-=-=-')
                

                print(direction)

                #when snake eats apple
                if did_snake_eat_apple(snake, apple) == True:
                    apple_location = new_apple_location(grid, snake, rows, columns)
                    print("apple_location", apple_location)
                    grid[apple_location[0]][apple_location[1]] == "A"
                    apple = [apple_location[0], apple_location[1]]
                    print("this is new apple", apple)
                    #snake.append([apple_location[0], apple_location[1]])
                else: #remove end of snake unless snake ate apple
                    snake.pop(0)

                #update grid with apple and snake (also prints apple and snake)
                update_grid(grid, snake, apple)

                #create snake
                snake_parts = create_snake(grid)
                for xy in snake_parts:
                    surface.blit(block,(xy[0]*40, xy[1]*40))
                
                #put everything on screen
                pygame.display.flip()
                
                #exit the game
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == QUIT:
                    running = False
                
                key_press_flag = True
                break


        if key_press_flag == False:
            print("---------------------------------------------------------------------")
            print("no key was pushed")
            print(direction)
            #refresh screen
            surface.fill((92, 25, 84))

            #move snake
            head_x, head_y, direction = move_snake_no_event(head_x, head_y, rows, columns, direction)
            snake.append([head_x, head_y])
            
            #check to see if snake bumped into wall or its self
            check_if_snake_died(snake, rows, columns)
            print(check_if_snake_died(snake, rows, columns))
            if check_if_snake_died(snake, rows, columns) == True:
                print("snake ran into a wall and the game has ended")
                running = False
                break
            print('-=-=-=-=-=-=-=-=-')

            #when snake eats apple
            if did_snake_eat_apple(snake, apple) == True:
                apple_location = new_apple_location(grid, snake, rows, columns)
                print("apple_location", apple_location)
                grid[apple_location[0]][apple_location[1]] == "A"
                apple = [apple_location[0], apple_location[1]]
                print("this is new apple", apple)
                #snake.append([apple_location[0], apple_location[1]])
            else: #remove end of snake unless snake ate apple
                snake.pop(0)

            #update grid with apple and snake (also prints apple and snake)
            update_grid(grid, snake, apple)

            #create snake
            snake_parts = create_snake(grid)
            for xy in snake_parts:
                surface.blit(block,(xy[0]*40, xy[1]*40))
            
            #put everything on screen
            pygame.display.flip()

    
        
                


            
            

