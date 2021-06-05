cmake_minimum_required(VERSION 3.5)

project(AoC2015 VERSION 1.0.0 DESCRIPTION "Advent Of Code 2015")

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(utils_lib
    common/utils.h
    common/utils.cpp
)
target_include_directories(utils_lib PUBLIC common/)

add_executable(Day1 
    src/day_1.cpp
)
target_link_libraries(Day1 PUBLIC utils_lib)

add_executable(Day2 
    src/day_2.cpp
)
target_link_libraries(Day2 PUBLIC utils_lib)

add_executable(Day3 
    src/day_3.cpp
)
target_link_libraries(Day3 PUBLIC utils_lib)

