# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Requirement 1
best_math_schools = schools[schools['average_math'] >= 640][['school_name', 'average_math']].sort_values('average_math', ascending=False)
# Requirement 2
schools["total_SAT"] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values("total_SAT", ascending=False).iloc[0:10]
# Requirement 3
#num_schools = schools.groupby('borough')['school_name'].count().reset_index(name="num_schools")
schools_gb_borough = schools.groupby('borough').agg(num_schools = ("school_name", "count"), average_SAT = ("total_SAT", "mean"), std_SAT = ("total_SAT", "std")).reset_index().round(2)
largest_std_dev = schools_gb_borough[schools_gb_borough['std_SAT'] == schools_gb_borough['std_SAT'].max()]
