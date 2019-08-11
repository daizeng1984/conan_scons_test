# Simple C++ Conan & Scons
A extremely simple starter template for very quick C++ idea test using conan and scons
# Setup
## General
Install conan and scons. If you are conda user, simple do `conda install -c conda-forge conan` and `conda install -c conda-forge scons`. I also use conda to install `clang`.

## Mac
Make sure xcode sdk is installed, e.g. `xcode-select --install` and if building with clang, please check the default profile in conan to use libc++.

If building conan package missing tools, use conda to fix the missing packages e.g. autoconf, automake, libtool etc.

## Linux 
TODO:
## Windows
TODO:

# Build
```bash
mkdir build && cd build
conan install .. --build missing
conan build ..
```

# Run
Just run `./build/main`
