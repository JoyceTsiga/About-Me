#assume 7% sales tax
def tax(taxamount,subtotal):
    theTotalAmount = subtotal*(1+taxamount/100)
    #theTotalAmount = 20     *(1+7/100)
    return theTotalAmount

#tipAmount is in integer form
def tip(tipAmount,subtotal):
    theTotalAmount = subtotal+tipAmount/100*subtotal
    return theTotalAmount

'''
    pizzaCost:
    s,m,l,xl, = 3,4,5,6
    sauce = .50
    toppings = .50 ea
'''

def pizzaCost(size,sauceFromUser,listOfToppings):
    #This list of variables equals this list of numbers
    sizeList     =  ["s","m","l","xl"]
    sizeCostList =  [3,4,5,6]
    sauce = .50
    toppings = .50
    totalCost=0
    #added in the size cost
    if size in sizeList:
        i=sizeList.index(size)      #finding the index of the size
        totalCost+=sizeCostList[i]  #pulling info
        #reduces lines 34 and 35 into 1 line
        #totalCost+=sizeCostList[sizeList.index(size)]
    #added in the sauce cost
    if sauceFromUser != "no":
        totalCost+=sauce
    #added in toppings cost
    totalCost+=len(listOfToppings)*.50
    #print(totalCost)
    return totalCost

#print(pizzaCost("m","mustard",["bacon","bacon","bacon","sausage","peps"]))

#orderpizaa is a void because it isn't return, so let's return something.
def orderPizza():
    name = input("What is your pizza's name? ")
    size = input("What is the size of your pizza? ")
    crust = input("What kind of crust do you want? ")
    sauce = input("What kind of sauce do you want? ")
    listOfToppings=[]
    ui = input("Done for no toppings or list toppings you want? ")
    #while the user is not done ordering
    while(ui != "done"):             #conditinal = ui does not equal "done"
        listOfToppings.append(ui)
        ui = input("Done for no toppings or list toppings you want? ")        
    print(f'''you ordered a {name} pizza
                the {size}
                with {crust}
                with {sauce}
                with these toppings:''')
    #since I'm not mutsting or resting the items... I can just use a for i in list:        
    for i in listOfToppings:
        print("\t\t"+i)

        return name,size,crust,sauce,listOfToppings     #returing a tuple

#calling to order a pizza
# when you call to order a pizza, you and the other person pick up the phone
# in python that means say the name pcik up your left(
# and the other person will pick up the right)
                            
def makingThePizza(name,size,crust,sauce,listOfToppings):
    pizza=f'''
    the name {name}
        the size {size}
        the crust {crust}
        the sauce {sauce}
        the toppings {listOfToppings}'''
    return pizza

#access items in a list     list[]
#access items in a tuples   tuples[]
#access items in a string   string[]
#name=orderPizza[0]
#size=orderPizza[1]
#etc....

'''
thePizzaIOrdered=orderPizza()  #the () are a data type = 
thePizza=makingThePizza(thePizzaIOrdered[0],thePizzaIOrdered[1],thePizzaIOrdered[2],thePizzaIOrdered[3],thePizzaIOrdered[4])
print(thePizza)
theTotalCostOfThePizza=pizzaCost(thePizzaIOrdered[1],thePizzaIOrdered[3],thePizzaIOrdered[4])
print(theTotalCostOfThePizza)
taxTotal=tax(7, theTotalCostOfThePizza)
tipTotal=tip(10,taxTotal)
print(taxTotal)
print(tipTotal)
'''

theOrder=[]
thePizzas=[]
ui=input("Welcome to Pizza the Hut, can I take your order? ")
while(ui!="stop"):
    theOrder.append(orderPizza())
    ui=input("Do you want another pizza? ")
for i in range(len(theOrder)):
    thePizzas.append(makingThePizza(theOrder[i][0],theOrder[i][1],theOrder[i][2],theOrder[i][3],theOrder[i][4]))
print(theOrder)
print(thePizzas)

def finalCost(size,sauceFromUser,listOfToppings,subtotal,taxAmount,tipAmount):
    cost=0
    sizeList     =  ["s","m","l","xl"]
    sizeCostList =  [3,4,5,6]
    sauce=.50
    listOfToppings=.50
    if size in sizeList:
        i=sizeList.index(size)     
        cost+=sizeCostList[i]
    if sauceFromUser != "no":
       cost+=sauceFromUser
    cost+=len(listOfToppings)*.50
    tax = subtotal*(1+taxAmount/100)
    tip = subtotal+tipAmount/100*subtotal
    cost+=tip
    cost+=tip
print("cost")






'''
def functionName(WhenYouNeedinfoFromOtherPartsOfTheProgram):
    print("hi")
    return "hi"   #return stops the function and gives that info back to the program
variableToholdTheReturnInfo=functionName("Something in here, yes I know we don't use, but I need something")
print(variableToholdTheReturnInfo)
'''


