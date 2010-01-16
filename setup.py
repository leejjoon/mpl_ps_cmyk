from distutils.core import setup

setup(
  name              = "ps_cmyk",
  version           = "0.1",
  description       = "",
  long_description  = """  """,
  url               = "",
  download_url      = "",
  author            = "",
  author_email      = "",
  platforms         = ["any"],
  license           = "MIT",
  packages          = ['mpl_toolkits','mpl_toolkits.ps_cmyk'],
  package_dir       = {'mpl_toolkits':'mpl_toolkits',
                       "mpl_toolkits.ps_cmyk":"mpl_toolkits/ps_cmyk"},
  package_data = {'mpl_toolkits.ps_cmyk': ['icc-files/*.icc']},
  )
