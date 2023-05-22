# Dictionary holding what each person is associating with
classList = {
}
def getNames():#returns a list of available names from the dictionary named classList
    names = ""
    for i in classList.keys():
        names = names + ", " + i
    return names

print("Input the keyword break whenever you would like to move on to the next section")

def getVotes():# Asks user for their vote by asking for name followed by a comma and then if they like savory, sweet or salty
    # This is then filtered, split, and then put into the classlist
    while True:
        inputRaw = input("Please write your name first, a comma, then if you prefer savory, sweet or salty: ")
        if "break" in inputRaw.lower():
            break
        if "," in inputRaw:
            inputSplit = inputRaw.split(",")
            if (len(inputSplit) == 2):
                classList[inputSplit[0].lower()] = inputSplit[1].lower()
            else:
                print("You may only use one comma")
        else:
            print("Please enter a name followed by a comma, then if you like salty, savory, or sweet")
def requestVotes():#This is run after all voting is done. It will show all results from polling
    getListForNames = list(classList.keys())
    while True:
        inp = input("How do you want to read, 1 if by number, 2 if by name:")
        if inp == "1":
            inputRaw = int(input("Who do you want to know about: "))
            if len(getListForNames) >= inputRaw:
                print(classList.get(getListForNames[inputRaw - 1]))
            else:
                print("You need to give a number that is within the list")
        elif inp.lower() == 'break':
            break
        elif inp == "2":
            names = getNames()
            print("The following are the available names: ")
            print(names)
            inputRaw = input("Who do you want to know about: ")
            if inputRaw.lower() in classList:
                print(classList.get(inputRaw.lower()))
            else:
                print("Type in a name that is available")
        else:
            print("Please put either break, 1 or 2")
    return getListForNames
def returnInfo():#This formats and returns information in a more legible and usable format
    getListForNames = requestVotes()
    salty = 0
    sweet = 0
    savory = 0
    other = []
    for i in getListForNames:
        current = classList.get(i)
        if "sweet" in current.lower():
            sweet += 1
            classList.pop(i)
        elif "salty" in current.lower():
            salty += 1
            classList.pop(i)
        elif "savor" in current.lower():
            savory += 1
            classList.pop(i)
        else:
            other.append(i)
            other.append(classList.get(i))
    print("Salty: ", salty)
    print("Savory: ", savory)
    print("Sweet: ", sweet)
    print("Other: ", other)
    for i in classList.keys():
        print(i + " put in "+ classList.get(i))


getVotes()
returnInfo()