# -*- coding: utf-8 -*-
import importlib, cb_base as Z
MODULES = ['cb_macro1', 'cb_macro2', 'cb_macro3', 'cb_ch26',
           'cb_micro1', 'cb_micro2', 'cb_micro3',
           'cb_crois', 'cb_divers', 'cb_entrep', 'cb_data']
CATS = {'macro': 'Macroéconomie et politiques',
        'ouverte': 'Économie ouverte et changes',
        'micro': 'Microéconomie et marchés',
        'croissance': 'Croissance, inégalités et développement',
        'entreprise': 'Entreprises, concurrence et travail',
        'inter': 'Commerce international et mondialisation'}
F = []
for m in MODULES:
    try:
        F += importlib.import_module(m).L
    except ModuleNotFoundError:
        pass
Z.monter(F, CATS, 'courbes.json')
