#!/usr/bin/python3
# -*- coding: utf-8 -*-

import kot


def KOT_Serial(name, self_datas: bool = False, folder: str = "", log: bool = True):
    

    folder = kot.core.kot.start_location if not folder != "" else folder

    name_hash = name + str(self_datas) + folder

    if name_hash in kot.core.kot.open_databases:
        return kot.core.kot.open_databases[name_hash]
    else:
        from kot import KOT

        database = KOT(name, self_datas=self_datas, folder=folder, log=log)
        kot.core.kot.open_databases[name_hash] = database
        return database
