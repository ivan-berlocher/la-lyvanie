# Chapitre 14
## Évaluer un outil IA avant de l'utiliser

---

Un nouvel outil IA sort chaque semaine.
Chacun promet de révolutionner votre vie.

Comment savoir lesquels valent le coup ?
Comment éviter les pièges ?

Voici votre guide d'évaluation.

---

### 14.1 La grille d'évaluation en 5 minutes

**Avant d'utiliser un nouvel outil IA, passez-le au crible :**

| Critère | Question | Score /5 |
|---------|----------|----------|
| **Transparence** | Qui est derrière ? Où sont mes données ? | |
| **Utilité réelle** | Résout-il un vrai problème que j'ai ? | |
| **Alternatives** | Existe-t-il des options sans IA ou plus éthiques ? | |
| **Coût caché** | Que dois-je donner en échange (données, attention) ? | |
| **Dépendance** | Puis-je m'en passer facilement ? | |

**Interprétation :**

- **20-25** : Outil potentiellement intéressant, à tester avec précaution
- **15-19** : Réfléchissez à deux fois, les risques sont significatifs
- **10-14** : Probablement pas une bonne idée
- **< 10** : Fuyez

---

### 14.2 Qui est derrière cet outil ?

**Les informations à chercher :**

- **L'entreprise** : Nom, pays, taille, historique
- **Les investisseurs** : Qui finance ? Quels intérêts ?
- **Le modèle économique** : Comment gagnent-ils de l'argent ?
- **Le track record** : Historique de scandales, de failles, de changements de conditions

**Où chercher :**

- Page "About" ou "À propos"
- Crunchbase (investisseurs, levées de fonds)
- Recherche Google "[nom] controversy" ou "[nom] scandal"
- Articles de presse

**Signaux d'alerte :**

❌ Entreprise opaque, pas d'information sur les fondateurs
❌ Financée par des fonds "douteux" ou liés à certains États
❌ Modèle économique flou ("gratuit" sans explication)
❌ Historique de failles de sécurité ou de revente de données

---

### 14.3 Que font-ils de vos données ?

**La politique de confidentialité révèle beaucoup.**

