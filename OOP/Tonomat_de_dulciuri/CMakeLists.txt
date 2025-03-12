cmake_minimum_required(VERSION 3.27)
project(Tonomat_de_dulciuri)

set(CMAKE_CXX_STANDARD 17)

add_executable(Tonomat_de_dulciuri main.cpp
        Dulciuri.cpp
        Dulciuri.h
        RepoDulciuri.h
        Service.cpp
        Service.h
        UIDulciuri.cpp
        UIDulciuri.h
        teste.cpp
        teste.h
        VectorDinamic.h
        ATM.cpp
        Tranzactie.cpp
        FileRepoDulciuri.h
        MyException.h
        Validator.h
)

# Adaugă directorul în care se află Service.h
target_include_directories(Tonomat_de_dulciuri PUBLIC path_to_Service_directory)
