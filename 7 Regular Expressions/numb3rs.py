import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        octets = ip.split(".")
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()