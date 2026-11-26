# -*- coding: utf-8 -*-
"""L'exemple fil rouge : « Faut-il toujours défendre le libre-échange ? »

Toutes les pièces portent sur le même sujet, du premier mot de l'accroche à
la dernière phrase de l'ouverture. Les références proviennent des cours
d'ÉcoSphère (chapitres 3, 6, 21, 22, 23 et 24).

Balisage : [[u:…]] = souligné dans la copie (titre d'ouvrage).
"""

from meth_base import piece, para, note, glob

SUJET = 'Faut-il toujours défendre le libre-échange ?'

# ============================================================ introduction

INTRO = piece(
 id='intro',
 t='Introduction rédigée',
 st='Quatre paragraphes : accroche isolée, analyse des termes, cadrage et '
    'problématique, annonce du plan isolée.',
 meta='4 paragraphes · environ 35 lignes manuscrites',
 chapeau='L’introduction doit faire trois choses à la fois : installer un '
         'enjeu, analyser les mots du sujet, et faire naître de cette '
         'analyse une question à laquelle le plan répond. Les quatre '
         'paragraphes ci-dessous suivent cet ordre.',
 paras=[
  para(role='Accroche', isole=True, txt=
    'En 1996, dans [[u:La mondialisation n’est pas coupable]], Paul Krugman '
    'soutenait que la désindustrialisation des économies avancées tenait '
    'd’abord au progrès technique et à l’évolution de la demande, et non à la '
    'concurrence des pays à bas salaires. Vingt-trois ans plus tard, dans un '
    'article de 2019 demandant « qu’ont raté les économistes sur la '
    'mondialisation ? », le même auteur reconnaît que la profession a '
    'sous-estimé les effets de l’ouverture sur l’emploi, sur les inégalités '
    'et sur certains territoires industriels. Qu’un des principaux '
    'théoriciens du commerce international révise ainsi son propre jugement '
    'indique que la défense du libre-échange n’a rien d’évident : elle dépend '
    'de ce que l’on mesure, et de qui l’on regarde.',
    notes=[
      note('i2', 'Qu’un des principaux théoriciens du commerce international '
                 'révise ainsi son propre jugement indique que la défense du '
                 'libre-échange n’a rien d’évident',
           'Voilà l’enjeu : l’accroche ne se contente pas de raconter une '
           'anecdote, elle en tire le problème du devoir. Si un économiste '
           'qui a bâti sa réputation sur la théorie du commerce révise son '
           'jugement, c’est que la recommandation libre-échangiste n’est pas '
           'une évidence scientifique mais une conclusion sous conditions. '
           'La dernière proposition — « de ce que l’on mesure, et de qui l’on '
           'regarde » — annonce déjà les deux limites développées en II.'),
      note('i2', 'En 1996, dans [[u:La mondialisation n’est pas coupable]], '
                 'Paul Krugman',
           'L’accroche est datée et exacte : elle s’appuie sur une position '
           'réellement tenue par Krugman, et non sur une citation vague. '
           'Deux dates — 1996 et 2019 — suffisent à construire le '
           'retournement. C’est ce qui permet au critère « sans erreurs » '
           'd’être rempli : rien ici n’est inventé ni approximatif.'),
    ]),

  para(role='Analyse des termes', txt=
    'Le libre-échange désigne un régime d’échanges internationaux affranchi '
    'des obstacles tarifaires et non tarifaires, dans lequel la '
    'spécialisation s’opère selon les avantages comparatifs ; il ne se '
    'confond ni avec l’absence de règles, puisqu’il s’organise depuis 1947 '
    'dans le cadre du GATT puis, après les accords de Marrakech de 1995, dans '
    'celui de l’Organisation mondiale du commerce, ni avec la mondialisation, '
    'qui englobe aussi les mouvements de capitaux et de personnes. Défendre '
    'n’est pas constater : le verbe fait basculer le sujet du registre '
    'positif, qui explique les déterminants des échanges, vers le registre '
    'normatif, qui évalue les gagnants, les perdants et la légitimité '
    'éventuelle du protectionnisme. Reste toujours, qui porte la véritable '
    'difficulté du sujet : l’adverbe interroge l’universalité de la '
    'recommandation, dans le temps — un pays doit-il s’ouvrir à tous les '
    'stades de son développement ? — comme dans l’espace — la prescription '
    'vaut-elle pour tous les pays, tous les secteurs et tous les groupes '
    'sociaux ? Défendre le libre-échange toujours reviendrait à tenir ses '
    'gains pour inconditionnels ; or la théorie économique énonce elle-même '
    'les conditions auxquelles ces gains se réalisent.',
    notes=[
      note('i3', 'Le libre-échange désigne un régime d’échanges '
                 'internationaux affranchi des obstacles tarifaires et non '
                 'tarifaires',
           'Premier terme défini. La définition est précise — « tarifaires et '
           'non tarifaires » — et surtout délimitée par deux bornes : ce que '
           'le libre-échange n’est pas. Le distinguer de l’absence de règles '
           'évite le contresens « libre-échange = loi de la jungle » ; le '
           'distinguer de la mondialisation évite un hors-sujet sur les '
           'capitaux et les migrations.'),
      note('i3', 'Défendre n’est pas constater : le verbe fait basculer le '
                 'sujet du registre positif, qui explique les déterminants '
                 'des échanges, vers le registre normatif',
           'Deuxième terme analysé. Beaucoup de copies sautent le verbe. Or '
           '« défendre » impose de prendre parti : le devoir ne décrira pas '
           'le commerce international, il jugera une recommandation. '
           'L’opposition positif / normatif, prise au chapitre sur l’analyse '
           'du commerce international, donne à cette remarque un fondement '
           'théorique au lieu d’une simple glose de vocabulaire.'),
      note('i3', 'Reste toujours, qui porte la véritable difficulté du sujet',
           'Troisième terme, et le plus important : l’adverbe est le mot qui '
           'fait le sujet. Le dire explicitement — « la véritable difficulté » '
           '— montre au correcteur que la hiérarchie entre les termes a été '
           'vue. L’analyse se déploie ensuite sur deux dimensions, le temps '
           'et l’espace, qui structureront la copie.'),
      note('i4', 'Défendre le libre-échange toujours reviendrait à tenir ses '
                 'gains pour inconditionnels ; or la théorie économique '
                 'énonce elle-même les conditions auxquelles ces gains se '
                 'réalisent.',
           'C’est la phrase qui transforme l’analyse en piste de réponse. '
           'Elle contient, sous forme ramassée, toute la démonstration à '
           'venir : I établira les gains, II exposera les conditions que la '
           'théorie elle-même énonce, III en tirera les conséquences. Le '
           '« or » marque le basculement. Sans cette phrase, l’analyse des '
           'termes resterait un exercice de vocabulaire.'),
    ]),

  para(role='Cadrage et problématique', txt=
    'Nous retiendrons le champ des échanges de biens et de services, en '
    'laissant de côté la mobilité des capitaux et du travail, parce que c’est '
    'sur les marchandises que porte la recommandation libre-échangiste '
    'classique et que c’est là que se concentrent les instruments de '
    'protection. La période retenue court de la construction du '
    'multilatéralisme commercial après 1947 au retour contemporain des droits '
    'de douane : c’est l’intervalle pendant lequel la prescription a été à la '
    'fois la plus consensuelle et la plus contestée, ce qui en fait le '
    'terrain d’épreuve du « toujours ». Dès lors, si la théorie démontre que '
    'l’ouverture accroît la richesse disponible, à quelles conditions et pour '
    'qui ce gain se réalise-t-il, et ces conditions permettent-elles encore '
    'de défendre le libre-échange sans réserve ?',
    notes=[
      note('i5', 'en laissant de côté la mobilité des capitaux et du travail, '
                 'parce que c’est sur les marchandises que porte la '
                 'recommandation libre-échangiste classique',
           'Le cadrage est établi — champ des biens et services — et surtout '
           'justifié : le « parce que » n’est pas décoratif. Un cadrage non '
           'justifié ressemble à une dérobade ; justifié, il prouve que '
           'l’exclusion est raisonnée et protège contre l’accusation de '
           'traitement partiel.'),
      note('i5', 'c’est l’intervalle pendant lequel la prescription a été à la '
                 'fois la plus consensuelle et la plus contestée, ce qui en '
                 'fait le terrain d’épreuve du « toujours »',
           'Deuxième volet du cadrage : la période. La justification est '
           'rattachée au mot clé du sujet — on choisit cette période parce '
           'qu’elle met « toujours » à l’épreuve. Un cadrage temporel justifié '
           'par le sujet lui-même, et non par commodité, vaut toujours mieux.'),
      note('i6', 'si la théorie démontre que l’ouverture accroît la richesse '
                 'disponible, à quelles conditions et pour qui ce gain se '
                 'réalise-t-il, et ces conditions permettent-elles encore de '
                 'défendre le libre-échange sans réserve ?',
           'La problématique découle directement de l’analyse des termes : '
           '« conditions » vient du paragraphe précédent, « pour qui » vient '
           'de l’accroche, « sans réserve » traduit « toujours ». Elle est '
           'formulée en une seule question, articulée en deux temps par la '
           'subordonnée introductive, et elle respecte le sens du sujet '
           'puisqu’elle porte sur la défense du libre-échange et non sur ses '
           'causes.'),
    ]),

  para(role='Annonce du plan', isole=True, txt=
    'La démonstration du gain à l’échange constitue le socle le plus solide '
    'de l’analyse économique et fonde une présomption favorable au '
    'libre-échange (I). Mais elle repose sur des hypothèses dont l’explicitation '
    'fait apparaître des perdants durables et des situations où la protection '
    'devient rationnelle (II). La question se déplace alors : il ne s’agit '
    'plus de choisir entre ouverture et fermeture, mais de déterminer le '
    'régime d’échange et les compensations qui rendent l’ouverture '
    'soutenable (III).',
    notes=[
      note('i7', 'fonde une présomption favorable au libre-échange (I). Mais '
                 'elle repose sur des hypothèses dont l’explicitation fait '
                 'apparaître des perdants durables',
           'L’annonce indique bien I, II et III, et elle n’est pas simpliste : '
           'on ne lit ni « d’abord les avantages » ni « ensuite les '
           'inconvénients ». Le mot « présomption » en I prépare déjà le '
           'renversement de II, et le « mais » articule les deux parties au '
           'lieu de les juxtaposer.'),
      note('i7', 'il ne s’agit plus de choisir entre ouverture et fermeture, '
                 'mais de déterminer le régime d’échange et les compensations '
                 'qui rendent l’ouverture soutenable (III)',
           'La troisième partie n’est pas contradictoire avec les deux '
           'premières : elle ne dit pas « finalement le libre-échange est '
           'bon » après avoir dit l’inverse. Elle change la question, ce qui '
           'est la seule façon correcte de dépasser une alternative. C’est '
           'aussi la réponse directe au mot « toujours » : ni toujours, ni '
           'jamais, mais sous quel régime.'),
      note('i1', 'La démonstration du gain à l’échange constitue le socle le '
                 'plus solide de l’analyse économique',
           'Ce paragraphe est isolé : il commence après un retour à la ligne '
           'et ne contient que l’annonce. Avec l’accroche également isolée, '
           'l’introduction compte quatre paragraphes nettement séparés — le '
           'correcteur repère l’architecture avant même de lire.'),
    ]),
 ],
 globaux=[
   glob('i1', 'Quatre paragraphes, dans l’ordre : accroche, analyse des '
              'termes, cadrage et problématique, annonce du plan. L’accroche '
              'et l’annonce sont seules sur leur paragraphe ; les deux '
              'paragraphes centraux peuvent être fondus en un seul si la '
              'copie est courte, mais jamais l’accroche avec la définition. '
              'Sur la copie, vérifiez simplement qu’on distingue quatre blocs '
              'à l’œil nu, sans lire.'),
 ],
)

