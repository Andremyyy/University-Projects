cmake_minimum_required(VERSION 3.27)
project(lab2)

set(CMAKE_CXX_STANDARD 17)

add_executable(lab2 Sources/lab2.cpp
        Headers/test.h
        Headers/utils.h
        Headers/io.h
        Sources/test.cpp
        Sources/io.cpp
        Sources/utils.cpp)
