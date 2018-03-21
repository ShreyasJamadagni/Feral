class Commands:
	local = locals()
	def default(options):
		return True

	# calling it 'prin' as 'print' messes with python
	def output(options):
		string = raw_input("output: ")

# It shouldn't request for a string if the option is invalid.

		return True

	def quit(options):
		return False

	def configure(options):
		print "configure_process with option", options
		return True

	def info(options):
		print "Version 0.0.1"
		print "Valid commands are: configure , info , print , quit ."
		return True 

	# d = dict([(fname, f) for fname, f in globals().items() if callable(f)]); dictionary of all functions
	# dsp = [f for fname, f in sorted(globals().items()) if callable(f)]; list of all functions
