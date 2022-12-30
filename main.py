# from isOdd import isOdd
#
# print(isOdd(1))
# print(isOdd(5))

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt
# # import numpy as np
# list1 = [1, 2, 3, 4, 5]
# plt.plot(list1)
# plt.show()

# import matplotlib

from progress.bar import Bar

bar = Bar('Processing', max=20)

for i in range(20):
    bar.next()
bar.finish()