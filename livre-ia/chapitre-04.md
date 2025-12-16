# Chapitre 4
## Les faiblesses cachées

---

Maintenant qu'on a vu ce que l'IA fait bien, parlons de ce qu'elle fait **mal**. 

Pas pour être négatif. Pour être réaliste.

Ces faiblesses ne sont pas des bugs à corriger. Ce sont des **limites fondamentales** de la technologie actuelle. Les connaître, c'est se protéger.

---

### 4.1 L'hallucination : mentir avec aplomb

C'est le problème numéro un.

L'IA peut inventer des faits, des citations, des références — avec une assurance totale. Elle ne dit jamais "je ne sais pas" de façon fiable. Elle génère toujours une réponse.

**Exemples réels :**

- Des avocats américains ont soumis des documents juridiques avec des citations de cas inventés par ChatGPT. Les juges n'ont pas apprécié.
- Des étudiants ont rendu des dissertations citant des livres qui n'existent pas.
- Des journalistes ont publié des articles avec des statistiques fabriquées.

**Pourquoi ça arrive ?**

Rappelez-vous : l'IA prédit le mot suivant. Elle ne vérifie pas la vérité.

Quand vous demandez "Cite-moi une étude sur X", l'IA génère une séquence de mots qui *ressemble* à une citation d'étude. Titre plausible, auteurs plausibles, journal plausible, année plausible.

Mais elle n'a pas de base de données d'études réelles. Elle hallucine une citation statistiquement vraisemblable.

**Le piège :**

Plus la question est spécifique, plus le risque d'hallucination est élevé. Pour les faits très courants, l'IA est généralement correcte. Pour les détails rares, c'est la loterie.

**Comment se protéger :**

- Ne jamais citer directement une source donnée par l'IA sans vérifier qu'elle existe
- Demander plusieurs sources et les recouper
- Être particulièrement vigilant sur les chiffres, dates, noms propres

---

### 4.2 L'incohérence : se contredire sans sourciller

Posez la même question deux fois, formulée différemment. Vous pouvez obtenir des réponses contradictoires.

**Exemple :**

> "Est-ce que le café est bon pour la santé ?"
> → "Le café a de nombreux bienfaits : antioxydants, concentration..."

> "Est-ce que le café est mauvais pour la santé ?"
> → "Le café présente des risques : anxiété, dépendance, troubles du sommeil..."

L'IA ne défend pas une position. Elle génère ce qui est statistiquement attendu après votre question. Si vous orientez la question vers le positif, elle génère du positif. Vers le négatif, du négatif.

**Pourquoi c'est problématique :**

L'IA n'a pas de "croyances" cohérentes. Elle n'a pas de modèle du monde qu'elle maintient d'une conversation à l'autre. Chaque réponse est générée indépendamment.

**Comment se protéger :**

- Ne pas prendre une réponse pour une vérité définitive
- Poser des questions sous différents angles pour voir si les réponses convergent
- Se méfier si l'IA semble toujours d'accord avec vous (biais de confirmation)

---

### 4.3 La mémoire de poisson rouge

Chaque fois que vous ouvrez une nouvelle conversation avec ChatGPT, c'est comme parler à quelqu'un qui ne vous a jamais rencontré.

**L'IA n'a pas de mémoire persistante par défaut.**

Elle ne se souvient pas :
- De ce que vous lui avez dit la semaine dernière
- De vos préférences
- De votre contexte personnel
- De vos projets en cours

**Et même dans une conversation en cours...**

La "fenêtre de contexte" est limitée. Après quelques milliers de mots échangés, l'IA commence à "oublier" le début de la conversation.

Vous avez déjà eu cette expérience ? Vous rappelez un détail mentionné au début de la discussion, et l'IA ne sait plus de quoi vous parlez.

**Conséquences :**

- Vous devez répéter votre contexte à chaque nouvelle session
- Les longues conversations deviennent incohérentes
- L'IA ne peut pas vraiment vous "connaître"

