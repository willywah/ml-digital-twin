import numpy as np
import pandas as pd
import json

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for inputs
n_samples = 50
P_pump = np.random.uniform(50, 150, n_samples)  # Pump Power (Watts)
Q_in = np.random.uniform(0.1, 1.0, n_samples)   # Tank Inflow Rate (m^3/s)

# Generate synthetic outputs based on the inputs
Q_pipe = 0.8 * P_pump + 0.2 * Q_in              # Simplified relationship for flow rate
P_pipe = 1.5 * Q_pipe + np.random.normal(0, 0.5, n_samples) # Pressure with some noise
H_tank = 10 * Q_in - 0.5 * Q_pipe + np.random.normal(0, 0.2, n_samples) # Tank Level

# Create a DataFrame for the dataset
dataset = pd.DataFrame({
    'P_pump': P_pump,
    'Q_in': Q_in,
    'Q_pipe': Q_pipe,
    'P_pipe': P_pipe,
    'H_tank': H_tank
})

# Convert the DataFrame to a dictionarys
data_dict = dataset.to_dict(orient='list')

# Specify the output directory
file_path = "pipe_pump_tank_data.json"

# Write the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(f"Data has been exported to {file_path}")

