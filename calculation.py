

def calculateHits(bs, attacks, amodels, rerollHit):
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
    misses = float((attacks * amodels) - numberOfHits)
    
    if rerollHit == 1:
        totalHits = float(numberOfHits + (misses*float(1/6)))
    elif rerollHit == 2:
        totalHits = float(numberOfHits + (misses * chanceToHit))
    elif rerollHit == 3:
        totalHits = numberOfHits
    return totalHits
                   
    
def calculateWounds(numofhits, str, tough, rerollWound):
    if str == tough:
        chanceToWound = float(1/2)
    elif str - tough == 1:
        chanceToWound = float(2/3)
    elif str - tough == 2:
        chanceToWound = float(2/3)
    elif str - tough == -1:
        chanceToWound = float(1/3)
    elif str - tough == -2:
        chanceToWound = float(1/3)
    elif str >= (2*tough): 
        chanceToWound = float(5/6)
    elif tough >= (2*str):
        chanceToWound = float(1/6)
        
    numberOfWounds = float(numofhits * chanceToWound)
    fails = float(numofhits - numberOfWounds)
    
    if rerollWound == 1:
        totalWounds = float(numberOfWounds + (fails*float(1/6)))
    elif rerollWound == 2: 
        totalWounds = float(numberOfWounds + (fails * chanceToWound))
    elif rerollWound == 3:
        totalWounds = numberOfWounds
     
    return totalWounds

def normalSave(numofWounds, armor, ap):
		if (armor + ap) <= 2:
			chanceToSave = float(5/6)
		elif (armor + ap) == 3:
			chanceToSave = float(2/3)
		elif (armor + ap) == 4:
			chanceToSave = float(1/2)
		elif (armor + ap) == 5:
			chanceToSave = float(1/3)
		elif (armor + ap) == 6:
			chanceToSave = float(1/6)
			
		numberOfSaves = float(chanceToSave * numofWounds)
		
		return numberOfSaves

def invuSave(numofWounds, invu):
		if invu <= 2:
			chanceToSave = float(5/6)
		elif invu == 3:
			chanceToSave = float(2/3)
		elif invu == 4:
			chanceToSave = float(1/2)
		elif invu == 5:
			chanceToSave = float(1/3)
		elif invu == 6:
			chanceToSave = float(1/6)
		
		numberOfSaves = float(chanceToSave * numofWounds)

		return numberOfSaves
	

def calculateSaveType(numofWounds, armor, invu, ap):
	if invu <= 1:
		saves = normalSave(numofWounds, armor, ap)
	elif armor + ap < invu:
		saves = normalSave(numofWounds, armor, ap)
	elif armor + ap > invu:
		saves = invuSave(numofWounds, invu)
	elif armor + ap == invu:
		saves = invuSave(numofWounds, invu)
		
	return saves
	

def calculateDamage(numofWounds, damage, saves):
    tempoutcome = float(damage * (numofWounds - saves))
    
    return tempoutcome
	
def calculateFNP(tempoutcome, fnp):
    if fnp <= 1:
        chanceToNull = 0
    elif fnp == 2:
        chanceToNull = float(5/6)
    elif fnp == 3:
        chanceToNull = float(2/3)
    elif fnp == 4:
        chanceToNull = float(1/2)
    elif fnp == 5: 
        chanceToNull = float(1/3)
    elif fnp == 6:
        chanceToNull = float(1/6)
    
    
    finalResult = float(tempoutcome * chanceToNull)
        
    return finalResult
	
	
	