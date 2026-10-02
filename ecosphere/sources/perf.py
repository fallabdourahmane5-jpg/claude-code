#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Optimisations de temps de chargement — strictement iso-comportement."""
import io, sys

SRC = 'app_v186.html'
DST = 'app_v188.html'

s = io.open(SRC, encoding='utf-8').read()
L = s.split('\n')


def rep(line_no, old, new):
    """Remplace `old` par `new` dans la ligne 1-indexée line_no."""
    i = line_no - 1
    assert old in L[i], 'ANCRE ABSENTE ligne %d : %r / trouvé %r' % (line_no, old[:60], L[i][:120])
    L[i] = L[i].replace(old, new, 1)


# ---------------------------------------------------------------- 1. decodeHtmlEntities
# createElement('textarea') + innerHTML à chaque appel (1 356 ms au profil).
assert L[2276].strip() == 'function decodeHtmlEntities(str){'
assert L[2277].strip() == "const t=document.createElement('textarea');"
assert L[2278].strip() == 't.innerHTML=str;'
assert L[2279].strip() == 'return t.value;'
assert L[2280].strip() == '}'
L[2276:2281] = [
    'var __ecoDheTA=null, __ecoDheC=new Map();',
    'function decodeHtmlEntities(str){',
    "  var k=(str===null)?'':String(str);",
    '  var v=__ecoDheC.get(k);',
    '  if(v!==undefined) return v;',
    "  if(!__ecoDheTA) __ecoDheTA=document.createElement('textarea');",
    '  __ecoDheTA.innerHTML=k;',
    '  v=__ecoDheTA.value;',
    '  if(__ecoDheC.size>40000) __ecoDheC.clear();',
    '  __ecoDheC.set(k,v);',
    '  return v;',
    '}',
]
delta = 12 - 5


def ln(n):
    """ligne d'origine -> ligne courante"""
    return n + delta if n > 2281 else n


# ---------------------------------------------------------------- 2. regex dormante
# /<(h[34])>(.*?)<\/ >.../ exige littéralement la sous-chaîne "</ >" : elle
# n'apparaît dans aucun cours, la regex ne produit donc jamais de carte, mais
# son backtracking coûte 988 ms. Garde exacte : pas de "</ >" => aucun match.
i = ln(2348) - 1
assert 'matchAll(/<(h[34])>' in L[i], L[i][:140]
L[i] = "  if(html.indexOf('</ >')<0) return cards;\n" + L[i]

# ---------------------------------------------------------------- 3. norm() global (3046-3055)
i0, i1 = ln(3046) - 1, ln(3055) - 1
assert L[i0].strip() == 'function norm(s){', L[i0]
assert L[i1].strip() == '}', L[i1]
L[i0] = L[i0].replace('function norm(s){', 'function __ecoNormRaw(s){', 1)
L[i1] = L[i1] + """
var __ecoNormC=new Map();
function norm(s){
  var k=String(s||'');
  var v=__ecoNormC.get(k);
  if(v===undefined){ if(__ecoNormC.size>80000) __ecoNormC.clear(); v=__ecoNormRaw(k); __ecoNormC.set(k,v); }
  return v;
}"""

# ---------------------------------------------------------------- 4. stripHTML (3057-3073)
j0, j1 = ln(3057) - 1, ln(3073) - 1
assert L[j0].strip() == 'function stripHTML(html){', L[j0]
assert L[j1].strip() == '}', L[j1]
L[j0] = L[j0].replace('function stripHTML(html){', 'function __ecoStripRaw(html){', 1)
L[j1] = L[j1] + """
var __ecoStripC=new Map(), __ecoStripPoids=0;
function stripHTML(html){
  var k=String(html||'');
  var v=__ecoStripC.get(k);
  if(v!==undefined) return v;
  v=__ecoStripRaw(k);
  if(__ecoStripPoids>12000000){ __ecoStripC.clear(); __ecoStripPoids=0; }
  __ecoStripPoids+=v.length;
  __ecoStripC.set(k,v);
  return v;
}"""

# ---------------------------------------------------------------- 5. norm() du bloc V43 (7885)
k0 = ln(7885) - 1
old = L[k0]
assert old.startswith("function norm(s){return String(s||'').toLowerCase().normalize('NFD')"), old[:90]
assert old.rstrip().endswith('.trim();}'), old[-40:]
L[k0] = (old.replace('function norm(s){', 'function __ecoNormV43Raw(s){', 1) + """
var __ecoNormV43C=new Map();
function norm(s){
  var k=String(s||'');
  var v=__ecoNormV43C.get(k);
  if(v===undefined){ if(__ecoNormV43C.size>80000) __ecoNormV43C.clear(); v=__ecoNormV43Raw(k); __ecoNormV43C.set(k,v); }
  return v;
}""")

out = '\n'.join(L)
io.open(DST, 'w', encoding='utf-8').write(out)
print('OK %s -> %s  (%.2f Mo)' % (SRC, DST, len(out.encode('utf-8')) / 1048576.0))