# =================================================================== plan

PLAN = {
 'sujet': SUJET,
 'pb': 'Si la théorie démontre que l’ouverture accroît la richesse '
       'disponible, à quelles conditions et pour qui ce gain se réalise-t-il, '
       'et ces conditions permettent-elles encore de défendre le '
       'libre-échange sans réserve ?',
 'chapeau': 'Trois parties de trois sous-parties, soit neuf paragraphes '
            'd’argumentation environ. L’équilibre visé est d’une page et '
            'demie à deux pages par grande partie.',
 'parties': [
  {'num': 'I', 'titre': 'Le gain à l’échange fonde une présomption favorable '
                        'au libre-échange',
   'pourquoi': 'Le titre répond au sujet par un verbe : « fonde une '
               'présomption ». Il ne dit pas « les avantages du '
               'libre-échange » — un intitulé de cours — mais énonce une '
               'thèse que la partie devra établir. Le mot « présomption » '
               'annonce qu’elle sera réfutable.',
   'sp': [
     ('A', 'La spécialisation selon les avantages comparatifs accroît la '
           'richesse disponible à facteurs constants',
      'Ricardo (1817), le drap et le vin, les coûts d’opportunité ; gain en '
      'production mondiale ou en économie de facteurs.'),
     ('B', 'Les rendements croissants étendent le gain aux échanges entre '
           'économies semblables',
      'Krugman, commerce intra-branche, variété et économies d’échelle ; la '
      'courbe du sourire comme contre-épreuve en II.'),
     ('C', 'L’histoire institutionnelle associe ouverture négociée et '
           'expansion des échanges',
      'Du GATT de 1947 à l’OMC de 1995 ; baisse continue des droits de '
      'douane industriels, aujourd’hui 3 % en moyenne mondiale.'),
   ]},
  {'num': 'II', 'titre': 'Mais les conditions du gain, une fois explicitées, '
                         'font apparaître des perdants et des exceptions '
                         'légitimes',
   'pourquoi': 'Le « mais » enchaîne sur I sans le détruire : on ne nie pas '
               'le gain, on en explicite les conditions. « Exceptions '
               'légitimes » répond frontalement au « toujours » du sujet.',
   'sp': [
     ('A', 'Le gain démontré est un gain agrégé : la théorie prévoit '
           'elle-même une redistribution entre facteurs',
      'HOS et Stolper-Samuelson (1941) ; Krugman 2019 ; courbe du sourire de '
      'Stan Shih et son creusement chez Baldwin. — Sous-partie rédigée '
      'ci-dessous.'),
     ('B', 'L’ajustement n’est ni instantané ni indolore : le choc '
           'd’importation se concentre sur des territoires',
      'Autor, Acemoglu, Malgouyres sur le choc chinois ; classes moyennes '
      'occidentales au 80ᵉ percentile chez Milanovic.'),
     ('C', 'Les rendements croissants rendent rationnelle une protection '
           'temporaire',
      'List (1841) et le protectionnisme éducateur ; réhabilitation par '
      'Krugman à partir des économies d’échelle.'),
   ]},
  {'num': 'III', 'titre': 'La question n’est donc plus l’ouverture mais le '
                          'régime d’échange et son accompagnement',
   'pourquoi': 'Le titre ne tranche pas « oui » ou « non » : il déplace '
               'l’objet. C’est ce déplacement qui permet de répondre à '
               '« toujours » sans tomber dans le relativisme.',
   'sp': [
     ('A', 'Le libre-échange régional ne vaut que si la création de trafic '
           'l’emporte sur le détournement',
      'Viner ; création contre détournement de trafic ; l’exemple de l’ASEAN, '
      'passée d’environ 4 % des exportations mondiales de biens en 1990 à '
      'environ 8 % en 2021.'),
     ('B', 'L’ouverture n’est soutenable que si elle est compensée et '
           'politiquement choisie',
      'Trilemme de Rodrik ; compensation des perdants ; protection sociale et '
      'politique industrielle.'),
     ('C', 'Devenu instrument de puissance, le commerce déplace le critère de '
           'l’efficacité vers la sécurité',
      'Luttwak (1990) et la géoéconomie ; Baldwin : l’interdépendance passe '
      'du statut d’opportunité à celui de vulnérabilité.'),
   ]},
 ],
 'notes': [
   {'k': 'i8', 'x': 'Les trois titres contiennent les termes du sujet ou leur '
                    'traduction : « libre-échange » en I, « exceptions » — '
                    'c’est-à-dire la négation de « toujours » — en II, '
                    '« régime d’échange » en III. Aucun ne pourrait coiffer '
                    'un chapitre de cours : chacun énonce une thèse '
                    'discutable, ce qui est la marque d’un titre de partie.'},
   {'k': 's2', 'x': 'Les neuf titres de sous-parties sont tous des phrases '
                    'affirmatives qui répondent à la problématique. Comparez '
                    'II.A — « Le gain démontré est un gain agrégé » — à ce '
                    'qu’on lit souvent : « Le théorème HOS ». Le premier est '
                    'un argument, le second un objet de cours. Un correcteur '
                    'qui ne lit que les titres doit comprendre la '
                    'démonstration.'},
   {'k': 'd1', 'x': 'Ce que le plan permet d’anticiper : trois parties de '
                    'trois sous-parties, donc neuf paragraphes '
                    'd’argumentation de volume comparable, soit un équilibre '
                    'prévu d’environ une page et demie à deux pages par '
                    'partie. Ce que le plan ne garantit pas, et qu’il faut '
                    'vérifier sur la copie complète : le nombre de lignes '
                    'réellement écrites. Le déséquilibre classique est une '
                    'partie III expédiée en une demi-page faute de temps. '
                    'Comptez les lignes de chaque partie à la relecture : si '
                    'l’écart dépasse un tiers, le plan n’a pas été tenu, même '
                    's’il était bon.'},
 ],
}

