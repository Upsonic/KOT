---
layout: default
title: BENCHMARK
nav_order: 10
has_children: false
---

# SET GET DELETE BENCHMARK
In here we will learn how to make benchmark for KOT database set, get and delete function. Also you can use `compress` and `encryption_key` as parameters.

```python
from kot import KOT

# Benchmark for set, get and delete functions together
print(KOT.benchmark(number=10000))
```

Output:

```console
4.072242259979248
```



# Set Benchmark
In here we will learn how to make benchmark for KOT database set function. Also you can use `compress` and `encryption_key` as parameters.

```python
from kot import KOT

# Benchmark for set function
print(KOT.benchmark_set(number=10000))
```

Output:

```console
4.3562116622924805
```

# Get Benchmark
In here we will learn how to make benchmark for KOT database get function. Also you can use `compress` and `encryption_key` as parameters.

```python
from kot import KOT

# Benchmark for get function
print(KOT.benchmark_get(number=10000))
```

Output:

```console
2.4775638580322266
```

# Delete Benchmark
In here we will learn how to make benchmark for KOT database delete function. Also you can use `compress` and `encryption_key` as parameters.

```python
from kot import KOT

# Benchmark for delete function
print(KOT.benchmark_delete(number=10000))
```

Output:

```console
0.722423791885376
```