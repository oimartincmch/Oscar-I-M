# COGS 18 FINAL PROJECT: BigChat
## Oscar Isaac Martinez
#BigChat is a chatbot that takes in 5 different function inputs (name, state, age, project, and end_chat). The interactive chatbot is responsive to my name, Prof. Ellis, and any TA or IA. From there, you will be asked what state you are from, and the chatbot will respond with the nickname for the respective state. Next, you will be asked your age. If 21 as I am, the chatbot will respond "Cheers!". Otherwise, it will resond "Nice!" and proceed to ask if you have started your COGS 18 project. If you have, it will congratulate you and loop back to the first question. If you have not finished your project, it will ask if you have started. If you have, BigChat will congratulate you. If you have not, BigChat will urge you to get started, then loop back to the first question. At this point, if you are done using BigChat, you can type 'quit' to end the chat, and you will receive a farewell from BigChat. I hope you enjoy this project, and I want to thank Professor Ellis and all the TAs for everything this quarter. 

def name_question():
    """Asks for name, takes input if valid, greets you with a Hi! If not Isaac/Prof. Ellis/TA/IA, will respond negatively."""
    stop = False
    print("\nWelcome to BigChat!:")
    while stop == False:
        inputStr = input("What's your name?")
        inputStr = inputStr.lower()
        if (inputStr == "oscar"):
            print("Hi Oscar!")
            stop = True
            
        elif (inputStr == "isaac"):
            print("Hi Isaac!")
            stop = True
            
        elif (inputStr == "shannon"):
            print("Hi Shannon!")
            stop = True
            
        elif (inputStr == "devendra"):
            print("Hi Devendra!")
            stop = True
            
        elif (inputStr == "shreenivas"):
            print("Hi Shreenivas!")
            stop = True
            
        elif (inputStr == "andrew"):
            print("Hi Andrew!")
            stop = True
            
        elif (inputStr == "chau"):
            print("Hi Chau")
            stop = True
            
        elif (inputStr == "duolan"):
            print("Hi Duolan!")
            stop = True
            
        elif (inputStr == "byungkwon"):
            print("Hi Byungkwon!")
            stop = True
            
        elif (inputStr == "sarah"):
            print("Hi Sarah!")
            stop = True
            
        elif (inputStr == "titan"):
            print("Hi Titan!")
            stop = True
            
        elif (inputStr == "zijian"):
            print("Hi Zijian!")
            stop = True
            
        elif (inputStr == "severine"):
            print("Hi Severine!")
            stop = True
            
        elif (inputStr == "stephen"):
            print("Hi Stephen!")
            stop = True
            
        else:
            print("\tNot Authorized to Use BigChat!")

