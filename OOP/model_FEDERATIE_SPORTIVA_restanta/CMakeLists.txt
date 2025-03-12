cmake_minimum_required(VERSION 3.27)
project(model_FEDERATIE_SPORTIVA_restanta)

set(CMAKE_CXX_STANDARD 17)

add_executable(model_FEDERATIE_SPORTIVA_restanta main.cpp
        Meci.h
        Repo.h
        Service.h
        Service.cpp
        UI.h
        UI.cpp
        Teste.h
        Teste.cpp)
