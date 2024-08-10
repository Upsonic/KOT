---
layout: default
title: CLI
nav_order: 10
has_children: false
parent: INTERFACES
---

# CLI

## Start
You can use `KOT` command directly.
```console
KOT --help
```

## Referance

You can use KOT in command line. KOT has a support all functions in command line.

### `set_data`

```console
kot --name <database_name> set <key_name> <value>
```

### `get_data`

```console
kot --name <database_name> get <key_name>
```

### `get_all`

```console
kot --name <database_name> get_all
```

### `delete_data`

```console
kot --name <database_name> delete <key_name>
```

### `list_databases`

```console
kot database_list
```

### `pop_database`

```console
kot database_pop <database_name>
```

### `pop_all_database`

```console
kot database_pop_all
```

### `rename_database`

```console
kot database_rename <database_name> <new_database_name>
```

### `delete_database`

```console
kot database_delete <database_name>
```
### `delete_all_database`

```console
kot database_delete_all
```

### `execute`

```console
kot execute <query>
```