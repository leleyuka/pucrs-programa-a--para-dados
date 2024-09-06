import csv
import random

input_file = 'steam_games.csv'
output_file = 'steam_games_sample.csv'

sample_size = 20

with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  
    data = list(reader)  

sample = random.sample(data, sample_size)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)  
    writer.writerows(sample)  

print(f"A sample of {sample_size} games has been saved to '{output_file}'")
