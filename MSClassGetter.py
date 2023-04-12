import numpy
import pyautogui
from PIL import Image
from numpy import asarray
import scipy.special
from time import sleep, time
import pickle

between_clicking_LOAD_and_Return = 1.5
between_clicking_SAVE_and_Return = 1.5
between_clicking_Return_after_LOAD_and_Shop = 11
between_clicking_Return_after_SAVE_and_Shop = 0
waiting_for_class_image_to_set_its_colors = 0.7
waiting_when_game_lagged = 11

static_coordinates_set = False
left = 0
top = 0
width = 0
height = 0
scale_x = 180
scale_y = 265
debug = False
frequent_config_loading = False

def load_user_configuration():
  try:
    with open("config_yourself.txt") as config_yourself:
      config_yourself_content = config_yourself.readlines()
    config_yourself_opened = True
  except:
    config_yourself_opened = False
    print("config_yourself.txt wasn't found in current directory. Proceeding with default settings.")

  global between_clicking_LOAD_and_Return
  global between_clicking_SAVE_and_Return
  global between_clicking_Return_after_LOAD_and_Shop
  global between_clicking_Return_after_SAVE_and_Shop
  global waiting_for_class_image_to_set_its_colors
  global waiting_when_game_lagged
  global static_coordinates_set
  global left
  global top
  global width
  global height
  global debug
  global frequent_config_loading
  if(config_yourself_opened):
    if(config_yourself_content[1][0] == "t"):
      between_clicking_LOAD_and_Return = float(config_yourself_content[4])
      between_clicking_SAVE_and_Return = float(config_yourself_content[6])
      between_clicking_Return_after_LOAD_and_Shop = float(config_yourself_content[8])
      between_clicking_Return_after_SAVE_and_Shop = float(config_yourself_content[10])
      waiting_for_class_image_to_set_its_colors = float(config_yourself_content[12])
      waiting_when_game_lagged = float(config_yourself_content[14])
      print("Delays loaded from config_yourself.txt")
    if(config_yourself_content[16][0] == "t"):
      left = float(config_yourself_content[21])
      top = float(config_yourself_content[23])
      width = float(config_yourself_content[25])
      height = float(config_yourself_content[27])
      static_coordinates_set = True
      print("Static coordinates loaded from config_yourself.txt")
    if(config_yourself_content[29][0] == "t"):
      debug = True
      print("Debug turned on.")
    if(config_yourself_content[31][0] == "t"):
      frequent_config_loading = True
      print("Frequent config loading turned on.")

load_user_configuration()

if(not static_coordinates_set):
  found = False
  while(not found):
    try:
      cords = pyautogui.locateOnScreen('cords.png')
      left = cords[0]
      top = cords[1]
      width = cords[2]
      height = cords[3]
    except:
      input("Screenshot wasn't found on screen. Take a screenshot and save it in this folder as cords.png. Then press enter")
      # pyautogui.screenshot(region=(cords)).show()
    else:
      found = True
  print("Given screenshot (top left corner, width and height): ")
  print(cords)

def capture_screen(shift_x, shift_y):
  image = pyautogui.screenshot(region=(left + shift_x, top + shift_y, width, height))
  newsize = (scale_x, scale_y)
  image = image.resize(newsize)
  image = image.convert("L")
  return image
# classes = ['lagged',
#             'wizard', 'astronomer', 'ice society', 'shaman', 'warlock',
#             'enchantress', 'summoner', 'bishop', 'mystic', 'druid',
#             'pyromancer', 'socerer', 'archemist', 'scholar', 'witch',
#             'electromancer', 'arbiter', 'arc mage', 'archaeologist', 'magician',
#             'mage', 'battle mage', 'warlord', 'dark mage']
classes = ['lagged',
            'wizard', 'astronomer', 'cryomancer', 'enchanter', 'warlock',
            'arcane scholar', 'summoner', 'bishop', 'mystic', 'druid',
            'pyromancer', 'sorcerer', 'alchemist', 'scholar', 'witch',
            'electromancer', 'moderator', 'arch mage', 'archaeologist', 'magician',
            'mage', 'battle mage', 'warlord', 'dark wizard']

full_width = width * 3.245
full_height = height * 3.8954
left_edge = left - (full_width - width) / 2
top_edge = top - (full_height - height) / 2
def click1():
  pyautogui.click(left_edge + 2.9611 * width, top_edge + 0.2889 * height) #"Tap to Continue" after buying class
  pyautogui.click(left_edge + 2.9611 * width, top_edge + 0.2889 * height) #click "X" in right upper corner to exit shop
  pyautogui.click(left_edge + 1.25 * width, top_edge + 3.5646 * height) #click "option"
#   pyautogui.click(left_edge + 2.6388 * width, top_edge + 2.6996 * height) #click "load"
  pyautogui.click(left_edge + 2.6388 * width, top_edge + 2.8777 * height) #click "load" in v0.88 as 2 new languages were added
  pyautogui.click(left_edge + 1.25 * width, top_edge + 2.5855 * height) #click "Run"
  sleep(between_clicking_LOAD_and_Return)
  pyautogui.click(left_edge + 1.25 * width, top_edge + 2.5855 * height) #click "Return"
  sleep(between_clicking_Return_after_LOAD_and_Shop) #in original v0.8593 it was sleep(1)
  pyautogui.click(left_edge + 0.5555 * width, top_edge + 3.5646 * height) #click "Shop"
  pyautogui.click(left_edge + 1.1111 * width, top_edge + 2.8517 * height) #click "Research Data"

