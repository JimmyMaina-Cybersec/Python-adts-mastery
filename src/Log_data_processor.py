# Extract timestamp, IP, method, endpoint, and collect all parameters into a list
log_entries = [
    (
        "2023-06-01 10:30:15",
        "192.168.1.100",
        "GET",
        "/api/users",
        "param1=value1",
        "param2=value2",
        "param3=value3",
    ),
    (
        "2023-06-01 10:31:22",
        "10.0.0.50",
        "POST",
        "/api/login",
        "username=john",
        "password=***",
    ),
    ("2023-06-01 10:32:45", "172.16.0.25", "DELETE", "/api/posts/123"),
]


def first(timestamp, ip, method, endpoint, *params):
    print(timestamp, ip, method, endpoint, *params)


def second(timestamp, ip, method, endpoint, username, password):
    print(timestamp, ip, method, endpoint, username, password)


def third(timestamp, ip, method, endpoint):
    print(timestamp, ip, method, endpoint)


if __name__ == "__main__":
    try:
        for entry in log_entries:
            if entry[0] == "2023-06-01 10:30:15":
                (timestamp, *lastArgs) = log_entries[0]
                first(timestamp, *lastArgs)
            elif entry[0] == "2023-06-01 10:31:22":
                (timestamp, *lastArgs) = log_entries[1]
                second(timestamp, *lastArgs)
            else:
                (timestamp, *lastArgs) = log_entries[2]
                third(timestamp, *lastArgs)
    except ValueError as e:
        print(e)
