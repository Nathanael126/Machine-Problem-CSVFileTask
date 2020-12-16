import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('activity.csv')
x, counter, steps_per_day, dates = 0, 0, [0], [0]
for y in df['date']:
    if y != dates[-1]:
        dates.append(y)
        if str(y) == "nan":
            pass
        else:
            steps_per_day.append(df['steps'][counter])
    else:
        if str(y) == "nan":
            pass
        else:
            steps_per_day[-1] += df['steps'][counter]
    counter += 1
steps_per_day.pop(0)
dates.pop(0)
for a in df['steps']:
    if str(a) == "nan":
        pass
    else:
        x += a
print(dates)
print(steps_per_day)
print("Mean is: " + str(x/len(df)))
print("Median is: " + str(df.sort_values('steps')['steps'][len(df)/2]))
plt.bar(dates, steps_per_day)
plt.title('Number of steps taken per day')
plt.xlabel('Dates')
plt.ylabel('Steps')
plt.show()
