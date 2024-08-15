import time
import requests
import json
import csv

# Replace these with your actual values
device_id = '7adc1419-fb0b-4ff9-ae03-4e5e4a2d10f5' 
thing_id = '92e65d9e-e129-4d18-9669-2c25d5c22eff'    
variable_name = 'distance'   

# API endpoint to get the current value of a variable
url = f"https://api2.arduino.cc/iot/v2/things/{thing_id}/properties/{variable_name}/value"

# Headers including your device ID
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {device_id}"  # Assuming you have an authorization setup
}

# Open a CSV file to store the sensor data
with open('sensor_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'distance'])

    # Run for 10 minutes
    end_time = time.time() + 10 * 60
    while time.time() < end_time:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            distance = data['value']  # Assuming the response includes a 'value' key
            
            # Get the current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            
            # Write the data to the CSV file
            writer.writerow([timestamp, distance])
            
            print(f"{timestamp} - Distance: {distance}")
        else:
            print("Failed to retrieve data from Arduino Cloud")

        # Wait for 30 seconds before the next request
        time.sleep(30)
