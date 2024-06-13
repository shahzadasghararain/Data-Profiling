import pandas as pd
from sklearn.impute import SimpleImputer
from pandas_profiling import ProfileReport
df = pd.read_excel('c:/data/cbi.xlsx') 
profile = ProfileReport(df, title="Titanic")
correlations = profile.description_set["correlations"]
print(correlations.keys())