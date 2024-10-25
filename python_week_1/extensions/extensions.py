def main():
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    file_name = input("file: ").lower().strip()

    if "." in file_name:
        suffix = file_name[file_name.rindex("."):]
    else:
        suffix = ""

    if suffix in media_types:
        print(media_types[suffix])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()








