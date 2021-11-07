import pandas as pd

pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df = pd.read_csv("2019/survey_results_public.csv")
schema_df = pd.read_csv('2019/survey_results_schema.csv')

# people = {
#     "first": ["Corey", 'Jane', 'John'],
#     "last": ["Schafer", 'Doe', 'Doe'],
#     "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
# }
#
# df = pd.DataFrame(people)
print(df.loc[0:2, 'Hobbyist':'Employment'])