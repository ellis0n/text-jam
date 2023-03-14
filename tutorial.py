def tutorial():
    print("its your first day on the job.")
    print("type HELP for a list of commands")
    print("your goal is to fill all your tables by the end of the week")
    print("the market runs on saturday. sunday is your day off")
    print("vendors may apply between monday and thursday")
    print("friday is the day you set up the market.")
    print("random events may occur during the week, or even on the day of the market")
    print("each week you'll have a revenue goal to meet")
    print("i havent thought past that yet lol")

# Tutorial
    if week == 1 and day == 1:
        print("tutorial? (y/n)")
        choice = input("> ").upper()
        while True:
            if choice == "Y":
                tutorial()
            elif choice == "N":
                print("who needs it, right? \n")
                break
            else:
                print("invalid selection")
                print("tutorial? (y/n)")
                choice = input("> ").upper()