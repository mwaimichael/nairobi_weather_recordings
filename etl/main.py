from load import load


if __name__ == '__main__':
    try:
        load()
        print("Loaded Successfully!")
    except Exception as e:
        print(e)

