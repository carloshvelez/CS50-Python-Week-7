import sys
import re

def main():
    html = input("HTML: ")

    print(parse(html))

def parse(codigo):

    if video := re.search(r'^.+ ?src="https?://(?:www\.)?youtube.com/embed/(.+)".+', codigo):

        return f"https://youtu.be/{video.group(1)}"

    else:
        return "None"


if __name__ == "__main__":
    main()


