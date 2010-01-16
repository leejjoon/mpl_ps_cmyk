import numpy as np

from os.path import dirname, join

import rgb2cmyk

_icc_dir = join(dirname(rgb2cmyk.__file__), "icc-files")

def rgb2cmyk(rgb):
    # rgb : ny, nx, 3
    rgb = np.asarray(rgb)
    orig_shape = rgb.shape
    rgb.shape = (-1, orig_shape[-1])

    import lcms

    RGB        = lcms.COLORB()
    CMYK        = lcms.COLORB()

    hCMYK   = lcms.cmsOpenProfileFromFile(join(_icc_dir, "USWebCoatedSWOP.icc"), "r")
    hAdobe  = lcms.cmsOpenProfileFromFile(join(_icc_dir, "AdobeRGB1998.icc"), "r")


    xform = lcms.cmsCreateTransform(hAdobe, lcms.TYPE_RGB_8,
                                    hCMYK, lcms.TYPE_CMYK_8,
                                    lcms.INTENT_PERCEPTUAL,
                                    lcms.cmsFLAGS_NOTPRECALC)

    def rgb2cmyk1(rgb1):
        RGB[0], RGB[1], RGB[2] = int(rgb1[0]), int(rgb1[1]), int(rgb1[2])
        lcms.cmsDoTransform(xform, RGB, CMYK, 1)
        return CMYK[0], CMYK[1], CMYK[2], CMYK[3]

    cmyk_ = np.array([rgb2cmyk1(rgb1) for rgb1 in rgb])

    shape = orig_shape[:-1] + (4,)
    cmyk = cmyk_.reshape(shape)


    lcms.cmsDeleteTransform(xform)
    lcms.cmsCloseProfile(hAdobe)
    lcms.cmsCloseProfile(hCMYK)

    return cmyk

if __name__ == '__main__':
    rgb = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 128, 128), (255, 255, 255)]
    cmyk = rgb2cmyk(rgb)
