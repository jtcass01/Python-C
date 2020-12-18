from ctypes import CDLL, c_float, RTLD_GLOBAL
from os.path import join, isfile, abspath
from unittest import TestCase, main, skip


def dir_path(file_path: str) -> str:
    if "/" in file_path:
        return '/'.join(file_path.split('/')[:-1])
    elif "\\" in file_path:
        return '\\'.join(file_path.split('\\')[:-1])


class Ctypes_Test(TestCase):
    CURRENT_WORKING_DIRECTORY = dir_path(abspath(__file__))

    def test_simple_add(self) -> None:
        print("Performing Ctypes simple add test.")

        ctypes_source_file_location = join(Ctypes_Test.CURRENT_WORKING_DIRECTORY, "c_code", "adder.so")
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

        ctypes_source_file_location = join(Ctypes_Test.CURRENT_WORKING_DIRECTORY, "test_connectors", "jetson_nano", 'librtiddsconnector.so')
        assert isfile(ctypes_source_file_location), "Unable to locate file " + ctypes_source_file_location

        rti = CDLL(ctypes_source_file_location, RTLD_GLOBAL)

        print("RTI DDS Connector load test was successful.")

    @skip
    def test_arm6v_rti_dds_connector_load(self) -> None:
        print("Performing rti dds connector load test.")

        ctypes_source_file_location = join(Ctypes_Test.CURRENT_WORKING_DIRECTORY, "test_connectors", "arm6vfphLinux3.xgcc4.7.2", 'librtiddsconnector.so')
        assert isfile(ctypes_source_file_location), "Unable to locate file " + ctypes_source_file_location

        rti = CDLL(ctypes_source_file_location, RTLD_GLOBAL)

        print("RTI DDS Connector load test was successful.")

    @skip
    def test_64Linux_rti_dds_connector_load(self) -> None:
        print("Performing rti dds connector load test.")

        ctypes_source_file_location = join(Ctypes_Test.CURRENT_WORKING_DIRECTORY, "test_connectors", "x64Linux2.6gcc4.4.5", 'librtiddsconnector.so')
        assert isfile(ctypes_source_file_location), "Unable to locate file " + ctypes_source_file_location
        rti = CDLL(ctypes_source_file_location, RTLD_GLOBAL)

        print("RTI DDS Connector load test was successful.")


if __name__ == "__main__":
    main()