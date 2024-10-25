def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return face

def main():
    user_input = input("user: ")
    response =convert(user_input)
    print(response)

if __name__=="__main__":
    main()