# ================================================= annonce des sous-parties

ANNONCE = piece(
 id='annonce',
 t='Annonce des sous-parties (ouverture de la partie II)',
 st='Un paragraphe distinct, placé juste après le titre de la grande partie, '
    'qui annonce A, B et C et la logique qui les relie.',
 meta='1 paragraphe · environ 8 lignes manuscrites',
 chapeau='Ce paragraphe n’est pas une table des matières : il doit faire '
         'comprendre pourquoi les sous-parties se suivent dans cet ordre, et '
         'donc pourquoi la démonstration progresse.',
 paras=[
  para(role='Titre de la partie', txt=
    'II. Mais les conditions du gain, une fois explicitées, font apparaître '
    'des perdants et des exceptions légitimes'),
  para(role='Annonce des sous-parties', txt=
    'L’examen des conditions du gain suit l’ordre dans lequel la théorie '
    'elle-même les relâche. Nous montrerons d’abord que le gain démontré en '
    'première partie est un gain agrégé, et que le modèle standard prévoit '
    'lui-même qu’il se paie d’une redistribution entre les facteurs de '
    'production (A). Nous verrons ensuite que cette redistribution, longtemps '
    'pensée comme un ajustement rapide, prend en réalité la forme de chocs '
    'durables et géographiquement concentrés (B). Nous établirons enfin que '
    'les rendements croissants, loin de constituer une curiosité théorique, '
    'peuvent rendre rationnelle une protection temporaire au nom du '
    'rattrapage (C). On passe ainsi d’une limite interne à la théorie à une '
    'limite empirique, puis à une justification positive de la protection : '
    'la contestation du libre-échange se déplace de ses effets vers ses '
    'fondements, ce qui atteint directement le « toujours » du sujet.',
    notes=[
      note('s1', 'Nous montrerons d’abord que le gain démontré en première '
                 'partie est un gain agrégé',
           'Le paragraphe est distinct : il suit le titre de la partie et '
           'précède le titre de A. Il annonce les trois sous-parties dans '
           'l’ordre, avec les repères (A), (B), (C) qui permettent au '
           'correcteur de suivre. Noter le rappel « démontré en première '
           'partie » : l’annonce raccroche la partie II à la partie I au '
           'lieu de repartir de zéro.'),
      note('s1', 'On passe ainsi d’une limite interne à la théorie à une '
                 'limite empirique, puis à une justification positive de la '
                 'protection',
           'Voilà la logique d’organisation, et c’est ce que le critère '
           'exige : non pas la liste des sous-parties, mais la raison de '
           'leur ordre. La progression va du plus faible au plus fort — une '
           'limite que la théorie reconnaît, puis un démenti des faits, puis '
           'un argument qui fonde positivement la protection. Chaque '
           'sous-partie est donc plus offensive que la précédente.'),
      note('s1', 'ce qui atteint directement le « toujours » du sujet',
           'La dernière proposition rattache l’ensemble au sujet. Une annonce '
           'de sous-parties qui ne nomme jamais le sujet laisse penser que la '
           'partie fonctionne pour elle-même. Ici, on rappelle ce que la '
           'partie II vient faire dans la démonstration d’ensemble.'),
    ]),
 ],
 globaux=[],
)

