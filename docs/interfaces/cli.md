---
layout: default
title: CLI
nav_order: 10
has_children: false
parent: INTERFACES
---

# CLI

## Start
You can use `Upsonic` command directly.
```console
Upsonic --help
```

## Referance

You can use Upsonic in command line. Upsonic has a support all functions in command line.

### `set_data`

```console
upsonic --name <database_name> set <key_name> <value>
```

### `get_data`

```console
upsonic --name <database_name> get <key_name>
```

### `get_all`

```console
upsonic --name <database_name> get_all
```

### `delete_data`

```console
upsonic --name <database_name> delete <key_name>
```

### `list_databases`

```console
upsonic database_list
```

### `pop_database`

```console
upsonic database_pop <database_name>
```

### `pop_all_database`

```console
upsonic database_pop_all
```

### `rename_database`

```console
upsonic database_rename <database_name> <new_database_name>
```

### `delete_database`

```console
upsonic database_delete <database_name>
```
### `delete_all_database`

```console
upsonic database_delete_all
```

### `execute`

```console
upsonic execute <query>
```