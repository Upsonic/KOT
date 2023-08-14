---
layout: default
title: CLI
nav_order: 10
has_children: false
parent: INTERFACES
---

# CLI

## Referance

You can use KOT in command line. KOT has a support all functions in command line.

### `set_data`

```console
KOT --name <database_name> set <key_name> <value>
```

### `get_data`

```console
KOT --name <database_name> get <key_name>
```

### `get_all`

```console
KOT --name <database_name> get_all
```

### `delete_data`

```console
KOT --name <database_name> delete <key_name>
```

### `list_databases`

```console
KOT database_list
```

### `pop_database`

```console
KOT database_pop <database_name>
```

### `pop_all_database`

```console
KOT database_pop_all
```

### `rename_database`

```console
KOT database_rename <database_name> <new_database_name>
```

### `delete_database`

```console
KOT database_delete <database_name>
```
### `delete_all_database`

```console
KOT database_delete_all
```

### `execute`

```console
KOT execute <query>
```