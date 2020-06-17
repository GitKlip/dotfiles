def find_dict_diff(d1: dict, d2: dict, path=""):
    for k in d1:
        if k not in d2:
            print(f"{path}:")
            print(f"{k} as key not in d2")
        else:
            if type(d1[k]) is dict:
                if path == "":
                    path = k
                else:
                    path = f"{path} -> {k}"
                findDiff(d1[k],d2[k], path)
            else:
                if d1[k] != d2[k]:
                    print(f"{path}:")
                    print(f" - {k} : {d1[k]}")
                    print(f" + {k} : {d2[k]}")
