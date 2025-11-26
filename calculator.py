# simple CLI calculator
import sys

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

def main():
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <add|sub|mul|div> a b")
        sys.exit(2)
    cmd, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    ops = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    if cmd not in ops:
        print("Unknown op")
        sys.exit(2)
    print(ops[cmd](a, b))

if __name__ == "__main__":
    main()
