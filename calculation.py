

def calculateHits(bs, attacks, amodels):
    if bs <= 2:
        chanceToHit = float(5/6)
    elif bs == 3:
        chanceToHit = float(2/3)
    elif bs == 4:
        chanceToHit = float(1/2)
    elif bs == 5:
        chanceToHit = float(1/3)
    elif bs == 6:
        chanceToHit = float(1/6)
    else:
        chanceToHit = float(0)

    numberOfHits = float(attacks * amodels * chanceToHit)
            
    return numberOfHits
                   
    
def calculateWounds(numofhits, str, tough):
    if str == tough:
        chanceToWound = float(1/2)
    elif (str - tough) == 1:
        chanceToWound = float(2/3)
    elif (str - tough) == -1:
        chanceToWound = float(1/3)
    elif str >= (2*tough): 
        chanceToWound = float(5/6)
    elif tough >= (2*str):
        chanceToWound = float(1/6)
        
    numberOfWounds = float(numofhits * chanceToWound)
     
    return numberOfWounds