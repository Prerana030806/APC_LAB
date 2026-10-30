import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]
categories = ["A", "B", "C", "D"]
values = [25, 30, 20, 25]

plt.figure()
plt.plot(months, sales, marker="o")
plt.title("Line Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure()
plt.bar(months, sales)
plt.title("Bar Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure()
plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

plt.figure()
plt.hist(sales, bins=5)
plt.title("Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
