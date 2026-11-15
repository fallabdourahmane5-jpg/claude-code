#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remplace entièrement la section « Recherche » d'ÉcoSphère.

v220 : la présentation des résultats est refaite (hiérarchie de la
réponse, mise en évidence discrète, « à ne pas confondre » lisible,
« où le retrouver » groupé par section, cadres allégés). Le moteur,
les définitions et les destinations sont ceux de la v219.

L'ancienne page et son moteur sont retirés : le balisage de #pg-search est
remplacé, et les fonctions de l'ancien index (doSearch, setF,
rebuildSearchIndex) sont neutralisées. Le nouveau moteur n'exploite plus
l'ancien tableau SEARCH_INDEX.

La nouvelle recherche travaille sur deux ensembles :
  — une charge de données embarquée, montée par rech_payload.py : définitions
    moissonnées dans les cours ou rédigées, sections des chapitres, formules,
    faits datés, dossiers d'« Autour d'une notion », idées de l'Atlas,
    chiffres et résumés ;
  — les contenus déjà présents en mémoire : notions de chapitre, fiches,
    auteurs, sujets, visualisations, page Formules, et surtout le texte même
    des cours, découpé en blocs au premier usage pour permettre la recherche
    de passages et l'ouverture du paragraphe exact.
"""
import io
import json
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v217.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v220.html'

s = io.open(SRC, encoding='utf-8').read()
assert s.rstrip().endswith('</script>')
assert 'eco-recherche-v218' not in s

DATA = json.load(open('recherche_payload.json'))

# --------------------------------------------------------------------- balisage
# l'ancienne page est retirée et remplacée
DEBUT = '<!-- SEARCH -->\n<div class="pg" id="pg-search">'
i = s.index(DEBUT)
j = s.index('<!-- AUTHORS -->', i)
ANCIEN = s[i:j]
assert 'doSearch()' in ANCIEN and len(ANCIEN) < 4000, len(ANCIEN)

NOUVEAU = '''<!-- RECHERCHE (v219) -->
<div class="pg" id="pg-search">
<div class="rq-wrap">
  <div class="rq-top">
    <h1 class="rq-h1">Recherche</h1>
    <p class="rq-sub">La réponse d’abord, les passages ensuite.</p>
  </div>
  <div class="rq-zone">
    <div class="rq-bar">
      <span class="rq-ic">🔍</span>
      <input class="rq-in" id="rq-in" type="text" autocomplete="off"
        spellcheck="false" aria-autocomplete="list"
        placeholder="Une notion, un auteur, une formule, un chiffre…">
      <button class="rq-x" id="rq-x" title="Effacer" aria-label="Effacer">✕</button>
    </div>
    <div class="rq-sug" id="rq-sug" role="listbox"></div>
  </div>
  <div id="rq-rep"></div>
  <div id="rq-fam"></div>
  <div class="rq-outils" id="rq-outils"></div>
  <div id="rq-res"></div>
</div>
</div>

'''
s = s[:i] + NOUVEAU + s[j:]

STYLE = r"""
<style id="eco-recherche-style-v220">
/* ÉcoSphère — recherche : présentation des résultats.
   La section suit désormais la palette sombre de l'application : plus de
   variante claire, qui faisait apparaître une page blanche au milieu d'une
   interface sombre. Les séparations reposent sur l'espace et la typographie
   plutôt que sur des cadres. */
#pg-search{
  --rq-c:#131720; --rq-c2:#171d2b;
  --rq-b:#242d42; --rq-b2:#1c2335;
  --rq-t:#e8eaf2; --rq-t2:#9ba5bf; --rq-t3:#78839e;
  --rq-a:#7c6af7; --rq-a2:#b3a4ff; --rq-af:rgba(124,106,247,.14);
  --rq-mi:#6af7c4; --rq-or:#f7a26a; --rq-ye:#e9ce7a; --rq-ro:#f78da8;
  --rq-om:0 1px 2px rgba(0,0,0,.25);
  --rq-oh:0 18px 44px rgba(0,0,0,.45);
}
#pg-search .rq-wrap{max-width:860px;margin:0 auto;padding:30px 20px 110px}
#pg-search .rq-top{display:flex;align-items:baseline;gap:13px;flex-wrap:wrap;
  margin-bottom:18px}
#pg-search .rq-h1{font-family:'Playfair Display',serif;font-size:1.9rem;
  font-weight:900;margin:0;color:var(--rq-t);letter-spacing:-.015em}
#pg-search .rq-sub{color:var(--rq-t3);font-size:.84rem;margin:0}

/* ---------------------------------------------------- barre de recherche */
#pg-search .rq-zone{position:relative;z-index:30;margin-bottom:26px}
#pg-search .rq-bar{display:flex;align-items:center;gap:10px;
  background:var(--rq-c);border:1px solid var(--rq-b);border-radius:14px;
  padding:3px 14px;transition:border-color .18s,box-shadow .18s,background .18s}
#pg-search .rq-bar:hover{border-color:#2e3a55}
#pg-search .rq-bar:focus-within{border-color:rgba(124,106,247,.6);
  background:var(--rq-c2);box-shadow:0 0 0 3px rgba(124,106,247,.12)}
#pg-search .rq-ic{font-size:.92rem;opacity:.5}
#pg-search .rq-in{flex:1;min-width:0;border:0;outline:0;background:transparent;
  font-family:inherit;font-size:1rem;color:var(--rq-t);padding:14px 2px}
#pg-search .rq-in::placeholder{color:var(--rq-t3)}
#pg-search .rq-x{border:0;background:transparent;color:var(--rq-t3);
  font-size:.86rem;cursor:pointer;padding:7px 4px;display:none;line-height:1;
  transition:color .15s}
#pg-search .rq-x.on{display:block}
#pg-search .rq-x:hover{color:var(--rq-t)}
#pg-search .rq-sug{display:none;position:absolute;left:0;right:0;
  top:calc(100% + 7px);background:var(--rq-c2);border:1px solid var(--rq-b);
  border-radius:13px;box-shadow:var(--rq-oh);overflow:hidden;max-height:360px;
  overflow-y:auto}
#pg-search .rq-sug.on{display:block}
#pg-search .rq-s{display:flex;align-items:center;gap:10px;padding:11px 15px;
  cursor:pointer;font-size:.88rem;color:var(--rq-t2);transition:background .13s}
#pg-search .rq-s + .rq-s{box-shadow:inset 0 1px 0 var(--rq-b2)}
#pg-search .rq-s:hover,#pg-search .rq-s.sel{background:var(--rq-af)}
#pg-search .rq-s b{color:var(--rq-t);font-weight:600}
#pg-search .rq-s:hover b,#pg-search .rq-s.sel b{color:var(--rq-a2)}
#pg-search .rq-s span{color:var(--rq-t3);font-size:.75rem;margin-left:auto;
  white-space:nowrap}

/* --------------------------------------------------------- la réponse */
#pg-search .rq-rep{max-width:700px;background:var(--rq-c);
  border:1px solid rgba(124,106,247,.22);border-radius:18px;
  padding:24px 30px 10px;margin-bottom:26px;
  box-shadow:0 14px 40px rgba(0,0,0,.3)}
#pg-search .rq-rep-k{display:flex;align-items:center;gap:7px;
  font-size:.64rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;
  color:var(--rq-a2);margin-bottom:12px}
#pg-search .rq-rep-k:before{content:"";width:5px;height:5px;border-radius:50%;
  background:var(--rq-a);box-shadow:0 0 0 3px rgba(124,106,247,.2)}
#pg-search .rq-rep-t{font-family:'Playfair Display',serif;font-size:1.62rem;
  font-weight:900;color:var(--rq-t);line-height:1.2;letter-spacing:-.01em;
  margin:0 0 7px}
#pg-search .rq-rep-m{display:flex;align-items:center;flex-wrap:wrap;gap:7px;
  font-size:.76rem;color:var(--rq-t3);margin-bottom:17px}
#pg-search .rq-rep-m i{font-style:normal;opacity:.45}
#pg-search .rq-rep-d{font-size:.95rem;line-height:1.78;color:var(--rq-t2);
  max-width:60ch}
#pg-search .rq-rep-d b{color:var(--rq-t);font-weight:600}

/* ------------------------------------------------- à ne pas confondre */
#pg-search .rq-conf{margin:20px 0 0;padding:13px 0 13px 15px;
  border-left:2px solid rgba(247,162,106,.6)}
#pg-search .rq-conf-t{font-size:.64rem;font-weight:800;letter-spacing:.11em;
  text-transform:uppercase;color:var(--rq-or);margin-bottom:8px}
#pg-search .rq-conf-d{font-size:.865rem;line-height:1.7;color:var(--rq-t);
  max-width:58ch}
#pg-search .rq-conf-d b{color:#f9c396;font-weight:600}
#pg-search .rq-conf-l{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:5px 14px}
#pg-search .rq-cf{display:inline-flex;align-items:baseline;gap:8px;border:0;
  justify-self:start;max-width:100%;
  background:transparent;font-family:inherit;font-size:.855rem;text-align:left;
  color:var(--rq-t);cursor:pointer;padding:4px 0;border-bottom:1px solid var(--rq-b2);
  transition:color .15s,border-color .15s}
#pg-search .rq-cf:hover{color:#f9c396;border-bottom-color:rgba(247,162,106,.5)}
#pg-search .rq-cf b{font-weight:600}
#pg-search .rq-cf i{font-style:normal;font-size:.72rem;color:var(--rq-t3);
  white-space:nowrap}

/* --------------------------------------------------- où le retrouver */
#pg-search .rq-ou{margin-top:22px;padding-top:4px}
#pg-search .rq-ou-t{display:flex;align-items:center;gap:8px;font-size:.63rem;
  font-weight:800;letter-spacing:.12em;text-transform:uppercase;
  color:var(--rq-t3);margin-bottom:4px}
#pg-search .rq-ou-t span{font-size:.68rem;letter-spacing:0;color:var(--rq-t3);
  opacity:.75}
#pg-search .rq-g{display:grid;grid-template-columns:112px minmax(0,1fr);
  gap:4px 16px;padding:10px 0;border-top:1px solid var(--rq-b2)}
#pg-search .rq-g-l{font-size:.75rem;color:var(--rq-t3);padding-top:2px}
/* une destination par ligne : deux titres de section mis côte à côte se
   lisaient comme une seule phrase */
#pg-search .rq-sg{display:flex;flex-direction:column;align-items:flex-start;
  gap:2px}
#pg-search .rq-sg + .rq-sg{margin-top:9px}
#pg-search .rq-sg-t{font-size:.71rem;font-weight:700;letter-spacing:.02em;
  color:var(--rq-t2);opacity:.85;margin-bottom:2px}
#pg-search .rq-o{border:0;background:transparent;font-family:inherit;
  font-size:.835rem;line-height:1.5;color:var(--rq-t2);cursor:pointer;
  padding:1px 0;text-align:left;max-width:100%;
  border-bottom:1px solid transparent;transition:color .15s,border-color .15s}
#pg-search .rq-o:hover{color:var(--rq-a2);border-bottom-color:rgba(124,106,247,.55)}
#pg-search .rq-cache{display:none}
#pg-search .rq-ou-plus{border:0;background:transparent;color:var(--rq-t3);
  font-size:.78rem;font-family:inherit;cursor:pointer;padding:1px 0;
  transition:color .15s}
#pg-search .rq-ou-plus:hover{color:var(--rq-a2)}
#pg-search .rq-g-c > .rq-ou-plus{display:block;margin-top:9px}

/* ------------------------------------------------------------ famille */
#pg-search .rq-fam{max-width:700px;margin:0 0 26px}
#pg-search .rq-fam-t{display:flex;align-items:center;gap:8px;font-size:.73rem;
  color:var(--rq-t3);margin-bottom:10px}
