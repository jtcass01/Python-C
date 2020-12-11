from ctypes import CDLL, c_float, RTLD_GLOBAL
from os.path import join, isfile, abspath
from unittest import TestCase, main


class Ctypes_Test(TestCase):
    def test_simple_add(self) -> None:
        print("Performing Ctypes simple add test.")

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
        print("Ctypes test was successful.")

    def test_rti_dds_connector_load(self) -> None:
        print("Performing rti dds connector load test.")

        ctypes_source_file_location = get_ctypes_source_file_location(c_types_source_file_name='librtiddsconnector.so')
        assert isfile(ctypes_source_file_location), "Unable to locate file " + ctypes_source_file_location

        rti = CDLL(ctypes_source_file_location, RTLD_GLOBAL)

        print("RTI DDS Connector load test was successful.")


def get_ctypes_source_file_location(c_types_source_file_name: str) -> str:
    ctypes_source_file_location = str(abspath(__file__))

    if "/" in ctypes_source_file_location:
        ctypes_source_file_location = '/'.join(ctypes_source_file_location.split('/')[:-1])
    elif "\\" in ctypes_source_file_location:
        ctypes_source_file_location = '\\'.join(ctypes_source_file_location.split('\\')[:-1])

    return join(ctypes_source_file_location, 'c_code', c_types_source_file_name)


if __name__ == "__main__":
    main()