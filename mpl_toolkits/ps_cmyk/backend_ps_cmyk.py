from matplotlib.backends.backend_ps import RendererPS, FigureCanvasPS
from matplotlib.backend_bases import FigureManagerBase
import numpy as npy

from os.path import dirname, join, exists

import backend_ps_cmyk

_icc_dir = join(dirname(backend_ps_cmyk.__file__), "icc-profiles")

def set_icc_dir(dir_name):
    _icc_dir = dirname

def get_icc_dir():
    return _icc_dir


class RendererPSCMYK(RendererPS):

    func_RGB2CMYK = None
    
    def _cmyk(self, im):
        self.check_porfile()

        h,w,s = im.as_rgba_str()

        rgba = npy.fromstring(s, npy.uint8)
        rgba.shape = (h, w, 4)
        rgb = rgba[:,:,:3]
        cmyk = RendererPSCMYK.func_RGB2CMYK(rgb)
        return h, w, (cmyk).astype(npy.uint8).tostring()

    def _get_image_h_w_bits_command(self, im):
        if im.is_grayscale:
            h, w, bits = self._gray(im)
            imagecmd = "image"
        else: # use cmyk colorspace
            h, w, bits = self._cmyk(im)
            imagecmd = "false 4 colorimage"

        return h, w, bits, imagecmd

    @classmethod
    def get_default_profile_names(cls):
        return cls._search_profile("sRGB.icm"), \
               cls._search_profile("USWebCoatedSWOP.icc")
        
    @classmethod
    def set_default_profiles(cls):
        rgb_name, cmyk_name = cls.get_default_profile_names()
        cls.use_profiles(rgb_name, cmyk_name)

    @classmethod
    def check_porfile(cls):
        if cls.func_RGB2CMYK is None:
            cls.set_default_profiles()
            
    @classmethod
    def use_profiles(cls, rgb_profile_name, cmyk_profile_name):
        _rgb = cls._search_profile(rgb_profile_name)
        _cmyk = cls._search_profile(cmyk_profile_name)
        from rgb2cmyk import RGB2CMYK
        rgb2cmyk = RGB2CMYK(_rgb, _cmyk)
        cls.func_RGB2CMYK = rgb2cmyk.transform

    @staticmethod
    def _search_profile(name):
        if exists(name):
            return name

        new_name = join(_icc_dir, name)
        if exists(new_name):
            return new_name

        raise RuntimeError("icc file not found : %s or %s" % (name, new_name))
        


    
class FigureCanvasPSCMYK(FigureCanvasPS):
    _renderer_class = RendererPSCMYK

    def print_eps_cmyk(self, outfile, *args, **kwargs):
        return self._print_ps(outfile, 'eps', *args, **kwargs)

    def print_ps_cmyk(self, outfile, *args, **kwargs):
        return self._print_ps(outfile, 'ps', *args, **kwargs)



from matplotlib.figure import Figure

def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    canvas = FigureCanvasPSCMYK(thisFig)
    manager = FigureManagerPSCMYK(canvas, num)
    return manager


class FigureManagerPSCMYK(FigureManagerBase):
    pass


FigureManager = FigureManagerPSCMYK


