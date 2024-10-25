import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    youtube_pattern = r'src=(?:"|\')https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)(?:"|\')'

    match = re.search(youtube_pattern, s)


    if match:
        video_id =match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None



if __name__ == "__main__":
    main()