#pg-search .rq-fam-t b{color:var(--rq-t2);font-weight:600}
#pg-search .rq-fam-t span{font-size:.68rem;opacity:.7}
#pg-search .rq-fam-l{display:flex;flex-wrap:wrap;gap:7px}
#pg-search .rq-k{display:inline-flex;align-items:baseline;gap:6px;
  border:1px solid var(--rq-b);background:rgba(124,106,247,.05);
  border-radius:999px;padding:6px 13px;font-size:.805rem;font-family:inherit;
  color:var(--rq-t2);cursor:pointer;white-space:nowrap;
  transition:color .16s,border-color .16s,background .16s,transform .16s}
#pg-search .rq-k:hover{color:var(--rq-a2);border-color:rgba(124,106,247,.55);
  background:rgba(124,106,247,.13);transform:translateY(-1px)}
#pg-search .rq-k em{font-style:normal;color:var(--rq-t3);font-size:.72rem}
#pg-search .rq-k:hover em{color:var(--rq-a2);opacity:.75}

/* ------------------------------------------------------------- outils */
#pg-search .rq-outils{display:flex;align-items:center;gap:10px;flex-wrap:wrap;
  margin:0 0 6px;padding-bottom:10px}
#pg-search .rq-cpt{font-size:.79rem;color:var(--rq-t3)}
#pg-search .rq-cpt b{color:var(--rq-t2);font-weight:600}
#pg-search .rq-fl{display:flex;align-items:center;gap:2px;flex-wrap:wrap;
  margin-left:auto}
#pg-search .rq-f{border:0;background:transparent;font-family:inherit;
  font-size:.795rem;color:var(--rq-t3);cursor:pointer;padding:5px 10px;
  border-radius:8px;white-space:nowrap;transition:color .15s,background .15s}
#pg-search .rq-f:hover{background:var(--rq-b2);color:var(--rq-t)}
#pg-search .rq-f.on{background:var(--rq-af);color:var(--rq-a2);font-weight:600}
#pg-search .rq-f u{text-decoration:none;opacity:.5;font-size:.72rem;
  margin-left:5px}
#pg-search select.rq-sel{display:none;border:1px solid var(--rq-b);
  border-radius:9px;padding:8px 10px;font-family:inherit;font-size:.82rem;
  background:var(--rq-c);color:var(--rq-t2);max-width:58%}

/* ---------------------------------------------------------- résultats */
#pg-search .rq-bloc-t{display:flex;align-items:center;gap:10px;
  margin:22px 0 2px;font-size:.66rem;text-transform:uppercase;
  letter-spacing:.12em;font-weight:800;color:var(--rq-t3)}
#pg-search .rq-bloc-t:after{content:"";flex:1;height:1px;background:var(--rq-b2)}
#pg-search .rq-bloc-t em{font-style:normal;letter-spacing:0;font-weight:500;
  text-transform:none;font-size:.73rem;opacity:.8}
#pg-search .rq-r{border-radius:12px;background:transparent;
  box-shadow:inset 0 -1px 0 var(--rq-b2);
  transition:background .16s,box-shadow .16s}
#pg-search .rq-r:hover{background:rgba(124,106,247,.045)}
#pg-search .rq-r.ouvert{background:rgba(124,106,247,.06);
  box-shadow:inset 2px 0 0 var(--rq-a)}
#pg-search .rq-rh{display:grid;grid-template-columns:minmax(0,1fr) auto auto;
  align-items:baseline;gap:6px 14px;padding:13px 15px 5px;cursor:pointer}
#pg-search .rq-rt{min-width:0;font-size:.925rem;font-weight:600;
  color:var(--rq-t);line-height:1.45;transition:color .15s}
#pg-search .rq-r:hover .rq-rt{color:#fff}
#pg-search .rq-rt i{font-style:normal;font-weight:400;color:var(--rq-t3);
  font-size:.78rem}
#pg-search .rq-rm{display:flex;align-items:baseline;gap:9px;white-space:nowrap}
#pg-search .rq-ty{display:inline-flex;align-items:center;gap:6px;
  font-size:.7rem;color:var(--rq-t3);white-space:nowrap}
#pg-search .rq-ty:before{content:"";width:5px;height:5px;border-radius:50%;
  background:currentColor;flex:none;opacity:.9}
#pg-search .rq-ty.d{color:var(--rq-mi)}
#pg-search .rq-ty.p{color:var(--rq-a2)}
#pg-search .rq-ty.a{color:var(--rq-ro)}
#pg-search .rq-ty.c{color:var(--rq-ye)}
#pg-search .rq-ty.v{color:var(--rq-or)}
#pg-search .rq-ch{font-size:.73rem;color:var(--rq-t3)}
#pg-search .rq-car{color:var(--rq-t3);font-size:.9rem;line-height:1;
  transition:transform .2s,color .15s;align-self:center;opacity:.6}
#pg-search .rq-r:hover .rq-car{opacity:1;color:var(--rq-a2)}
#pg-search .rq-r.ouvert .rq-car{transform:rotate(90deg)}
/* la troncature à deux lignes n'admet pas de remplissage bas : il laisserait
   voir une troisième ligne coupée. L'écart passe donc par la marge. */
#pg-search .rq-ex{padding:0 15px;margin-bottom:13px;font-size:.845rem;
  line-height:1.65;color:var(--rq-t2);max-width:76ch;display:-webkit-box;
  -webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
#pg-search .rq-r.ouvert .rq-ex{display:block;-webkit-line-clamp:unset}
#pg-search .rq-corps{display:none;padding:2px 15px 16px}
#pg-search .rq-r.ouvert .rq-corps{display:block}
#pg-search .rq-corps .rq-conf{margin-top:4px}
#pg-search .rq-path{font-size:.75rem;color:var(--rq-t3);margin:12px 0 11px;
  padding-left:11px;border-left:1px solid var(--rq-b)}
#pg-search .rq-go{display:inline-flex;align-items:center;gap:8px;
  border:1px solid rgba(124,106,247,.45);background:rgba(124,106,247,.1);
  color:var(--rq-a2);border-radius:10px;padding:9px 15px;font-size:.82rem;
  font-family:inherit;font-weight:600;cursor:pointer;
  transition:background .16s,border-color .16s,color .16s}
#pg-search .rq-go:hover{background:var(--rq-a);border-color:var(--rq-a);
  color:#fff}
#pg-search .rq-corps .rq-ou{margin-top:18px}
#pg-search .rq-plus{display:block;width:100%;border:1px solid var(--rq-b2);
  background:transparent;border-radius:11px;padding:12px;margin-top:14px;
  font-family:inherit;font-size:.82rem;color:var(--rq-t3);cursor:pointer;
  transition:color .16s,border-color .16s,background .16s}
#pg-search .rq-plus:hover{color:var(--rq-a2);border-color:rgba(124,106,247,.4);
  background:rgba(124,106,247,.05)}

/* mise en évidence du terme cherché : une teinte, pas un surligneur */
#pg-search mark{background:rgba(124,106,247,.15);color:#cfc4ff;
  box-shadow:inset 0 -1px 0 rgba(124,106,247,.55);border-radius:3px;
  padding:0 2px;font-weight:500}
#pg-search .rq-rep-d mark{color:#d8d0ff}

/* ------------------------------------------------- clavier et pointage */
#pg-search button{-webkit-tap-highlight-color:rgba(124,106,247,.2)}
#pg-search button:focus-visible,#pg-search .rq-rh:focus-visible{
  outline:2px solid rgba(124,106,247,.75);outline-offset:3px;border-radius:6px}
@media(prefers-reduced-motion:reduce){
  #pg-search *,.rq-flash{transition:none !important;animation:none !important}
}

/* -------------------------------------------------------------- états */
#pg-search .rq-vide{max-width:700px;border:1px solid var(--rq-b2);
  border-radius:16px;padding:30px 28px;color:var(--rq-t2);font-size:.9rem;
  line-height:1.75;background:var(--rq-c)}
#pg-search .rq-vide b{color:var(--rq-t)}
#pg-search .rq-vide-t{font-family:'Playfair Display',serif;font-size:1.2rem;
  font-weight:900;color:var(--rq-t);margin-bottom:10px}
#pg-search .rq-pistes{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px}
#pg-search .rq-corr{font-size:.83rem;color:var(--rq-t2);
  background:rgba(247,162,106,.07);border-left:2px solid rgba(247,162,106,.55);
  border-radius:0 10px 10px 0;padding:10px 14px;margin-bottom:14px;
  line-height:1.6;flex:1 1 100%}
#pg-search .rq-corr b{color:#f9c396;font-weight:600}
#pg-search .rq-corr button{border:0;background:transparent;color:var(--rq-a2);
  font-family:inherit;font-size:.83rem;cursor:pointer;padding:0 2px;
  border-bottom:1px solid rgba(124,106,247,.45);transition:color .15s}
#pg-search .rq-corr button:hover{color:#fff}
.rq-flash{animation:rqflash 2.8s ease-out 1}
@keyframes rqflash{0%{background:rgba(124,106,247,.34)}
  55%{background:rgba(124,106,247,.18)}100%{background:transparent}}

/* ----------------------------------------------------------- tablette */
@media(max-width:900px){
  #pg-search .rq-wrap{padding:24px 18px 100px}
  #pg-search .rq-rep{padding:22px 24px 10px}
  #pg-search .rq-g{grid-template-columns:96px minmax(0,1fr);gap:4px 12px}
}