def click2():
  pyautogui.click(left_edge + 2.9611 * width, top_edge + 0.2889 * height) #"Tap to Continue" after buying class
  pyautogui.click(left_edge + 2.9611 * width, top_edge + 0.2889 * height) #click "X" in right upper corner to exit shop
  pyautogui.click(left_edge + 1.25 * width, top_edge + 3.5646 * height) #click "option"
  pyautogui.click(left_edge + 1.9491 * width, top_edge + 2.6996 * height) #click "save"
  pyautogui.click(left_edge + 1.25 * width, top_edge + 2.5855 * height) #click "Run"
  sleep(between_clicking_SAVE_and_Return)
  pyautogui.click(left_edge + 1.25 * width, top_edge + 2.5855 * height) #click "go back"
  pyautogui.click(left_edge + 2.9611 * width, top_edge + 0.2889 * height) #exit options

def click3():
  sleep(between_clicking_Return_after_SAVE_and_Shop)    #to test if 0 works
  pyautogui.click(left_edge + 0.5555 * width, top_edge + 3.5646 * height) #click "Shop"
  pyautogui.click(left_edge + 1.1111 * width, top_edge + 2.8517 * height) #click "Research Data"

class neuralNetwork:
  
  def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    self.inodes = inputnodes
    self.hnodes = hiddennodes
    self.onodes = outputnodes
    self.lr = learningrate
    
    self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
    self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
      
  def train(self, inputs_list, targets_list):
    inputs = numpy.array(inputs_list, ndmin=2).T
    targets = numpy.array(targets_list, ndmin=2).T
    hidden_inputs = numpy.dot(self.wih, inputs)
    hidden_outputs = scipy.special.expit(hidden_inputs)
    final_inputs = numpy.dot(self.who, hidden_outputs)
    final_outputs = scipy.special.expit(final_inputs)
    
    output_errors = targets - final_outputs
    hidden_errors = numpy.dot(self.who.T, output_errors)
    self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
    self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

  def save(self):
      file = open('NN_save.txt','wb')
      file.write(pickle.dumps(self.__dict__))
      file.close()
  
  def load(self):
    file = open('NN_save.txt','rb')
    dataPickle = file.read()
    file.close()
    self.__dict__ = pickle.loads(dataPickle)
      
  def query(self, inputs_list):
    inputs = numpy.array(inputs_list, ndmin=2).T
    hidden_inputs = numpy.dot(self.wih, inputs)
    hidden_outputs = scipy.special.expit(hidden_inputs)
    final_inputs = numpy.dot(self.who, hidden_outputs)
    final_outputs = scipy.special.expit(final_inputs)
    return final_outputs

input_nodes = scale_x * scale_y
hidden_nodes = 100
output_nodes = 25
learning_rate = 0.01
epochs = 1

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

n.load()

def check_screen():
  image = capture_screen(0, 0)
  structurized = []
  array = asarray(image)
  for row in array:
    for value in row:
      structurized.append(value)
  data = structurized
  output = n.query(data)
  summarize = []
  for row in output:
    summarize.append(row[0])
  return summarize.index(max(summarize))

if_repeat = True
while(if_repeat):
  already_gotten = 0
  number_of_tries = 0
  choosen_class = input("Write class name, which you want to get, exactly as its name is written in the game and press enter: ").lower()
  while(not (choosen_class in classes)):
    print("Given class does not exist. List of all classes:")
    for temp in range(len(classes) - 1):
      print(classes[temp + 1])
    choosen_class = input("Write again class name, which you want to get, exactly as its name is written in the game (choose from list above) and press enter: ")
  prompt = "Write 1 if you want the program to save searched " + choosen_class + " in game google cloud by spending gems only into " + choosen_class + " or 0 to don't buy anything, but just to stop when it finds first " + choosen_class + ". Then press enter: "
  if_save = False
  done = False
  while(not done):
    _if_save = input(prompt)
    if(_if_save == '1'):
      if_save = True
      done = True
    elif(_if_save == '0'):
      done = True
  demanded_number_of_choosen = 1
  if(if_save):
    prompt = "Write number of " + choosen_class + " which you want to get: "
    _number = input(prompt)
    demanded_number_of_choosen = int(_number)
  index = classes.index(choosen_class)
  temp = 0
  almost_ended = False
  while((already_gotten < demanded_number_of_choosen) and (if_save or already_gotten == 0)):
    if(frequent_config_loading):
      load_user_configuration()
    if(debug):
      start = time()
    number_of_tries += 1
    if(almost_ended):
      almost_ended = False
    else:
      click1()
    sleep(waiting_for_class_image_to_set_its_colors)
    temp = check_screen()
    if(temp == 0):
      print("Game load has lagged. Waiting 10 seconds before processing further.")
      sleep(waiting_when_game_lagged)
    elif(temp == index):
      print("Number of tries:", number_of_tries, " Drawn class:", classes[temp], " Number of", choosen_class, "already received:", already_gotten)
      already_gotten += 1
      if(if_save):
        almost_ended = True
        click2()
        if(already_gotten < demanded_number_of_choosen):
          click3()
    else:
      print("Number of tries:", number_of_tries, " Drawn class:", classes[temp], " Number of", choosen_class, "already received:", already_gotten)
    if(debug):
      end = time()
      print("Cycle duration: " + str(end - start) + " s")
  print("Done!;)")
  prompt = "Write 1 if you want to continue or 0 if you want to exit. Then press enter: "
  if_save = False
  done = False
  while(not done):
    _if_save = input(prompt)
    if(_if_save == '1'):
      done = True
    elif(_if_save == '0'):
      if_repeat = False
      done = True