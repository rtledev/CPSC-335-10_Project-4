#Richard Le
#Richard.le@csu.fullerton.edu
#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu
#Jeremy Mejia
#fr.jeremy@csu.fullerton.edu



#Part A: Exhaustive Optimization Approach

from itertools import combinations


def stock_maximization_A (M, items):
    #stores current best stock
    bestStocks = 0
    #Stores best company pairs
    bestSet = []
    
    #Amount of companies
    companies = len(items)

    #try all subsets
    for subset in range(companies + 1):
        
        #generate combinations
        for combos in combinations(range(companies), subset):
            
            totalStocks = 0
            totalCost = 0

            #total stocks and cost for subset
            for i in combos:
                totalStocks += items[i][0]
                totalCost += items[i][1]
            
            #skip if greater than budget
            if totalCost > M:
                continue
            #updates answer for better subset
            if totalStocks > bestStocks:
                bestStocks = totalStocks
                bestSet = list(combos)

    return M,bestSet


    
#Part B: Dynamic Programming Approach
def stock_maximization_B (M, items):

    #table stores best stock values 
    dpTable = [0] * (M + 1 )

    #keeps track of selected companies for budget
    companies = [[] for _ in range(M + 1)]
    
    #loop throuhg each company
    for j, (stock, cost) in enumerate(items):

        #move backwards to prevent use of same item
        for i in range(M, cost -1, -1):

            #stock value and  current company
            amount = dpTable[i - cost] + stock

            #update selected companies if current one is better
            if amount > dpTable[i]:

                dpTable[i] = amount
                companies[i] = companies[i - cost] + [j] 

    
    return M, companies[M]


#example values
stocks = [[1,2], [3,3], [5,6], [6,7]]
cash = 10

#display answers
print(stock_maximization_A(cash, stocks))
print(stock_maximization_B(cash, stocks))