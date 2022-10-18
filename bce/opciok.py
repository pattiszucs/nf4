from scipy.stats import norm
import numpy as np

class Option:
    def __init__(self,right:str,strike:float,expiry,pos:int):
        self.right=right #call or pt
        self.pos=pos
        self.strike=strike
        self.expiry=expiry
        self.vola=np.nan

    def initVola(self):
        self.Vola=0.2

    def calcPrice(self, S: float, timeToExp: float, vola: float, rate=0):
        #timeToExp: hány év múlva jár le
        if not np.isnan(vola):
            IV = vola
        else:
            IV = self.vola if not np.isnan(self.vola) else self.initVola
        if np.isnan(IV):
            print("Vola is not set!")
            return np.nan
        t = timeToExp
        if t > 0:
            d1 = (np.log(S / self.strike) + (rate + IV ** 2 / 2) * t) / (IV * np.sqrt(t))
            d2 = d1 - IV * np.sqrt(t)
            if self.right == 'C':
                return (S * norm.cdf(d1) - norm.cdf(d2) * self.strike * np.exp(-rate * t)) * self.pos
            else:
                return (norm.cdf(-d2) * self.strike * np.exp(-rate * t) - S * norm.cdf(-d1)) * self.pos
        elif t == 0:
            return self.calcPayoff(S)
        else:
            print("expired!")
            return np.nan


    def calcPayoff(self,spot)->float:
        if self.right=="C":
            return max(spot-self.strike,0)*self.pos
        elif self.right=="P":
            return max(self.strike-spot,0)*self.pos
        else:
            print("Wrong option type")
            return None

