# -*- coding: utf-8 -*-
import meth_base as M
from meth_grille import GRILLE
from meth_fil import PIECES, PLAN, SUJET

PLAN['sujetLibelle'] = SUJET
M.monter(GRILLE, PIECES, PLAN, 'methode.json')
