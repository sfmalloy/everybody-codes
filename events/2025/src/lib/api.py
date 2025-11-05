import json
import os
from base64 import b16decode
from pathlib import Path
from typing import Any

import httpx
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

API_URL = 'https://everybody.codes/api'
CDN_URL = 'https://everybody-codes.b-cdn.net'
USER_AGENT = 'email:sfmalloy.dev@gmail.com repo:github.com/sfmalloy/everybody-codes'


def download(event: int, quest: int, part: int):
    seed = __get_seed()
    encrypted = __get_encrypted_input(event, quest, part, seed)
    key = __get_aes_key(event, part, quest)
    decrpyted = __decrypt_input(key, encrypted)
    with open(f'inputs/quest{quest:02d}/part{part}.txt', 'w') as f:
        f.write(decrpyted)
    print('Downloaded input successfully')


def __get_seed():
    path = Path('inputs/me.json')
    if path.exists():
        with path.open() as f:
            me = json.load(f)
            return me.get('seed')

    res = httpx.get(
        f'{API_URL}/user/me',
        headers={'User-Agent': USER_AGENT},
        cookies={'everybody-codes': os.getenv('EC_SESSION')},
    )
    data = __cache_response(path, res)
    return data.get('seed')


def __get_encrypted_input(event: int, quest: int, part: int, seed: int):
    path = Path(f'inputs/quest{quest:02d}/encrypted.json')
    if path.exists():
        with path.open() as f:
            data = json.load(f)
            return data.get(str(part))

    res = httpx.get(f'{CDN_URL}/assets/{event}/{quest}/input/{seed}.json')
    data = __cache_response(path, res)
    return data.get(str(part))


def __get_aes_key(event: int, part: int, quest: int):
    path = Path(f'inputs/quest{quest:02d}/keys.json')
    if path.exists():
        with path.open() as f:
            data = json.load(f)
            return data.get(f'key{part}')

    res = httpx.get(
        f'{API_URL}/event/{event}/quest/{quest}',
        headers={'User-Agent': USER_AGENT},
        cookies={'everybody-codes': os.getenv('EC_SESSION')},
    )
    data = __cache_response(path, res)
    return data.get(f'key{part}')


def __decrypt_input(key: str, encrypted: str) -> str:
    encrypted_bytes = b16decode(encrypted.upper())
    key_bytes = key.encode()
    iv_bytes = key_bytes[:16]

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv_bytes)
    return unpad(cipher.decrypt(encrypted_bytes), 16).decode(encoding='utf-8')


def __cache_response(path: Path, res: httpx.Response) -> Any:
    data = res.json()
    with path.open('w') as f:
        json.dump(data, f, indent=4)
    return data