# ====================================================== sous-partie rédigée

SP = piece(
 id='souspartie',
 t='Sous-partie II.A rédigée',
 st='Trois arguments, trois paragraphes : la théorie prévoit la '
    'redistribution ; les économistes l’ont sous-estimée ; le gain lui-même '
    'est inégalement capté.',
 meta='3 paragraphes + un graphique · environ une page manuscrite',
 chapeau='Chaque paragraphe suit le même ordre : une affirmation qui répond '
         'au sujet, l’auteur qui l’étaye, le mécanisme déroulé, puis le fait '
         'ou le chiffre qui démontre. Lisez d’abord les trois premières '
         'phrases seules : elles doivent suffire à comprendre la '
         'démonstration.',
 paras=[
  para(role='Titre de la sous-partie', txt=
    'A. Le gain démontré est un gain agrégé : la théorie prévoit elle-même '
    'une redistribution entre facteurs'),

  para(role='Argument 1', txt=
    'Défendre le libre-échange toujours supposerait que le gain à l’échange '
    'profite à tous, alors que la théorie standard n’établit qu’un gain '
    'global. Le modèle HOS, construit par Eli Heckscher et Bertil Ohlin puis '
    'formalisé par Paul Samuelson, explique en effet la spécialisation par '
    'les dotations relatives en facteurs : chaque pays exporte le bien qui '
    'utilise intensément le facteur dont il est le mieux doté. Le mécanisme '
    'est alors transparent. L’ouverture accroît la demande mondiale adressée '
    'au facteur abondant, dont la rémunération s’élève ; elle réduit la '
    'demande adressée au facteur rare, dont la rémunération baisse ; le '
    'commerce de biens revient donc à un échange indirect de facteurs de '
    'production. C’est exactement ce qu’établissent Wolfgang Stolper et Paul '
    'Samuelson dans « Protection and Real Wages », publié en 1941 alors que '
    'le débat américain portait sur les effets des droits de douane : la '
    'protection élève la rémunération réelle du facteur rare, et '
    'symétriquement l’ouverture la diminue. Le résultat est décisif pour '
    'notre sujet, car il ne s’agit pas d’un effet secondaire mais d’une '
    'conséquence nécessaire du modèle : dans une économie avancée '
    'relativement abondante en travail qualifié, l’ouverture aux échanges '
    'avec des pays abondants en travail peu qualifié élève mécaniquement le '
    'rendement des qualifications et comprime les salaires les moins '
    'qualifiés. La stagnation des classes moyennes occidentales que Branko '
    'Milanovic situe autour du quatre-vingtième percentile mondial dans '
    '[[u:Global Inequality]] (2016), avec une croissance réelle proche de '
    'zéro entre 1988 et 2008, en donne la traduction mesurable.',
    notes=[
      note('d3', 'Défendre le libre-échange toujours supposerait que le gain '
                 'à l’échange profite à tous',
           'Le paragraphe débute par un argument, pas par un auteur ni par '
           'une définition. On y retrouve littéralement les mots du sujet — '
           '« défendre », « toujours », « libre-échange » — ce qui permet au '
           'correcteur de vérifier d’un coup d’œil que le paragraphe répond '
           'bien à la question posée.'),
      note('d4', 'Le modèle HOS, construit par Eli Heckscher et Bertil Ohlin '
                 'puis formalisé par Paul Samuelson',
           'L’auteur intervient en deuxième position, pour étayer. '
           'Comparez avec l’ordre inverse, fréquent et fautif : « Selon le '
           'modèle HOS, les pays se spécialisent… » — là, c’est le cours qui '
           'parle et l’argument disparaît. Ici, l’affirmation est posée, puis '
           'le modèle vient la soutenir : le « en effet » marque ce rapport '
           'de subordination.'),
      note('d5', 'L’ouverture accroît la demande mondiale adressée au facteur '
                 'abondant, dont la rémunération s’élève ; elle réduit la '
                 'demande adressée au facteur rare, dont la rémunération '
                 'baisse ; le commerce de biens revient donc à un échange '
                 'indirect de facteurs de production.',
           'Voilà le mécanisme déroulé. Trois propositions reliées par des '
           'points-virgules, chacune étant une étape causale : hausse de la '
           'demande au facteur abondant, baisse pour le facteur rare, '
           'interprétation du commerce comme échange de facteurs. Nommer '
           '« Stolper-Samuelson » sans écrire ces trois étapes ne vaudrait '
           'presque rien : c’est la chaîne causale, pas l’étiquette, qui '
           'prouve la compréhension.'),
      note('d6', 'publié en 1941 alors que le débat américain portait sur les '
                 'effets des droits de douane',
           'La référence est datée — 1941 — et contextualisée : on dit à quoi '
           'les auteurs répondaient. Dater sans contextualiser donne une '
           'impression de fiche apprise ; contextualiser montre qu’on sait '
           'pourquoi la question se posait à ce moment-là. Deux membres de '
           'phrase suffisent.'),
      note('d7', '« Protection and Real Wages »',
           'C’est un article : il va entre guillemets. À côté, '
           '[[u:Global Inequality]] est un ouvrage : il se souligne à la '
           'règle sur la copie manuscrite. Respecter cette distinction coûte '
           'une seconde et signale au correcteur que les références sont '
           'maîtrisées et non récitées.'),
      note('d8', 'avec une croissance réelle proche de zéro entre 1988 et 2008',
           'Le paragraphe revient aux faits, et le chiffre démontre quelque '
           'chose de précis : il ne sert pas d’ornement. Le mécanisme '
           'théorique prédit que le facteur relativement rare dans les pays '
           'avancés — le travail peu qualifié — voit sa rémunération '
           'comprimée ; la croissance quasi nulle des classes moyennes '
           'occidentales sur vingt ans est précisément ce que l’on devrait '
           'observer si le mécanisme opère. Le fait vérifie la théorie, il ne '
           'l’illustre pas.'),
    ]),

  para(role='Argument 2', txt=
    'Cette redistribution n’est pas un accident du modèle mais sa conséquence '
    'nécessaire, ce qui interdit de défendre l’ouverture au nom du seul gain '
    'moyen. Paul Krugman l’a lui-même reconnu dans son article de 2019 sur ce '
    'que les économistes ont raté de la mondialisation, écrit dans un contexte '
    'de montée du protectionnisme et de contestation des accords commerciaux : '
    'la profession a raisonné en termes d’effets agrégés de long terme et a '
    'de ce fait sous-estimé des effets très concentrés sur l’emploi, sur les '
    'inégalités et sur certains territoires. Le mécanisme de cette erreur est '
    'instructif. Un gain net positif pour une économie prise comme un tout '
    'reste parfaitement compatible avec des pertes lourdes pour des groupes '
    'identifiables, dès lors que rien ne garantit que les gagnants indemnisent '
    'les perdants ; et l’asymétrie est accentuée par la répartition des '
    'effets, puisque les gains sont diffus — quelques points de pouvoir '
    'd’achat répartis sur l’ensemble des consommateurs — tandis que les pertes '
    'sont concentrées sur un bassin d’emploi ou une filière. La profondeur de '
    'cette réorganisation se mesure d’ailleurs dans la structure même des '
    'échanges : la part de valeur ajoutée domestique contenue dans les '
    'exportations des principales économies européennes est passée d’environ '
    '85 à 90 % dans les années 1960 à près de 70 % aujourd’hui, signe que '
    'l’ouverture a déplacé la production bien plus profondément que ne le '
    'laissait supposer un raisonnement en gains moyens.',
    notes=[
      note('d3', 'Cette redistribution n’est pas un accident du modèle mais sa '
                 'conséquence nécessaire, ce qui interdit de défendre '
                 'l’ouverture au nom du seul gain moyen.',
           'Deuxième argument, nettement distinct du premier : le premier '
           'établissait que la théorie prévoit une redistribution, celui-ci '
           'établit qu’on ne peut pas l’écarter comme un détail. Le '
           'paragraphe s’ouvre encore sur une affirmation contenant un terme '
           'du sujet — « défendre » — et le mot « interdit » marque qu’on '
           'argumente, qu’on ne décrit pas.'),
      note('d4', 'Paul Krugman l’a lui-même reconnu dans son article de 2019',
           'L’auteur vient après l’affirmation, pour l’étayer. L’effet est '
           'ici renforcé par le choix de la référence : c’est l’un des '
           'principaux défenseurs du libre-échange qui concède le point. '
           'Mobiliser un auteur contre son camp supposé est l’un des usages '
           'les plus efficaces d’une référence.'),
      note('d5', 'Un gain net positif pour une économie prise comme un tout '
                 'reste parfaitement compatible avec des pertes lourdes pour '
                 'des groupes identifiables, dès lors que rien ne garantit '
                 'que les gagnants indemnisent les perdants',
           'Le mécanisme est expliqué et non asséné : on montre pourquoi un '
           'solde positif peut coexister avec des pertes, et à quelle '
           'condition — l’absence de compensation. Cette condition reparaîtra '
           'en III.B, ce qui donne à la copie sa continuité.'),
      note('d6', 'écrit dans un contexte de montée du protectionnisme et de '
                 'contestation des accords commerciaux',
           'Contextualisation de la référence de 2019. Le lecteur comprend '
           'que le revirement de Krugman n’est pas une lubie mais une '
           'réponse à une situation : il écrit après le tournant '
           'protectionniste américain. Date plus contexte, en une seule '
           'incise.'),
      note('d8', 'est passée d’environ 85 à 90 % dans les années 1960 à près '
                 'de 70 % aujourd’hui',
           'Le chiffre démontre que la réorganisation productive est massive, '
           'ce qui soutient directement l’argument : si l’ouverture n’avait '
           'déplacé la production qu’à la marge, le raisonnement en gains '
           'moyens serait acceptable. Noter la prudence — « environ », '
           '« près de » — qui est préférable à une précision fausse.'),
    ]),

  para(role='Argument 3', txt=
    'Le gain lui-même n’est enfin pas également capté le long des chaînes de '
    'valeur, ce qui achève de disqualifier une défense inconditionnelle du '
    'libre-échange. Stan Shih a formalisé cette inégalité par la courbe du '
    'sourire : la valeur ajoutée est élevée en amont, dans la recherche et la '
    'conception, et en aval, dans le marketing et les services, mais faible au '
    'centre, au moment de l’assemblage. Le mécanisme tient aux qualifications '
    'et au critère d’implantation qui en découle. Les extrémités de la chaîne '
    'exigent des compétences rares et se localisent donc dans les économies '
    'avancées ou sur les grands marchés, tandis que l’assemblage, activité '
    'routinière, se décide d’abord sur le coût salarial unitaire ; un pays qui '
    's’ouvre en se spécialisant dans l’assemblage participe donc pleinement au '
    'commerce mondial tout en restant cantonné à l’étape qui le rémunère le '
    'moins. Richard Baldwin montre en comparant les années 1970 aux années '
    '2000 que ce sourire s’est creusé, la valeur captée aux extrémités '
    'augmentant tandis que celle de l’assemblage diminuait. La trajectoire de '
    'l’ASEAN le confirme sans l’infirmer : sa part dans les exportations '
    'mondiales de biens est passée d’environ 4 % en 1990 à environ 8 % en '
    '2021, mais cette progression tient largement à son insertion dans les '
    'chaînes de valeur asiatiques organisées autour de la Chine, c’est-à-dire '
    'à une position dans la chaîne autant qu’à un volume d’échanges.',
    notes=[
      note('d3', 'Le gain lui-même n’est enfin pas également capté le long des '
                 'chaînes de valeur, ce qui achève de disqualifier une '
                 'défense inconditionnelle du libre-échange.',
           'Troisième argument, encore distinct : après « la théorie prévoit '
           'la redistribution » et « les économistes l’ont sous-estimée », '
           'voici « le gain lui-même est inégalement capté ». « Enfin » '
           'signale la clôture de la sous-partie, et « défense '
           'inconditionnelle » reprend le « toujours » du sujet.'),
      note('d5', 'Les extrémités de la chaîne exigent des compétences rares et '
                 'se localisent donc dans les économies avancées ou sur les '
                 'grands marchés, tandis que l’assemblage, activité '
                 'routinière, se décide d’abord sur le coût salarial '
                 'unitaire',
           'Le mécanisme explique la forme de la courbe au lieu de la '
           'décrire : si l’on ne dit pas pourquoi la valeur est faible au '
           'centre — faible qualification, donc arbitrage sur le coût — la '
           'courbe du sourire n’est qu’une image. La conséquence est ensuite '
           'tirée explicitement pour le sujet.'),
      note('d6', 'Richard Baldwin montre en comparant les années 1970 aux '
                 'années 2000 que ce sourire s’est creusé',
           'La référence est datée par la comparaison elle-même : c’est le '
           'rapprochement de deux périodes qui fait le résultat. Préciser '
           '« en comparant les années 1970 aux années 2000 » vaut mieux '
           'qu’une date isolée, car cela dit aussi comment le résultat a été '
           'obtenu.'),
      note('d8', 'sa part dans les exportations mondiales de biens est passée '
                 'd’environ 4 % en 1990 à environ 8 % en 2021',
           'Le fait est utilisé avec nuance — « le confirme sans l’infirmer » '
           '— et c’est ce qui lui donne sa valeur démonstrative. Un doublement '
           'de la part dans les exportations mondiales pourrait passer pour '
           'un démenti ; on montre qu’il est compatible avec l’argument '
           'puisque ce qui compte est la position dans la chaîne, non le '
           'volume. Savoir retourner un fait apparemment contraire est ce qui '
           'distingue une copie qui raisonne d’une copie qui récite.'),
      note('d2', 'Stan Shih a formalisé cette inégalité par la courbe du '
                 'sourire',
           'Trois paragraphes, trois arguments autonomes : la sous-partie est '
           'consistante. Chacun pourrait être supprimé sans détruire les deux '
           'autres, mais l’ensemble est plus fort que ses parties, car on '
           'passe de la théorie aux faits puis à la structure des échanges.'),
    ]),

  para(role='Graphique', txt=
    '[Graphique dans la copie] En abscisse : les étapes successives de la '
    'chaîne de valeur, de la recherche et développement à l’assemblage puis '
    'aux services après-vente. En ordonnée : la valeur ajoutée créée à chaque '
    'étape. Deux courbes : en trait plein, les années 1970 ; en pointillé, '
    'les années 2000. Lecture : les deux courbes ont la forme d’un sourire, '
    'mais celle des années 2000 est nettement plus creusée — la valeur '
    'ajoutée a augmenté en amont comme en aval, et diminué au centre. Le '
    'graphique montre donc que l’approfondissement de la division '
    'internationale du processus productif a accentué l’écart entre les '
    'étapes, et non qu’il l’a créé.',
    notes=[
      note('d9', 'En abscisse : les étapes successives de la chaîne de valeur, '
                 'de la recherche et développement à l’assemblage puis aux '
                 'services après-vente. En ordonnée : la valeur ajoutée créée '
                 'à chaque étape.',
           'Les deux axes sont nommés et les variables explicitées. C’est le '
           'minimum : un graphique dont on ne sait pas ce qu’il porte ne vaut '
           'rien, même bien tracé. Écrivez les axes avant de tracer la '
           'courbe, pas après.'),
      note('d9', 'en trait plein, les années 1970 ; en pointillé, les années '
                 '2000',
           'La légende est nécessaire ici parce qu’il y a deux courbes. Sur '
           'une copie manuscrite, distinguez-les par le trait — plein contre '
           'pointillé — et non par la couleur, qui peut disparaître à la '
           'photocopie et que le correcteur ne lira pas toujours.'),
      note('d9', 'Le graphique montre donc que l’approfondissement de la '
                 'division internationale du processus productif a accentué '
                 'l’écart entre les étapes, et non qu’il l’a créé.',
           'Voilà la lecture commentée, et c’est elle qui rapporte des '
           'points : on ne décrit pas le tracé, on dit ce qu’il établit — et '
           'ici aussi ce qu’il n’établit pas. Un graphique suivi de la seule '
           'phrase « on observe une courbe en forme de sourire » est un '
           'graphique perdu.'),
    ]),
 ],
 globaux=[
   glob('d2', 'Ce que la sous-partie montre : trois arguments distincts, un '
              'par paragraphe, chacun tenant seul. Ce qu’il faut vérifier sur '
              'la copie complète : qu’aucune des neuf sous-parties ne tombe à '
              'un seul paragraphe. Le symptôme habituel est une sous-partie '
              'C expédiée en quatre lignes parce que le temps manque — mieux '
              'vaut alors prévoir deux sous-parties solides que trois '
              'bancales.'),
   glob('f1', 'Ce critère ne se juge que sur la copie entière. Trois réflexes '
              'rapportent plus que la relecture générale : vérifier les '
              'accords sujet-verbe des phrases longues, relire les noms '
              'propres et les titres — Stolper, Samuelson, Heckscher, Ohlin, '
              'Milanovic s’écorchent vite — et contrôler que chaque '
              'paragraphe est visiblement détaché, avec un alinéa. Gardez dix '
              'minutes pour cela : c’est le seul critère de la grille qui se '
              'gagne entièrement après la rédaction.'),
 ],
)

