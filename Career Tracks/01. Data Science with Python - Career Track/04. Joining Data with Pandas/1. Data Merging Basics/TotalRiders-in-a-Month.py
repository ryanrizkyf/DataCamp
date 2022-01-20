# Your goal is to find the total number of rides provided to passengers passing through the Wilson station (station_name == 'Wilson'), 
# when riding Chicago's public transportation system on weekdays (day_type == 'Weekday') in July (month == 7). 
# Luckily, Chicago provides this detailed data, but it is in three different tables. 
# You will work on merging these tables together to answer the question. 
# This data is different from the business related data you have seen so far, 
# but all the information you need to answer the question is provided.

# The cal, ridership, and stations DataFrames have been loaded for you. 
# The relationship between the tables can be seen in the diagram below.

# Instructions
# Merge the ridership and cal tables together, starting with the ridership table on the left and save the result to the variable ridership_cal. 
# If you code takes too long to run, your merge conditions might be incorrect.
# Extend the previous merge to three tables by also merging the stations table.
# Create a variable called filter_criteria to select the appropriate rows from the merged table so that you can sum the rides column.

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal)

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations)

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())
