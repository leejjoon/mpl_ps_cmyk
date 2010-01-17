

import matplotlib.backend_bases
from backend_ps_cmyk import FigureCanvasPSCMYK

matplotlib.backend_bases.register_backend("eps_cmyk", FigureCanvasPSCMYK)
matplotlib.backend_bases.register_backend("ps_cmyk", FigureCanvasPSCMYK)

def use_profiles(rgb_profile_name, cmyk_profile_name):
    from backend_ps_cmyk import RendererPSCMYK
    RendererPSCMYK.use_profiles(rgb_profile_name, cmyk_profile_name)

