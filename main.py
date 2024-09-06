import linecache
import os
import time

import requests, json
from winotify import Notification
import tracemalloc

import config

test_response = ("{\"status\":{\"timestamp\":\"2024-09-05T09:55:25.205Z\",\"error_code\":0,\"error_message\":null,"
                 "\"elapsed\":41,\"credit_count\":1,\"notice\":null},\"data\":{\"id\":20396,\"symbol\":\"KAS\","
                 "\"name\":\"Kaspa\",\"amount\":1,\"last_updated\":\"2024-09-05T09:53:00.000Z\",\"quote\":{\"USD\":{"
                 "\"price\":0.15029155497222327,\"last_updated\":\"2024-09-05T09:53:00.000Z\"}}}}")
response_counter = 0


def get_response():
    request1 = requests.request("GET", url=config.URL, params=config.PARAMS, headers=config.HEADER)
    content1 = json.dumps(request1.text, indent=4, sort_keys=True, default=lambda o: '<not serializable>')
    return str(content1)


def get_kas_price(json_content):
    global response_counter
    content1 = json.loads(json_content)
    kas_price = content1["data"]["quote"]["USD"]["price"]
    response_counter += 1
    return kas_price


def check_counter():
    global response_counter
    if response_counter >= 322:
        return True
    else:
        return False


def get_system_time():
    seconds_from_epoch = int(time.time())
    seconds = seconds_from_epoch % (24 * 3600)
    hour = str(seconds // 3600 + 3)
    if hour == "24":
        hour = "0"
    elif hour == "25":
        hour = "1"
    elif hour == "26":
        hour = "2"
    seconds %= 3600
    minutes = str(seconds // 60)
    if minutes == "0":
        minutes = "00"
    seconds %= 60
    time1 = hour + ":" + minutes
    return time1


def check_time():
    global response_counter
    time1 = get_system_time()
    match time1:
        case "0:00":
            response_counter = 0
            return True
        case "1:00":
            return True
        case "2:00":
            return True
        case "3:00":
            return True
        case "4:00":
            return True
        case "5:00":
            return True
        case "6:00":
            return True
        case "7:00":
            return True
        case "8:00":
            return True
        case "9:00":
            return True
        case "10:00":
            return True
        case "11:00":
            return True
        case "12:00":
            return True
        case "13:00":
            return True
        case "14:00":
            return True
        case "15:00":
            return True
        case "16:00":
            return True
        case "17:00":
            return True
        case "18:00":
            return True
        case "19:00":
            return True
        case "20:00":
            return True
        case "21:00":
            return True
        case "22:00":
            return True
        case "23:00":
            return True
        case _:
            return False


def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


def main():
    # tracemalloc.start()
    notif = Notification(app_id="Crypto widget", title="Process started", msg="Process is running in background",
                           duration="short")
    notif.show()
    while True:
        a = check_time()
        if a == True:
            if check_counter() == False:
                kp1 = str(round(get_kas_price(json.loads(get_response())), 5))
                notif = Notification(app_id="Crypto widget", title="KAS price", msg=kp1, duration="short")
                notif.show()
        time.sleep(60)
        # snapshot = tracemalloc.take_snapshot()
        # display_top(snapshot)
        # tracemalloc.stop()


if __name__ == "__main__":
    main()
