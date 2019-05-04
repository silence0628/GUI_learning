from PIL import Image
import numpy as np


data = np.loadtxt('Cs137_1.txt')
data = data.reshape(64, 64)
data = np.resize(data, (171, 171))

new_im = Image.fromarray(data)

new_im.resize((171, 171))

new_im.show()
# import scipy.misc
# scipy.misc.imsave('./tmp/tmp.jpg', data)