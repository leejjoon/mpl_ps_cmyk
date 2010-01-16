from matplotlib.backends.backend_ps import RendererPS, FigureCanvasPS
from matplotlib.backend_bases import FigureManagerBase #, FigureCanvasBase
import numpy as npy

class RendererPSCMYK(RendererPS):

    def _cmyk(self, im):
        h,w,s = im.as_rgba_str()

        rgba = npy.fromstring(s, npy.uint8)
        rgba.shape = (h, w, 4)
        rgb = rgba[:,:,:3]
        from rgb2cmyk import rgb2cmyk
        cmyk = rgb2cmyk(rgb)
        return h, w, (cmyk).astype(npy.uint8).tostring()

    def _get_image_h_w_bits_command(self, im):
        if im.is_grayscale:
            h, w, bits = self._gray(im)
            imagecmd = "image"
        else: # use cmyk colorspace
            h, w, bits = self._cmyk(im)
            imagecmd = "false 4 colorimage"

        return h, w, bits, imagecmd

    
class FigureCanvasPSCMYK(FigureCanvasPS):
    _renderer_class = RendererPSCMYK

    def print_eps_cmyk(self, outfile, *args, **kwargs):
        return self._print_ps(outfile, 'eps', *args, **kwargs)



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


if __name__ == '__main__':
    import matplotlib.backend_bases

    imshow(np.arange(100).reshape(10,10))

    matplotlib.backend_bases.register_backend("eps_cmyk", FigureCanvasPSCMYK)
    savefig("a.eps", format="eps_cmyk")
