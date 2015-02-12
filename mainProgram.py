# importing required modules
import netCDFapis as api
import sys,getopt as options
import constants as constants

# main function definition
def main():
	# print welcome note
	print constants.S_WELCOME_NOTE
	# read arguments and load file name
	inputFileName = readArguments()
	#initialize input choice to empty
	inputChoice = ''
	print inputFileName
	while(True):
		# display options list in API
		displyOptions()
		# read user input
		inputChoice = raw_input(constants.S_ENTER_NOTE)
		# execute specific function
		executeOption(inputChoice, inputFileName)

# function to disply options to user
def displyOptions():
	# display available options to user
	print constants.S_CHOICE_NOTE
	print constants.S_CHOICE_OPTION_1
	print constants.S_CHOICE_OPTION_2
	print constants.S_CHOICE_OPTION_3
	print constants.S_CHOICE_OPTION_4
	print constants.S_CHOICE_OPTION_5
	print constants.S_CHOICE_OPTION_6
	print constants.S_CHOICE_OPTION_7
	print constants.S_CHOICE_OPTION_8
	print constants.S_CHOICE_OPTION_9
	print constants.S_CHOICE_OPTION_10
	print constants.S_CHOICE_OPTION_11
	print constants.S_QUIT_NOTE
	
# function to execute option
def executeOption(choice, inputFileName):
	# execute api function based on choice
	if choice == constants.N_OPTION_1:
		api.ndims(inputFileName)
	elif choice == constants.N_OPTION_2:
		api.get_global_dim_names(inputFileName)
	elif choice == constants.N_OPTION_3:
		api.get_global_dim_lens(inputFileName)
	elif choice == constants.N_OPTION_4:
		api.nvars(inputFileName)
	elif choice == constants.N_OPTION_5:
		api.get_var_names(inputFileName)
	elif choice == constants.N_OPTION_6:
		api.get_var_dim_lens(inputFileName)
	elif choice == constants.N_OPTION_7:
		api.get_var_dim_names(inputFileName)
	elif choice == constants.N_OPTION_8:
		api.get_num_of_points(inputFileName)
	elif choice == constants.N_OPTION_9:
		api.get_num_of_Cells(inputFileName)
	elif choice == constants.N_OPTION_10:
		api.get_data(inputFileName)
	elif choice == constants.N_OPTION_11:
		api.plot_histogram(inputFileName)
	elif choice == constants.S_QUIT_VAR:
		print constants.S_GOODBYE_NOTE
		sys.exit()
	else:
		print constants.S_CHOICE_ERROR

# function to read input from user 
def readArguments():
	# try to get name from args else throw error msg
	try:
		# get options and argument list values
		opts, args = options.getopt(sys.argv[1:],constants.S_ARGS_VAR)
	except options.GetoptError:
		print constants.S_INPUT_ERROR
		sys.exit(2)
	# parse args and proceed accordingly  
	for opt, arg in opts:
		# disply help for h
		if opt == constants.S_HELP_VAR :
			print constants.S_INPUT_ERROR
			sys.exit()
		# store and dispay file name for i
		elif opt == constants.S_INPUT_VAR:
			inputFileName = arg
	# print input file name     
	return inputFileName

# if the function is the main function start executing 
if __name__ == '__main__':    
	main()