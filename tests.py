from functions.run_python_file import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    # print("Result for calculator/main.py:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    # print("Result for calculator/tests.py:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    # print("Result for ../main.py:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    # print("Result for nonexistent.py:")
    print(result)



    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for lorem.txt:")
    # print(result)
    # print("")

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for pkg/morelorem.txt:")
    # print(result)
    # print("")

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for pkg/morelorem.txt:")
    # print(result)
    # print("")


if __name__ == "__main__":
    test()
