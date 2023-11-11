'''

'''


class rental():

    def __init__(self, index):
        self.index = index
                                                                                # funtions for setting up a new property dictionary that will be saved until user enters quit
    def newProperty(self):
        self.stage_one()
        self.stage_two()
        self.stage_three()
        self.cocroi()
        self.propertyIndexGenerator(self.name)
        self.cashFlow(self.name)
        self.roiBreakDown()

    def stage_one(self):
        self.name = input('Please choose a name for the proposed property.\n    Note: Shorter names are best for user convenience.\n ')
        cost = intCheckLoop(input('Enter property value.\n'))
        self.index[self.name] = {'Sale price': cost,}
            

    def stage_two(self):
        self.income = {}
        while True:
            x = input('Enter the income source you would like to add, ie Rent, Laundry, Storage, etc. Or enter "f" to move on.\n')
            if x.lower() == 'f':
                break
            else:
                self.dictGenIncome(x)

    def stage_three(self):
        self.expences = {}
        while True:
            x = input('Enter the expence you would like to add, ie Taxes, Insurance, Utilities, HOA, Lawn Care, etc. Or enter "f" to move on.\n')
            if x.lower() == 'f':
                break
            else:
                self.dictGenExpence(x)

    def cocroi(self):
            self.initial_investment = {}
            self.initial_investment['Down-Payment'] = (intCheckLoop(input('Enter dollar ammount of the down-payment\n')))
            self.initial_investment['Closing Cost'] = (intCheckLoop(input('Enter dollar ammount of the closing costs\n')))
            self.initial_investment['Reports'] = (intCheckLoop(input('Enter dollar ammount of the reports\n')))
            self.initial_investment['Misc.'] = (intCheckLoop(input('Enter dollar ammount of any miscelaneous investment expences\n')))

    def propertyIndexGenerator(self, name):
        self.index[name]['Income'] = self.income
        self.index[name]['Expences'] = self.expences
        self.index[name]['Initial Investment'] = self.initial_investment
        self.index[name]['Cash Flow'] = self.sumFinder(self.index[name]['Income']) - self.sumFinder(self.index[name]['Expences'])
        self.index[name]['Cash-on-cash ROI'] = self.index[name]['Sale price'] - self.sumFinder(self.index[name]['Initial Investment'])

    def cashFlow(self, property):
        print(f"Your monthly cash flow for {property} is expected to be {self.sumFinder(self.index[property]['Income']) - self.sumFinder(self.index[property]['Expences'])}\n")

    def roiBreakDown(self):
        print(f"Your estimated return on investment for property {self.name} is {self.index[self.name]['Cash-on-cash ROI']}")

                                                                                # funtions for referencing and editing saved dictionaries

    
    def propertyList(self):
        print(list(i for i in self.index.keys()))
    
    def viewProperty(self, user_view):
        while True:
            self.propertyList()
            if user_view not in self.index.keys():
                user_view = ("Property does not exist. please check the spelling and case and try again\n")
            else:
                self.propertyBreakDown(user_view)
                self.propertySubMenu(user_view)
                break

    def propertyBreakDown(self, user_view):
        print(self.index[user_view])
        for key, value in self.index[user_view]:
            print(key, value)

    def propertySubMenu(self, user_view):
       while True:
            action = input("Would you like to edit this property?\n"
                        "To edit Sale price, type: Price\n"
                        "To edit Income, type: Income\n"
                        "To edit Expences, type: Expences\n"
                        "To edit Initial Investment, type: Initial\n"
                        "To quit, type: Quit\n")
            
            if action.lower() == "quit":
                break

            elif action.lower() == "price":
                self.index[user_view]['Sale price'] = intCheckLoop(input('Enter property value.\n'))

            elif action.lower() == "income":
                self.stage_two()
                self.index[user_view]['Income'] = self.income

            elif action.lower() == "expences":
                self.stage_three()
                self.index[user_view]['Expences'] = self.expences

            elif action.lower() == "initial":
                self.cocroi()
                self.index[user_view]['Initial Investment'] = self.initial_investment

            else:
                print(f"{action} is not a valid command. please try again")
            

                                                                                # supporting funtions for new property setup process
    def sumFinder(self, dict):
        return sum([i for i in dict.values()])

    def dictGenExpence(self, u_input):
        if u_input not in self.expences.keys():
            self.expences[u_input] = intCheckLoop(input(f'Enter the amount you plan to charge for {u_input}.\n'))
        else:
            oops = input('The expence you have chosen already exists. would you like to change it? Y/N\n')
            if oops.lower() == 'y':
                self.dictGenExpence(input('Enter the expense you would like to add, ie Taxes, Insurance, Utilities, HOA, Lawn Care, etc.\n'))
        
    def dictGenIncome(self, u_input):
        if u_input not in self.income.keys():
            self.income[u_input] = intCheckLoop(input(f'Enter the amount you plan to charge for {u_input}.\n'))
        else:
            oops = input('The source you have chosen already exists. would you like to change it? Y/N\n')
            if oops.lower() == 'y':
                self.dictGenIncome(input('Enter the income source you would like to add, ie Rent, Laundry, Storage, etc.\n'))

    

                                                                                # Universal funtions.... cause I can

def intCheckLoop(user_input):
    while True:
        try:
            x = int(user_input)
            break
        except ValueError:
            user_input = input("Input not valid. Please enter only numbers.")
    return x




rental_liberary = {}
new_rental = rental(rental_liberary)

def run():
    print('Hello, and welcome to Oop calculator, the newest addition to the Oop family. Brought to you by Machine Creations at the request of Coding Temple.')
    while True:
        action = input("What can our automated services do for you?\n"
                       "To create a new rental, type: Create\n"
                       "To see a list of your saved properties, type: Saved\n"
                       "To view and/or edit a saved property, type: View\n"
                       "To quit, type: Quit\n")
        
        if action.lower() == "quit":
            break

        elif action.lower() == "create":
            new_rental.newProperty()

        elif action.lower() == "saved":
            new_rental.propertyList()

        elif action.lower() == "view":
            new_rental.propertyList()
            new_rental.viewProperty(input("\nWhich property would you like to view\n"))


        else:
            print(f"{action} is not a valid command. please try again")
run()
