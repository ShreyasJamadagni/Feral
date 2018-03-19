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

	def configure(self):
		print "configure_process"
		return True

	def info(self):
		print "info_process"
		return True 
