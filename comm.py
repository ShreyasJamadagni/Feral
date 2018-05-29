class Commands:

    local = locals()

    def default(options):
        print(options, ", Default")

        return True

    # calling it 'prin' as 'print' messes with python
    def output(options):
        # It shouldn't request for a string if the option is invalid.
        print(options, ", Output")

        return True

    def quit(options):
        return False

    def configure(options):
        print(options, ", configure")
        return True

    def info(options):
        print(options)
        print("Version 0.1.0")
        print("Valid commands are: configure , info , print , quit .")
        return True

    def load(options):
        print(options)
        return True
