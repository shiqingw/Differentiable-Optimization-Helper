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

if(EXISTS "/usr/lib/x86_64-linux-gnu/lapack")
    link_directories("/usr/lib/x86_64-linux-gnu/lapack")
endif()

if(EXISTS "/usr/lib/x86_64-linux-gnu/lapack")
    link_directories("/usr/lib/x86_64-linux-gnu/lapack")
endif()

target_link_libraries(diffOptHelper PUBLIC pybind11::module xtensor-python Python::NumPy LAPACK)

target_compile_definitions(diffOptHelper PRIVATE VERSION_INFO=0.1.0)
