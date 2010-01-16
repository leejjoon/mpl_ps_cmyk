

import matplotlib.backend_bases
from backend_ps_cmyk import FigureCanvasPSCMYK

matplotlib.backend_bases.register_backend("eps_cmyk", FigureCanvasPSCMYK)
