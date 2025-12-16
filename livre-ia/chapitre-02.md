# Chapitre 2
## Comment fonctionne ChatGPT (version honnête)

---

### 2.1 Le secret : la prédiction statistique du langage

Vous savez maintenant que ChatGPT prédit le mot suivant. Mais comment ?

Imaginez un jeu. Je vous donne le début d'une phrase, vous devez deviner la suite :

> "Le chat est monté sur le..."

Vous pensez probablement : toit, arbre, canapé, lit. Pas : réfrigérateur quantique, théorème, démocratiquement.

Pourquoi ? Parce que vous avez lu et entendu des millions de phrases. Vous savez, intuitivement, quels mots vont ensemble.

ChatGPT fait la même chose — mais à une échelle industrielle.

Prenons un exemple concret. Le modèle voit :

> "La tour Eiffel a été construite en"

Il calcule la probabilité de chaque mot possible :
- "1889" → 73%
- "1887" → 8%
- "Paris" → 4%
- "fer" → 3%
- ... (des milliers d'autres mots avec des probabilités infimes)

Il choisit "1889" (ou parfois un autre mot moins probable, pour varier les réponses).

Puis il recommence avec : "La tour Eiffel a été construite en 1889"

Le mot suivant le plus probable ? Peut-être "par", "pour", "et", un point...

Et ainsi de suite, mot après mot, jusqu'à la fin de la réponse.

**C'est tout.**

Pas de base de données de faits.
Pas de moteur de recherche intégré.
Pas de raisonnement logique.

Juste : quel mot vient probablement après ?

---

### 2.2 L'entraînement : avaler Internet pour apprendre à parler

D'où viennent ces probabilités ?

De l'**entraînement**. Pendant des mois, le modèle a "lu" une quantité astronomique de texte :

- Wikipédia (toutes les langues)
- Des millions de livres
- Des milliards de pages web
- Des forums, des articles, des conversations
- Du code source (GitHub, Stack Overflow)

On estime que GPT-4 a été entraîné sur environ **13 trillions de tokens** (un token ≈ un mot ou morceau de mot). Pour comparaison, si vous lisiez 24h/24, il vous faudrait environ 400 000 ans pour lire tout ça.

**Comment l'entraînement fonctionne :**

1. On prend un texte existant : "Le chat dort sur le canapé"
2. On cache le dernier mot : "Le chat dort sur le ___"
3. On demande au modèle de deviner
4. S'il dit "canapé" → bien, on ne change rien
5. S'il dit "fromage" → mal, on ajuste les paramètres

On répète ce processus des milliards de fois, sur des milliards de phrases.

Progressivement, le modèle "apprend" (au sens mathématique) quels mots vont avec quels autres mots, dans quels contextes.

**Ce qui est capturé :**

- La grammaire (le modèle sait que "le chat mange" est correct, pas "chat le mange")
- Les faits (si "Paris est la capitale de la France" apparaît souvent, le modèle le reproduira)
- Le style (il peut imiter un ton formel, humoristique, poétique)
- Le raisonnement apparent (il a vu des millions d'arguments logiques)

**Ce qui N'est PAS capturé :**

- La vérité (le modèle ne sait pas ce qui est vrai, juste ce qui est fréquent)
- L'actualité (il ne sait rien de ce qui s'est passé après sa date d'entraînement)
- Votre contexte (il ne sait rien de vous, sauf ce que vous lui dites dans la conversation)

---

### 2.3 L'attention : comment le modèle "lit" votre question

Voici le concept clé qui a révolutionné l'IA : **l'attention**.

Quand vous posez une question, le modèle ne lit pas mot par mot, de gauche à droite. Il regarde **tous les mots en même temps** et calcule lesquels sont importants pour lesquels.

Exemple :

> "Le chat qui appartient à Marie et qui a un pelage roux dort sur le canapé de sa maison"

Quand le modèle doit prédire ce qui vient après "dort sur le canapé de sa", il doit comprendre que "sa" se réfère à "Marie", pas au "chat" ni au "canapé".

Comment fait-il ? Il calcule des scores d'attention :
- "sa" est fortement connecté à "Marie" (c'est un pronom possessif qui se réfère à elle)
- "sa" est peu connecté à "chat" ou "canapé"

Ce mécanisme d'attention permet au modèle de gérer des phrases longues et complexes, avec des références qui traversent des dizaines de mots.

**Le Transformer**

L'architecture qui implémente cette attention s'appelle le **Transformer** (d'où le "T" de GPT — Generative Pre-trained Transformer).

C'est l'innovation de 2017 qui a tout changé. Avant les Transformers, les modèles de langage étaient beaucoup plus limités. Ils "oubliaient" le début d'une phrase quand ils arrivaient à la fin.

Le Transformer peut regarder le contexte entier d'un coup.

**La fenêtre de contexte**

Mais cette fenêtre a une limite. ChatGPT-3.5 pouvait "voir" environ 4 000 tokens à la fois. GPT-4 peut en voir 32 000, voire 128 000 dans certaines versions.

Au-delà ? Le modèle ne voit plus. C'est comme si vous aviez une conversation mais oubliiez tout ce qui s'est dit il y a plus de 10 minutes.

C'est pourquoi les longues conversations avec ChatGPT peuvent devenir incohérentes : le modèle "oublie" le début.

---

### 2.4 Pourquoi chaque réponse est différente (même pour la même question)

Faites l'expérience. Posez exactement la même question à ChatGPT deux fois. Vous n'obtiendrez pas la même réponse.

Pourquoi ?

Parce que le modèle ne choisit pas toujours le mot le plus probable. Il y a un paramètre appelé **température** qui introduit du hasard.

- **Température = 0** : le modèle choisit toujours le mot le plus probable. Réponses prévisibles, répétitives.
- **Température élevée** : le modèle choisit parfois des mots moins probables. Réponses plus créatives, mais aussi plus risquées.

ChatGPT utilise une température intermédiaire. Assez de variété pour ne pas être ennuyeux, assez de prudence pour ne pas dire n'importe quoi (enfin, pas trop).

**Conséquence importante :**

Il n'y a pas UNE réponse de ChatGPT à une question. Il y a une distribution de réponses possibles. Celle que vous voyez est un tirage dans cette distribution.

Si vous n'aimez pas une réponse, vous pouvez simplement la régénérer. Vous obtiendrez souvent quelque chose de différent.

---

### 2.5 Ce que le modèle "sait" vs. ce qu'il "invente"

C'est la question la plus importante. Et la plus difficile.

**Le modèle ne sait rien au sens propre.**

Il n'a pas de mémoire de faits. Il n'a pas de base de données à consulter. Il génère des séquences de mots basées sur des patterns statistiques.

Quand il dit "Paris est la capitale de la France", ce n'est pas parce qu'il "sait" ce fait. C'est parce que cette séquence de mots a une probabilité très élevée dans son modèle statistique.

**Le problème :**

Des séquences fausses peuvent aussi avoir une haute probabilité.

Exemple : "Le premier homme sur la Lune était Neil Armstrong en 1969."

C'est vrai. Le modèle va probablement le dire correctement.

Mais que se passe-t-il si vous demandez : "Qui était le troisième homme à marcher sur la Lune ?"

Le modèle va générer une réponse. Mais il y a de bonnes chances qu'elle soit fausse, parce que ce fait est moins fréquent dans les données d'entraînement.

**Comment distinguer ?**

Vous ne pouvez pas. Pas en regardant la réponse.

Le modèle ne dit jamais "je ne suis pas sûr" de façon fiable. Il génère des réponses avec la même assurance, qu'elles soient vraies ou fausses.

**Les "connaissances" du modèle sont :**

✅ Fiables pour :
- Les faits très courants (capitales, dates célèbres, définitions standard)
- Les patterns linguistiques (grammaire, style)
- Les structures logiques simples

❌ Peu fiables pour :
- Les faits rares ou récents
- Les chiffres précis (statistiques, prix, mesures)
- Tout ce qui nécessite un raisonnement complexe
- Tout ce qui n'était pas dans les données d'entraînement

**La règle d'or :**

Ne faites jamais confiance à une réponse de ChatGPT sans vérification, surtout si l'exactitude compte.

---

### Ce que vous pouvez faire

1. **Comprenez le mécanisme.** ChatGPT prédit des mots, il ne raisonne pas. Cette compréhension change tout.

2. **Vérifiez les faits.** Jamais de confiance aveugle. Surtout pour les chiffres, les dates, les noms propres.

3. **Utilisez la régénération.** Si une réponse ne vous convient pas, demandez-en une autre. Le modèle peut faire mieux au deuxième essai.

4. **Soyez conscient des limites temporelles.** Le modèle ne sait rien de ce qui s'est passé après sa date d'entraînement.

5. **Gardez vos conversations courtes.** Plus la conversation est longue, plus le modèle "oublie" le contexte initial.

---

*Chapitre suivant : Les super-pouvoirs (réels)*
