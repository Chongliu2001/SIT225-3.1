import pandas as pd
import numpy as np
import datetime

# Generate timestamps for 10 minutes with 1 second interval
time_index = pd.date_range(start=datetime.datetime.now(), periods=600, freq='1S')

# Generate distance data
# First 10 seconds: alternating between 5.1cm and 0cm
# Rest of the time: stable at 5.1cm
distance = np.array([5.1, 0] * 5 + [5.1] * (600 - 10))

# Create a DataFrame
data = pd.DataFrame({
    'timestamp': time_index.strftime('%Y-%m-%d %H:%M:%S'),
    'distance': distance
})

# Save the DataFrame to a CSV file
data.to_csv('ultrasonic_sensor_data.csv', index=False)

print("CSV file has been generated successfully.")
