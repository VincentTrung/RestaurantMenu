from datetime import date  #for date

#Hardcoded Menu data
tipAmount = [0, 0.10, 0.15]
Item = ['Cookies', 'Croissont', 'Coffee', 'Muffin', 'Bagel']
Menu = {
    '1': 1,
    '2': 2.25,
    '3': 1.75,
    '4': 3.75,
    '5': 2.50,
    Item[0]: 1,
    Item[1]: 2.25,
    Item[2]: 1.75,
    Item[3]: 3.75,
    Item[4]: 2.50,
}


def showAbout():
    """show logo and menu aswell as instructions to order"""
    print("""
__________        __  .__                         
\______   \ _____/  |_|  |__  __ __  ____   ____  
 |    |  _// __ \   __\  |  \|  |  \/    \_/ __ \ 
 |    |   \  ___/|  | |   Y  \  |  /   |  \  ___/ 
 |______  /\___  >__| |___|  /____/|___|  /\___  >
        \/     \/          \/           \/     \/  
                  
  """)
    print("""Welcome to Bethune's Bear Cafe 
Please type the products you would like to eat, up to a limit of 5 choice dishes.
To complete your order, please type EXIT""")
    print("""
  ~Bethune's Bear Cafe~
  ---------------------------- """)
    print("  1.", Item[0], (15 - len(Item[0])) * '-', "$", Menu['1'])
    print("  2.", Item[1], (15 - len(Item[1])) * '-', "$", Menu['2'])
    print("  3.", Item[2], (15 - len(Item[2])) * '-', "$", Menu['3'])
    print("  4.", Item[3], (15 - len(Item[3])) * '-', "$", Menu['4'])
    print("  5.", Item[4], (15 - len(Item[4])) * '-', "$", Menu['5'])
    print("  ----------------------------")
    print('')


#Loop for however
def askInput():
    allPrices = []

    try:  #collect items they want
        for i in range(5):
            index = input()
            if index == "EXIT":
                break
            prices = Menu[index]
            if isinstance(int(index), int):
                print(Item[int(index) - 1])
            allPrices.append(prices)
    except:  #end if error
        print(
            "Please reorder again, make sure you entered your items either by the number or in the correct spelling above."
        )
        quit()

    #calculate the costs of all the prices
    mealCost = 0
    for i in range(len(allPrices)):
        if allPrices[i] == "EXIT":
            break
        mealCost += float(allPrices[i])
    return mealCost


def calcTax(bill):
    """Adds 13% tax to a restaurant bill."""
    bill *= 0.13
    return bill


def calcTip(bill):
    """Adds tip to a restaurant bill after tax"""
    #present tip options
    print("")
    print("-" * 30)
    print("1. ", (tipAmount[0] * 100), "%")
    print("2. ", (tipAmount[1] * 100), "%")
    print("3. ", (tipAmount[2] * 100), "%")
    print("-" * 30)

    #ask how much tip and calculate
    askTip = float(input("Choose from one of the options how much you'd like to tip: "))
    print('')
    if askTip == 1:
        return (tipAmount[0] * bill)
    elif askTip == 2:
        return (tipAmount[1] * bill)
    elif askTip == 3:
        return (tipAmount[2] * bill)


def showReceipt(mealCost):
    """Displays the receipt in a User friendly format with the tax, tip and total."""
    #calculations
    Tax = calcTax(mealCost)
    Tip = calcTip(Tax + mealCost)
    Total = Tax + Tip + mealCost
    #format and display information
    print("""
  
  


  """)
    print('------------------------------')
    print("Receipt printed   ", date.today())  #display the date
    print("""------------------------------
      "Bethune Café"
------------------------------""")
    #format number to 2 decimals
    print("Subtotal: ", format(mealCost, '.2f'))
    print("Tax: ", format(Tax, '.2f'))
    print("Tip: ", format(Tip, '.2f'))
    print("Total: ", format(Total, '.2f'))
    print("""
----------------------
**********************
Thank you for visiting
**********************
""")