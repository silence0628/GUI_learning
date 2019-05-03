import numpy as np

data = np.loadtxt('Cs137_1.txt')
end_list = [[0, 0]]

for i in range(len(data)):
    end_list.append([int(i), data[i]])
    print(end_list)
    print(len(end_list))