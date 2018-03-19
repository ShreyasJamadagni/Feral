from comm import Commands
c = Commands()
# from commands import *

class Process_handler() :
	# later make a json file to have a list of all the commands instead of hardcoding them.
	commands = {"": c.default, 
				"print": c.prin, 
				"info": c.info, 
				"configure": c.configure, 
				"quit": c.quit} # "" stands for 'Default.'

	def execute(string):
		return commands[string]()