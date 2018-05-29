from process_handler import Process_handler
handler = Process_handler()


def main():
    running = True

    while(running):
        running = handler.execute(input("shell-> "))
        print("")

    print("[Process Complete]")


main()
