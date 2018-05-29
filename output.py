from comm import Commands

class Output(Commands):
	validOptions = ["-l", "-C", "-help"]

	def execute(options):
		# option validation loop
		for option in options:
			if option != "-l" and option != "-C" and option != "-help":
				print option, "is not a valid command!"
				return True
				break
				pass

		string = raw_input("output: ")
		for option in options:
			if option == "-l":
				string = string.lower()
			if option == "-C":
				string = string.upper()
			if option == "-help":
				print "Valid options are: -l , -C , and -help"

		print string
			
		return True

	t = execute(["-l", "-help"])