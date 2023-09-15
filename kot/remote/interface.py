#!/usr/bin/python3
# -*- coding: utf-8 -*-

from kot import KOT, KOT_Remote

def KOT_Cloud(database_name):
    return KOT_Remote(
        database_name, "http://free.cloud.kotdatabase.dev:5000", "onuratakan"
    )  # pragma: no cover


def KOT_Cloud_Pro(database_name, access_key):
    return KOT_Remote(
        database_name, "http://pro.cloud.kotdatabase.dev:5001", access_key
    )  # pragma: no cover


def KOT_Cloud_Dedicated(database_name, password, dedicated_key):
    dedicated_key = dedicated_key.replace("dedicatedkey-", "")
    dedicated_key = dedicated_key.encode()
    resolver = KOT("dedicate_resolver")
    resolver.set(dedicated_key.decode(), dedicated_key)
    host = resolver.get(dedicated_key.decode(), encryption_key="dedicatedkey")
    return KOT_Remote(database_name, host, password)  # pragma: no cover


def KOT_Cloud_Dedicated_Prepare(host):
    resolver = KOT("dedicate_resolver")
    resolver.set(host, host, encryption_key="dedicatedkey")
    host = resolver.get(host)
    host = host.decode()
    host = "dedicatedkey-" + host
    return host
