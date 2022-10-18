import numpy as np
from scipy.stats import norm
from bce import opciok

opt=Option("C",100,"20221215",1)
print(opt.calcPayoff(120))