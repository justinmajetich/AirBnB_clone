#!/usr/bin/python3

if __name__ == "__main__":
    strings = input("Please type in inputs\n")
    string_list = strings.split()
    kvp_dict = {}
    for i in range(len(string_list)):
        kvp = string_list[i].partition("=")
        key = kvp[0]
        value = kvp[2]
        if value[0] == value[-1] and value[0] == '"':
            value = value[1:-1]
            print(f"New Value: {value}")
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    continue
        print(type(value))
        kvp_dict[key] = value

    print(kvp_dict)
