import datetime, humanize, random

# datetime is used to calculate the time taken
# humanize is used to make the output more readable
# random is used to generate the list

def getRandomList(length):
    """ Generate a random list of integers between 0 and length, with length length, where length is an integer greater than zero"""
    return [random.randint(0,length) for i in range(length)]

def bubbleSort(l):
    """ Sort the list using a bubble sort algorithm """
    length = len(l)
    swaps=False     # used to detect whether the list is sorted
    for i in range(length):     # run through the list until its sorted
        for j in range(length - i):
            a = l[j]    # set a to current item
            if a != l[-1]:  # if a is not the last item
                b = l[j + 1]    # b is the next item
                if a > b:       # if a is bigger swap the items
                    l[j] = b
                    l[j + 1] = a
                    swaps=True
        # check for a sort
        if not swaps:
            break
    return l

def insertionSort(l):
    """ Sort the list using an insertion sort algorithm """
    newList = []    # create a new list which will be the sorted one
    for item in l:
        newList.append(item)    # add item to new list
        pos=len(newList)-1      # get position of added item
        while newList[pos-1] > newList[pos]:    # when the item is smaller than the one to the left
            newList[pos-1],newList[pos] = newList[pos],newList[pos-1]   # move the item left one
            pos-=1  # keep the focus on the newly added item
            if pos == 0:    # make sure the code doesnt break
                break
    return newList


def getTimeTaken(l,sortType):
    """ Calculates the time taken to sort list l using algorithm sortType """
    print(f"\n\n\tStart time: {datetime.datetime.now()}",end="")    # for some reason it doesnt work if i dont print the values before i store them
                                                                    # dunno why, and i dont care to find out
    startDateTime = datetime.datetime.now() # set value for starttime

    # execute the sort
    if sortType == "bubble":
        bubbleSort(l)
    elif sortType == "insertion":
        insertionSort(l)

    print(f"\tEnd time: {datetime.datetime.now()}")                 # see above
    return datetime.datetime.now() - startDateTime # return difference (will return a timedelta)


def getResults(l,sortType):
    time = getTimeTaken(l,sortType)
    # humanize library is used to make the values more readable/understandable
    print(f"\n\nThe list of {len(l)} random integers took {humanize.time.precisedelta(time)} (or {time}) to complete using the {sortType} sort")


def displayMenu():
    print("\nType in \"exit\" at any input point to exit the program\n\n")
    while True: # while true is used combined with break\sysexit to exit the loops - frees up ram and makes the code look neater
        while True:
            # ask the user which sort to use
            
            print("\nWhich sort would you like to use? (\"bubble\" | \"insertion\")")
            sortType=input("\t").lower()

            # exit check
            if sortType=="exit":
                raise SystemExit

            # error checking
            if sortType in ["bubble","insertion"]:
                break

            print("\nInvalid Input")


        while True:
            # ask the user for the length of the list
            
            print("\nHow many items would you like to have in the list?")
            length=input("\t")
            
            # exit check
            if length=="exit":
                raise SystemExit

            # error checking
            if length.isnumeric():
                break

            print("\nInvalid Input")

        testList = getRandomList(int(length))
    
        getResults(testList.copy(), sortType)   # use testlist.copy() to allow for the list to be sorted multiple times

        while True:
            # ask the user whether they would like to run the other sort on the same list
            
            print("\n\n\nWould you like to test the other sort with the same list? (\"yes\" | \"no\")")
            retry=input("\t").lower()

            # exit check
            if length=="exit":
                raise SystemExit

            # error checking
            if retry in ["yes","no"]:
                break

            print("\nInvalid Input")

        if retry=="yes":
            getResults(testList.copy(), "bubble" if sortType == "insertion" else "insertion")


displayMenu()

