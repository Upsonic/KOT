#!/usr/bin/python3
# -*- coding: utf-8 -*-



def Upsonic_Cloud(database_name):
    from upsonic import Upsonic, Upsonic_Remote
    return Upsonic_Remote(
        database_name, "http://free.cloud.upsonicdatabase.dev:5000", "onuratakan"
    )  # pragma: no cover


def Upsonic_Cloud_Pro(database_name, access_key):
    from upsonic import Upsonic, Upsonic_Remote
    return Upsonic_Remote(
        database_name, "http://pro.cloud.upsonicdatabase.dev:5001", access_key
    )  # pragma: no cover


def Upsonic_Cloud_Dedicated(database_name, password, dedicated_key):
    from upsonic import Upsonic, Upsonic_Remote
    dedicated_key = dedicated_key.replace("dedicatedkey-", "")
    dedicated_key = dedicated_key.encode()
    resolver = Upsonic("dedicate_resolver")
    resolver.set(dedicated_key.decode(), dedicated_key)
    host = resolver.get(dedicated_key.decode(), encryption_key="dedicatedkey")
    return Upsonic_Remote(database_name, host, password)  # pragma: no cover


def Upsonic_Cloud_Dedicated_Prepare(host):
    from upsonic import Upsonic, Upsonic_Remote
    resolver = Upsonic("dedicate_resolver")
    resolver.set(host, host, encryption_key="dedicatedkey")
    host = resolver.get(host)
    host = host.decode()
    host = "dedicatedkey-" + host
    return host
