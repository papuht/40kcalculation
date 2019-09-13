class Attacker:
    def __init__(self, name, str, damage, ap, bs, attacks, mc):
        #self.name = name;   #Asetettu komenteiksi toistaiseksi jotta eivät tekisi vielä mitään
        #self.str = float(str);
        #self.damage = float(damage);
        #self.ap = float(ap);
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