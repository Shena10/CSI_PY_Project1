
# check user if inputs are positive numbers:
def num_check (user_number):
	valid = False
      while not valid:        
            error = "Please enter a number that is greater than zero"        
            try:        
                  # ask user to enter a number
                  response = float(input(user_number))            
                  # checks number is more than zero 
                  if user_number > 0:
                      return response            
                  # outputs error if input is invalid
                  else:
                      print(error)
                      print()                
            except ValueError:
                  print(error)  

# post distance check question
def dist_check (num_check(),fence_length, post_dist):
	valid = False
	while not valid:
		mult_error = "The length of the fence is not an integer multiple of the post distance."
		try:
			# check if post_dist is a number
			response = num_check(post_dist)
			# calculate post/fence distance 
			fence_post_dist = fence_length % post_dist
			# check if fence length is a multiple of post distance
			if fence_post_dist = 0:
				num_posts = fence_length/post_dist + 1
				return num_posts
			# outputs mult_error if the modulo is not 0
			else:
				print(mult_error)
				print("You wanted your fence to be this length: " %fence_length)
				print()
		except ValueError:
			print(mult_error)

# board length check question
def board_check (num_check(),board_length,fence_length, post_dist):
	valid = False
	while not valid:
		board_error = "This is not correct"
		try:
			response = num_check(user_input)
			# check if board length is the same as post distance
			if board_length >= post_dist and board_length < fence_length:
				return board_length
			# outputs board_error if board_length < post_dist
			else:
				print("You need a board length at least as long as " %post_dist)
				print("The board length cannot be longer than " %fence_length)
				print()
		except ValueError:
			print(board_error)

# board height check question
def int_check ():
	valid = False
	while not valid:
		int_error = "This is not correct"
		try:
			# check if board length is the same as post distance
			if board_length >= post_dist and board_length < fence_length:
				return board_length
			# outputs board_error if board_length < post_dist
			else:
				print("You need a board length at least as long as " %post_dist)
				print("The board length cannot be longer than " %fence_length)
				print()
		except ValueError:
			print(board_error)

# start of input
keep_going = ""
while keep_going == "":
	# get user input for width and check
	width = num_check ("What is the width of the fence? ")
	# get user input for the fence_length and check
	fence_length = num_check ("What is the length of the fence? ")
	# get post distance and check
	post_dist = dist_check ("How far apart would you like the posts? ")
	num_posts = num_posts
	# get board length
	board_length = board_check ("How long do you want the boards to be? ")
	# get number of boards
	num_boards = fence_length/(num_posts -1)
	# get number of boards from top to bottom between each post
	board_height = int_check ("How many boards do you want between each post? ")
