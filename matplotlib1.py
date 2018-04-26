import matplotlib.pyplot as plt

x = [1, 3, 5]
y = [7, 8, 5]
x2 = [3, 4, 5]
y2 = [4, 8, 9]
plt.plot(x, y, 'r-', label='red line')
plt.plot(x2, y2, 'b-', label='blue line')
plt.xlabel('NUM')
plt.ylabel('Important Var')
plt.title('My first matplot graph\nwowow')
plt.legend()
plt.show()

# some basic hand-on practice with matplotlib
# plt is a general shorten for matplotlib.pyplot. Since it's kind general in coding, should keep it as what it's.
# plt.plot([x]/y, fmt, data=None, *kwargs)
# as you can see, we can simply add characters for our lines
# and if you need to show legend, don't forget use plt.legend() after you adding label for each line
