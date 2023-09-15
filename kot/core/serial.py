#!/usr/bin/python3
# -*- coding: utf-8 -*-


def KOT_Serial(name, self_datas: bool = False, folder: str = "", log: bool = True):
    from kot import start_location, open_databases

    folder = start_location if not folder != "" else folder

    name_hash = name + str(self_datas) + folder

    if name_hash in open_databases:
        return open_databases[name_hash]
    else:
        from kot import KOT

        database = KOT(name, self_datas=self_datas, folder=folder, log=log)
        open_databases[name_hash] = database
        return database
