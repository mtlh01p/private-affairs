# For beginners, all code in a single file without functions 
board_size = 10 
valid_orientations = ['horizontal', 'vertical'] 
# Exercise 1: Basic Conditional Statements 
x, y = 5, 8 
if 1 <= x <= board_size and 1 <= y <= board_size:
    print("Coordinates (", x, ", ", y, ") are valid: True")
else:
    print("Coordinates (", x, ", ", y, ") are valid: False")
#One more example 
x, y = 10, -1 
if 1 <= x <= board_size and 1 <= y <= board_size:
    print("Coordinates (", x, ", ", y, ") are valid: True")
else:
    print("Coordinates (", x, ", ", y, ") are valid: False")
x, y, orientation = 4, 6, 'horizontal' 
if 1 <= x <= board_size and 1 <= y <= board_size and (orientation in valid_orientations):
    print("Inputs (", x, ", ", y, ", ", orientation, ") are valid: True")
else:
    print("Inputs (", x, ", ", y, ", ", orientation, ") are valid: False")
x, y, orientation = 11, 3, 'diagonal' 
if 1 <= x <= board_size and 1 <= y <= board_size and (orientation in valid_orientations):
    print("Inputs (", x, ", ", y, ", ", orientation, ") are valid: True")
else:
    print("Inputs (", x, ", ", y, ", ", orientation, ") are valid: False")
x, y, ship_length, orientation = 3, 5, 4, 'horizontal' 
if 1 <= x <= board_size and 1 <= y <= board_size and (orientation in valid_orientations) and (1 <= ship_length <= 4):
    print("Placement (", x, ", ", y, ", ", ship_length, ", " , orientation, ") is valid: True")
else:
    print("Placement (", x, ", ", y, ", ", ship_length, ", " , orientation, ") is valid: False")
x, y, ship_length, orientation = 7, 7, 4, 'vertical' 
if 1 <= x <= board_size and 1 <= y <= board_size and (orientation in valid_orientations) and (1 <= ship_length <= 4):
    print("Placement (", x, ", ", y, ", ", ship_length, ", " , orientation, ") is valid: True")
else:
    print("Placement (", x, ", ", y, ", ", ship_length, ", " , orientation, ") is valid: False")