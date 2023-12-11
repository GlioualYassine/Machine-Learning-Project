from matplotlib import pyplot as plt
# #loading data
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.style.use('fivethirtyeight')


# #ploting data
# plt.plot(dev_x,dev_y,label = 'All Devs',marker=',',color='m',linestyle='-.')
plt.plot(dev_x,dev_y,label = 'All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(dev_x,py_dev_y,label = 'Python Devs')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
# plt.plot(dev_x,js_dev_y,color='r',label = 'JS Devs',marker='o')
plt.plot(dev_x,js_dev_y,label = 'JS Devs')

print(plt.style.available)

#adding labels and title
plt.title('Median Salary (USD) by Age')

#adding legend of the plot
#plt.legend(['All devs','Python devs'])
plt.legend()
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
# plt.tight_layout()
# plt.grid()
plt.show()


