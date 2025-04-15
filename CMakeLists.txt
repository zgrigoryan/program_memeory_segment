cmake_minimum_required(VERSION 3.10)
project(cache_aware_oblivious_matmul)

set(CMAKE_CXX_STANDARD 17)

add_executable(memory_segments main.cpp)
