# Set the minimum required version of CMake
cmake_minimum_required(VERSION 3.4...3.18)

# Define the project name and the language used
project(diffOptHelper)

add_subdirectory(pybind11)
# add_subdirectory(eigen3)

# Define the module that will be created from the C++ source files
pybind11_add_module(diffOptHelper
    src/diffOptPybind.cpp
    src/diffOptHelper.cpp
    src/ellipsoidMethods.cpp
    src/ellipseMethods.cpp
    src/logSumExpMethods.cpp
)

# Include directories for headers using find_package or fallback to environment variables
find_package(Eigen3 REQUIRED)  # Eigen library
# message(FATAL_ERROR "Eigen3 find result: ${Eigen3_FIND_RESULT}")
find_package(xtensor CONFIG REQUIRED)  # xtensor library
find_package(xtensor-blas CONFIG REQUIRED)  # xtensor-blas library
find_package(xtensor-python CONFIG REQUIRED)  # xtensor-python library
find_package(LAPACK REQUIRED)  # LAPACK library

# Find Python in the version range 3.7 to the latest compatible version
find_package(Python3 3.7 REQUIRED COMPONENTS Interpreter Development)
message(STATUS "Using Python executable: ${Python3_EXECUTABLE}")

# Then, try to find NumPy
find_package(Python3 COMPONENTS NumPy)
if(NOT Python3_NumPy_FOUND)
    # Get the site-packages directory
    execute_process(
        COMMAND "${Python3_EXECUTABLE}" -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
        OUTPUT_VARIABLE PYTHON_SITE_PACKAGES
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    message(STATUS "Python site-packages directory: ${PYTHON_SITE_PACKAGES}")

    # Assuming NumPy headers are located in 'numpy/core/include' relative to site-packages
    set(NumPy_INCLUDE_DIR "${PYTHON_SITE_PACKAGES}/numpy/core/include")

    # Check if the manually set path actually exists
    if(EXISTS "${NumPy_INCLUDE_DIR}")
        message(STATUS "Manually set NumPy include directory: ${NumPy_INCLUDE_DIR}")
    else()
        message(FATAL_ERROR "Failed to find NumPy include directory at the constructed path: ${NumPy_INCLUDE_DIR}")
    endif()
endif()

target_include_directories(diffOptHelper PRIVATE
    ${pybind11_INCLUDE_DIR}
    ${Eigen3_INCLUDE_DIRS}
    ${xtensor_INCLUDE_DIRS}
    ${xtensor-blas_INCLUDE_DIRS}
    ${xtensor-python_INCLUDE_DIRS}
    ${LAPACK_INCLUDE_DIRS}
    ${Python_NumPy_INCLUDE_DIRS}
)

# Link libraries
target_link_libraries(diffOptHelper PRIVATE ${LAPACK_LIBRARIES} ${xtensor_LIBRARIES} ${xtensor-blas_LIBRARIES})

# Compiler options
target_compile_features(diffOptHelper PRIVATE cxx_std_14)
