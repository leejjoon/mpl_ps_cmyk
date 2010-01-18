from distutils.core import setup

from distutils.command.install import install as _install

import os.path

_adobe_icc_zip_file = "AdobeICCProfilesCS4Mac_end-user.zip"
_adobe_url = "http://www.adobe.com/support/downloads/detail.jsp?ftpID=4074"
if not os.path.exists(_adobe_icc_zip_file):
    msg = "The package requires %s in the current directory.\nThe file can be downloaded from %s" % (_adobe_icc_zip_file, _adobe_url)
    raise RuntimeError(msg)

def install_iccfiles(basedir):
    icc_dir = os.path.join(basedir,
                           "mpl_toolkits", "ps_cmyk", "icc-profiles")
    import zipfile
    zf = zipfile.ZipFile("AdobeICCProfilesCS4Mac_end-user.zip")
    zfil = zf.infolist()
    for zfi in zfil:
        if zfi.filename.endswith("icc"):
            buf = zf.read(zfi.filename)
            outpath = os.path.join(icc_dir, os.path.basename(zfi.filename))
            open(outpath, "w").write(buf)
    
class install(_install):
    def run(self):
        _install.run(self)
        install_iccfiles(self.install_purelib)

setup(
  name              = "ps_cmyk",
  version           = "0.1",
  description       = "matplotlib postscript backend w/ images in cmyk colorspace.",
  long_description  = """matplotlib postscript backend w/ images in cmyk colorspace.""",
  url               = "http://github.com/leejjoon/mpl_ps_cmyk",
  download_url      = "http://github.com/leejjoon/mpl_ps_cmyk/downloads",
  author            = "Jae-Joon Lee",
  author_email      = "lee.j.joon@gmail.com",
  platforms         = ["any"],
  license           = "MIT",
  packages          = ['mpl_toolkits','mpl_toolkits.ps_cmyk'],
  package_dir       = {'mpl_toolkits':'mpl_toolkits',
                       "mpl_toolkits.ps_cmyk":"mpl_toolkits/ps_cmyk"},
  package_data = {'mpl_toolkits.ps_cmyk': ['icc-profiles/*.ic*']},
  cmdclass={'install': install},
  )
