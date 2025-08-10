import os
import subprocess

def main():
    for filename in os.listdir("."):
        if not os.path.isfile(filename):
            continue
        if filename.startswith("Ninjabrain") and filename.endswith(".jar"):
            subprocess.run(["javaw", "-jar", filename])
            break

if __name__ == "__main__":
    main()
