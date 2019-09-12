class Attacker:
    def __init__(self, bs, attacks, mc):
        self.bs = float(bs);
        self.attacks = float(attacks);
        self.mc = float(mc);
    
    def getatData(self):
        return self.bs, self.attacks, self.mc
        
    def getBS(self):
        return self.bs
        
    def getAtt(self):
        return self.attacks
        
    def getMC(self):
        return self.mc