cmake_minimum_required(VERSION 3.18..3.20)

project(mymodule)

find_package(LAPACK REQUIRED)
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

# Determine platform and conditionally link libraries
if(NOT APPLE)
  find_package(OpenBLAS REQUIRED)
  target_link_libraries(diffOptHelper PUBLIC pybind11::module xtensor-python Python::NumPy LAPACK OpenBLAS)
else()
    target_link_libraries(diffOptHelper PUBLIC pybind11::module xtensor-python Python::NumPy LAPACK)
endif()

target_compile_definitions(diffOptHelper PRIVATE VERSION_INFO=0.1.0)
