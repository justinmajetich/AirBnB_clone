#!/usr/bin/python3

if __name__ == "__main__":
    strings = input("Please type in inputs\n")
    string_list = strings.split()
    print(string_list)
    for i in range(len(string_list)):
        kvp = string_list[i].split("=")
        key = kvp[0]
        value = kvp[1]
        print(f"{key}: {value:}")
