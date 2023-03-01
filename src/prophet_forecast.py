from data_generator import DataGenerator
from prophet import Prophet
import pandas as pd

# generate the data
data_generator = DataGenerator()
X, y = data_generator.get_data()

# convert the data into a dataframe
df = pd.DataFrame({'ds': X, 'y': y})

print(df.head())