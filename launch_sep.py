import sys
import subprocess as sb

if __name__ == '__main__':
    args = sys.argv
    if not args:
        sb.Popen(args = "python3 ./app_main.py".split())
    else:
        print(f"executing python3 ./{args[1]}")
        sb.Popen(args = f"python3 ./{args[1]}".split())
    sys.exit(0)
