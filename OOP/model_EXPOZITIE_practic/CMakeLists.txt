cmake_minimum_required(VERSION 3.27)
project(model_EXPOZITIE_practic)

set(CMAKE_CXX_STANDARD 17)

add_executable(model_EXPOZITIE_practic main.cpp
        ObiectArta.h
        Repo.h
        Service.h
        Service.cpp
        UI.h
        UI.cpp
        Teste.h
        Teste.cpp)
