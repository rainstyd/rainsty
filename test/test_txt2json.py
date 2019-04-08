# test_txt2json.py


def main():
    dict = {}
    with open('../file/sq2.txt', 'r', encoding='utf-8') as r:
        for line in r.readlines():
            line = line[:-1].split(',')
            if line[0] not in dict:
                    dict[line[0]] = {}
        r.seek(0)

        for line in r.readlines():
            line = line[:-1].split(',')
            if line[0] in dict:
                if line[1] not in dict[line[0]]:
                    dict[line[0]][line[1]] = {}

        r.seek(0)

        for line in r.readlines():
            line = line[:-1].split(',')
            if line[0] in dict:
                if line[1] in dict[line[0]]:
                    if line[2] not in dict[line[0]][line[1]] and line[2] != '':
                        dict[line[0]][line[1]][line[2]] = {}
                    elif line[2] not in dict[line[0]][line[1]] and line[2] == '':
                        dict[line[0]][line[1]]['return'] = 0

        r.seek(0)

        for line in r.readlines():
            line = line.replace('\n', '').split(',')
            if line[0] in dict:
                if line[1] in dict[line[0]]:
                    if line[2] in dict[line[0]][line[1]]:
                        if 'return' in dict[line[0]][line[1]]:
                            del dict[line[0]][line[1]]['return']
                        if line[3] not in dict[line[0]][line[1]][line[2]] and line[3] != '':
                            dict[line[0]][line[1]][line[2]][line[3]] = {'return': 0}
                        elif line[3] not in dict[line[0]][line[1]][line[2]] and line[3] == '':
                            dict[line[0]][line[1]][line[2]]['return'] = 0
    import json
    print(json.dumps(dict, separators=(',', ':'), ensure_ascii=False, indent=4))
    with open('../file/WordLibrary_test.json', 'w', encoding='utf-8') as w:
        w.write(json.dumps(dict, separators=(',', ':'), ensure_ascii=False, indent=4))


if __name__ == '__main__':
    main()
