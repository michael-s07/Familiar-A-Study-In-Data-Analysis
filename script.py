# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind

lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

print(lifespans.head())


vein_pack_lifespans = lifespans.lifespan[lifespans.pack=='vein']
print(np.mean(vein_pack_lifespans))

tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print(pval)

artery_pack_lifespans = lifespans.lifespan[lifespans.pack=='artery']
print(np.mean(artery_pack_lifespans))

tstat, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(pval)

print(iron.head())
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)


chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval)
