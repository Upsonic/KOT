#!/usr/bin/python3
# -*- coding: utf-8 -*-

import upsonic


def Upsonic_Serial(name, self_datas: bool = False, folder: str = "", log: bool = True, enable_hashing:bool=False):
    

    folder = upsonic.core.upsonic.start_location if not folder != "" else folder

    name_hash = name + str(self_datas) + folder

    if name_hash in upsonic.core.upsonic.open_databases:
        return upsonic.core.upsonic.open_databases[name_hash]
    else:
        from upsonic import Upsonic

        database = Upsonic(name, self_datas=self_datas, folder=folder, log=log, enable_hashing=enable_hashing)
        upsonic.core.upsonic.open_databases[name_hash] = database
        return database
