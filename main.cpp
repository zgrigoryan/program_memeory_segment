/**
 * Compile the program and analyze the memory layout using: 
 * * `size` to check segment sizes * `objdump -t` to find segment locations 
 * * Use `readelf -S` to inspect segment sections Questions to answer: 
 * * Which variables belong to which segment? 
 * * What happens if the `global_var_uninitialized` is given a value? 
 * * Observe how memory layout changes with optimization flags (-O0, -O2)
 */
#include <iostream>
#include <cstdlib> // for malloc and free
#include <new> // for new and delete
#include <cstring> // for strcpy
#include <cstdio> // for printf
#include <cstddef> // for size_t
#include <algorithm> // for std::sort
#include <vector> // for std::vector
#include <string> // for std::string

// Global variables
// Initialized global variable (data segment)
int global_var_initialized = 42; 
int global_var_uninitialized; // BSS segment
// Uncommenting the line below will initialize the variable and move it to the data segment
// int global_var_uninitialized = 0; 

// Constant global variable (data segment)
const char* msg = "Hello"; 

void func() { } 

int main() { 
    int local_var = 10; // Stack
    int* heap_var = new int(20); // Heap
    std::cout << msg << std::endl; 
    delete heap_var; 
}