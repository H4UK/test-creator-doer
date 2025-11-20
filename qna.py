import main


def start():
    while True:
        x = 1
        main.start()
        if x == 0:
            break
        again = input("Do you want to restart? y/n: ")
        again = again.strip()
        if again == 'y':
            pass
        elif again == "n":
            print("Bye!")
            break
        else:
            print("Case sensitive,\n I will end this program 'cause idc")
            break


try:
    start()

except KeyboardInterrupt as error:
    print("WHAAAA------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    yesorno = input("Restart? y/n     ")
    if yesorno == "y":
        print("OK....\n\n\n\n\n\n\n\n\n\n\n\n\n")
        start()
    elif yesorno == "n":
        print("ok.....\n\n\n\n\n\n\n\n\n\n\n\n")
        print("BYEEE")
    else:
        print(
            "WHAAAAAAAAAAAAA---------------\n\n\nYOU DIDN't PUT ANYTHING THAT I ASKED YOU TO PUT IT, IT'S EITHER Y OR N, IDC I'M ENDING")

