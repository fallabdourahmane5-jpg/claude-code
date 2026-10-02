#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Étape 3 : les deux MutationObserver de relibellage re-parcourent la totalité
des conteneurs de page à chaque lot de mutations. Pendant le démarrage, les
rendus produisent des centaines de lots : on regroupe les appels (debounce
50 ms) sans toucher à la logique de relibellage elle-même — même parcours,
même ordre, simplement une passe par rafale au lieu d'une par lot."""
import io

SRC = 'app_v189.html'
DST = 'app_v190.html'

L = io.open(SRC, encoding='utf-8').read().split('\n')


def trouve(frag, apres=0):
    for j in range(apres, len(L)):
        if frag in L[j]:
            return j
    raise AssertionError('ANCRE ABSENTE : %r' % frag[:80])


HELPER = """/* PERF — regroupement des passes de relibellage (une par rafale de mutations) */
if(!window.__ecoGroupe){
  window.__ecoGroupe = function(cle, fn){
    var enAttente = false;
    return function(){
      if(enAttente) return;
      enAttente = true;
      setTimeout(function(){ enAttente = false; try{ fn(); }catch(e){} }, 50);
    };
  };
}
"""

# ---------- couche « Chapitre 22 » -> « Deuxième année — Chapitre 2 » ----------
i = trouve("if(el) new MutationObserver(function(){ relibeller(el); })")
old = "new MutationObserver(function(){ relibeller(el); })"
new = "new MutationObserver(window.__ecoGroupe(id, function(){ relibeller(el); }))"
assert old in L[i]
L[i] = L[i].replace(old, new, 1)

# ---------- couche « Chapitre 21 » -> « 2ᵉ année — Chapitre 1 » ----------
j = trouve('      var mo = new MutationObserver(function(){')
assert L[j + 1].strip() == 'if(enCours) return;', L[j + 1]
assert L[j + 2].strip() == 'enCours = true;', L[j + 2]
assert L[j + 3].strip() == 'try{ relabelNode(el); } finally { enCours = false; }', L[j + 3]
assert L[j + 4].strip() == '});', L[j + 4]
L[j:j + 5] = [
    '      var mo = new MutationObserver(window.__ecoGroupe(sel, function(){',
    '        if(enCours) return;',
    '        enCours = true;',
    '        try{ relabelNode(el); } finally { enCours = false; }',
    '      }));',
]

# le helper est posé en tête du premier des deux blocs <script> concernés
iS = max(k for k in range(0, min(i, j)) if L[k].strip() == '<script>')
L[iS] = L[iS] + '\n' + HELPER

out = '\n'.join(L)
io.open(DST, 'w', encoding='utf-8').write(out)
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(out.encode('utf-8')) / 1048576.0))
