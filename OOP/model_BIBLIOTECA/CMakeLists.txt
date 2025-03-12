cmake_minimum_required(VERSION 3.27)
project(model_BIBLIOTECA)

set(CMAKE_CXX_STANDARD 17)

add_executable(model_BIBLIOTECA main.cpp
        Carte.h
        Repo.h
        FileRepo.h
        Service.h
        Service.cpp
        UI.h
        UI.cpp
        Teste.h
        Teste.cpp)
