# Chapitre 8
## Vos données, leur trésor

---

Chaque fois que vous tapez quelque chose dans ChatGPT, où va cette information ?

C'est une question que presque personne ne pose. Et c'est un problème.

---

### 8.1 Ce qui se passe quand vous tapez dans ChatGPT

Vous écrivez : "Mon fils de 8 ans a des difficultés en maths. Comment l'aider ?"

Voici le trajet de cette information :

**1. Transmission**

Votre question quitte votre ordinateur, traverse Internet, et arrive sur des serveurs d'OpenAI (hébergés chez Microsoft Azure).

**2. Traitement**

Le modèle génère une réponse. Votre question et la réponse sont stockées.

**3. Conservation**

Par défaut, cette conversation est conservée. Pendant combien de temps ? Ça dépend des versions et des politiques — qui changent.

**4. Utilisation potentielle**

Sauf si vous avez désactivé cette option, votre conversation peut être :
- Lue par des employés d'OpenAI (pour améliorer le service)
- Utilisée pour entraîner les futurs modèles
- Analysée pour détecter des abus

---

### 8.2 Où vont vos conversations ?

**Physiquement**

Vos données sont stockées sur des serveurs Microsoft Azure, principalement aux États-Unis. Des copies peuvent exister dans d'autres régions.

**Juridiquement**

Ces données sont soumises au droit américain. Cela signifie :
- Le Cloud Act permet au gouvernement US d'y accéder
- Les tribunaux américains peuvent les demander
- La FISA (loi de surveillance) peut s'appliquer

**Concrètement**

Si vous êtes un citoyen européen lambda, personne ne va probablement fouiller vos conversations sur ChatGPT. Mais le *potentiel* existe.

---

### 8.3 Qui peut les lire ? (humains et machines)

**Les humains**

Oui, des employés d'OpenAI peuvent lire vos conversations. C'est dans les conditions d'utilisation.

Pourquoi ? Pour :
- Améliorer le modèle
- Détecter les abus
- Répondre aux demandes légales

Ce n'est pas de la surveillance active de tout le monde. Mais des conversations sont échantillonnées et examinées.

**Les machines**

Vos données alimentent des systèmes automatiques :
- Détection de contenu problématique
- Analyse des patterns d'utilisation
- (Potentiellement) Entraînement des futurs modèles

---

### 8.4 La différence entre "stocké" et "utilisé pour entraîner"

C'est une distinction cruciale que beaucoup de gens ne comprennent pas.

**Stocké**

Votre conversation est conservée dans une base de données. Elle peut être retrouvée, relue, analysée.

**Utilisé pour entraîner**

Votre conversation est incorporée dans les données qui servent à créer la prochaine version du modèle. Elle devient, en quelque sorte, une partie permanente de l'IA.

**La différence**

- Une donnée stockée peut être supprimée sur demande
- Une donnée utilisée pour l'entraînement est "digérée" — elle influence le modèle, mais n'est plus identifiable comme telle

**OpenAI permet de refuser l'entraînement**

Depuis 2023, vous pouvez aller dans les paramètres et désactiver l'utilisation de vos conversations pour l'entraînement. Mais c'est opt-out (il faut le faire activement), pas opt-in.

---

### 8.5 Comment (essayer de) protéger vos données

**Règle n°1 : Ne jamais partager d'informations sensibles**

Jamais. Vraiment.

❌ Pas de numéros de carte bancaire
❌ Pas de mots de passe
❌ Pas de numéros de sécurité sociale
❌ Pas de données médicales détaillées
❌ Pas de secrets professionnels
❌ Pas de documents confidentiels

**Règle n°2 : Désactiver l'entraînement**

Sur ChatGPT : Settings → Data Controls → Chat History & Training → Désactiver

Attention : cela désactive aussi l'historique. Vous ne pourrez pas retrouver vos anciennes conversations.

**Règle n°3 : Utiliser des comptes non identifiables**

Si vous voulez plus d'anonymat, utilisez une adresse email qui ne révèle pas votre identité.

**Règle n°4 : Envisager des alternatives locales**

Des modèles comme Llama peuvent tourner sur votre propre ordinateur. Rien n'est envoyé à l'extérieur.

---

### 8.6 Les options "privacy" : ce qu'elles font vraiment

**ChatGPT — Mode sans historique**

Quand vous désactivez l'historique :
- Vos conversations ne sont pas sauvegardées dans votre compte
- Elles ne sont pas utilisées pour l'entraînement
- MAIS : elles sont quand même conservées 30 jours "pour abus" avant suppression

**ChatGPT — Temporary Chat**

Un mode encore plus éphémère, où même la mémoire de session est réduite.

**ChatGPT Enterprise / API**

Les versions payantes pour entreprises ont des garanties plus fortes : données non utilisées pour l'entraînement, suppression sur demande, parfois conformité RGPD explicite.

**Le problème du "trust me"**

Tout cela repose sur la confiance. Vous devez croire qu'OpenAI fait ce qu'elle dit. Il n'y a pas de vérification indépendante possible.

---

### Cas concrets qui doivent vous alerter

**Le médecin qui demande un diagnostic**

Un médecin tape les symptômes d'un patient dans ChatGPT pour avoir une idée de diagnostic. Ces données médicales viennent de partir aux États-Unis.

**L'avocat qui demande un conseil**

Un avocat copie-colle un contrat confidentiel pour demander une analyse. Ce contrat est maintenant sur les serveurs d'OpenAI.

**L'employé qui résume un document interne**

Un employé utilise ChatGPT pour résumer un rapport stratégique de son entreprise. Ce rapport est potentiellement accessible à OpenAI.

**Tous ces cas sont réels.** Ils se produisent tous les jours.

---

### Ce que vous pouvez faire

1. **Avant de taper, demandez-vous : "Est-ce que j'accepterais que cette info soit publique ?"** Si non, ne la mettez pas dans l'IA.

2. **Désactivez l'entraînement** dans les paramètres de ChatGPT.

3. **Pour les usages sensibles, utilisez des alternatives locales** ou des versions entreprise avec des garanties contractuelles.

4. **Formez vos proches.** Beaucoup de gens ne réalisent pas les implications.

5. **Exercez vos droits RGPD.** Vous pouvez demander à OpenAI quelles données ils ont sur vous, et demander leur suppression.

---

*Chapitre suivant : Le regard européen — Vos droits*
