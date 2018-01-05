import sys

def main():

    file_name = sys.argv[1]
    f = open(file_name, "r")

    tokens = []
    x = 0
    with open(file_name) as f:
        lines = f.read().splitlines()
        for line in lines:
                x = x + 1
                print x, line
    f.close()

if __name__ == "__main__":
    main()
