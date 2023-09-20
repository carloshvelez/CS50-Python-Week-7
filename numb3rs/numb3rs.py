import re
import sys

def main():
    ip = input("IPv4 Address: ")

    if validate(ip):
        print("True")
    else:
        print("False")



def validate(ip):
    if coincide := re.search (r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3}).(\d{1,3})$", ip):

        a, b, c, d = coincide.groups()

        print(a,b,c,d)

        if 0 <= int(a) <= 255 and 0 <= int(b) <= 255 and 0 <= int(c) <= 255 and 0 <= int(d) <= 255:
            return True


    return False


if __name__ == "__main__":
    main()
