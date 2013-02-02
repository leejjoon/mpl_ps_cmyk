import numpy as np

import lcms

#import rgb2cmyk

class RGB2CMYK(object):
    def __init__(self, rgb_profile_name, cmyk_profile_name):
        self._rgb_profile_name = rgb_profile_name
        self._cmyk_profile_name = cmyk_profile_name

        print self._rgb_profile_name, self._cmyk_profile_name
        
        self.RGB_profile   = lcms.cmsOpenProfileFromFile(self._rgb_profile_name, "r")
        self.CMYK_profile  = lcms.cmsOpenProfileFromFile(self._cmyk_profile_name, "r")

        self.RGB2CMYK_transform = lcms.cmsCreateTransform(self.RGB_profile,
                                                          lcms.TYPE_RGB_8,
                                                          self.CMYK_profile,
                                                          lcms.TYPE_CMYK_8,
                                                          lcms.INTENT_PERCEPTUAL,
                                                          lcms.cmsFLAGS_NOTPRECALC)

    def __del__(self):
        lcms.cmsDeleteTransform(self.RGB2CMYK_transform)
        lcms.cmsCloseProfile(self.CMYK_profile)
        lcms.cmsCloseProfile(self.RGB_profile)

    def transform(self, rgb):
        # rgb : ny, nx, 3
        rgb = np.asarray(rgb, dtype=np.int)
        orig_shape = rgb.shape
        rgb.shape = (-1, orig_shape[-1])

        RGB = lcms.COLORB()
        CMYK = lcms.COLORB()

        cmyk_ = [(lcms.cmsDoTransform(self.RGB2CMYK_transform,
                                      RGB, CMYK, 1),
                  (CMYK[0], CMYK[1], CMYK[2], CMYK[3]))[1] \
                 for rgb1 in rgb for
                 RGB[0], RGB[1], RGB[2] in [map(int, rgb1)]]

        shape = orig_shape[:-1] + (4,)
        cmyk = np.array(cmyk_).reshape(shape)

        return cmyk

if __name__ == '__main__':
    rgb = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 128, 128), (255, 255, 255)]

    rgb2cmyk = RGB2CMYK("AdobeRGB1998.icc", "USWebCoatedSWOP.icc")
    cmyk = rgb2cmyk.transform(rgb)
