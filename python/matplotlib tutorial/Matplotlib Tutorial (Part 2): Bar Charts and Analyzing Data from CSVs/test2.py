from matplotlib import pyplot as plt
import numpy as np
import csv

from collections import Counter
#very useful package to make count of different classes

#plt uses line plot by default
#now using the csv file


plt.style.use("fivethirtyeight")

with open('Matplotlib Tutorial/Matplotlib Tutorial (Part 2): Bar Charts and Analyzing Data from CSVs/data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))  

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))


# print(language_counter)
print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])


languages.reverse()
popularity.reverse()

#barh - horizontal chart
plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()

