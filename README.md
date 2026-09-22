# Variations and Benchmarking of Insertion Sort and Shellsort

A comprehensive research and benchmarking project exploring diverse algorithmic variations of **insertion sort** and **Shellsort**.

The project implements and analyzes standard insertion sort implementations optimized for Python, their inverted variants, and binary search optimizations. Furthermore, it features merge-like recursive variations that utilize the sorted state of sublists. Finally, it investigates Shellsort implementations driven by distinct gap sequences, benchmarking important step sequences alongside original mathematical adaptations.

---

## 📂 Repository Structure

The project consists of two core scripts, both equipped with a complete benchmark that tests the algorithms under various input data distributions.

* **`variants_of_insertion_sort.py`** – Contains classical, unidirectional, binary search, and recursive merge-like variations of insertion sort, along with swap-based derivatives (Gnome sort, Sifting sort, and "I can't believe it can sort" (ICBICS)).
* **`variants_of_Shellsort.py`** – Implements Shellsort using a variety of step sequences (gaps) from literature and modern mathematics, evaluating performance across large list sizes.

---

## 🔍 Implemented Algorithms & Variations

### 1. Insertion Sort Variations (`variants_of_insertion_sort.py`)

Every non-swap-based algorithm family is cross-implemented using three distinct data-shifting mechanisms. The implementation type is explicitly defined by the function name prefix:

| Function Prefix | Shifting Mechanism | Operational Strategy |
| :--- | :--- | :--- |
| **`no_prefix`** | Standard Nested Loops | Sequential adjacent element shifting. |
| **`_` (Single Underscore)** | Python Slicing (`[:]`) | Leverages C-level memory block copies. |
| **`__` (Double Underscore)** | In-Place Mutation | In-place reordering using `.pop()` and `.insert()`. |

#### Core Algorithm Families:

* **Standard & Inverted insertion sort:** Forward-scanning insertion contrasted against backward-scanning (right-to-left) implementations, both generating sorted lists in ascending order.
* **With binary search (`_wbs`):** Reduces position-lookup complexity from `O(n)` to `O(log n)` using an overflow-avoidant midpoint calculation, maximizing language-agnostic portability.
* **Merge-like insertion sort:** Recursive variations that split the list in half (resembling top-down merge sort) and leverage the pre-sorted state of sublists during the merge phase.
* **Unidirectional variations:** Algorithms that strictly scan elements from a fixed direction to determine the correct insertion position.

#### Swap-Based Derivatives:

* `swap_based_insertion_sort`: Eliminates multi-position shifting in favor of consecutive adjacent exchanges.
* `gnome_sort` & `jumping_gnome_sort`: Standard and state-tracking optimized variants of the garden gnome algorithm.
* `sifting_sort`: Scans for out-of-order adjacent elements and sifts them backward into the sorted partition. This exchange mechanism serves as the foundation for the core loops of the Shellsort algorithms.
* `i_cant_believe_it_can_sort` (ICBICS): The infamous, parodic sorting routine included for completeness.

### 2. Shellsort Variations (`variants_of_Shellsort.py`)

Except for `Shellsort2` and `Shellsort6`, these implementations analyze gap sequences given in Keith McLuckie & Angus Barber's book, *Sorting Routines for Microcomputers* (Macmillan Education UK, 1986).

* **`Shellsort0`:** The original diminishing increment sequence $\lfloor n/2^k \rfloor$ by Donald Shell.
* **`Shellsort1`:** A frequently used Hibbard's sequence $2^k - 1$.
* **`Shellsort2` (Plastic Constant Adaptation):** An original, non-standard sequence driven by the geometric ratio of the **Plastic Constant** ($\rho \approx 1.3247$), maintaining highly uniform gap reduction ratios.
* **`Shellsort3`:** The Papernov-Stasevich sequence based on numbers of the form $2^k + 1$.
* **`Shellsort4`:** Knuth's sequence $(3^k - 1) / 2$.
* **`Shellsort5`:** A sequence composed of the integers $1, 3, 5, 11, 21, 43, \dots$.
* **`Shellsort6`:** Sedgewick's sequence based on numbers of the form $4^k + 3 \cdot 2^{k - 1} + 1$.

---

## 📊 Empirical Benchmarking Suite

Both scripts feature a built-in benchmark that tests the algorithms across multiple input data distributions.

* **Insertion sort** variants are tested on small-to-moderate lists (**10,000 to 20,000 elements**) due to quadratic asymptotic scaling.
* **Shellsort** variants are tested on large lists (**100,000 to 500,000 elements**).

### Data Distributions Tested:

1. **Uniformly Distributed:** Random integers generated across a wide spread to track general-case efficiency.
2. **Normally Distributed:** Gaussian curve distribution simulated using random integers.
3. **Partially Sorted (Extended):** Pre-sorted list extended with random, unsorted data.
4. **Reverse-Sorted:** List populated in descending order to test upper-bound worst cases.
5. **Interleaved:** Interlaced list of distinct integers with alternating subsegments.
6. **"Pipe Organ":** List whose values increase linearly to a midpoint and decrease symmetrically to the end.
7. **Sorted:** List already in ascending order to measure baseline validation overhead.
8. **Constant:** List populated entirely by identical integers.

---

## 🚀 Execution Guide

The project relies entirely on native Python 3 libraries and contains zero external package dependencies.

### Execute Insertion Sort Benchmarks:

```bash
python3 variants_of_insertion_sort.py
```

### Execute Shellsort Benchmarks:

```bash
python3 variants_of_Shellsort.py
```
