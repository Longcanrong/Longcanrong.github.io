import matplotlib.pyplot as plt
#I don't kown what pseudocode to write, it is a little too obvious of real codes
UK_cities = [0.56, 0.62, 0.04, 9.7]
China_cities = [0.58, 8.4, 29.9, 22.2]
print(UK_cities)
print(China_cities)

plt.figure()
plt.pie(UK_cities)
plt.show()
plt.pie(China_cities)
plt.show()
plt.clf()