Cherchez :
- **Collecte** : Quelles données ? (Seulement ce que j'entre ? Ou plus ?)
- **Utilisation** : Pour quoi ? (Améliorer le service ? Entraîner des modèles ? Publicité ?)
- **Partage** : Avec qui ? (Partenaires ? Affiliés ? "Tiers" ?)
- **Conservation** : Combien de temps ?
- **Droits** : Comment accéder, modifier, supprimer ?

**Les formulations à repérer :**

- "Nous pouvons partager vos données avec nos partenaires" → ⚠️ Qui sont ces partenaires ?
- "Pour améliorer nos services" → ⚠️ Inclut l'entraînement de modèles ?
- "Conformément à la loi applicable" → ⚠️ Quelle loi ? Celle du pays de l'entreprise.
- "Nous pouvons modifier cette politique à tout moment" → ⚠️ Sans vous prévenir ?

---

### 14.4 Le vrai test : l'essayer avec des données fictives

**Avant d'y mettre vos vraies informations :**

1. **Créez un compte avec une adresse email dédiée** (pas votre email principal)
2. **Utilisez des données fictives** (faux nom, fausse adresse)
3. **Testez les fonctionnalités** avec des contenus non sensibles
4. **Observez le comportement** : publicités ciblées ? Emails ? Notifications ?
5. **Essayez de supprimer votre compte** : facile ou compliqué ?

**Ce que le test révèle :**

- La qualité réelle de l'outil (au-delà du marketing)
- La facilité d'usage (ou les dark patterns)
- Le respect de vos choix (ou les manipulations)
- La possibilité de partir (ou le verrouillage)

---

### 14.5 Les alternatives à considérer

**Avant d'adopter un outil IA commercial, demandez-vous :**

| Question | Exemples d'alternatives |
|----------|------------------------|
| **Puis-je faire sans IA ?** | Méthodes traditionnelles, outils simples |
| **Existe-t-il une version open source ?** | Ollama, LocalAI, Whisper local |
| **Y a-t-il des options européennes ?** | Mistral, OVHcloud, Scaleway |
| **Puis-je auto-héberger ?** | Solutions on-premise |
| **Y a-t-il des coopératives ou associations ?** | Framasoft, Chatons |

**Le principe de subsidiarité numérique :**

Utilisez la solution la plus locale, la plus simple, la moins invasive qui répond à votre besoin.

---

### 14.6 Cas pratiques

**Cas 1 : Un nouvel assistant de rédaction**

Promesse : "Écrivez 10x plus vite avec l'IA !"

**Questions à poser :**
- Mes textes sont-ils stockés et analysés ?
- Servent-ils à entraîner d'autres modèles ?
- Un humain peut-il les lire ?
- Que se passe-t-il si l'entreprise ferme ?

**Alternatives possibles :**
- Modèle local (Ollama + interface)
- Outil open source (LibreChat)
- Simplement ne pas utiliser d'IA pour écrire

---

**Cas 2 : Une app photo qui "embellit" vos photos**

Promesse : "Rendez vos photos magnifiques en un clic !"

**Questions à poser :**
- Mes photos sont-elles envoyées sur des serveurs ?
- Sont-elles stockées ? Combien de temps ?
- Les visages sont-ils analysés ? Pour quoi ?
- Ces photos peuvent-elles être utilisées pour de la reconnaissance faciale ?

**Signaux d'alarme :**
- App gratuite sans modèle économique évident
- Demande d'accès à toute la galerie photo
- Conditions d'utilisation qui donnent des droits sur vos images

**Alternative :**
- Logiciel de retouche local (Photoshop, GIMP, Pixelmator)

---

**Cas 3 : Un outil de transcription de réunions**

Promesse : "Ne prenez plus jamais de notes !"

**Questions à poser :**
- Les enregistrements audio sont-ils conservés ?
- Les transcriptions sont-elles analysées ?
- Qui a accès aux contenus des réunions ?
- Est-ce conforme au RGPD pour des réunions avec des tiers ?
- Ai-je le consentement des participants ?

**Point légal important :**
En France, enregistrer une réunion sans prévenir les participants est illégal.
Même avec leur accord, transférer ces données à un service tiers pose des questions RGPD.

---

### 14.7 La matrice décision finale

**Quand vous avez évalué un outil, utilisez cette matrice :**

```
                    Utilité réelle
                    Faible    Haute
                   ┌─────────┬─────────┐
         Élevés   │  NON    │ RÉFLÉCHIR│
Risques           ├─────────┼─────────┤
         Faibles  │ POURQUOI│   OUI   │
                   └─────────┴─────────┘
```

- **NON** : Risques élevés + faible utilité = passez votre chemin
- **RÉFLÉCHIR** : Utile mais risqué = précautions maximales, données fictives, usage limité
- **POURQUOI** : Peu risqué mais peu utile = pourquoi s'embêter ?
- **OUI** : Utile et peu risqué = testez avec précaution

---

### 14.8 Checklist finale avant adoption

| # | Vérification | ✓/✗ |
|---|--------------|-----|
| 1 | J'ai identifié l'entreprise et son pays | |
| 2 | J'ai lu (ou au moins parcouru) la politique de confidentialité | |
| 3 | J'ai cherché des avis et des critiques | |
| 4 | J'ai testé avec des données fictives | |
| 5 | J'ai vérifié que je peux supprimer mon compte | |
| 6 | J'ai considéré les alternatives | |
| 7 | J'ai évalué l'utilité réelle pour MON cas | |
| 8 | J'ai informé les personnes concernées (si données partagées) | |
| 9 | Je suis prêt à arrêter si ça tourne mal | |
| 10 | J'accepte consciemment le compromis données/service | |

---

### Ce que vous pouvez faire

1. **Appliquez cette grille au prochain outil IA qu'on vous propose.** Ça prend 10 minutes et ça peut vous éviter bien des problèmes.

2. **Partagez la grille avec vos proches.** Aidez-les à évaluer avant d'adopter.

3. **Soyez patient.** Un outil qui existe depuis 6 mois a moins prouvé qu'un outil qui existe depuis 6 ans.

4. **Acceptez de dire non.** Tout le monde n'a pas besoin de chaque nouvel outil IA.

5. **Réévaluez régulièrement.** Les conditions changent, les entreprises évoluent, les risques aussi.

---

*Chapitre suivant : Protéger ses données au quotidien*
