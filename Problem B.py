import matplotlib.pyplot as plt
import pandas as pd
import datetime

df = pd.read_csv('activity.csv')
steps, counter, dates = [], 0, [0]
for x in df['interval']:
    if x == 5:
        if str(df['steps'][counter]) == "nan":
            pass
        else:
            steps.append(df['steps'][counter])
    counter += 1
steps.sort()
for y in df['date']:
    if y != dates[-1]:
        dates.append(y)
dates.pop(0)
print("The maximum number of steps is: " + str(steps[-1]))
plt.plot_date(dates, steps)
plt.title('Average daily activity')
plt.xlabel('5 Minute intervals')
plt.ylabel('Average')
plt.show()
