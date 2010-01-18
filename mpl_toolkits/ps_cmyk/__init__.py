


def _init():
    import matplotlib.backend_bases
    from backend_ps_cmyk import FigureCanvasPSCMYK
    import matplotlib.tight_bbox as tight_bbox

    for format in ["eps_cmyk", "ps_cmyk"]:
        matplotlib.backend_bases.register_backend(format, FigureCanvasPSCMYK)
        tight_bbox._adjust_bbox_handler_d[format] = tight_bbox.adjust_bbox_pdf

_init()

def use_profiles(rgb_profile_name, cmyk_profile_name):
    from backend_ps_cmyk import RendererPSCMYK
    RendererPSCMYK.use_profiles(rgb_profile_name, cmyk_profile_name)



