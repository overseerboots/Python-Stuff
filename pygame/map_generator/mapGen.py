import random
# 0 = soil
# 1 = water
# 2 = sand
# 3 = grass
# 4 = tree
# 5 - cave
size = 30
map = []

water_chance = 5 # how may intitial points of water
water_percent = 70 # chance of new water
grass_percent = 3 # chance of grass
tree_percent = 90 # chance of grass
cave_percent = 95 # chance of cave

def save_map(map):
  with open("map.txt", 'w') as f:
    for row in map:
      line = ""
      for character in row:
        line += str(character)
      f.write(line + "\n")

def coloured(text,r,g,b):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)

def display_map(map):
    for row in map:
        line = ""
        for character in row:
            if character == 0: #soil
                line += coloured("X", 200,60,60) #brown
            if character == 1: #water
                line += coloured("~", 0,0,255) #blue
            if character == 2: #Sand
                line += coloured("S", 200,200,0) #blue
            if character == 3: #Grass
                line += coloured('"', 0,220,0) #green
            if character == 4: #Grass
                line += coloured('^', 100,255,100) #green
            if character == 5: #Cave
                line += coloured('M', 50,50,50) #gray

            


        print(line)

###########  Generate Map ###############
for row in range(0, size):
    row_data = []
    for col in range(0, size):
        row_data.append(0) #int
    map.append(row_data)

###########  Water Generation  ##########
# --- Generate water Points
for chance in range(water_chance):
    x = random.randint(1, size -1)
    y = random.randint(1, size -1)
    map[y][x] = 1 # water

# --- Generate lakes


for chance in range(water_chance):
 
    for y in range(1,size-1): #loop over the row
        for x in range(1, size-1): # loop over columns
            if map[y][x] == 1: #its water
                num = random.randint(0,100)
                if num > water_percent:
                    map[y][x-1] = 1 # left

                num = random.randint(0,100)
                if num > water_percent:
                    map[y][x+1] = 1  #right

                if num > water_percent:
                    map[y-1][x] = 1  #top

                num = random.randint(0,100)
                if num > water_percent:
                    map[y+1][x] = 1  #bottom

#### Generate Sand ##############################
def adjacent(map, x,y,val):
  if map[y][x+1] == val: #right
    return True
  if map[y][x-1] == val: #left
    return True
  if map[y-1][x] == val: #above
    return True
  if map[y+1][x] == val: #below
    return True

  return False


for y in range(1, size-1):
  for x in range(1, size-1):
    # sand
    if map[y][x] == 0 and adjacent(map,x,y,1):
      map[y][x] = 2 #sand

for y in range(0, size):
  for x in range(0, size):
    #### grass generation ######
    if map[y][x] == 0:  # soil
      num = random.randint(0,100)
      if num > grass_percent:
        map[y][x] = 3 #grass

    #### trees ##################
    if map[y][x] == 3:  # grass
      num = random.randint(0,100)
      if num > tree_percent:
        map[y][x] = 4 #tree

    #### trees ##################
    if map[y][x] == 3:  # grass
      num = random.randint(0,100)
      if num > cave_percent:
        map[y][x] = 5 #cave




display_map(map)
save_map(map)