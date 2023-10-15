---
layout: default
title: BENCHMARK
nav_order: 20
has_children: false
---

# SET GET DELETE BENCHMARK
In here we will learn how to make benchmark for Upsonic database set, get and delete function. Also you can use `compress` and `encryption_key` as parameters.

```python
from upsonic import Upsonic

# Benchmark for set, get and delete functions together
print(Upsonic.benchmark(number=10000))
```

Output:

```console
4.072242259979248
```



# Set Benchmark
In here we will learn how to make benchmark for Upsonic database set function. Also you can use `compress` and `encryption_key` as parameters.

```python
from upsonic import Upsonic

# Benchmark for set function
print(Upsonic.benchmark_set(number=10000))
```

Output:

```console
4.3562116622924805
```

# Get Benchmark
In here we will learn how to make benchmark for Upsonic database get function. Also you can use `compress` and `encryption_key` as parameters.

```python
from upsonic import Upsonic

# Benchmark for get function
print(Upsonic.benchmark_get(number=10000))
```

Output:

```console
2.4775638580322266
```

# Delete Benchmark
In here we will learn how to make benchmark for Upsonic database delete function. Also you can use `compress` and `encryption_key` as parameters.

```python
from upsonic import Upsonic

# Benchmark for delete function
print(Upsonic.benchmark_delete(number=10000))
```

Output:

```console
0.722423791885376
```