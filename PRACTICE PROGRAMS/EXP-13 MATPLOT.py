import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++"]
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("Course Distribution")

plt.show()
