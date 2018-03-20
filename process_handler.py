from comm import Commands
c = Commands()
# from commands import *

class Process_handler:
	proc = {"": c.default, 
			"print": c.prin, 
			"quit": c.quit, 
			"info": c.info, 
			"configure": c.configure}

	def execute(self, phrase):
		command = ""
		option = ""
		i = 0
		buff = []
		for c in phrase:
			buff.append(c)

		for j in buff:
			if (j != " "):
				command = command + j

			elif (j == " "):
				k = i + 1
				while (k<len(buff)): #Find how to get the length of a list.
					option = option + buff[k]
					k = k + 1
				
				break

			i = i + 1

		print 
		if (option == ""):
			option = "null"

		for key in self.proc:
			if (command == key):
				return self.proc[command](option)

		print command, "is not a command!"
		return True
