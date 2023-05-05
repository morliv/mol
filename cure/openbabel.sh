#!/usr/bin/bash

git clone https://github.com/openbabel/openbabel.git
cd openbabel
git checkout openbabel-3-1-1 
mkdir build
cd build
cmake -DWITH_MAEPARSER=OFF -DWITH_COORDGEN=OFF -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON ..
make
make install