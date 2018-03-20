class Commands:
	def default(self, option):
		print "default_process with option", option
		return True

	# calling it 'prin' as 'print' messes with python
	def prin(self, option):
		phrase = raw_input("print: ")
		
		if option == "-l":
			print phrase.lower()
		elif option == "-C":
			print phrase.upper()

		return True

	def quit(self, option):
		print "quit_process with option", option
		return False

	def configure(self, option):
		print "configure_process with option", option
		return True

	def info(self, option):
		print "info_process with option", option
		return True 

	# d = dict([(fname, f) for fname, f in globals().items() if callable(f)]); dictionary of all functions
	# dsp = [f for fname, f in sorted(globals().items()) if callable(f)]; list of all functions
