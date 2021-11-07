import pandas as pd

pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

#df = pd.read_csv("2019/survey_results_public.csv")
schema_df = pd.read_csv('2019/survey_results_schema.csv')

print(schema_df)