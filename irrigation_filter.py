import json
import csv
from datetime import datetime, time

class IrrigationFilter:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_json_data()

    def load_json_data(self):
        with open(self.json_file, 'r') as file:
            return json.load(file)

    def filter_by_time_range(self, start_time, end_time):
        filtered_data = []
        for entry in self.data:
            entry_time = datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S').time()
            if start_time <= entry_time <= end_time:
                filtered_data.append(entry)
        return filtered_data

    def display_statistics(self, filtered_data):
        print(f"Total entries: {len(filtered_data)}")
        # Additional statistics can be calculated here

    def export_to_csv(self, filtered_data, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = filtered_data[0].keys() if filtered_data else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_data)

if __name__ == '__main__':
    json_file_path = 'irrigation_data.json'  # Replace with your JSON file path
    output_file_path = 'filtered_irrigation_data.csv'
    filter_instance = IrrigationFilter(json_file_path)
    start_time = time(5, 0)  # 5:00 AM
    end_time = time(23, 59)  # 11:59 PM
    filtered_data = filter_instance.filter_by_time_range(start_time, end_time)
    filter_instance.display_statistics(filtered_data)
    filter_instance.export_to_csv(filtered_data, output_file_path)