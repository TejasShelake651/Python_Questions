# Multiple Exceptions and try-except-else-finally flow

def test_division():
    print("ZeroDivisionError & Full try-except-else-finally flow:")
    for denom in [0, 5]:
        try:
            print(f"Attempting 100 / {denom}:")
            res = 100 / denom
        except ZeroDivisionError:
            print("  -> Caught ZeroDivisionError: You cannot divide by zero!")
        else:
            print(f"  -> Else block executed! Result = {res}")
        finally:
            print("  -> Finally block executed: Clean up finished.")


def test_index():
    print("\nIndexError:")
    try:
        sample_list = [10, 20, 30]
        _ = sample_list[10]
    except IndexError as e:
        print("  -> Caught IndexError:", e)


def test_file_not_found():
    print("\nFileNotFoundError:")
    try:
        with open("non_existent_file_xyz123.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print("  -> Caught FileNotFoundError:", e)


if __name__ == "__main__":
    test_division()
    test_index()
    test_file_not_found()
