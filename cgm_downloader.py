from pydexcom import Dexcom
import matplotlib.pyplot as plt

"""Change EMAIL info and PASSWORD info to your info as a String"""
dexcom = Dexcom("EMAIL@EMAIL.COM","PASSWORD")
readings = dexcom.get_glucose_readings()

xvalues,yvalues = [],[]
for x in readings:
    xvalues.append(x.time)
    yvalues.append(x.value)

plt.plot(xvalues, yvalues, color='blue', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='green', markersize=10)
plt.ylim(60,220)
plt.xlim()
plt.xlabel("Time")
plt.ylabel("Glucose Levels")
plt.title("Blood Glucose")
plt.show()
