class Commands:
	def default(self):
		print "default_process"
		return True

	# calling it 'prin' as 'print' messes with python
	def prin(self):
		print "print_process"
		return True

	def quit(self):
		print "quit_process"
		return False

	def configure(self):
		print "configure_process"
		return True

	def info(self):
		print "info_process"
		return True 

	# d = dict([(fname, f) for fname, f in globals().items() if callable(f)]); dictionary of all functions
	# dsp = [f for fname, f in sorted(globals().items()) if callable(f)]; list of all functions