/* ---------------------------------------------------------- téléphone */
@media(max-width:640px){
  #pg-search .rq-wrap{padding:18px 14px 90px}
  #pg-search .rq-h1{font-size:1.45rem}
  #pg-search .rq-sub{display:none}
  #pg-search .rq-zone{margin-bottom:20px}
  #pg-search .rq-in{font-size:.95rem;padding:13px 2px}
  #pg-search .rq-rep{padding:19px 17px 8px;border-radius:15px;margin-bottom:22px}
  #pg-search .rq-rep-t{font-size:1.3rem}
  #pg-search .rq-rep-d{font-size:.9rem;line-height:1.72}
  #pg-search .rq-conf-l{grid-template-columns:minmax(0,1fr)}
  #pg-search .rq-g{grid-template-columns:minmax(0,1fr);gap:5px;padding:11px 0}
  #pg-search .rq-g-l{font-size:.68rem;text-transform:uppercase;
    letter-spacing:.09em;font-weight:700;padding-top:0}
  #pg-search .rq-fl{display:none}
  #pg-search select.rq-sel{display:block;margin-left:auto;max-width:52%}
  #pg-search .rq-rh{grid-template-columns:minmax(0,1fr) auto;padding:12px 12px 4px}
  #pg-search .rq-rm{grid-column:1 / -1;order:3;flex-wrap:wrap;
    white-space:normal}
  #pg-search .rq-ex{padding:6px 12px 0;margin-bottom:12px}
  #pg-search .rq-corps{padding:2px 12px 14px}
  #pg-search .rq-go{width:100%;justify-content:center}
  #pg-search .rq-vide{padding:22px 18px}
}
</style>
"""
MOTEUR = r"""
<script id="eco-recherche-v218">
(function(){
'use strict';
if(window.__ECO_RECH_V218) return;
window.__ECO_RECH_V218 = true;

var D = __PAYLOAD__;

/* Les grands tableaux de l'application sont déclarés avec const au premier
   niveau d'un script : ils sont dans la portée lexicale globale mais ne sont
   pas des propriétés de window. On les lit donc par leur nom. */
function G(nom){
  try { return (new Function('try{return ' + nom + '}catch(e){return undefined}'))(); }
  catch(e){ return undefined; }
}
var _cache = {};
function g(nom){
  if(!(nom in _cache)) _cache[nom] = G(nom);
  return _cache[nom];
}
function oublier(){ _cache = {}; }

/* ====================================================== normalisation */
function nz(s){
  return (s==null?'':String(s)).toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g,'')
    .replace(/[’‘ʼ]/g,"'")
    .replace(/œ/g,'oe').replace(/æ/g,'ae')
    .replace(/\s+/g,' ').trim();
}
function sing(w){
  /* on ne retire jamais le « x » final : taux, prix, flux ne sont pas des
     pluriels */
  if(w.length>5 && /eaux$/.test(w)) return w.slice(0,-1);
  if(w.length>5 && /aux$/.test(w)) return w.slice(0,-3)+'al';
  if(w.length>5 && /ail$/.test(w)) return w.slice(0,-3)+'al';
  if(w.length>3 && /s$/.test(w) && !/ss$/.test(w)) return w.slice(0,-1);
  return w;
}
var PETITS = {de:1,du:1,des:1,la:1,le:1,les:1,un:1,une:1,et:1,ou:1,au:1,aux:1,
  en:1,dans:1,par:1,pour:1,sur:1,ce:1,ces:1,sa:1,se:1,son:1,ses:1,qui:1,que:1,
  est:1,sont:1,aux:1,ne:1,pas:1,plus:1,avec:1,sans:1,sous:1,leur:1,leurs:1};
function toks(s){
  var t = nz(s).replace(/[^a-z0-9' ]+/g,' ').replace(/'/g,' ');
  var o = [], a = t.split(' '), i;
  for(i=0;i<a.length;i++){ if(a[i].length>1) o.push(sing(a[i])); }
  return o;
}
function motsUtiles(s){
  var a = toks(s), o = [], i;
  for(i=0;i<a.length;i++) if(!PETITS[a[i]]) o.push(a[i]);
  return o.length ? o : a;
}
var RE_ART = /^(le|la|les|l|un|une|des|du|de|d|au|aux|ce|cet|cette|ces|son|sa|ses|leur|leurs|mon|notre)\s+/;
function cle(s){
  var t = toks(s).join(' '), p;
  do { p = t; t = t.replace(RE_ART,''); } while(t !== p && t);
  return t || toks(s).join(' ');
}

/* ====================================================== blocs des cours */
var RE_MARQ = /^\s*(?:[IVXLC]{1,6}\.|[A-Z]{1,2}\.|\d{1,2}\s*[-.)])\s*/;
function R_TITRE(t){ return String(t||'').replace(RE_MARQ,'').trim(); }

var SEL = 'h2,h3,h4,h5,p,li,.db,table,blockquote';
var BL = {}, NX = {}, OFF = {}, PRET = {}, VOC = null, VOCB = null;

function blocsChapitre(k){
  if(PRET[k]) return BL[k];
  var CC = g('CH_CONTENT');
  var h = (CC && CC[k] && CC[k].cours) || '';
  var d = document.createElement('div');
  d.innerHTML = h;
  var out = [], h2='', h3='', h4='', n = 0;
  d.querySelectorAll(SEL).forEach(function(el){
    if(el.closest('.db') && !el.classList.contains('db')) return;
    if(el.tagName === 'TABLE' && el.closest('.db')) return;
    var tag = el.classList.contains('db') ? 'db' : el.tagName.toLowerCase();
    var txt = (el.innerText||'').replace(/\s+/g,' ').trim(), dt='', dd='';
    if(tag === 'db'){
      var a = el.querySelector('.dt'), b = el.querySelector('.dd');
      dt = a ? (a.innerText||'').replace(/\s+/g,' ').trim() : '';
      dd = b ? (b.innerText||'').replace(/\s+/g,' ').trim() : '';
      txt = (dt + ' : ' + dd).trim();
    }
    if(tag === 'h2'){ h2 = txt; h3=''; h4=''; }
    else if(tag === 'h3'){ h3 = txt; h4=''; }
    else if(tag === 'h4' || tag === 'h5'){ h4 = txt; }
    el.setAttribute('data-rb', String(n));
    out.push({g:tag, x:txt, dt:dt, dd:dd, p:[h2,h3,h4]});
    n++;
  });
  /* on réinjecte le balisage marqué : les liens profonds pourront viser
     le bloc exact, y compris si le chapitre est rouvert plus tard */
  try{ if(CC && CC[k]) CC[k].cours = d.innerHTML; }catch(e){}
  /* le texte indexé est une suite de jetons au singulier séparés par des
     espaces : la recherche d'une expression y respecte les frontières de
     mots et ignore les différences de pluriel */
  var txts = [], offs = [], pos = 0, i;
  for(i=0;i<out.length;i++){
    var t = ' ' + toks(out[i].x).join(' ') + ' ';
    offs.push(pos); txts.push(t); pos += t.length + 1;
  }
  BL[k] = out; NX[k] = txts.join('\n'); OFF[k] = offs; PRET[k] = true;
  return out;
}

function tousLesBlocs(){
  Object.keys(D.ch).forEach(function(k){ blocsChapitre(k); });
}

function blocAt(k, off){
  var a = OFF[k], lo = 0, hi = a.length - 1, r = 0;
  while(lo <= hi){ var m = (lo+hi)>>1;
    if(a[m] <= off){ r = m; lo = m+1; } else hi = m-1; }
  return r;
}

/* ====================================================== vocabulaire */
function vocabulaire(){
  if(VOC) return VOC;
  var S = Object.create(null);
  function av(s){ var a = toks(s), i; for(i=0;i<a.length;i++) S[a[i]] = 1; }
  Object.keys(D.def).forEach(function(c){ av(D.def[c].t); });
  D.sec.forEach(function(x){ av(x.t); });
  D.dos.forEach(function(x){ av(x.t); });
  D.atl.forEach(function(x){ av(x.t); av(x.n); });
  try{ (g('AUTHORS')||[]).forEach(function(a){ av(a.name); av(a.idea); }); }catch(e){}
  try{ var CC = g('CH_CONTENT')||{}; Object.keys(CC).forEach(function(k){
    (CC[k].notions||[]).forEach(function(n){ av(n.term); }); }); }catch(e){}
  Object.keys(NX).forEach(function(k){
    var a = NX[k].replace(/[^a-z0-9 ]+/g,' ').split(' '), i;
    for(i=0;i<a.length;i++) if(a[i].length>2) S[sing(a[i])] = 1;
  });
  VOC = S;
  VOCB = Object.create(null);
  Object.keys(S).forEach(function(w){
    var b = w.charAt(0) + w.length;
    (VOCB[b] = VOCB[b] || []).push(w);
  });
  return VOC;
}
function dist1(a,b,max){
  if(Math.abs(a.length-b.length) > max) return max+1;
  var i=0, j=0, d=0;
  while(i<a.length && j<b.length){
    if(a[i]===b[j]){ i++; j++; continue; }
    d++; if(d>max) return d;
    if(a.length>b.length) i++;
    else if(a.length<b.length) j++;
    else { i++; j++; }
  }
  return d + (a.length-i) + (b.length-j);
}
function corriger(w){
  vocabulaire();
  if(VOC[w]) return w;
  var max = w.length >= 8 ? 2 : (w.length >= 5 ? 1 : 0);
  if(!max) return w;
  var best = null, bd = max + 1, l = w.charAt(0), i, dl, b, arr, k;
  for(dl = -max; dl <= max; dl++){
    for(i = 0; i < 2; i++){
      b = (i ? l : '') + (w.length + dl);
      arr = VOCB[(i ? l : '') + (w.length + dl)];
      if(i === 0) arr = null;
      if(!arr) continue;
      for(k = 0; k < arr.length; k++){
        var d = dist1(w, arr[k], bd - 1);
        if(d < bd){ bd = d; best = arr[k]; if(!d) return best; }
      }
    }
  }
  /* seconde passe : première lettre différente (faute de frappe initiale) */
  if(!best && w.length >= 6){
    var cles = Object.keys(VOCB), z;
    for(z = 0; z < cles.length; z++){
      if(Math.abs(parseInt(cles[z].slice(1),10) - w.length) > 1) continue;
      arr = VOCB[cles[z]];
      for(k = 0; k < arr.length; k++){
        var dd = dist1(w, arr[k], 1);
        if(dd < bd){ bd = dd; best = arr[k]; }
      }
    }
  }
  return best || w;
}

/* ====================================================== entrées */
var E = null;

function act(a){ return a; }

function ajouterEntrees(){
  if(E) return E;
  var L = [];
  function add(o){
    o.g = o.g || cle(o.t);
    o.nt = cle(o.t);
    o.nd = toks((o.d||'') + ' ' + (o.kw||'')).join(' ');
    L.push(o);
  }
  /* 1. définitions (cours moissonnés + rédigées) */
  Object.keys(D.def).forEach(function(c){
    var v = D.def[c];
    var ou = (v.ou||[]).filter(function(z){ return D.ch[z[0]]; });
    add({y:'def', t:v.t, d:v.d, c:ou.length?ou[0][0]:'', b:ou.length?ou[0][1]:-1,
         al:v.al||[], o:v.o, ou:ou, g:c, x:v.x||'',
         k:ou.length?['ch',ou[0][0],ou[0][1]]:null});
  });
  /* 2. notions des chapitres (déjà en mémoire) */
  try{
    var CC = g('CH_CONTENT')||{};
    Object.keys(CC).forEach(function(k){
      if(!D.ch[k]) return;
      (CC[k].notions||[]).forEach(function(n){
        if(!n.term || !n.def) return;
        add({y:(n.type==='formule'?'formule':'notion'), t:n.term, d:n.def,
             c:k, b:-1, k:['nt',k,n.term]});
      });
    });
  }catch(e){}
  /* 3. sections des chapitres */
  D.sec.forEach(function(x){
    add({y:'sect', t:x.t, d:'', kw:x.p, c:x.c, b:x.b, path:x.p,
         k:['ch',x.c,x.b]});
  });
  /* 4. auteurs */
  try{
    (g('AUTHORS')||[]).forEach(function(a){
      add({y:'auteur', t:a.name, d:(a.idea||''),
           kw:[a.courant,a.detail,a.phrase,(a.oeuvres||[]).join(' ')].join(' '),
           c:String(a.ch||''), b:-1, k:['au',a.name]});
    });
  }catch(e){}
  /* 5. formules : page Formules + blocs de cours */
  try{
    document.querySelectorAll('#pg-formulas .cardx').forEach(function(el,i){
      var b = el.querySelector('b'), n = el.querySelector('.s-note');
      if(!b) return;
      el.setAttribute('data-rf', String(i));
      add({y:'formule', t:(b.innerText||'').trim(),
           d:(n?(n.innerText||'').trim():''), c:'', b:i, k:['fo',i]});
    });
  }catch(e){}
  D.fml.forEach(function(x){
    add({y:'formule', t:x.t, d:x.d, c:x.c, b:x.b, k:['ch',x.c,x.b]});
  });
  /* 6. faits datés */
  D.fai.forEach(function(x){
    add({y:'fait', t:String(x.an), d:x.d, kw:x.p, c:x.c, b:x.b,
         an:x.an, g:'fait-'+x.c+'-'+x.b, k:['ch',x.c,x.b]});
  });
  /* 7. dossiers d'« Autour d'une notion » */
  D.dos.forEach(function(x){
    add({y:'dossier', t:x.t, d:x.d, c:(x.ch&&x.ch.length?String(x.ch[0]):''),
         b:-1, etat:x.et, k:['do',x.cle]});
  });
  /* 8. idées de l'Atlas */
  D.atl.forEach(function(x){
    add({y:'atlas', t:x.t, d:x.d, kw:(x.no||[]).join(' ')+' '+x.n, c:x.c,
         b:-1, aut:x.n, g:'atlas-'+nz(x.n)+'-'+cle(x.t), k:['at',x.c]});
  });
  /* 9. chiffres */
  D.chf.forEach(function(x){
    add({y:'chiffre', t:(x.v+' — '+(x.u||'')).replace(/ — $/,''), d:x.d,
         kw:[x.z,x.p,(x.k||[]).join(' ')].join(' '), c:x.c, b:-1,
         g:'chf-'+x.c+'-'+nz(x.v), k:['ci',x.c]});
  });
  /* 10. résumés */
  D.res.forEach(function(x){
    add({y:'resume', t:'Résumé — '+(D.ch[x.c]?D.ch[x.c].t:('chapitre '+x.c)),
         d:x.d, kw:x.q+' '+(x.i||[]).join(' '), c:x.c, b:-1,
         g:'res-'+x.c, k:['re',x.c]});
  });
  /* 11. sujets */
  try{
    (g('SUBJECTS_BANK_PREMIUM')||[]).forEach(function(z){
      add({y:'sujet', t:z.title, d:'', c:String(z.chapter||''), b:-1,
           g:'suj-'+z.id, k:['su',String(z.chapter||'')]});
    });
  }catch(e){}
  /* 12. fiches — l'habillage de révision est retiré pour que la fiche
         rejoigne la notion au lieu de faire doublon */
  var FICHE_OK = {definition:1, 'définition':1, 'notion-clé':1, notion:1,
    formule:1, auteur:1, ouvrage:1, courant:1, tableau:1};
  var RE_HABIT = /^\s*(?:d[ée]finis|que faut-il retenir de|quel concept correspond [àa] cette (?:d[ée]finition|id[ée]e)|quel auteur associer [àa] l['’]id[ée]e suivante|rappelle|explique|cite)\s*:?\s*/i;
  try{
    (g('FC_DATA')||[]).forEach(function(f){
      if(!f.term || !f.def) return;
      if(!FICHE_OK[f.type]) return;
      var t = String(f.term).replace(RE_HABIT, '').replace(/\s*\?\s*$/, '').trim();
      if(t.length < 2) return;
      add({y:'fiche', t:t, d:f.def, c:String(f.ch||''), b:-1,
           g:'fc-'+cle(t)+'-'+(f.ch||''), k:['fc',f.ch]});
    });
  }catch(e){}
  /* 13. visualisations */
  try{
    (g('visualisationsStrategiques')||g('VZ')||[]).forEach(function(v){
      add({y:'visu', t:v.titre, d:v.resume||'', kw:v.fam||'', c:'', b:-1,
           g:'vz-'+v.cle, k:['vz',v.cle]});
      (v.noeuds||[]).forEach(function(n){
        add({y:'visu', t:n.t, d:n.r||n.defi||'', kw:v.titre, c:'', b:-1,
             g:'vz-'+v.cle+'-'+n.id, k:['vz',v.cle]});
      });
    });
  }catch(e){}
  E = L;
  return E;
}

/* ====================================================== score */
var PRIO = {def:460, notion:330, sect:150, dossier:250, atlas:160, auteur:200,
  formule:180, chiffre:130, fait:95, sujet:80, fiche:70, visu:110, resume:-320,
  passage:0};
var TYPE_LIB = {def:'définition', notion:'notion', sect:'section de cours',
  passage:'passage du cours', auteur:'auteur', formule:'formule',
  chiffre:'chiffre', fait:'fait daté', dossier:'dossier', atlas:'idée (Atlas)',
  chiffre_:'chiffre', sujet:'sujet', fiche:'fiche', resume:'résumé',
  visu:'visualisation'};
var TYPE_CL = {def:'d', notion:'d', sect:'p', passage:'p', auteur:'a',
  formule:'', chiffre:'c', fait:'c', dossier:'', atlas:'v', sujet:'',
  fiche:'', resume:'r', visu:'v'};

function noter(e, Q){
  var s = 0, i, n = 0;
  var nt = e.nt, nd = e.nd, ntp = ' ' + nt + ' ', ndp = ' ' + nd + ' ';
  var expr = (Q.pm && Q.pm.length) ? Q.pm.join(' ')
             : (Q.mots.length ? Q.mots.join(' ') : '');
  var court = Q.cle.length <= 3;
  if(nt === Q.cle) s += 1000;
  else if((e.al||[]).indexOf(Q.cle) >= 0) s += 940;
  else if(court){
    /* sigle ou mot très court : on exige un jeton entier, jamais un morceau */
    if(ntp.indexOf(' ' + Q.cle + ' ') >= 0) s += 620;
  }
  else if(nt.indexOf(Q.cle + ' ') === 0)
    s += 700 - Math.min(140, (nt.length - Q.cle.length) * 4);
  else if(Q.cle && ntp.indexOf(' ' + Q.cle + ' ') >= 0) s += 560;
  else if(Q.cle && nt.indexOf(Q.cle) >= 0) s += 420;
  else if(Q.cle && Q.cle.indexOf(nt + ' ') === 0 && nt.length >= 4) s += 300;
  for(i=0;i<Q.mots.length;i++) if(ntp.indexOf(' '+Q.mots[i]+' ') >= 0) n++;
  if(Q.mots.length) s += Math.round(230 * n / Q.mots.length);
  var dansD = expr && ndp.indexOf(' ' + expr + ' ') >= 0;
  if(dansD) s += 180;
  var nd2 = 0;
  for(i=0;i<Q.mots.length;i++) if(ndp.indexOf(' '+Q.mots[i]+' ') >= 0) nd2++;
  if(Q.mots.length) s += Math.round(70 * nd2 / Q.mots.length);
  /* un résultat n'est retenu que s'il correspond vraiment : expression
     présente, ou tous les mots de la requête présents */
  var couvre = (n === Q.mots.length && Q.mots.length > 0) || dansD ||
               (nd2 === Q.mots.length && Q.mots.length > 0) ||
               (!court && Q.cle && nt.indexOf(Q.cle) >= 0);
  if(!couvre) return 0;
  s += (PRIO[e.y] || 0);
  if(e.y === 'resume'){
    /* un résumé ne remonte que si la requête y figure littéralement */
    if(!dansD && n < Q.mots.length) return 0;
  }
  if(e.y === 'auteur'){
    if(nt === Q.cle) s += 700;
    else if(Q.mots.length <= 2){
      /* le nom de famille seul doit suffire à faire remonter l'auteur */
      var np = nt.split(' ');
      if(np.length && Q.mots.indexOf(np[np.length-1]) >= 0) s += 640;
    }
  }
  if(e.y === 'dossier' && e.etat === 'hors-cours') s -= 260;
  if(e.y === 'sect' && !e.d) s -= 40;
  if(e.c && Q.ch && String(e.c) === Q.ch) s += 120;
  return s;
}

/* ====================================================== passages */
function chercherPassages(Q, lim){
  var out = [], ks = Object.keys(D.ch), i, k;
  for(i=0;i<ks.length;i++){
    k = ks[i];
    if(!PRET[k]) blocsChapitre(k);
    var t = NX[k], trouve = {};
    var pm = (Q.pm && Q.pm.length) ? Q.pm : Q.mots;
    var expr = pm.length ? (' ' + pm.join(' ') + ' ') : '';
    if(expr && pm.length > 1){
      var p = t.indexOf(expr), garde = 0;
      while(p >= 0 && garde < 400){
        var b = blocAt(k, p);
        if(!trouve[b]) trouve[b] = {b:b, exact:1, n:0};
        trouve[b].n++;
        p = t.indexOf(expr, p + expr.length - 1); garde++;
      }
    }
    if(Q.mots.length){
      /* tous les jetons de la requête dans le même bloc */
      var m0 = ' ' + Q.mots[0] + ' ', q = t.indexOf(m0), g2 = 0;
      while(q >= 0 && g2 < 2500){
        var bb = blocAt(k, q);
        if(!trouve[bb]){
          var xb = ' ' + toks((BL[k][bb]||{}).x || '').join(' ') + ' ';
          var tous = 1, j;
          for(j=0;j<Q.mots.length;j++)
            if(xb.indexOf(' ' + Q.mots[j] + ' ') < 0){ tous = 0; break; }
          if(tous) trouve[bb] = {b:bb, exact:(Q.mots.length === 1 ? 1 : 0), n:1};
        }
        q = t.indexOf(m0, q + m0.length - 1); g2++;
      }
    }
    Object.keys(trouve).forEach(function(bk){
      var z = trouve[bk], bl = BL[k][z.b];
      if(!bl || bl.x.length < 24) return;
      if(bl.g === 'h2' || bl.g === 'h3') return;  /* les titres : type « sect » */
      if(!z.exact && Q.mots.length > 1){
        /* mots dispersés : on exige que la section parle du sujet, sinon le
           rapprochement est fortuit */
        var ts = ' ' + toks((bl.p[1] || bl.p[0] || '') + ' ' + (bl.p[2] || '')).join(' ') + ' ';
        var un = 0;
        for(var w = 0; w < Q.mots.length; w++)
          if(ts.indexOf(' ' + Q.mots[w] + ' ') >= 0){ un = 1; break; }
        if(!un) return;
      }
      var etiq = bl.p[2] || '';
      var GEN_ET = /^(idee|idee cle|idee centrale|idee generale|idee essentielle|schema|formule|exemple|mecanisme|etape|pourquoi|remarque|attention|consequence|definition|synthese|resume|rappel|document|lecture|cas|mot cle a retenir|a retenir|conclusion|objectif|constat|limite|critique|principe|logique|precision|nuance|application|illustration|comparaison|tableau)\b/;
      if(etiq && GEN_ET.test(nz(R_TITRE(etiq)))) etiq = '';
      var sect = bl.p[1] || bl.p[0] || '';
      var titrePass = (sect ? R_TITRE(sect) : D.ch[k].t)
        + (etiq ? ' — ' + R_TITRE(etiq) : '');
      out.push({y:'passage',
        nt:cle(titrePass), nd:toks(bl.x).join(' '),
        t:(sect ? R_TITRE(sect) : D.ch[k].t) + (etiq ? ' — ' + R_TITRE(etiq) : ''),
        d:bl.x, c:k, b:z.b,
        path:[bl.p[0], bl.p[2]].filter(Boolean).map(R_TITRE).join(' › '),
        sect:sect,
        sc: (z.exact ? 620 : 300) + Math.min(60, z.n*12)
            + (bl.g === 'db' ? 240 : 0) + (bl.g === 'li' ? -25 : 0)
            + (pm.length && (' ' + toks(sect).join(' ') + ' ')
                 .indexOf(' ' + pm.join(' ') + ' ') >= 0 ? 190 : -110),
        k:['ch',k,z.b]});
    });
  }
  out.sort(function(a,b){ return b.sc - a.sc; });
  return out.slice(0, lim || 400);
}

/* ====================================================== recherche */
var FILTRE = 'tout';
var FAM = {
  tout:null,
  definitions:['def','notion'],
  cours:['passage','sect'],
  auteurs:['auteur'],
  formules:['formule'],
  chiffres:['chiffre'],
  faits:['fait'],
  dossiers:['dossier'],
  atlas:['atlas'],
  sujets:['sujet'],
  fiches:['fiche'],
  resumes:['resume'],
  visu:['visu']
};
var FAM_LIB = {tout:'Tout', definitions:'Définitions', cours:'Cours',
  auteurs:'Auteurs', formules:'Formules', chiffres:'Chiffres',
  faits:'Faits & dates', dossiers:'Dossiers', atlas:'Atlas', sujets:'Sujets',
  fiches:'Fiches', resumes:'Résumés', visu:'Visualisations'};

var SANS_CORRECTION = false;
function analyser(q){
  var brut = nz(q);
  var ch = null;
  var m = brut.match(/\bchapitre\s+(\d{1,2})\b/);
  if(m) ch = m[1];
  var sansch = brut.replace(/\bchapitre\s+\d{1,2}\b/g,' ').trim();
  var mots = motsUtiles(sansch);
  /* correction des fautes de frappe */
  var corr = [], change = 0, i;
  for(i=0;i<mots.length;i++){
    var c = SANS_CORRECTION ? mots[i] : corriger(mots[i]);
    if(c !== mots[i]) change = 1;
    corr.push(c);
  }
  /* la correction n'est retenue que si la forme écrite ne donne rien :
     « capital » ne doit jamais devenir « capitale » */
  if(change && !SANS_CORRECTION){
    var brutQ = {nq:nz(sansch), cle:cle(sansch), mots:mots, syn:[]};
    if(aQuelqueChose(brutQ)){ corr = mots; change = 0; }
  }
  var nq = cle(sansch);
  var syn = [];
  var k = nq;
  if(D.syn[k]) syn = D.syn[k].slice(0);
  /* deux listes distinctes : l'expression complète pour la recherche de
     suite de mots, les mots pleins pour la couverture et les corrections */
  var pm = toks(sansch);
  if(change){
    /* on reporte les corrections dans l'expression complète */
    var j = 0;
    pm = pm.map(function(w){
      if(j < mots.length && w === mots[j]){ var c2 = corr[j]; j++; return c2; }
      return w;
    });
  }
  return {brut:brut, nq:nz(sansch), cle:nq, mots:corr, mots0:mots, pm:pm,
          corrige:change, ch:ch, syn:syn,
          tete:(pm.length === 1)};
}

function texteSection(c, b){
  /* le contenu d'une section : les premiers blocs qui la suivent */
  var v = BL[c];
  if(!v) { blocsChapitre(c); v = BL[c]; }
  if(!v) return '';
  var out = [], i;
  for(i = b + 1; i < v.length && out.length < 4; i++){
    if(v[i].g === 'h2' || v[i].g === 'h3') break;
    if(v[i].x.length > 18) out.push(v[i].x);
  }
  return out.join(' ');
}

/* types qui nomment une notion : deux clés différentes = deux notions */
var NOMME = {def:1, notion:1, dossier:1, auteur:1, fiche:1, atlas:1, visu:1};
/* types qui situent une notion : ils rejoignent la carte de la notion */
var SITUE = {sect:1, passage:1, chiffre:1, fait:1, resume:1, formule:1,
  sujet:1, atlas:1, visu:1, fiche:1};

function fusionner(res, Q){
  var PR = {def:9, notion:8, auteur:9, dossier:7, atlas:6, formule:6,
    passage:5, sect:4, chiffre:4, fait:3, visu:3, sujet:2, fiche:2, resume:1};
  var syn = {};
  (Q.syn || []).forEach(function(z){ syn[cle(z)] = 1; });
  Object.keys(D.syn).forEach(function(k){
    if((D.syn[k] || []).map(cle).indexOf(Q.cle) >= 0) syn[cle(k)] = 1;
  });

  /* toutes les façons d'écrire la notion cherchée */
  var VAR = [(Q.pm && Q.pm.length ? Q.pm : Q.mots).join(' ')];
  Object.keys(syn).forEach(function(z){ if(z) VAR.push(z); });
  VAR = VAR.filter(function(z, i){ return z && VAR.indexOf(z) === i; });

  /* la notion cherchée : d'abord le libellé exact, ensuite un synonyme */
  var principal = null, rangPrin = -1;
  res.forEach(function(r){
    if(!NOMME[r.y]) return;
    var rang = r.nt === Q.cle ? 2 : (syn[r.nt] ? 1 : 0);
    if(!rang) return;
    var pr = PR[r.y] || 0;
    var mieux = false;
    if(!principal) mieux = true;
    else if(rang > rangPrin) mieux = true;
    else if(rang === rangPrin){
      var pp = PR[principal.y] || 0;
      if(pr > pp) mieux = true;
      else if(pr === pp){
        var dr = (r.d||'').length, dp = (principal.d||'').length;
        if(dr > dp + 60) mieux = true;
        else if(dp <= dr + 60 && r.sc > principal.sc) mieux = true;
      }
    }
    if(mieux){ principal = r; rangPrin = rang; }
  });

  var par = Object.create(null), ordre = [];
  function groupe(cl){
    if(!par[cl]){ par[cl] = {cle:cl, items:[], sc:0}; ordre.push(par[cl]); }
    return par[cl];
  }
  var tete = null;
  if(principal){
    tete = groupe('@' + Q.cle);
    tete.items.push(principal);
    tete.sc = principal.sc + 60;
  }

  res.forEach(function(r){
    if(r === principal) return;
    var memeNotion = (r.nt === Q.cle) || !!syn[r.nt];
    /* une occurrence qui porte la notion, sous l'une de ses écritures,
       rejoint sa carte au lieu de former un résultat de plus */
    var porte = memeNotion;
    if(!porte && tete){
      var champ = ' ' + r.nt + ' ' + r.nd + ' ', z;
      if(SITUE[r.y] || r.y === 'passage'){
        for(z = 0; z < VAR.length && !porte; z++)
          if(champ.indexOf(' ' + VAR[z] + ' ') >= 0) porte = true;
      }
      /* un dossier ou une idée dont le titre développe la notion */
      if(!porte && (r.y === 'dossier' || r.y === 'atlas' || r.y === 'visu')){
        for(z = 0; z < VAR.length && !porte; z++)
          if(r.nt.indexOf(VAR[z] + ' ') === 0) porte = true;
      }
    }
    if(tete && porte){
      tete.items.push(r);
      return;
    }
    var cl = NOMME[r.y] ? cle(r.t) : (r.g || cle(r.t));
    var gr = groupe(cl);
    gr.items.push(r);
    if(r.sc > gr.sc) gr.sc = r.sc;
  });

  ordre.forEach(function(g){
    g.items.sort(function(a,b){
      var d = (PR[b.y] || 0) - (PR[a.y] || 0);
      return d || (b.sc - a.sc);
    });
    g.prim = g.items[0];
    /* dans la carte de la notion, on ne garde qu'un endroit par section */
    if(g === tete){
      var vus = Object.create(null), gardes = [g.prim];
      g.items.slice(1).forEach(function(r){
        var sig = r.y === 'passage' || r.y === 'sect'
          ? 'l-' + r.c + '-' + cle(r.sect || r.t)
          : r.y + '-' + (r.g || cle(r.t));
        if(vus[sig]) return;
        vus[sig] = 1;
        gardes.push(r);
      });
      g.items = gardes.slice(0, 26);
    }
  });
  ordre.sort(function(a,b){ return b.sc - a.sc; });
  return ordre;
}

function aQuelqueChose(Q){
  ajouterEntrees();
  var i, n = 0;
  for(i=0;i<E.length && n < 1;i++) if(noter(E[i], Q) > 0) n++;
  if(n) return true;
  /* sinon, un passage de cours suffit */
  var ks = Object.keys(D.ch);
  for(i=0;i<ks.length;i++){
    var k = ks[i];
    if(!PRET[k]) blocsChapitre(k);
    var pmq = (Q.pm && Q.pm.length) ? Q.pm : Q.mots;
    if(pmq.length && NX[k].indexOf(' ' + pmq.join(' ') + ' ') >= 0) return true;
    if(Q.mots.length === 1 && NX[k].indexOf(' ' + Q.mots[0] + ' ') >= 0) return true;
  }
  return false;
}

/* ------------------------------------------------- familles de notions */
var FAM_IDX = null;
function familles(){
  if(FAM_IDX) return FAM_IDX;
  ajouterEntrees();
  var f = Object.create(null), i, e, m;
  for(i=0;i<E.length;i++){
    e = E[i];
    if(e.y !== 'def' && e.y !== 'notion' && e.y !== 'dossier') continue;
    m = e.nt.split(' ');
    if(m.length < 2) continue;
    var tete = m[0];
    if(tete.length < 4) continue;
    var l = (f[tete] = f[tete] || []);
    if(!l.some(function(z){ return z.nt === e.nt; })) l.push(e);
  }
  FAM_IDX = f;
  return f;
}
function familleDe(Q){
  /* les notions de la même famille que la requête : « capital » donne
     capital humain, public, naturel, social, technologique… ; « capital
     humain » donne ses voisines */
  var f = familles(), m = Q.cle.split(' ');
  if(!m.length || !m[0]) return null;
  var tete = m[0];
  var l = (f[tete] || []).slice(0);
  if(l.length < 2) return null;
  l.sort(function(a,b){
    var d = (b.y === 'def' ? 1 : 0) - (a.y === 'def' ? 1 : 0);
    return d || a.nt.length - b.nt.length;
  });
  return {tete:tete, membres:l.slice(0, 18)};
}

function chercher(q){
  var Q = analyser(q);
  if(!Q.mots.length && !Q.ch) return {Q:Q, groupes:[], n:0};
  ajouterEntrees();
  var res = [], i, e;
  var cibles = FAM[FILTRE];
  for(i=0;i<E.length;i++){
    e = E[i];
    if(cibles && cibles.indexOf(e.y) < 0) continue;
    var sc = noter(e, Q);
    if(Q.syn.length && !sc){
      for(var z=0; z<Q.syn.length; z++){
        var Q2 = {nq:Q.syn[z], cle:cle(Q.syn[z]), mots:motsUtiles(Q.syn[z]), ch:Q.ch};
        var s2 = noter(e, Q2);
        if(s2){ sc = Math.round(s2 * 0.92); break; }
      }
    }
    if(sc > 0){
      var x = Object.assign({}, e, {sc:sc});
      x.exact = estExact(x, Q);
      res.push(x);
    }
  }
  if(!cibles || cibles.indexOf('passage') >= 0){
    /* une requête d'un seul mot qui ouvre une famille doit montrer les
       notions, non des centaines de paragraphes */
    var fam0 = familleDe(Q);
    var limP = (Q.tete && fam0 && fam0.membres.length >= 3) ? 24 : 260;
    var pas = chercherPassages(Q, limP);
    if(!pas.length && Q.syn.length){
      for(var y=0; y<Q.syn.length && !pas.length; y++){
        pas = chercherPassages({nq:Q.syn[y], cle:cle(Q.syn[y]),
          mots:motsUtiles(Q.syn[y])}, 260);
      }
    }
    if(Q.ch) pas = pas.filter(function(p){ return p.c === Q.ch; });
    res = res.concat(pas);
  }
  if(Q.ch) res = res.filter(function(r){ return !r.c || String(r.c) === Q.ch; });
  res.forEach(function(r){ if(r.exact === undefined) r.exact = estExact(r, Q); });
  var groupes = fusionner(res, Q);
  groupes.forEach(function(g){
    g.exact = g.items.some(function(r){ return r.exact; });
  });
  /* les correspondances exactes d'abord, le reste ensuite */
  var ex = groupes.filter(function(g){ return g.exact; });
  var ap = groupes.filter(function(g){ return !g.exact; });
  var PLAFOND = 60;
  var tronque = Math.max(0, groupes.length - PLAFOND);
  if(ex.length > PLAFOND) ex = ex.slice(0, PLAFOND);
  if(ex.length + ap.length > PLAFOND)
    ap = ap.slice(0, Math.max(6, PLAFOND - ex.length));
  return {Q:Q, groupes:groupes, exactes:ex, elargies:ap, n:res.length,
          tronque:tronque, montres:ex.length + ap.length,
          famille:familleDe(Q), reponse:reponsePrincipale(ex, Q)};
}

function estExact(r, Q){
  if(!Q.mots || !Q.mots.length) return false;
  var pm = (Q.pm && Q.pm.length) ? Q.pm : Q.mots;
  var expr = ' ' + pm.join(' ') + ' ';
  if(r.nt === Q.cle) return true;
  if((r.al||[]).indexOf(Q.cle) >= 0) return true;
  if((' ' + (r.nt||'') + ' ').indexOf(expr) >= 0) return true;
  if((' ' + (r.nd||'') + ' ').indexOf(expr) >= 0) return true;
  return false;
}

var REP_OK = {def:1, notion:1, dossier:1, auteur:1, formule:1, atlas:1};
function reponsePrincipale(exactes, Q){
  /* une réponse n'est mise en avant que si une entrée porte exactement le
     libellé cherché : sinon on laisse la liste parler */
  if(!exactes.length) return null;
  var syn = (Q.syn || []).map(cle);
  var kq = (Q.pm && Q.pm.length) ? Q.pm.join(' ') : Q.cle;
  var i, g, r;
  for(i = 0; i < Math.min(exactes.length, 5); i++){
    g = exactes[i]; r = g.prim;
    if(!REP_OK[r.y]) continue;
    if(!r.d || r.d.length < 40) continue;
    var bon = r.nt === Q.cle || r.nt === kq
      || (r.al||[]).indexOf(Q.cle) >= 0 || (r.al||[]).indexOf(kq) >= 0
      || syn.indexOf(r.nt) >= 0;
    if(bon) return g;
  }
  return null;
}

/* ====================================================== rendu */
function esc(s){ return (s==null?'':String(s))
  .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
  .replace(/"/g,'&quot;'); }

function surligner(txt, Q, al){
  var t = esc(txt), zones = [], i;
  var cibles = [];
  if(Q.nq && Q.nq.length >= 3) cibles.push(Q.nq);
  if(Q.pm && Q.pm.length > 1) cibles.push(Q.pm.join(' '));
  if(Q.mots && Q.mots.length > 1) cibles.push(Q.mots.join(' '));
  for(i=0;i<(Q.mots||[]).length;i++) if(Q.mots[i].length > 2) cibles.push(Q.mots[i]);
  (Q.syn||[]).forEach(function(z){ if(z && z.length > 2) cibles.push(nz(z)); });
  (al||[]).forEach(function(z){
    if(!z || z.length < 3) return;
    if(Q.cle === z || (Q.syn||[]).indexOf(z) >= 0 || cle(z) === Q.cle)
      cibles.push(nz(z));
  });
  if(!cibles.length) return t;
  var nt = nz(t);
  cibles.forEach(function(c){
    var p = nt.indexOf(c), garde = 0;
    while(p >= 0 && garde < 60){
      var fin = p + c.length;
      while(fin < nt.length && /[a-z0-9]/.test(nt.charAt(fin))) fin++;
      zones.push([p, fin]);
      p = nt.indexOf(c, p + c.length); garde++;
    }
  });
  if(!zones.length) return t;
  zones.sort(function(a,b){ return a[0]-b[0]; });
  var fz = [], cur = zones[0].slice();
  for(i=1;i<zones.length;i++){
    if(zones[i][0] <= cur[1]) cur[1] = Math.max(cur[1], zones[i][1]);
    else { fz.push(cur); cur = zones[i].slice(); }
  }
  fz.push(cur);
  var out = '', pos = 0;
  fz.forEach(function(z){
    out += t.slice(pos, z[0]) + '<mark>' + t.slice(z[0], z[1]) + '</mark>';
    pos = z[1];
  });
  return out + t.slice(pos);
}

function extrait(txt, Q, long){
  var t = ' ' + (txt||'').replace(/\s+/g,' ').trim() + ' ';
  var n = nz(t), lim = long || 260;
  var p = -1, i;
  if(Q.pm && Q.pm.length > 1) p = n.indexOf(' ' + Q.pm.join(' ') + ' ');
  if(p < 0 && Q.mots && Q.mots.length > 1) p = n.indexOf(' ' + Q.mots.join(' ') + ' ');
  if(p < 0 && Q.nq && Q.nq.length >= 3) p = n.indexOf(Q.nq);
  if(p < 0) for(i=0;i<(Q.mots||[]).length;i++){ p = n.indexOf(Q.mots[i]); if(p>=0) break; }
  if(p < 0) return t.trim().slice(0, lim) + (t.length > lim ? '…' : '');
  if(t.length <= lim) return t.trim();
  var a = Math.max(0, p - Math.round(lim*0.34));
  var pt = t.lastIndexOf('. ', p);
  if(pt > a - 70 && pt > 0 && pt < p) a = pt + 2;
  else { var sp = t.indexOf(' ', a); if(sp > 0 && sp < p) a = sp + 1; }
  var b = Math.min(t.length, a + lim);
  var sp2 = t.lastIndexOf(' ', b);
  if(sp2 > a + 60) b = sp2;
  return (a > 1 ? '…' : '') + t.slice(a, b).trim() + (b < t.length - 1 ? '…' : '');
}

function lieu(r){
  if(r.y === 'auteur') return r.c && D.ch[r.c] ? D.ch[r.c].l : 'auteurs';
  if(r.y === 'visu') return 'visualisations';
  if(r.y === 'dossier') return 'Autour d’une notion'
    + (r.etat === 'hors-cours' ? ' · hors cours' : '');
  if(r.y === 'atlas') return 'Atlas' + (D.ch[r.c] ? ' · ' + D.ch[r.c].l : '');
  if(r.y === 'resume') return 'résumés' + (D.ch[r.c] ? ' · ' + D.ch[r.c].l : '');
  if(r.y === 'sujet') return 'sujets' + (D.ch[r.c] ? ' · ' + D.ch[r.c].l : '');
  if(r.y === 'fiche') return 'fiches' + (D.ch[r.c] ? ' · ' + D.ch[r.c].l : '');
  if(r.y === 'chiffre') return 'chiffres' + (D.ch[r.c] ? ' · ' + D.ch[r.c].l : '');
  if(!r.c || !D.ch[r.c]) return '';
  return D.ch[r.c].l;
}

function texteDe(r, Q){
  var t = r.d || '';
  if(!t && r.y === 'sect'){ try{ t = texteSection(r.c, r.b); }catch(e){} }
  if(!t && r.y === 'sujet') t = 'Sujet de dissertation.';
  return t;
}

/* --------------------------------------------------- où le retrouver
   Les destinations ne sont plus une suite de pastilles : elles sont
   réparties par section — Cours, Fiches, Atlas, Visualisations… — et, dans
   le cours, regroupées par chapitre, pour ne plus répéter dix fois le même
   libellé de chapitre. */
var OU_GROUPES = [
  ['cours',    'Cours'],
  ['notions',  'Notions'],
  ['fiches',   'Fiches'],
  ['resumes',  'Résumés'],
  ['dossiers', 'Dossiers'],
  ['atlas',    'Atlas'],
  ['auteurs',  'Auteurs'],
  ['chiffres', 'Chiffres & faits'],
  ['formules', 'Formules'],
  ['visu',     'Visualisations'],
  ['sujets',   'Sujets']
];

function chLib(c){ return D.ch[c] ? D.ch[c].l : (c || ''); }
function chCourt(l){
  return String(l || '').replace('Chapitre ', 'ch.').replace('2ᵉ année — ', '2ᵉ ');
}

/* coupe au dernier mot entier plutôt qu'au milieu d'un mot */
function coupe(s, n){
  s = String(s == null ? '' : s).replace(/\s+/g, ' ').trim();
  if(s.length <= n) return s;
  var t = s.slice(0, n), e = t.lastIndexOf(' ');
  if(e > n * 0.55) t = t.slice(0, e);
  return t.replace(/[\s,;:.’'-]+$/, '') + '…';
}

function ouItems(l, cap){
  function bt(e){
    return '<button class="rq-o" data-k="' + esc(e.k) + '">' + esc(e.l)
      + '</button>';
  }
  if(l.length <= cap + 1) return l.map(bt).join('');
  return l.slice(0, cap).map(bt).join('')
    + '<span class="rq-cache" data-cache="1">' + l.slice(cap).map(bt).join('')
    + '</span><button class="rq-ou-plus" data-tout="1">+ '
    + (l.length - cap) + ' autres</button>';
}

function puces(g, Q, cap){
  var vus = Object.create(null), vusLib = Object.create(null);
  var ents = [], prim = g.prim;
  cap = cap || 5;
  function pose(k, grp, ch, lib){
    var sig = JSON.stringify(k);
    if(vus[sig] || !lib) return;
    /* deux blocs distincts portant le même intitulé dans le même chapitre
       n'ont pas à figurer deux fois dans la liste des destinations */
    var sigl = grp + '|' + (ch || '') + '|' + nz(lib);
    if(vusLib[sigl]) return;
    vus[sig] = 1; vusLib[sigl] = 1;
    ents.push({k:sig, g:grp, ch:ch || '', l:lib});
  }
  if(prim.y === 'def' && prim.ou && prim.ou.length){
    prim.ou.forEach(function(z){
      if(!D.ch[z[0]]) return;
      pose(['ch', z[0], z[1]], 'cours', chLib(z[0]),
        z[1] >= 0 ? 'le passage' : 'le chapitre');
    });
  }
  var parL = Object.create(null);
  g.items.forEach(function(r){
    if(r === prim) return;
    var y = r.y;
    if(y === 'passage' || y === 'sect'){
      var sg = r.c + '|' + cle(r.sect || r.t);
      if(parL[sg]) return;
      parL[sg] = 1;
      pose(r.k, 'cours', chLib(r.c), coupe(R_TITRE(r.sect || r.t), 56));
    }
    else if(y === 'notion')  pose(r.k, 'notions', chLib(r.c), coupe(r.t, 48));
    else if(y === 'fiche')   pose(r.k, 'fiches', '', chLib(r.c));
    else if(y === 'resume')  pose(r.k, 'resumes', '', chLib(r.c));
    else if(y === 'dossier') pose(r.k, 'dossiers', '', coupe(r.t, 52));
    else if(y === 'atlas')   pose(r.k, 'atlas', '',
      (r.aut ? r.aut + ' — ' : '') + coupe(r.t, 44));
    else if(y === 'auteur')  pose(r.k, 'auteurs', '', r.t);
    else if(y === 'chiffre') pose(r.k, 'chiffres', '', coupe(r.t, 52));
    else if(y === 'fait')    pose(r.k, 'chiffres', '',
      String(r.an) + (r.t ? ' — ' + coupe(r.t, 40) : ''));
    else if(y === 'formule') pose(r.k, 'formules', '', coupe(r.t, 50));
    else if(y === 'sujet')   pose(r.k, 'sujets', '', coupe(r.t, 64));
    else if(y === 'visu')    pose(r.k, 'visu', '', coupe(r.t, 46));
  });
  if(!ents.length) return '';

  var html = '', maxSg = cap >= 3 ? 3 : 2;
  OU_GROUPES.forEach(function(G0){
    var l = ents.filter(function(e){ return e.g === G0[0]; });
    if(!l.length) return;
    var corps;
    if(G0[0] === 'cours' || G0[0] === 'notions'){
      var ordre = [], parCh = Object.create(null);
      l.forEach(function(e){
        if(!parCh[e.ch]){ parCh[e.ch] = []; ordre.push(e.ch); }
        parCh[e.ch].push(e);
      });
      var sgs = ordre.map(function(c){
        return '<div class="rq-sg">'
          + (c ? '<span class="rq-sg-t">' + esc(c) + '</span>' : '')
          + ouItems(parCh[c], cap) + '</div>';
      });
      /* au-delà de trois chapitres, les suivants restent pliés : la carte
         de réponse n'a pas à dérouler vingt destinations */
      corps = sgs.length <= maxSg + 1 ? sgs.join('')
        : sgs.slice(0, maxSg).join('')
          + '<span class="rq-cache" data-cache="1">' + sgs.slice(maxSg).join('')
          + '</span><button class="rq-ou-plus" data-tout="1">+ '
          + (sgs.length - maxSg) + ' chapitres</button>';
    } else {
      corps = '<div class="rq-sg">' + ouItems(l, cap) + '</div>';
    }
    html += '<div class="rq-g"><div class="rq-g-l">' + G0[1] + '</div>'
      + '<div class="rq-g-c">' + corps + '</div></div>';
  });
  return '<div class="rq-ou"><div class="rq-ou-t">Où le retrouver'
    + '<span>' + ents.length + '</span></div>' + html + '</div>';
}

/* ------------------------------------------------- à ne pas confondre */
function confondre(r, fam){
  if(r.x)
    return '<div class="rq-conf"><div class="rq-conf-t">À ne pas confondre'
      + '</div><div class="rq-conf-d">' + esc(r.x) + '</div></div>';
  if(!fam || fam.membres.length < 2) return '';
  var autres = fam.membres.filter(function(z){ return z.nt !== r.nt; }).slice(0, 6);
  if(!autres.length) return '';
  return '<div class="rq-conf"><div class="rq-conf-t">À ne pas confondre avec'
    + '</div><div class="rq-conf-l">' + autres.map(function(z){
        return '<button class="rq-cf" data-q="' + esc(z.t) + '"><b>'
          + esc(z.t) + '</b>'
          + (z.c && D.ch[z.c] ? '<i>' + esc(chCourt(D.ch[z.c].l)) + '</i>' : '')
          + '</button>';
      }).join('') + '</div></div>';
}

/* --------------------------------------------------------------- réponse */
function rendreReponse(g, Q, fam){
  if(!g) return '';
  var r = g.prim;
  var meta = ['<span class="rq-ty ' + (TYPE_CL[r.y] || '') + '">'
    + esc(TYPE_LIB[r.y] || r.y) + '</span>'];
  if(lieu(r)) meta.push(esc(lieu(r)));
  if(r.o && r.o.indexOf('redigee') >= 0)
    meta.push('définition rédigée d’après le cours');
  else if(r.o && r.o.indexOf('cours-encadre') >= 0)
    meta.push('définition du cours');
  var alias = (r.al || []).filter(function(z){
    return z && z !== r.nt && (z === Q.cle || (Q.syn || []).indexOf(z) >= 0); });
  if(alias.length)
    meta.push('aussi écrit ' + esc(alias.join(', ').toUpperCase()));
  return '<div class="rq-rep">'
    + '<div class="rq-rep-k">Réponse</div>'
    + '<div class="rq-rep-t">' + esc(r.t) + '</div>'
    + '<div class="rq-rep-m">' + meta.join('<i>·</i>') + '</div>'
    + '<div class="rq-rep-d">' + surligner(texteDe(r, Q), Q, r.al) + '</div>'
    + confondre(r, fam) + puces(g, Q, 3) + '</div>';
}

/* --------------------------------------------------------------- famille */
function rendreFamille(fam, Q){
  if(!fam) return '';
  var l = fam.membres.filter(function(z){ return z.nt !== Q.cle; });
  if(l.length < 2) return '';
  return '<div class="rq-fam"><div class="rq-fam-t">Les formes de <b>« '
    + esc(fam.tete) + ' »</b> dans tes chapitres<span>' + l.length + '</span>'
    + '</div><div class="rq-fam-l">' + l.map(function(z){
        return '<button class="rq-k" data-q="' + esc(z.t) + '">' + esc(z.t)
          + (z.c && D.ch[z.c] ? '<em>' + esc(chCourt(D.ch[z.c].l)) + '</em>' : '')
          + '</button>';
      }).join('') + '</div></div>';
}

/* --------------------------------------------------------------- lignes */
function rendreLigne(g, Q, i){
  var r = g.prim;
  var txt = texteDe(r, Q);
  var chemin = r.path || (r.y === 'sect' ? r.p : '');
  return '<div class="rq-r" data-i="' + i + '">'
    + '<div class="rq-rh" data-bascule="1">'
    + '<span class="rq-rt">' + surligner(r.t, Q, r.al)
    + (g.items.length > 1 ? ' <i>· ' + g.items.length + ' occurrences</i>' : '')
    + '</span>'
    + '<span class="rq-rm">'
    + '<span class="rq-ty ' + (TYPE_CL[r.y] || '') + '">'
    + esc(TYPE_LIB[r.y] || r.y) + '</span>'
    + (lieu(r) ? '<span class="rq-ch">' + esc(lieu(r)) + '</span>' : '')
    + '</span>'
    + '<span class="rq-car">›</span></div>'
    + (txt ? '<div class="rq-ex">' + surligner(extrait(txt, Q, 300), Q, r.al)
        + '</div>' : '')
    + '<div class="rq-corps">'
    + confondre(r, null)
    + (chemin ? '<div class="rq-path">' + esc(chemin) + '</div>' : '')
    + '<button class="rq-go" data-k="' + esc(JSON.stringify(r.k)) + '">'
    + 'Ouvrir ' + esc(ouLib(r)) + ' <span>→</span></button>'
    + puces(g, Q, 2)
    + '</div></div>';
}
function ouLib(r){
  if(r.y === 'passage' || r.y === 'sect' || r.y === 'def' || r.y === 'fait'
     || r.y === 'notion') return 'le passage';
  if(r.y === 'auteur') return 'la fiche de l’auteur';
  if(r.y === 'dossier') return 'le dossier';
  if(r.y === 'atlas') return 'l’Atlas';
  if(r.y === 'chiffre') return 'les chiffres';
  if(r.y === 'resume') return 'le résumé';
  if(r.y === 'sujet') return 'les sujets';
  if(r.y === 'fiche') return 'les fiches';
  if(r.y === 'visu') return 'la visualisation';
  if(r.y === 'formule') return 'les formules';
  return 'la section';
}

var PAS = 12;
var MONTRE = {ex:PAS, el:PAS};

function rendre(R){
  var Q = R.Q;
  var rep = document.getElementById('rq-rep');
  var fam = document.getElementById('rq-fam');
  var out = document.getElementById('rq-outils');
  var box = document.getElementById('rq-res');

  if(!R.groupes.length){
    rep.innerHTML = ''; fam.innerHTML = '';
    out.innerHTML = barreOutils(R);
    var pistes = ['position extérieure nette','capital humain',
      'avantage comparatif','anomie','Bairoch','destruction créatrice'];
    box.innerHTML = '<div class="rq-vide"><div class="rq-vide-t">'
      + 'Rien dans ÉcoSphère ne porte cette expression.</div>'
      + 'La recherche balaie le texte des quatorze chapitres, les fiches, les '
      + 'auteurs, les sujets, les dossiers, l’Atlas, les chiffres et les '
      + 'résumés. Si l’expression n’y est pas, c’est qu’elle n’est pas '
      + 'traitée dans tes cours.'
      + '<div class="rq-pistes">' + pistes.map(function(x){
          return '<button class="rq-k" data-q="' + esc(x) + '">' + esc(x)
            + '</button>';
        }).join('') + '</div></div>';
    return;
  }
  rep.innerHTML = rendreReponse(R.reponse, Q, R.famille);
  fam.innerHTML = rendreFamille(R.famille, Q);
  out.innerHTML = barreOutils(R);

  var h = '';
  var ex = R.exactes.filter(function(g){ return g !== R.reponse; });
  if(ex.length){
    h += '<div class="rq-bloc-t">Correspondances exactes<em>' + ex.length
      + '</em></div>';
    h += ex.slice(0, MONTRE.ex).map(function(g, i){
      return rendreLigne(g, Q, 'e' + i); }).join('');
    if(ex.length > MONTRE.ex)
      h += '<button class="rq-plus" data-plus="ex">Afficher '
        + Math.min(PAS, ex.length - MONTRE.ex) + ' résultats de plus · '
        + (ex.length - MONTRE.ex) + ' restants</button>';
  }
  if(R.elargies.length){
    h += '<div class="rq-bloc-t">Recherche élargie<em>' + R.elargies.length
      + ' · l’expression n’y figure pas telle quelle</em></div>';
    h += R.elargies.slice(0, MONTRE.el).map(function(g, i){
      return rendreLigne(g, Q, 'l' + i); }).join('');
    if(R.elargies.length > MONTRE.el)
      h += '<button class="rq-plus" data-plus="el">Afficher '
        + Math.min(PAS, R.elargies.length - MONTRE.el) + ' résultats de plus · '
        + (R.elargies.length - MONTRE.el) + ' restants</button>';
  }
  box.innerHTML = h;
}

function barreOutils(R){
  var Q = R.Q, c = comptesRequete(R);
  var tot = R.groupes.length;
  var msg = '<div class="rq-cpt"><b>' + (R.montres || tot) + '</b> '
    + ((R.montres || tot) > 1 ? 'résultats' : 'résultat')
    + (R.tronque ? ' les plus pertinents sur ' + tot : '')
    + (R.exactes.length && R.elargies.length
        ? ' · ' + R.exactes.length + ' exacts' : '')
    + (Q.ch ? ' · chapitre ' + esc(Q.ch) : '') + '</div>';
  var ordre = ['tout','definitions','cours','auteurs','dossiers','atlas',
    'chiffres','faits','formules','sujets','fiches','resumes','visu'];
  var dispo = ordre.filter(function(f){
    return f === 'tout' || f === FILTRE || (c[f] || 0) > 0; });
  var liens = dispo.slice(0, 7).map(function(f){
    var n = f === 'tout' ? tot : (c[f] || 0);
    return '<button class="rq-f' + (f === FILTRE ? ' on' : '') + '" data-f="'
      + f + '">' + FAM_LIB[f] + '<u>' + n + '</u></button>';
  }).join('');
  var sel = '<select class="rq-sel" id="rq-sel">' + dispo.map(function(f){
    var n = f === 'tout' ? tot : (c[f] || 0);
    return '<option value="' + f + '"' + (f === FILTRE ? ' selected' : '')
      + '>' + FAM_LIB[f] + ' (' + n + ')</option>';
  }).join('') + '</select>';
  var corr = '';
  if(Q.corrige)
    corr = '<div class="rq-corr">Aucun résultat pour '
      + '« <b>' + esc(Q.brut) + '</b> » : recherche élargie à « <b>'
      + esc(Q.mots.join(' ')) + '</b> ».'
      + '<button data-litteral="1">chercher « ' + esc(Q.brut)
      + ' » littéralement</button></div>';
  return corr + msg + sel + '<div class="rq-fl">' + liens + '</div>';
}

function comptesRequete(R){
  /* effectifs par famille de type, sur la requête en cours */
  var c = Object.create(null);
  R.groupes.forEach(function(g){
    Object.keys(FAM).forEach(function(f){
      if(f === 'tout') return;
      if((FAM[f]||[]).indexOf(g.prim.y) >= 0) c[f] = (c[f]||0) + 1;
    });
  });
  return c;
}

/* ====================================================== ouverture */
function ouvrir(k){
  if(!k) return;
  var t = k[0];
  try{
    if(t === 'ch'){
      var ch = k[1], b = k[2];
      if(typeof openCh === 'function') openCh(Number(ch) || ch);
      if(typeof showSect === 'function') { try{ showSect('cours'); }catch(e){} }
      if(b != null && b >= 0) viserBloc(ch, b);
    } else if(t === 'nt'){
      if(typeof openCh === 'function') openCh(Number(k[1]) || k[1]);
      if(typeof showSect === 'function') { try{ showSect('notions'); }catch(e){} }
      viserTexte('sect-notions', k[2]);
    } else if(t === 'au'){
      if(typeof openAuthorByName === 'function') openAuthorByName(k[1]);
      else if(typeof allerAuteur === 'function') allerAuteur(k[1]);
    } else if(t === 'do'){
      if(typeof window.ouvrirNotion === 'function') window.ouvrirNotion(k[1]);
      else if(typeof allerDossier === 'function') allerDossier(k[1]);
    } else if(t === 'at'){
      if(typeof allerAtlas === 'function') allerAtlas(k[1]);
      else showPg('atlas');
    } else if(t === 'ci'){
      if(typeof window.ouvrirChiffres === 'function') window.ouvrirChiffres(k[1]);
      else showPg('chiffres');
    } else if(t === 're'){
      if(typeof window.ouvrirResume === 'function') window.ouvrirResume(k[1]);
      else showPg('resumes');
    } else if(t === 'su'){
      if(typeof ouvrirSujets === 'function') ouvrirSujets(Number(k[1]) || k[1]);
      else showPg('subjects');
    } else if(t === 'fc'){
      showPg('fc');
      if(typeof filterFC === 'function') setTimeout(function(){
        filterFC(Number(k[1]) || 0); }, 60);
    } else if(t === 'vz'){
      if(typeof window.VZ_OUVRIR === 'function') window.VZ_OUVRIR(k[1]);
      else showPg('visualisations');
    } else if(t === 'fo'){
      showPg('formulas');
      viser('[data-rf="' + k[1] + '"]', 'pg-formulas');
    }
  }catch(e){ try{ console.warn('[recherche]', e); }catch(_){} }
}
function viserBloc(c, b){
  /* d'abord le marquage posé au découpage ; s'il a été effacé par un
     réaffichage du chapitre, on retrouve le bloc par son texte */
  var bl = (BL[c] || [])[b];
  var cible = bl ? nz(bl.x).slice(0, 80) : '';
  var essais = 0;
  (function boucle(){
    essais++;
    var p = document.getElementById('sect-cours');
    var el = p ? p.querySelector('[data-rb="' + b + '"]') : null;
    if(!el && p && cible){
      var cands = p.querySelectorAll(SEL), i;
      for(i = 0; i < cands.length; i++){
        var z = nz(cands[i].innerText || '');
        if(z.length > 10 && (z.indexOf(cible) === 0 || cible.indexOf(z.slice(0, 60)) === 0)){
          el = cands[i]; break;
        }
      }
      if(!el){
        for(i = 0; i < cands.length; i++){
          if(nz(cands[i].innerText || '').indexOf(cible.slice(0, 50)) >= 0){
            el = cands[i]; break;
          }
        }
      }
    }
    if(el){ flasher(el); return; }
    if(essais < 16) setTimeout(boucle, 120);
  })();
}
function flasher(el){
  try{ el.scrollIntoView({behavior:'smooth', block:'center'}); }
  catch(e){ try{ el.scrollIntoView(); }catch(_){} }
  el.classList.remove('rq-flash');
  void el.offsetWidth;
  el.classList.add('rq-flash');
}
function viser(sel, dans){
  var essais = 0;
  (function boucle(){
    essais++;
    var p = document.getElementById(dans);
    var el = p ? p.querySelector(sel) : document.querySelector(sel);
    if(el){
      try{ el.scrollIntoView({behavior:'smooth', block:'center'}); }
      catch(e){ el.scrollIntoView(); }
      el.classList.remove('rq-flash');
      void el.offsetWidth;
      el.classList.add('rq-flash');
      return;
    }
    if(essais < 14) setTimeout(boucle, 110);
  })();
}
function viserTexte(dans, texte){
  var essais = 0, cible = nz(texte);
  (function boucle(){
    essais++;
    var p = document.getElementById(dans);
    if(p){
      var els = p.querySelectorAll('.dt'), i;
      for(i=0;i<els.length;i++){
        if(nz(els[i].textContent).indexOf(cible) === 0){
          var bl = els[i].closest('.db') || els[i];
          try{ bl.scrollIntoView({behavior:'smooth', block:'center'}); }
          catch(e){ bl.scrollIntoView(); }
          bl.classList.remove('rq-flash'); void bl.offsetWidth;
          bl.classList.add('rq-flash');
          return;
        }
      }
    }
    if(essais < 14) setTimeout(boucle, 110);
  })();
}

/* ====================================================== interface */
var MINUT = null, DERNIER = null, SUG = [], SUGi = -1;

function compter(){
  ajouterEntrees();
  var c = Object.create(null), i;
  for(i=0;i<E.length;i++) c[E[i].y] = (c[E[i].y]||0) + 1;
  var tot = 0;
  Object.keys(D.ch).forEach(function(k){ tot += D.ch[k].n; });
  c.passage = tot;
  return c;
}

/* ------------------------------------------------------- suggestions */
var PREFIX = null;
function prefixes(){
  if(PREFIX) return PREFIX;
  ajouterEntrees();
  var l = [], i, e;
  for(i=0;i<E.length;i++){
    e = E[i];
    if(e.y !== 'def' && e.y !== 'notion' && e.y !== 'dossier'
       && e.y !== 'auteur') continue;
    l.push(e);
  }
  l.sort(function(a,b){
    var p = {def:3, notion:2, auteur:2, dossier:1};
    return (p[b.y]||0) - (p[a.y]||0) || a.nt.length - b.nt.length;
  });
  PREFIX = l;
  return l;
}
function suggerer(q){
  var k = cle(q);
  if(!k || k.length < 2) return [];
  var l = prefixes(), out = [], vus = Object.create(null), i, e;
  for(i=0;i<l.length && out.length < 8; i++){
    e = l[i];
    if(e.nt.indexOf(k) !== 0) continue;
    if(vus[e.nt]) continue;
    vus[e.nt] = 1;
    out.push(e);
  }
  for(i=0;i<l.length && out.length < 8; i++){
    e = l[i];
    if((' ' + e.nt + ' ').indexOf(' ' + k) < 0) continue;
    if(vus[e.nt]) continue;
    vus[e.nt] = 1;
    out.push(e);
  }
  return out;
}
function rendreSug(q){
  var z = document.getElementById('rq-sug');
  if(!z) return;
  SUG = (q || '').length >= 2 ? suggerer(q) : [];
  SUGi = -1;
  if(!SUG.length){ z.classList.remove('on'); z.innerHTML = ''; return; }
  z.innerHTML = SUG.map(function(e, i){
    return '<div class="rq-s" data-i="' + i + '" role="option"><b>'
      + esc(e.t) + '</b><span>' + esc(TYPE_LIB[e.y] || e.y)
      + (e.c && D.ch[e.c] ? ' · ' + esc(D.ch[e.c].l) : '') + '</span></div>';
  }).join('');
  z.classList.add('on');
}
function fermerSug(){
  var z = document.getElementById('rq-sug');
  if(z){ z.classList.remove('on'); }
  SUGi = -1;
}

/* ------------------------------------------------------- recherche */
function lancer(v, garderSug){
  var inp = document.getElementById('rq-in');
  if(v != null) inp.value = v;
  var q = (inp.value || '').trim();
  document.getElementById('rq-x').classList.toggle('on', !!q);
  if(!garderSug) fermerSug();
  MONTRE = {ex:PAS, el:PAS};
  if(!q){
    document.getElementById('rq-rep').innerHTML = '';
    document.getElementById('rq-fam').innerHTML = '';
    document.getElementById('rq-outils').innerHTML = '';
    document.getElementById('rq-res').innerHTML =
      '<div class="rq-vide"><div class="rq-vide-t">Que cherches-tu ?</div>'
      + 'Une notion, une définition, un auteur, une formule, un chiffre, une '
      + 'date. La recherche couvre le texte des <b>quatorze chapitres</b> au '
      + 'paragraphe près, et toutes les autres sections d’ÉcoSphère.'
      + '<div class="rq-pistes">'
      + ['capital','taux de change','position extérieure nette','anomie',
         'avantage comparatif','destruction créatrice'].map(function(x){
          return '<button data-q="' + esc(x) + '">' + esc(x) + '</button>';
        }).join('') + '</div></div>';
    return;
  }
  DERNIER = chercher(q);
  rendre(DERNIER);
}

function litteral(){
  /* refaire la recherche sans correction orthographique */
  if(!DERNIER) return;
  var q = DERNIER.Q.brut;
  SANS_CORRECTION = true;
  DERNIER = chercher(q);
  SANS_CORRECTION = false;
  rendre(DERNIER);
}

function brancher(){
  var inp = document.getElementById('rq-in');
  if(!inp || inp.__rq) return;
  inp.__rq = 1;

  inp.addEventListener('input', function(){
    clearTimeout(MINUT);
    rendreSug(inp.value.trim());
    MINUT = setTimeout(function(){ lancer(null, true); }, 150);
  });
  inp.addEventListener('keydown', function(e){
    if(e.key === 'ArrowDown' || e.key === 'ArrowUp'){
      if(!SUG.length) return;
      e.preventDefault();
      SUGi += (e.key === 'ArrowDown' ? 1 : -1);
      if(SUGi < 0) SUGi = SUG.length - 1;
      if(SUGi >= SUG.length) SUGi = 0;
      var z = document.getElementById('rq-sug');
      [].forEach.call(z.querySelectorAll('.rq-s'), function(el, i){
        el.classList.toggle('sel', i === SUGi); });
    } else if(e.key === 'Enter'){
      if(SUGi >= 0 && SUG[SUGi]) lancer(SUG[SUGi].t);
      else lancer();
      fermerSug();
    } else if(e.key === 'Escape'){
      fermerSug();
    }
  });
  inp.addEventListener('blur', function(){ setTimeout(fermerSug, 160); });

  document.getElementById('rq-x').addEventListener('click', function(){
    lancer(''); inp.focus();
  });
  document.getElementById('rq-sug').addEventListener('mousedown', function(e){
    var el = e.target.closest('[data-i]');
    if(!el) return;
    e.preventDefault();
    var i = Number(el.getAttribute('data-i'));
    if(SUG[i]) lancer(SUG[i].t);
  });
  document.getElementById('rq-outils').addEventListener('click', function(e){
    var b = e.target.closest('[data-f]');
    if(b){ FILTRE = b.getAttribute('data-f'); lancer(); return; }
    if(e.target.closest('[data-litteral]')){ litteral(); return; }
  });
  document.getElementById('rq-outils').addEventListener('change', function(e){
    var s = e.target.closest('#rq-sel');
    if(s){ FILTRE = s.value; lancer(); }
  });

  function clics(e){
    var q = e.target.closest('[data-q]');
    if(q){ lancer(q.getAttribute('data-q')); return; }
    var pl = e.target.closest('[data-plus]');
    if(pl){
      var k = pl.getAttribute('data-plus');
      MONTRE[k] += PAS;
      rendre(DERNIER);
      return;
    }
    var tt = e.target.closest('[data-tout]');
    if(tt){
      var l = tt.parentNode.querySelector('[data-cache]');
      if(l){ l.style.display = 'contents'; }
      tt.remove();
      return;
    }
    var k2 = e.target.closest('[data-k]');
    if(k2){
      var a = null;
      try{ a = JSON.parse(k2.getAttribute('data-k')); }catch(err){}
      ouvrir(a);
      return;
    }
    var bs = e.target.closest('[data-bascule]');
    if(bs){
      var r = bs.closest('.rq-r');
      if(r) r.classList.toggle('ouvert');
      return;
    }
  }
  document.getElementById('rq-res').addEventListener('click', clics);
  document.getElementById('rq-rep').addEventListener('click', clics);
  document.getElementById('rq-fam').addEventListener('click', clics);

  lancer();
}

/* l'ancien moteur est désactivé : plus rien ne le lit ni ne le reconstruit */
function neutraliser(){
  try{
    window.doSearch = function(){ try{ lancer(); }catch(e){} };
    window.setF = function(){};
    window.rebuildSearchIndex = function(){};
  }catch(e){}
}

function preparer(){
  var ks = Object.keys(D.ch), i = 0;
  (function suite(){
    if(i >= ks.length){ vocabulaire(); return; }
    try{ blocsChapitre(ks[i]); }catch(e){}
    i++;
    setTimeout(suite, 0);
  })();
}

function demarrer(){
  neutraliser();
  brancher();
  preparer();
}

if(typeof window.showPg === 'function'){
  var vieux = window.showPg;
  window.showPg = function(id){
    var r = vieux.apply(this, arguments);
    if(id === 'search'){
      setTimeout(function(){
        brancher();
        var i = document.getElementById('rq-in');
        if(i && !i.value){ try{ i.focus(); }catch(e){} }
      }, 40);
    }
    return r;
  };
}

if(document.readyState === 'loading')
  document.addEventListener('DOMContentLoaded', function(){ setTimeout(demarrer, 600); });
else setTimeout(demarrer, 600);
[1200, 3000, 6000].forEach(function(t){ setTimeout(function(){
  try{ neutraliser(); brancher(); }catch(e){} }, t); });

setTimeout(function(){
  try{
    var c = compter();
    console.log('[ÉcoSphère v219] Recherche — ' + c.passage + ' blocs de cours, '
      + Object.keys(D.def).length + ' définitions, ' + c.auteur + ' auteurs, '
      + c.dossier + ' dossiers, ' + c.atlas + ' idées, ' + c.chiffre
      + ' chiffres, ' + c.fait + ' faits datés, '
      + Object.keys(familles()).length + ' familles de notions');
  }catch(e){}
}, 8000);

window.__ECO_RECHERCHE = {familles:familles, familleDe:familleDe,
  debug:function(q){
    var R = chercher(q);
    return {n:R.n, groupes:R.groupes.length, Q:{cle:R.Q.cle, mots:R.Q.mots,
      corrige:R.Q.corrige, ch:R.Q.ch},
      liste:R.groupes.slice(0,14).map(function(g){ return {
        cle:g.cle, sc:g.sc, n:g.items.length,
        prim:{y:g.prim.y, t:g.prim.t, c:g.prim.c, b:g.prim.b, sc:g.prim.sc},
        types:g.items.map(function(x){ return x.y; })};})};
  },
  chercher:chercher, analyser:analyser,
  blocs:function(k){ return blocsChapitre(k); }, entrees:ajouterEntrees,
  compter:compter, filtre:function(f){ FILTRE = f; poserChips(); lancer(); },
  ouvrir:ouvrir, lancer:lancer, cle:cle, nz:nz};
})();
</script>
"""

MOTEUR = MOTEUR.replace('__PAYLOAD__', json.dumps(
    DATA, ensure_ascii=False, separators=(',', ':')))

s = s.rstrip() + '\n' + STYLE.strip() + '\n\n' + MOTEUR.strip() + '\n'
io.open(DST, 'w', encoding='utf-8').write(s)
print('ancien balisage retiré : %d octets' % len(ANCIEN))
print('définitions embarquées : %d' % len(DATA['def']))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
