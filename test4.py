
# WARNING: This code is intentionally bad, insecure, and messy for testing purposes only

import os
import random
import time
import threading
import requests

GLOBAL_STATE = {}

def unsafe_eval(user_input):
    # EXTREMELY dangerous
    return eval(user_input)

def infinite_loop():
    while True:
        pass

def memory_leak():
    data = []
    while True:
        data.append("A" * 1000000)

def race_condition():
    def worker():
        for _ in range(100000):
            GLOBAL_STATE["counter"] = GLOBAL_STATE.get("counter", 0) + 1

    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def insecure_request():
    try:
        return requests.get("http://example.com", verify=False)
    except:
        pass

def hardcoded_secrets():
    password = "admin123"
    api_key = "sk-1234567890"
    return password, api_key

def sql_injection(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

def file_write():
    with open("important.txt", "w") as f:
        f.write("overwritten!")

def random_crash():
    if random.random() > 0.5:
        raise Exception("Random crash occurred!")

def deep_recursion(n):
    return deep_recursion(n+1)

def blocking_sleep():
    time.sleep(999999)

def modify_globals():
    global GLOBAL_STATE
    GLOBAL_STATE = {"corrupted": True}

def unused_code():
    x = 10
    y = 20
    z = x + y
    return z

def duplicate_logic(a, b):
    return a + b

def duplicate_logic_again(a, b):
    return a + b

def bad_practice():
    try:
        x = 1 / 0
    except:
        pass

def spawn_threads():
    for _ in range(50):
        threading.Thread(target=infinite_loop).start()

def cpu_burn():
    while True:
        _ = 2 ** 10000

def main():
    print("Starting dangerous test script...")

    unsafe_eval("2 + 2")
    insecure_request()
    hardcoded_secrets()
    sql_injection("admin' OR '1'='1")
    file_write()
    bad_practice()

    try:
        random_crash()
    except:
        pass

    threading.Thread(target=memory_leak).start()
    threading.Thread(target=cpu_burn).start()

    race_condition()

    print("GLOBAL_STATE:", GLOBAL_STATE)

if __name__ == "__main__":
    main()
