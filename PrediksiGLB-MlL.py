import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt

# Reading data from the file
FileDB = r"C:\Users\asus\Downloads\data_GL.txt"
Database = pd.read_csv(FileDB, sep=";")

# Check Column Names
print("Column Names in DataFrame:", Database.columns)

# Remove leading spaces from column names
Database.columns = Database.columns.str.strip()

# Verify and Select Columns
if 't' in Database.columns and 'Position' in Database.columns and 'Velocity' in Database.columns:
    # Separating data and target
    X = Database[['t']]
    y = Database[['Position', 'Velocity']]

    # Giving names to features in X
    X.columns = ['t']

    # Creating SVR model for Position
    clf_position = svm.SVR()
    clf_position.fit(X, y['Position'])

    # Creating SVR model for Velocity
    clf_velocity = svm.SVR()
    clf_velocity.fit(X, y['Velocity'])

    # Making predictions for some specific time values
    time_values = np.linspace(0, 2.4, 10).reshape(-1, 1)
    predictions_position = clf_position.predict(time_values)
    predictions_velocity = clf_velocity.predict(time_values)

    # Creating subplot with 2 rows and 2 columns
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Plotting Position vs Time
    axs[0, 0].scatter(X, y['Position'], color='black', label='Actual Position')
    axs[0, 0].plot(time_values, predictions_position, color='red', label='Predicted Position')
    axs[0, 0].set_ylabel('Position')
    axs[0, 0].legend()

    # Plotting Velocity vs Time
    axs[0, 1].scatter(X, y['Velocity'], color='blue', label='Actual Velocity')
    axs[0, 1].plot(time_values, predictions_velocity, color='green', label='Predicted Velocity')
    axs[0, 1].set_ylabel('Velocity')
    axs[0, 1].legend()

    # Plotting Position vs Velocity
    axs[1, 0].scatter(y['Position'], y['Velocity'], color='purple', label='Actual Position vs Velocity')
    axs[1, 0].set_xlabel('Position')
    axs[1, 0].set_ylabel('Velocity')
    axs[1, 0].legend()

    # Plotting Predicted Position vs Predicted Velocity
    axs[1, 1].scatter(predictions_position, predictions_velocity, color='orange', label='Predicted Position vs Velocity')
    axs[1, 1].set_xlabel('Predicted Position')
    axs[1, 1].set_ylabel('Predicted Velocity')
    axs[1, 1].legend()

    # Displaying the predictions
    for time, position, velocity in zip(time_values, predictions_position, predictions_velocity):
        print(f"Time = {time[0]:.2f} s, Predicted (Position, Velocity) = ({position:.2f} m, {velocity:.2f} m/s) ")

    plt.show()

else:
    print("Columns 't', 'Position', or 'Velocity' not found in the DataFrame.")
