from distutils.core import setup

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
  package_data = {'mpl_toolkits.ps_cmyk': ['icc-profiles-1.0.1/*.ic*']},
  )