# ================================================================ transition

TRANS = piece(
 id='transition',
 t='Transition entre la partie I et la partie II',
 st='Un paragraphe isolé qui dit ce que I a établi, quelle question reste '
    'ouverte, et pourquoi cela justifie II.',
 meta='1 paragraphe isolé · environ 7 lignes manuscrites',
 chapeau='La transition se place après la dernière sous-partie de I et avant '
         'le titre de II, séparée des deux par un saut de ligne. Elle n’est '
         'ni un résumé ni une annonce : elle fait avancer le raisonnement.',
 paras=[
  para(role='Fin de la partie I', txt=
    '… c’est donc bien l’ouverture négociée, et non l’ouverture subie, que '
    'l’histoire institutionnelle associe à l’expansion des échanges.'),
  para(role='Transition', isole=True, txt=
    'Le gain à l’échange n’est donc pas une croyance : il est démontré par la '
    'théorie, prolongé par l’analyse des rendements croissants et confirmé '
    'par l’histoire du multilatéralisme commercial. Mais cette démonstration '
    'établit un gain pour l’économie prise comme un tout, à facteurs '
    'constants, et une fois l’ajustement achevé. Or ces trois précisions sont '
    'autant d’hypothèses : elles supposent que le gain agrégé se diffuse, que '
    'les facteurs se réallouent effectivement, et que le temps de '
    'l’ajustement est court. Reste donc à savoir ce que devient la '
    'recommandation libre-échangiste lorsque ces hypothèses sont levées — '
    'autrement dit si le « toujours » du sujet résiste à l’examen des '
    'conditions mêmes du gain.',
    notes=[
      note('t2', 'Le gain à l’échange n’est donc pas une croyance : il est '
                 'démontré par la théorie, prolongé par l’analyse des '
                 'rendements croissants et confirmé par l’histoire du '
                 'multilatéralisme commercial.',
           'Premier temps : ce que la partie I a établi. La phrase résume les '
           'trois sous-parties sans les réciter — on ne lit pas « dans un '
           'premier temps nous avons vu que… », mais le contenu lui-même, '
           'articulé. Le lecteur sait ce qui est acquis et ne le discutera '
           'plus.'),
      note('t2', 'Or ces trois précisions sont autant d’hypothèses : elles '
                 'supposent que le gain agrégé se diffuse, que les facteurs '
                 'se réallouent effectivement, et que le temps de '
                 'l’ajustement est court.',
           'Deuxième temps, et c’est là que la transition dépasse le bilan. '
           'On ne se contente pas de dire « mais il y a des limites » : on '
           'nomme les trois hypothèses implicites de la partie I, qui sont '
           'exactement ce que la partie II va lever, sous-partie par '
           'sous-partie. La transition crée ainsi la nécessité de la suite au '
           'lieu de l’annoncer.'),
      note('t2', 'autrement dit si le « toujours » du sujet résiste à l’examen '
                 'des conditions mêmes du gain',
           'Troisième temps : le retour à la problématique. La question '
           'relancée n’est pas une question nouvelle, c’est celle de '
           'l’introduction, reformulée à la lumière de ce que I vient '
           'd’établir. C’est à cette condition qu’une transition « fait le '
           'point sur le raisonnement » au lieu de servir de charnière '
           'décorative.'),
    ]),
  para(role='Début de la partie II', txt=
    'II. Mais les conditions du gain, une fois explicitées, font apparaître '
    'des perdants et des exceptions légitimes'),
 ],
 globaux=[
   glob('t1', 'Sur la copie, la transition doit se voir avant d’être lue : un '
              'saut de ligne au-dessus, un saut de ligne en dessous, et le '
              'titre de la partie suivante nettement détaché. Certains '
              'préfèrent un léger retrait du bloc entier, ce qui fonctionne '
              'aussi. Ce qu’il ne faut pas faire : coller la transition à la '
              'fin du dernier paragraphe de I, où elle devient invisible, ni '
              'la placer après le titre de II, où elle ne transite plus de '
              'rien. Vérifiez vos deux transitions — entre I et II, puis '
              'entre II et III — en regardant la copie de loin.'),
 ],
)