**Solutions partielles :**

Certains outils (comme ChatGPT avec la mémoire activée) tentent de pallier ce problème en stockant des informations entre sessions. Mais c'est limité et imparfait.

---

### 4.4 L'absence de bon sens

L'IA peut résoudre des problèmes mathématiques complexes et échouer sur des questions qu'un enfant de 5 ans réussirait.

**Exemples célèbres :**

> "J'ai mis des pommes dans un frigo, puis je les ai sorties. Où sont les pommes ?"
> 
> L'IA peut parfois répondre "dans le frigo" — oubliant la deuxième partie de la phrase.

> "Combien de fois la lettre 'r' apparaît dans 'fraise' ?"
> 
> L'IA se trompe régulièrement sur ce type de question simple.

**Pourquoi ?**

Le "bon sens" humain vient d'une compréhension du monde physique, de l'expérience incarnée, de millions d'interactions avec la réalité.

L'IA n'a vu que du texte. Elle n'a jamais tenu une pomme, ouvert un frigo, compté sur ses doigts. Elle n'a pas de modèle physique du monde — juste des patterns linguistiques.

**Le paradoxe :**

L'IA peut expliquer la relativité générale mais échouer à compter des lettres. Elle excelle sur ce qui est bien documenté dans le texte, et échoue sur ce qui est "évident" mais rarement explicité.

---

### 4.5 Le perroquet stochastique : répéter sans comprendre

En 2021, des chercheurs ont publié un article influent intitulé "On the Dangers of Stochastic Parrots" (Sur les dangers des perroquets stochastiques).

Leur argument : les LLM ne "comprennent" pas le langage. Ils reproduisent des patterns statistiques, comme un perroquet qui répète des phrases sans savoir ce qu'elles signifient.

**Est-ce vrai ?**

C'est un débat philosophique non résolu. Mais pragmatiquement :

- L'IA peut générer des réponses sensées sans aucune compréhension au sens humain
- Elle peut aussi générer du non-sens parfaitement grammatical
- Elle ne distingue pas les deux

**Conséquence pratique :**

Ne supposez jamais que l'IA "comprend" votre problème. Elle génère des séquences de mots qui *ressemblent* à une réponse pertinente. C'est souvent utile, parfois trompeur.

---

### 4.6 Pourquoi l'IA ne peut pas "vérifier" ses propres réponses

Vous pourriez penser : "OK, l'IA hallucine parfois. Mais pourquoi ne vérifie-t-elle pas ses réponses avant de les donner ?"

**Parce qu'elle ne peut pas.**

L'IA n'a pas accès à Internet en temps réel (sauf plugins spécifiques). Elle n'a pas de base de données de faits à consulter. Elle n'a pas de mécanisme interne pour distinguer vrai et faux.

Quand on lui demande de "vérifier", elle génère une nouvelle séquence de mots qui *ressemble* à une vérification. Ce n'en est pas vraiment une.

**L'illusion de l'auto-correction :**

> "Es-tu sûr de ta réponse précédente ?"
> → "Vous avez raison, laissez-moi corriger..."

L'IA peut changer sa réponse simplement parce que vous avez exprimé un doute — même si sa première réponse était correcte.

Elle n'a pas de confiance calibrée dans ses propres sorties.

---

### Ce que vous pouvez faire

1. **Partez du principe que l'IA peut se tromper.** Toujours. Sur tout. Vérifiez ce qui compte.

2. **Méfiez-vous de l'assurance.** L'IA écrit avec la même confiance, qu'elle ait raison ou tort.

3. **Ne demandez pas à l'IA de "vérifier".** Elle ne peut pas vraiment le faire. Vérifiez vous-même.

4. **Gardez vos conversations courtes.** Plus la conversation est longue, plus le risque d'incohérence augmente.

5. **Croisez les sources.** Si un fait compte, vérifiez-le ailleurs que dans l'IA.

---

*Chapitre suivant : La carte du pouvoir*
