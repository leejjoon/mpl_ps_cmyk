import matplotlib
matplotlib.use("PS")
import numpy as np

import mpl_toolkits.ps_cmyk

import matplotlib.pyplot as plt

plt.imshow(np.arange(100).reshape(10,10))

# use default profiles
plt.savefig("test_rgb.eps", format="eps")

# use default profiles
plt.savefig("test_cmyk.eps", format="eps_cmyk")


# use specified profiles
mpl_toolkits.ps_cmyk.use_profiles("sRGB.icm", "ISOuncoated.icc")
plt.savefig("test_cmyk2.eps", format="eps_cmyk")

