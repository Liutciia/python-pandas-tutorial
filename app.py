#print("Hello World")

import pandas as pd

#exercise 2:
#data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame)

#exercise 4:
#ages = pd.Series([23,45,7,34,6,63,36,78,54,34])
#print(ages)

#exercise 4.1:
#date_range = pd.date_range(start='2021-05-01',end='2021-05-12')
#print(date_range)

#exercise 4.2: 
#my_series = pd.Series([2, 4, 6, 8, 10])
#def devided(x):
#    return x / 2
#resulted_series = my_series.apply(devided)

#resulted_series = my_series.apply(lambda x: x / 2)
#print(resulted_series)

#exercise 5: 
#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
#dataframe = pd.DataFrame(data,columns=['Brand','Model','Color'])
#print(dataframe)

#exercise 5.1: 
#data = [
#   { 
#        "brand": "Toyota", 
#        "make": "Corolla",
#        "color": "Blue"
#    },
#    {
#        "brand": "Ford", 
#        "make": "K",
#        "color": "Yellow"
#    },
#    {
#        "brand": "Porche", 
#        "make": "Cayenne",
#        "color": "White"
#    },
#    {
#        "brand": "Tesla", 
#        "make": "Model S",
#        "color": "Red"
#    }
#]
#DataFrame = pd.DataFrame(data)
#print(DataFrame)

#exercise 5.2:
#Data_Frame = pd.read_csv(".learn/assets/pokemon_data.csv")
#print(Data_Frame.iloc[133,6])

#exercise 5.3:
#DataFrame = pd.read_csv(".learn/assets/pokemon_data.csv")
#DataFrame = DataFrame.head(3)
#print(DataFrame)

#exercise 5.4:
#DataFrame = pd.read_csv(".learn/assets/pokemon_data.csv")
#DataFrame = DataFrame.tail(3)
#print(DataFrame)

#exercise 5.5:
#data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame[['Name','Type 1']][0:10])

#exercise 5.6:
#data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame.loc[data_frame['Attack'] > 80])

#exercise 5.7:
#data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
#data_frame = data_frame.loc[data_frame['Legendary']]
#num_pokemons = len(data_frame)
#print(num_pokemons)

#exercise 6:
#data_set = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#print(data_set.head(5))

#exercise 6.1:
#data_set = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#data_set = data_set.drop(["Unnamed: 0"],axis=1)
#del data_set["Unnamed: 0"]
#print(data_set.head(5))

#exercise 6.2:
#data_set = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#value_counts = data_set['Gender'].value_counts()
#print(value_counts)

#exercise 6.3:
#data_set = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#data_frame = data_set.groupby("Name").sum()
#num_groups = len(data_frame)
#print(num_groups)
