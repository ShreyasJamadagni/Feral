class Commands:
	def default(self, options):
		print "default_process with option", options
		return True

	# calling it 'prin' as 'print' messes with python
	def prin(self, options):
		for option in options:
			if option == "-l":
				print raw_input("print: ").lower()
			elif option == "-C":
				print raw_input("print: ").upper() 

		return True

	def quit(self, options):
		print "quit_process with option", options
		return False

	def configure(self, options):
		print "configure_process with option", options
		return True

	def info(self, options):
		print "info_process with option", options
		return True 

	# d = dict([(fname, f) for fname, f in globals().items() if callable(f)]); dictionary of all functions
	# dsp = [f for fname, f in sorted(globals().items()) if callable(f)]; list of all functions
