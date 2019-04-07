import pandas as pd
from itertools import chain



food_data = pd.read_csv(r"/Users/mohitgupta/Food.csv")

RespondentID = list(chain.from_iterable([food_data.iloc[:,0]] * len(range(3,43))))



Cuisines_Knowledge = list(chain.from_iterable([food_data.iloc[:,1]] * len(range(3,43))))




Interest_in_world_cuisines = list(chain.from_iterable([food_data.iloc[:,2]] * len(range(3,43))))



Location = list(chain.from_iterable([food_data.iloc[:,-1]] * len(range(3,43))))



Education = list(chain.from_iterable([food_data.iloc[:,-2]] * len(range(3,43))))





Household_Income = list(chain.from_iterable([food_data.iloc[:,-3]] * len(range(3,43))))




Age = list(chain.from_iterable([food_data.iloc[:,-4]] * len(range(3,43))))



Gender = list(chain.from_iterable([food_data.iloc[:,-5]] * len(range(3,43))))




Rating = []

for i in range(3,43):
    Rating.append(food_data.iloc[:, i])


Rating = list(chain.from_iterable(Rating))




Country = ['Algeria', 'Argentina', 'Australia', 'Belgium', 'Bosnia & Hergovina', 'Brazil', 'Cameroon', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Ecuador',
        'England', 'France', 'Germany', 'Ghana', 'Grees', 'Honduras', 'Iran', 'Italy', 'Ivory Coast', 'Japan', 'Mexico', 'Netherlands',
        'Nigeria', 'Portugal', 'Russia', 'South Korea', 'Spain', 'Switzerland', 'United States', 'Uruguay', 'China', 'India', 'Thailand', 'Turkey',
        'Cuba', 'Ethiopia', 'Vietnam', 'Ireland']


Country = [item for item in Country for i in range(len(food_data.iloc[:,0]))]



final_list = pd.DataFrame(
    {'Respondent ID': RespondentID,
     'Cuisine Knowledge': Cuisines_Knowledge,
     'Interest In World Cuisines': Interest_in_world_cuisines,
     'Country': Country,
     'Rating': Rating,
     'Gender': Gender,
     'Age': Age,
     'Household Income': Household_Income,
     'Education': Education,
     'Location': Location

    })



final_list.to_csv('Food_Data_New.csv', index=None, header=True)





