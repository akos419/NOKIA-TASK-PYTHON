print("""---------MENU FUNCTIONS----------
1.PHONE BOOK
2.MESSAGES
3.CHAT
4.CALL REGISTER
5.TONES
6.SETTINGS
7.CALL DIVERT
8.MUSIC
9.GAMES
10.CALCULATOR
11.REMINDERS
12.CLOCK
13.PROFILES
14.SERVICES
15.SIM SERVICES
""")
print("Enter your choice here: ")
choice = int(input())

match choice:
    case 1:
        print("""-------PHONE BOOK OPTIONS------
1.SEARCH
2.SERVICE NOS.
3.ADD NAME
4.ERASE
5.EDIT
6.COPY
7.ASSIGN TONE
8.EDIT B'CARD
9.OPTIONS
10.SPEED DIALS
11.VOICE TAGS
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("Number searched successfully")
            case 2:
                print("07036322837")
            case 3:
                print("Name=Kamdilinna Akosionu")
            case 4:
                print("Number erased successfully")
            case 5:
                print("Numbers edited successfully")
            case 6:
                print("Number copied successfully")
            case 7:
                print("Tone assigned successfully")
            case 8:
                print("B'day card sent successfully")
            case 9:
                print("""------OPTIONS MENU------
1.MEMORY IN USE
2.TYPE OF VIEW
3.MEMORY STATUS
""")
                print("Enter your choice here: ")
                choice = int(input())
                match choice:
                    case 1:
                        print("Memory in use checked successfully")
                    case 2:
                        print("Type of view checked successfully")
                    case 3:
                        print("Memory status checked successfully")
            case 10:
                print("Speed dials checked successfully")
            case 11:
                print("Voice tags checked successfully")

    case 2:
        print("""--------MESSAGES MENU------
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("Message written successfully")
            case 2:
                print("Inbox entered successfully")
            case 3:
                print("Outbox entered successfully")
            case 4:
                print("Picture messages entered")
            case 5:
                print("Templates entered")
            case 6:
                print("Smileys entered")
            case 7:
                print("""---------MESSAGE SETTINGS-------
1.SET 1
2.COMMON
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("""---------SET 1 SETTINGS-------
1.Message centre number
2.Message sent as
3.Message validity
""")
                        print("Enter your choice here: ")
                        choice = int(input())

                        match choice:
                            case 1:
                                print("Message number centre checked")
                            case 2:
                                print("Messages sent as...")
                            case 3:
                                print("Message validity checked")
                    case 2:
                        print("""---------COMMON SETTINGS-------
1.Delivery reports
2.Reply via the same centre
3.Character support
""")
                        print("Enter your choice here: ")
                        choice = int(input())

                        match choice:
                            case 1:
                                print("Delivery reports opened")
                            case 2:
                                print("You have replied with the same centre")
                            case 3:
                                print("Character support provided")
            case 8:
                print("Info service provided")
            case 9:
                print("Voice mailbox number checked")
            case 10:
                print("Service command editor checked")

    case 3:
        print("Chat opened successfully")

    case 4:
        print("""--------CALL REGISTER MENU------
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call list
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("Missed calls checked")
            case 2:
                print("Received calls checked")
            case 3:
                print("Dialled numbers checked")
            case 4:
                print("Recent call list erased")
            case 5:
                print("""---------CALL DURATION OPTIONS-------
1.Last call duration
2.All calls' duration
3.Received calls' duration
4.Dialled calls' duration
5.Clear timers
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("Last call duration checked")
                    case 2:
                        print("All calls' duration checked")
                    case 3:
                        print("Received calls' duration checked")
                    case 4:
                        print("Dialled calls' duration checked")
                    case 5:
                        print("Timers cleared")
            case 6:
                print("""---------CALL COST OPTIONS-------
1.Last call cost
2.All calls' cost
3.Clear counters
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("Last call cost checked")
                    case 2:
                        print("All calls' cost checked")
                    case 3:
                        print("Counters cleared")
            case 7:
                print("""---------CALL COST SETTINGS-------
1.Call cost limit
2.Show costs in
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("Call cost limit configured")
                    case 2:
                        print("Costs showed")
            case 8:
                print("Prepaid credit cecked")

    case 5:
        print("""--------TONES MENU------
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("Ringing tone set")
            case 2:
                print("Ringing volume set")
            case 3:
                print("Incoming call tone set")
            case 4:
                print("Message alert tone set")
            case 5:
                print("Keypad tone set")
            case 6:
                print("Warning tone set")
            case 7:
                print("Vibrating alert tone set")
            case 8:
                print("Screen saver set")

    case 6:
        print("""--------SETTINGS MENU------
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("""---------CALL SETTINGS OPTIONS-------
1.Automatic redial
2.Speed dialling
3.Call waiting options
4.Own number sendng
5.Phone line in use
6.Automatic answer
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("Automatic redial configured")
                    case 2:
                        print("Speed dialling configured")
                    case 3:
                        print("Call waiting options selected")
                    case 4:
                        print("Own number sent")
                    case 5:
                        print("Phone line to use selected")
                    case 6:
                        print("Automatic answer chosen")
            case 2:
                print("""---------PHONE SETTINGS OPTIONS-------
1.Language
2.Cell info display
3.Welcome note
4.Network selection
5.Confirm SIM service actions
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("Language chosen")
                    case 2:
                        print("Cell info display configured")
                    case 3:
                        print("Welcome note set")
                    case 4:
                        print("Network selected")
                    case 5:
                        print("SIM service actions confirmed")
            case 3:
                print("""---------SECURITY SETTINGS OPTIONS-------
1.PIN code request
2.Call barring service
3.Fixed dialling
4.Closed user group
5.Security level
6.Change access codes
""")
                print("Enter your choice here: ")
                choice = int(input())

                match choice:
                    case 1:
                        print("PIN code provided")
                    case 2:
                        print("Call barring service activated")
                    case 3:
                        print("Fixed dialling activated")
                    case 4:
                        print("Closed user group set")
                    case 5:
                        print("Security level determined")
                    case 6:
                        print("Access codes changed")
            case 4:
                print("Factory settings restored")

    case 7:
        print("Call divert setting has been activated")

    case 8:
        print("""--------MUSIC MENU------
1. Music player
2. Radio
3. Recorder
4. Track list
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("Music player opened")
            case 2:
                print("Radio opened")
            case 3:
                print("Recorder opened")
            case 4:
                print("Track list made")

    case 9:
        print("NOKIA games are opened")

    case 10:
        print("Phone calculator has been activated")

    case 11:
        print("Reminders have been set")

    case 12:
        print("""--------CLOCK MENU------
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
""")
        print("Enter your choice here: ")
        choice = int(input())

        match choice:
            case 1:
                print("Alarm clock opened")
            case 2:
                print("Clock settings opened")
            case 3:
                print("Date settings opened")
            case 4:
                print("Stopwatch opened")
            case 5:
                print("Countdown timer opened")
            case 6:
                print("Date and time updated automatically")

    case 13:
        print("You have entered the Profiles dashboard")

    case 14:
        print("You have entered the Services dashboard")

    case 15:
        print("You have entered the SIM Services dashboard")
