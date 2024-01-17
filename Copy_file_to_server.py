
#!C:/Users/<user>/AppData/Local/Programs/Python/<python_version>/python.exe
# -*- coding: utf-8 -*-
import os
import shutil
import sys


def normalize_path(path):
    # Check if the path has a drive letter without '$' sign, and add it if necessary
    if len(path) > 1 and path[1] == ':':
        if not path.startswith("\\\\"):
            path = "\\" + path
        if path[2] != '$':
            path = path[:2] + "$" + path[2:]
    return path


def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def copy_file(source, destination):
    # Normalize the paths to handle drive letters without '$' sign
    # source = normalize_path(source_path)
    # destination = normalize_path(destination_path)
    if os.path.isfile(source):
        try:
            total_size = os.path.getsize(source)
            copied_size = 0
            block_size = 64 * 1024  # 64 KB block size

            with open(source, 'rb') as src_file, open(destination, 'wb') as dest_file:
                while True:
                    block = src_file.read(block_size)
                    if not block:
                        break
                    dest_file.write(block)
                    copied_size += len(block)
                    copied_percent = min(100, int((copied_size / total_size) * 100))
                    sys.stdout.write("\r[" + "=" * int(copied_percent) + ">" + " " * (
                            100 - int(copied_percent)) + f"] {copied_percent}%")
                    sys.stdout.flush()

            print("\n[INFO] Copy", os.path.basename(source), "to", os.path.basename(destination), "successful..!")
        except Exception as e:
            print(f"[ERROR] An error occurred: {str(e)}")
            return


def copy_directory(source_path, destination_path):
    # Normalize the paths to handle drive letters without '$' sign
    # source = normalize_path(source_path)
    # destination = normalize_path(destination_path)
    try:
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        total_size = get_directory_size(source_path)
        copied_size = 0

        for item in os.listdir(source_path):
            source_path = os.path.join(source_path, item)
            destination_path = os.path.join(destination_path, item)

            if os.path.isdir(source_path):
                # If it's a directory, recursively copy it
                copy_directory(source_path, destination_path)
            else:
                # If it's a file, copy it
                shutil.copy2(source_path, destination_path)
                copied_size += os.path.getsize(source_path)
                copied_percent = min(100, int((copied_size / total_size) * 100))
                sys.stdout.write("\r[" + "=" * int(copied_percent) + ">" + " " * (
                        100 - int(copied_percent)) + f"] {copied_percent}%")
                sys.stdout.flush()

        print("\n[INFO] Copy", os.path.basename(source), "to", os.path.basename(destination), "successful..!")
    except Exception as e:
        print(f"[ERROR] An error occurred: {str(e)}")


if __name__ == "__main__":
    terminal_width = 0
    try:
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
    except OSError:
        terminal_width = 100
    print("=" * terminal_width)
    source = input("[INPUT] Enter the source path: ")
    print("=" * terminal_width)
    destination = input("[INPUT] Enter the destination path: ")
    print("*" * terminal_width)
    block_size = 64 * 1024  # 64 KB block size

    if os.path.isdir(source):
        copy_directory(source, destination)
    elif os.path.isfile(source):
        copy_file(source, destination)
    else:
        print(f"[ERROR] {source} does not exist.")
