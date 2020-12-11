from ctypes import CDLL, c_float
from os.path import join, isfile, abspath


def get_ctypes_source_file_location(c_types_source_file_name: str) -> str:
    ctypes_source_file_location = str(abspath(__file__))

    if "/" in ctypes_source_file_location:
        ctypes_source_file_location = '/'.join(ctypes_source_file_location.split('/')[:-1])
    elif "\\" in ctypes_source_file_location:
        ctypes_source_file_location = '\\'.join(ctypes_source_file_location.split('\\')[:-1])

    return join(ctypes_source_file_location, 'c_code', c_types_source_file_name)


if __name__ == "__main__":
    ctypes_source_file_location = get_ctypes_source_file_location(c_types_source_file_name='adder.so')

    assert isfile(ctypes_source_file_location), "Unable to locate file " + ctypes_source_file_location

    #load the shared object file
    adder = CDLL(ctypes_source_file_location)

    #Find sum of integers
    assert adder.add_int(4,5) == 9

    #Find sum of floats
    a = c_float(5.5)
    b = c_float(4.1)

    add_float = adder.add_float
    add_float.restype = c_float
    c_types_float_result = add_float(a, b)

    assert round(c_types_float_result, 2) == round(9.6, 2)
