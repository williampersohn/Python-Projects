import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if url := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"', s):
        ret = ("https://youtu.be/" + url.group(1))
        return ret
    return None



...

if __name__ == "__main__":
    main()
