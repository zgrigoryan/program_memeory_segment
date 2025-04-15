# 🧠 Memory Layout Analysis of a C++ Program

## 📄 Description

This repository contains an analysis of the memory layout of a basic C++ program, focusing on how variables are mapped to segments such as `.text`, `.data`, `.bss`, `stack`, and `heap`.

The goal is to understand how different variables and functions are stored in memory and how compiler optimization levels affect binary layout.

We used the following tools:
- `size`: to view the size of memory segments.
- `objdump -t`: to locate symbol addresses and segment info.
- `otool -l`: macOS equivalent of `readelf -S`, to inspect segment layout.

## 📂 Files

- `main.cpp`: Source code.
- `results.py`: Python script for visualization of the results
- `build/`: Contains compiled binaries and command outputs.
- `analysis/`: Terminal outputs of `size`, `objdump`, and `otool`.
- `diagrams/`: Visualization attempts 

## 🧪 Questions and Answers

### 1. **Which variables belong to which segment?**

| Identifier                  | Memory Segment   | Notes                                                            |
|----------------------------|------------------|------------------------------------------------------------------|
| `global_var_initialized`   | `.data`           | Initialized global variable                                      |
| `global_var_uninitialized` | `.bss`            | Uninitialized global variable                                    |
| `msg`                      | `.rodata`         | String literal in `.rodata`, pointer itself in `.data`           |
| `func()`                   | `.text`           | Code segment (function code)                                     |
| `main()`                   | `.text`           | Code segment (function code)                                     |
| `local_var`                | Stack             | Local variable allocated at runtime                              |
| `heap_var`                 | Heap              | Dynamically allocated memory using `new`                         |

---

### 2. **What happens if `global_var_uninitialized` is given a value?**

```cpp
int global_var_uninitialized = 0;
```

It moves from the **BSS** to the **data** segment because it becomes an **initialized variable**. This increases the `.data` section size.

### 3. **How does memory layout change with `-O0` and `-O2`?**

| Tool       | Observation                                           |
|------------|-------------------------------------------------------|
| `size`     | `.text` and `.data` sections might shrink at `-O2`   |
| `objdump`  | Some functions may be missing (inlined or optimized) |
| `otool`    | Section addresses or sizes may be different           |

- `size` 
After running the size command for the two executables the results were identical, though one file was compiled using optimizaion, the other was not optimized. 

- `objdump` 
In case of *objdump*, there is already difference visible. For example, just simply looking at *.text* sections, there is a ~40 line difference, inidcating section shrinks when using *-O2* flag. 

- `otool`
For *otool* there are address and size differences, for instance: 

| -O0       | -O2                                           |
|------------|-------------------------------------------------------|
| Load command 18
      cmd LC_CODE_SIGNATURE
  cmdsize 16
  dataoff 59264
 datasize 608    | Load command 18
      cmd LC_CODE_SIGNATURE
  cmdsize 16
  dataoff 53344
 datasize 576 |

---
## 🧪 Build & Run 

Although this repository does not have any functionality and the .cpp code is used simply for analyzing segments in memory in C/C++ programming, you can still run the following for compilation and running: 

```bash
g++ main.cpp -o main
```
```bash
./main
```
---

## Visualization

This program uses `matplotlib` library in python to create visual plots. 

This plot shows the segments when compiling with -O0 flag
[Memory-Layout](diagrams/memory_layout.png)

This plot shows the differences of _TEXT section between -O0 and -O2 flags: 
[Text-Size-Comparison](diagrams/text_size_comparison.png)


## 🧰 Commands Used for Analysis

```bash
g++ -g -O0 main.cpp -o build/memory_layout_O0
g++ -g -O2 main.cpp -o build/memory_layout_O2

size build/memory_layout_O0 > analysis/size_output_O0.txt
size build/memory_layout_O2 > analysis/size_output_O2.txt

objdump -t build/memory_layout_O0 > analysis/objdump_O0.txt
objdump -t build/memory_layout_O2 > analysis/objdump_O2.txt

otool -l build/memory_layout_O0 > analysis/otool_O0.txt
otool -l build/memory_layout_O2 > analysis/otool_O2.txt
```

*Please note that in the analysis folder, .txt files include two results, one where `global_var_uninitialized` is initialized and one where it's not.*

---