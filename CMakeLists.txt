cmake_minimum_required(VERSION 3.18..3.20)

project(diffOptHelper)

find_package(OpenBLAS REQUIRED)
find_package(Python REQUIRED COMPONENTS Interpreter Development NumPy)
find_package(pybind11 REQUIRED CONFIG)
find_package(xtensor REQUIRED)
find_package(xtensor-blas REQUIRED)
find_package(xtensor-python REQUIRED)

pybind11_add_module(
    diffOptHelper
    src/diffOptPybind.cpp
    src/diffOptHelper.cpp
    src/ellipsoidMethods.cpp
    src/ellipseMethods.cpp
    src/logSumExpMethods.cpp
)

# If OpenBLAS provides a target, use it directly. If not, specify the library path as you did.
target_link_libraries(diffOptHelper PUBLIC
    pybind11::module
    xtensor-python
    Python::NumPy
    ${OpenBLAS_LIBRARIES}  # Use the variable set by find_package if available
    pthread m dl
)

target_include_directories(diffOptHelper PUBLIC
    ${OpenBLAS_INCLUDE_DIRS}  # Include this if find_package sets this variable
)

target_compile_definitions(diffOptHelper PRIVATE VERSION_INFO=0.1.0)