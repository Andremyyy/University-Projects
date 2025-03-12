cmake_minimum_required(VERSION 3.27)
project(gestiune_apartamente)

set(CMAKE_CXX_STANDARD 17)

add_executable(gestiune_apartamente main.cpp
        Cheltuieli.cpp
        Cheltuieli.h
        tests.cpp
        tests.h
        Repo.cpp
        Repo.h
        Service.cpp
        Service.h
        Service.h
        UI.cpp
        UI.h)
