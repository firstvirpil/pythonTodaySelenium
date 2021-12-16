import easyocr

# то работает но ругается Shadows name 'file_path' from outer scope

file_path = input("Enter a file path: ")
file_name = file_path.split('.')[0]


def text_recognition(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=0)

    return result


def main():
    # file_path = input("Enter a file path: ")
    # print(text_recognition(file_path=file_path))
    return ''.join(text_recognition(file_path=file_path))


# a = main()
# b = ''.join(a)

with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(main())

if __name__ == "__main__":
    main()
