# Chicago provides a list of taxicab owners and vehicles licensed to operate within the city, for public safety. 
# Your goal is to merge two tables together. One table is called taxi_owners, with info about the taxi cab company owners, 
# and one is called taxi_veh, with info about each taxi cab vehicle. 
# Both the taxi_owners and taxi_veh tables have been loaded for you and you can explore them in the IPython shell.

# Choose the column you would use to merge the two tables on using the .merge() method.

taxi_owners = pd.read_csv('taxi_owners.csv')
taxi_veh = pd.read_csv('taxi_vehicles.csv')

print(taxi_owners.head())
print(taxi_veh.head())

# Answer
# on = 'vid'