def state_question():
    """Asks for what state you are from, and will return the national nickname of whatever state input is given."""
    stop = False
    while stop == False:
        inputStr = input("What state are you from?")
        inputStr = inputStr.lower()
        if (inputStr == "alabama"):
            print("The Yellowhammer State!")
            stop = True
        elif (inputStr == "alaska"):
            print("The Last Frontier!")
            stop = True
        elif (inputStr == "arizona"):
            print("The Grand Canyon State!")
            stop = True
        elif (inputStr == "arkansas"):
            print("The Natural State!")
            stop = True
        elif (inputStr == "california"):
            print("The Golden State!")
            stop = True
        elif (inputStr == "colorado"):
            print("The Centennial State!")
            stop = True
        elif (inputStr == "connecticut"):
            print("The Constitution State!")
            stop = True
        elif (inputStr == "delaware"):
            print("The First State!")
            stop = True
        elif (inputStr == "florida"):
            print("The Sunshine State!")
            stop = True
        elif (inputStr == "georgia"):
            print("The Peach State!")
            stop = True
        elif (inputStr == "hawaii"):
            print("The Aloha State!")
            stop = True
        elif (inputStr == "idaho"):
            print("The Gem State!")
            stop = True
        elif (inputStr == "illinois"):
            print("The Prairie State!")
            stop = True
        elif (inputStr == "indiana"):
            print("The Hoosier State!")
            stop = True
        elif (inputStr == "iowa"):
            print("The Hawkeye State!")
            stop = True
        elif (inputStr == "kansas"):
            print("The Sunflower State!")
            stop = True
        elif (inputStr == "kentucky"):
            print("The Bluegrass State!")
            stop = True
        elif (inputStr == "louisiana"):
            print("The Pelican State!")
            stop = True
        elif (inputStr == "maine"):
            print("The Pine Tree State!")
            stop = True
        elif (inputStr == "maryland"):
            print("The Old Line State!")
            stop = True
        elif (inputStr == "massachusetts"):
            print("The Bay State!")
            stop = True
        elif (inputStr == "michigan"):
            print("The Great Lakes State!")
            stop = True
        elif (inputStr == "minnesota"):
            print("The North Star State!")
            stop = True
        elif (inputStr == "mississippi"):
            print("The Magnolia State!")
            stop = True
        elif (inputStr == "missouri"):
            print("The Show Me State!")
            stop = True
        elif (inputStr == "montana"):
            print("The Treasure State!")
            stop = True
        elif (inputStr == "nebraska"):
            print("The Cornhusker State!")
            stop = True
        elif (inputStr == "nevada"):
            print("The Silver State!")
            stop = True
        elif (inputStr == "new Hamsphire"):
            print("The Granite State!")
            stop = True
        elif (inputStr == "new Jersey"):
            print("The Garden State!")
            stop = True
        elif (inputStr == "new Mexico"):
            print("The Land of Enchantment!")
            stop = True
        elif (inputStr == "new York"):
            print("The Empire State!")
            stop = True
        elif (inputStr == "north Carolina"):
            print("The Tar Heel State!")
            stop = True
        elif (inputStr == "north Dakota"):
            print("The Peace Garden State!")
            stop = True
        elif (inputStr == "ohio"):
            print("The Buckeye State!")
            stop = True
        elif (inputStr == "oklahoma"):
            print("The Sooner State!")
            stop = True
        elif (inputStr == "oregon"):
            print("The Beaver State!")
            stop = True
        elif (inputStr == "pennsylvania"):
            print("The Keystone State!")
            stop = True
        elif (inputStr == "rhode Island"):
            print("The Ocean State!")
            stop = True
        elif (inputStr == "south Carolina"):
            print("The Palmetto State!")
            stop = True
        elif (inputStr == "south Dakota"):
            print("The Mount Rushmore State!")
            stop = True
        elif (inputStr == "tennesee"):
            print("The Volunteer State!")
            stop = True
        elif (inputStr == "texas"):
            print("The Lone Star State!")
            stop = True
        elif (inputStr == "utah"):
            print("The Beehive State!")
            stop = True
        elif (inputStr == "vermont"):
            print("The Green Mountain State!")
            stop = True
        elif (inputStr == "virginia"):
            print("The Old Dominion State!")
            stop = True
        elif (inputStr == "washington"):
            print("The Evergreen State!")
            stop = True
        elif (inputStr == "west Virginia"):
            print("The Mountain State!")
            stop = True
        elif (inputStr == "wisconsin"):
            print("The Badger State!")
            stop = True
        elif (inputStr == "wyoming"):
            print("The Equality/Cowboy State!")
            stop = True
        else:
            print("\tI don't recognize that state, try again!")

def age_question():
    """Asks for age input, will respond 'Nice!' to any input other than an empty string, as well as alternatively resonding 'Cheers!' if 21"""
    stop = False
    while stop == False:
        inputStr = input("How old are you?")
        if (inputStr == "21"):
            print("Cheers!")
            stop = True
        elif (inputStr == ''):
            print("Try again!")
        else:
            print("Nice!")
            stop = True

def proj_question():
    """Asks for project completion. Congratulates you if have finished or have started. If have not finished, different output. If have not started, another output."""
    stop = False
    qstr = "Have you finished your project?"
    while stop == False:
        inputStr = input(qstr)
        inputStr = inputStr.lower()
        if (inputStr == "yes"):
            print("Congratulations!")
            stop = True
        elif (inputStr == "no"):
            qstr = "Well have you started?"
            if input(qstr) == "no":
                print("You better get on that!")
                stop = True
            else:
                print("Great! Keep working, but remember to make time for yourself!")
                stop = True
        else:
            print("\tTry again")

def end_chat(inputStr):
    """Ends chat if 'quit' is in input string. Can only quit upon initial 'INPUT:'"""
    #some inspiration from Professor Ellis's A3. UCSD Fall 2019.
    if 'quit' in inputStr:
        output = True
    else:
        output = False
    return output

def big_chat():
    """Main function to run chatbot. Prints farewell messageif quitting."""
    #some inspiration from Professor Ellis's A3. UCSD Fall 2019.
    chat = True
    while chat:
        msg = input('INPUT :\t')
        out_msg = None
        
        if end_chat(msg): 
            out_msg = 'Bye! I hope you enjoyed using BigChat!'
            print('Bye! I hope you enjoyed using BigChat!')
            chat = False
            break
        name_question()
        state_question()
        age_question()
        proj_question()