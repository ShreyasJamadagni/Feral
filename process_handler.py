from comm import Commands
c = Commands()
# from commands import *

class Process_handler:
	proc = {"": c.default, "print": c.prin, "quit": c.quit, "info": c.info, "configure": c.configure}

	def execute(self, string):
		for key in self.proc:
			if (string == key):
				return self.proc[string]()

		print string, "is not a command!"
		return True
