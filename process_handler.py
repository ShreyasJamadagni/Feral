from comm import Commands
c = Commands()
# from commands import *

class Process_handler:
	def execute(self, phrase):
		i = 0
		options = []
		option = ""
		command = ""
		while (i < len(phrase)):
			# command detection loop
			if phrase[i] != " ":
				command = command + phrase[i]

			# option detection loop
			elif phrase[i] == " ":
				k = i + 1
				while (k<len(phrase)):
					if phrase[k] != " ":
						option = option + phrase[k]
					if phrase[k] == " " or k == len(phrase) - 1:
						options.append(option)
						option = ""

					k = k + 1
				break

			i = i + 1

		if command == "":
			command = "default"
		for key in c.local:
			if (command == key):
				return c.local[command](options)

		print command, "is not a command!" # if command is not valid
		return True
