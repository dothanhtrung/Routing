from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import subprocess
def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    command = ["pkg-config", "--libs", "--cflags", ' '.join(packages)]
    output = subprocess.check_output(command)
    output = output.decode("utf-8")
    for token in output.split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

ext_modules=[
    Extension("Routing",
              ["Routing.pyx"],
              **pkgconfig("libnl-3.0 libnl-cli-3.0"))  # Unix-like specific
			      ]

setup(
  name = "Routing",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules,
)