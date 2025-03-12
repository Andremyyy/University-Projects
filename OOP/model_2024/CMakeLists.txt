cmake_minimum_required(VERSION 3.27)
project(model_2024)

set(CMAKE_CXX_STANDARD 17)

add_executable(model_2024 main.cpp
        Bacterie.h
        Repo.h
        Service.h
        Service.cpp
        UI.h
        UI.cpp
)
