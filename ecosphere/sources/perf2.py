#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Étape 2 : les trois balayages `body *` qui lisent textContent sur 76 000 nœuds."""
import io

SRC = 'app_v188.html'
DST = 'app_v189.html'

L = io.open(SRC, encoding='utf-8').read().split('\n')

HELPER = """<script>
/* ============================================================
   PERF — balayages « body * » du nettoyage de l'en-tête
   Les trois boucles concernées comparent textContent.trim() à des chaînes
   courtes. Lire textContent sur chacun des ~76 000 éléments reconstruit le
   texte de tout le sous-arbre (plusieurs Mo par conteneur de page) : ~1 s.
   __ecoSmall(limite) renvoie, dans l'ordre du document, les éléments dont le
   nombre de caractères NON blancs du sous-arbre est <= limite. Comme
   textContent.trim().length >= ce nombre, aucun élément susceptible d'égaler
   une chaîne de longueur <= limite n'est écarté : le résultat des boucles est
   identique, seul le coût change. Le comptage se fait en une passe ascendante
   sans concaténer aucune chaîne, avec arrêt dès que la limite est dépassée.
   ============================================================ */
window.__ecoSmall = function(limite){
  var els = document.querySelectorAll('body *');
  var cap = limite + 1, out = [], i, el, c, t, d;
  for(i = els.length - 1; i >= 0; i--){          // enfants avant parents
    el = els[i]; t = 0;
    for(c = el.firstChild; c; c = c.nextSibling){
      if(c.nodeType === 3){
        d = c.data;
        /* trim() natif : la somme des longueurs rognées nœud par nœud reste
           <= textContent.trim().length, donc toujours une borne inférieure. */
        t += d.trim().length;
      } else if(c.nodeType === 1){
        t += (c.__ecoLen || 0);
      } else if(c.nodeType === 4){
        t += c.data.trim().length;
      }
      if(t >= cap){ t = cap; break; }
    }
    el.__ecoLen = t;
    if(t <= limite) out.push(el);
  }
  out.reverse();                                  // ordre du document
  return out;
};
</script>
"""

def trouve(frag, apres=0):
    for j in range(apres, len(L)):
        if frag in L[j]:
            return j
    raise AssertionError('ANCRE ABSENTE : %r' % frag[:70])


# les trois boucles, reperees par leur contexte unique
iA = trouve("if (t === 'CLASSE PRÉPARATOIRE • TOUS LES CHAPITRES') {")
iB = trouve("if (t === 'Abdourahmane') {")
iC = trouve("const all = Array.from(document.querySelectorAll('body *'));")

# 'CLASSE PRÉPARATOIRE • TOUS LES CHAPITRES' = 40 caracteres
jA = iA - 2
assert L[jA].strip() == "document.querySelectorAll('body *').forEach(el => {", L[jA]
L[jA] = L[jA].replace("document.querySelectorAll('body *')", '__ecoSmall(40)', 1)
# 'Abdourahmane' = 12 caracteres
jB = iB - 2
assert L[jB].strip() == "document.querySelectorAll('body *').forEach(el => {", L[jB]
L[jB] = L[jB].replace("document.querySelectorAll('body *')", '__ecoSmall(12)', 1)
# test t.length < 140  ->  limite 139
L[iC] = L[iC].replace("Array.from(document.querySelectorAll('body *'))", '__ecoSmall(139)', 1)

# le helper est pose juste avant le <script> qui ouvre le premier bloc concerne
iS = max(j for j in range(0, min(jA, jB, iC)) if L[j].strip() == '<script>')
L[iS] = HELPER + L[iS]

out = '\n'.join(L)
io.open(DST, 'w', encoding='utf-8').write(out)
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(out.encode('utf-8')) / 1048576.0))
