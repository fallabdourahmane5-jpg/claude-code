# -*- coding: utf-8 -*-
"""Remplace, dans un fichier de dossiers, des chaînes littérales trop courtes
par une version rallongée, en recollant les concaténations implicites."""
import sys, json

def runs_de(t):
    runs, i, n = [], 0, len(t)
    while i < n:
        if t[i] == '"':
            start, lits = i, []
            while i < n and t[i] == '"':
                j = i + 1
                while j < n and t[j] != '"':
                    if t[j] == '\\':
                        j += 1
                    j += 1
                lits.append(t[i + 1:j])
                i = j + 1
                k = i
                while k < n and t[k] in ' \n\t':
                    k += 1
                if k < n and t[k] == '"':
                    i = k
                else:
                    break
            runs.append((start, i, ''.join(lits)))
        else:
            i += 1
    return runs

def appliquer(fichier, table):
    t = open(fichier, encoding='utf-8').read()
    n = 0
    for start, end, val in reversed(runs_de(t)):
        if val in table:
            t = t[:start] + '"' + table[val].replace('"', '\\"') + '"' + t[end:]
            n += 1
    open(fichier, 'w', encoding='utf-8').write(t)
    return n

if __name__ == '__main__':
    fichier, table = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
    print('remplacés', appliquer(fichier, table))
