# -*- coding: utf-8 -*-

# import numpy as np
import Image
import matplotlib.pyplot as plt

plt.plot(range(10))
plt.savefig('testplot.png')
Image.open('testplot.png').save('testplot.jpg','JPEG')