# ================================================================ conclusion

CONCL = piece(
 id='conclusion',
 t='Conclusion rédigée',
 st='Une réponse nuancée, puis le déplacement que le devoir a opéré, puis une '
    'ouverture qui change de critère.',
 meta='3 paragraphes · environ 18 lignes manuscrites',
 chapeau='La conclusion répond d’abord, et seulement ensuite ouvre. Le test : '
         'si elle pouvait être placée en introduction sans rien changer, elle '
         'n’apporte rien.',
 paras=[
  para(role='Réponse au sujet', txt=
    'Au terme de ce parcours, le libre-échange apparaît comme une '
    'recommandation qu’il faut défendre, mais jamais toujours. La théorie '
    'établit un gain à l’échange robuste, que l’histoire du multilatéralisme '
    'commercial confirme ; mais ce gain est agrégé, et la théorie énonce '
    'elle-même les conditions auxquelles il se réalise : mobilité des '
    'facteurs, brièveté de l’ajustement, compensation des perdants. Dès lors '
    'que ces conditions ne sont pas réunies — et la concentration '
    'territoriale du choc d’importation montre qu’elles ne le sont pas '
    'toujours —, la protection cesse d’être une erreur économique pour '
    'devenir, dans des cas précis et bornés, un instrument rationnel : '
    'protection temporaire d’une industrie naissante chez Friedrich List, '
    'correction d’une concurrence faussée, préservation d’une capacité jugée '
    'stratégique. La défense du libre-échange relève donc d’une présomption '
    'et non d’un principe : elle vaut par défaut, et se renverse lorsque ses '
    'conditions ne sont pas remplies.',
    notes=[
      note('c1', 'le libre-échange apparaît comme une recommandation qu’il '
                 'faut défendre, mais jamais toujours',
           'La réponse est donnée dès la première phrase, et elle tranche : '
           'ni « oui », ni « non », mais « oui sauf à certaines conditions ». '
           'Elle reprend les deux verbes du sujet — « défendre », '
           '« toujours » — ce qui prouve qu’on répond bien à la question '
           'posée et non à une question voisine.'),
      note('c1', 'La théorie établit un gain à l’échange robuste, que '
                 'l’histoire du multilatéralisme commercial confirme ; mais '
                 'ce gain est agrégé, et la théorie énonce elle-même les '
                 'conditions auxquelles il se réalise',
           'La progression du raisonnement est résumée sans que le plan soit '
           'récité : on ne lit ni « dans une première partie », ni « nous '
           'avons ensuite vu ». Les trois mouvements du devoir sont présents '
           '— le gain, ses conditions, le renversement — mais sous forme '
           'd’enchaînement logique. C’est la différence entre résumer un '
           'raisonnement et réciter un sommaire.'),
      note('c1', 'La défense du libre-échange relève donc d’une présomption et '
                 'non d’un principe : elle vaut par défaut, et se renverse '
                 'lorsque ses conditions ne sont pas remplies.',
           'Voilà ce que la conclusion apporte de plus que l’introduction. '
           'L’introduction annonçait une tension ; la conclusion livre un '
           'statut logique — présomption réfutable — que seule la '
           'démonstration permettait d’établir. Placez cette phrase en '
           'introduction : elle serait une affirmation gratuite. Ici, elle '
           'est un résultat.'),
    ]),

  para(role='Ce que le devoir a déplacé', txt=
    'Le raisonnement aura en outre déplacé la question elle-même. Posée en '
    'termes d’ouverture ou de fermeture, elle n’admet pas de réponse '
    'générale ; posée en termes de régime d’échange, elle en admet une : ce '
    'qui est en cause n’est pas le degré d’ouverture mais les règles qui '
    'l’encadrent et les compensations qui l’accompagnent. C’est le sens du '
    'trilemme de Dani Rodrik, pour qui hypermondialisation, démocratie et '
    'souveraineté nationale ne peuvent être pleinement conciliées : défendre '
    'le libre-échange sans réserve revient à sacrifier l’un des deux autres '
    'termes, et donc à opérer un choix politique que l’argument économique ne '
    'suffit pas à fonder.',
    notes=[
      note('c1', 'Posée en termes d’ouverture ou de fermeture, elle n’admet '
                 'pas de réponse générale ; posée en termes de régime '
                 'd’échange, elle en admet une',
           'Second apport de la conclusion : le devoir n’a pas seulement '
           'répondu, il a reformulé. Dire ce que la démonstration a changé '
           'dans la question est l’un des moyens les plus sûrs de dépasser '
           'l’introduction. Attention toutefois : cela ne vaut que si la '
           'partie III a effectivement opéré ce déplacement — sinon, c’est '
           'une promesse non tenue.'),
    ]),

  para(role='Ouverture', isole=True, txt=
    'Reste que l’objet même du débat s’est déplacé depuis quelques années. '
    'Les droits de douane américains ne visent plus seulement à protéger '
    'l’emploi national : ils relèvent d’une logique de compétition '
    'stratégique et de domination technologique, ce que Richard Baldwin '
    'résume en observant que l’interdépendance, longtemps perçue comme une '
    'opportunité, se lit désormais comme une vulnérabilité. Si le commerce '
    'devient un instrument de puissance, la question n’est plus seulement de '
    'savoir s’il faut défendre le libre-échange, mais s’il est encore '
    'possible de le défendre sur le terrain de la seule efficacité '
    'économique.',
    notes=[
      note('c2', 'Si le commerce devient un instrument de puissance, la '
                 'question n’est plus seulement de savoir s’il faut défendre '
                 'le libre-échange, mais s’il est encore possible de le '
                 'défendre sur le terrain de la seule efficacité économique.',
           'L’ouverture prolonge réellement la réflexion parce qu’elle change '
           'de critère de jugement : tout le devoir a pesé le libre-échange à '
           'l’aune de l’efficacité ; l’ouverture demande si ce critère est '
           'encore le bon. C’est un déplacement, pas un argument '
           'supplémentaire.'),
      note('c2', 'Les droits de douane américains ne visent plus seulement à '
                 'protéger l’emploi national',
           'Vérifiez qu’une ouverture n’est pas un morceau de développement '
           'oublié. Si « les droits de douane comme arme géoéconomique » '
           'avait constitué une sous-partie de III, cette ouverture ferait '
           'doublon et perdrait sa fonction. Ici, la partie III traitait du '
           'régime d’échange et de sa soutenabilité politique : la '
           'géoéconomie ouvre bien sur autre chose.'),
    ]),
 ],
 globaux=[],
)

PIECES = [INTRO, ANNONCE, SP, TRANS, CONCL]
