import os

class Color:
    primary = 0x3EE2B7
    transparent = 0x2F3136
    blurple_old = 0x7289DA
    blurple = 0x5865F2
    danger = 0xE92323
    warning = 0xE9B623
    success = 0x44E923

class Auth:
    discord_auth = {
        "debug":"OTkxNjI5OTgwMzQ3OTQwOTM1.GSpN9O.RG3Sjrv-wD12MSE7eADCzvGt8_Mw4gSb7MmIpk",
        "release": "OTkxNjI5OTgwMzQ3OTQwOTM1.GSpN9O.RG3Sjrv-wD12MSE7eADCzvGt8_Mw4gSb7MmIpk"
    }
    mongo_auth = {
        "url":"",
        "username":"",
        "auth":{
            "debug":"",
            "release": ""
        }
    }
    qiwi_auth = ""

class Other:
    shard_count = 1
    slash = None
    premium_cost = 99
    invoice_lifetime = 360 # в минутах
    p2p = None
    uptime = 0
