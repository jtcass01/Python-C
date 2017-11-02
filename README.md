# Python-C
Quick example of calling C code within python for future reference.  This is helpful as Python's computations are very time expensive.

# Compiling
    For Linux
    $  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c

    For Mac
    $ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
