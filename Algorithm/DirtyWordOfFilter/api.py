# api.py

import os
import json

HERE = os.path.realpath(__file__).strip()[:-6]


class DFAFilter(object):
    def __init__(self):
        self.keyword_chains = {}
        with open(os.path.join(HERE, 'static', 'WordLibrary.json'), 'r', encoding='utf-8') as f:
            self.keyword_chains = json.loads(f.read())
        self.delimit = '\x00'

    def filter(self, message, word_re="*"):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        if step_ins == 1:
                            level = level[char]
                        else:
                            ret.append(word_re * step_ins)
                            start += step_ins - 1
                            break
                    else:
                        ret.append(word_re * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)
