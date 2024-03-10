# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, "drives_right"])


# Print out drives_right column as DataFrame
print(cars.iloc[:, [-1]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0, -1]])
