# Chapitre 10
## Questions à poser à OpenAI/Microsoft/Google

---

Vous utilisez leurs produits tous les jours. Mais savez-vous vraiment ce qu'ils font de vos données ?

Voici les questions que vous devriez poser — et les réponses que vous devriez obtenir.

---

### 10.1 "Mes conversations sont-elles lues par des humains ?"

**La vraie réponse :**

Oui, potentiellement.

OpenAI, Google, et les autres emploient des équipes de "reviewers" (examinateurs) qui lisent des échantillons de conversations pour :
- Améliorer la qualité des réponses
- Détecter les abus
- Entraîner les systèmes de modération

Ce n'est pas de la surveillance systématique de tout le monde. Mais vos conversations peuvent être sélectionnées aléatoirement.

**Ce que ça signifie :**

- Ne partagez jamais d'informations que vous ne voudriez pas qu'un inconnu lise
- Les conversations "embarrassantes" ou "sensibles" peuvent être vues par des humains
- Il n'y a pas de confidentialité absolue

---

### 10.2 "Mes données servent-elles à entraîner le modèle ?"

**OpenAI (ChatGPT)**

Par défaut : OUI
Mais vous pouvez désactiver cette option dans Settings → Data Controls

**Google (Gemini)**

Par défaut : OUI pour Gemini gratuit
Non pour Gemini Advanced et les versions Workspace

**Microsoft (Copilot)**

Ça dépend de la version :
- Copilot gratuit : données potentiellement utilisées
- Copilot Pro / Enterprise : garanties contractuelles plus fortes

**Claude (Anthropic)**

Par défaut : OUI pour la version gratuite
Opt-out disponible dans les paramètres

**La règle générale :**

Version gratuite = vos données peuvent être utilisées
Version payante/entreprise = généralement non (mais vérifiez les conditions)

---

### 10.3 "Où sont physiquement stockées mes données ?"

**OpenAI**

Serveurs Microsoft Azure, principalement aux États-Unis.
Soumis au droit américain (Cloud Act, FISA).

**Google**

Datacenters Google dans le monde entier.
Pour les utilisateurs européens, possibilité de stockage en Europe (mais pas garanti par défaut).

**Microsoft**

Azure datacenters globaux.
Options de résidence des données pour les clients entreprise.

**Pourquoi c'est important :**

- Le lieu de stockage détermine quel droit s'applique
- Les données aux US sont accessibles au gouvernement américain
- Même si stockées en Europe, une entreprise américaine peut être contrainte de les fournir

---

### 10.4 "Que se passe-t-il si je supprime mon compte ?"

**OpenAI**

- Vos conversations sont supprimées de votre interface
- Mais OpenAI conserve des données "désidentifiées" pour l'entraînement
- Les sauvegardes peuvent persister plusieurs semaines/mois

**Google**

- Processus de suppression via Google Account
- Délai de propagation : jusqu'à plusieurs mois
- Certaines données peuvent être conservées pour des raisons légales

**La réalité :**

"Supprimer" ne signifie jamais "effacer instantanément et définitivement de tous les systèmes".

Les données traversent des caches, des sauvegardes, des systèmes d'archivage. La suppression complète prend du temps et n'est jamais 100% garantie.

---

### 10.5 "Pourquoi Copilot et ChatGPT donnent des réponses différentes ?"

C'est une question que beaucoup de gens se posent.

**Les deux utilisent des modèles GPT d'OpenAI. Mais :**

- Les versions peuvent être différentes (GPT-4, GPT-4o, GPT-4 Turbo...)
- Les "system prompts" sont différents (instructions cachées qui guident le comportement)
- Les politiques de modération sont différentes
- L'intégration avec d'autres services varie (Copilot peut chercher sur Bing)

**Microsoft personnalise**

Copilot a des instructions spécifiques qui le rendent plus "prudent" sur certains sujets, plus intégré à l'écosystème Microsoft, et parfois plus limité que ChatGPT direct.

**Ce que ça signifie :**

Le même modèle sous-jacent peut donner des expériences très différentes selon qui l'emballe.

---

### 10.6 Checklist : 10 questions avant d'utiliser un outil IA

Avant de confier vos données à un nouvel outil IA, posez-vous ces questions :

| # | Question | Réponse à chercher |
|---|----------|-------------------|
| 1 | **Qui est derrière ?** | Entreprise, pays, investisseurs |
| 2 | **Où sont stockées mes données ?** | USA, Europe, autre |
| 3 | **Mes données servent-elles à l'entraînement ?** | Oui/Non, opt-out possible ? |
| 4 | **Des humains peuvent-ils lire mes données ?** | Pour modération, amélioration ? |
| 5 | **Puis-je exporter mes données ?** | Format, facilité |
| 6 | **Puis-je supprimer mes données ?** | Comment, délai réel |
| 7 | **Quelles sont les conditions RGPD ?** | Conformité, DPO, procédures |
| 8 | **Quelle est la politique de sécurité ?** | Chiffrement, audits |
| 9 | **Que se passe-t-il si l'entreprise est vendue ?** | Transfert des données |
| 10 | **Y a-t-il des alternatives plus respectueuses ?** | Options locales, européennes |

**Où trouver ces informations :**

- Privacy Policy / Politique de confidentialité
- Terms of Service / Conditions d'utilisation
- Help Center / FAQ
- Trust Center (pour les entreprises)

---

### Modèle de demande d'information

Si les informations ne sont pas claires, vous pouvez écrire :

> Objet : Demande d'information sur le traitement des données
>
> Madame, Monsieur,
>
> J'utilise votre service [nom du service] et je souhaite comprendre comment mes données sont traitées.
>
> Merci de me préciser :
> 1. Si mes conversations sont utilisées pour entraîner vos modèles
> 2. Où mes données sont physiquement stockées
> 3. Qui peut y avoir accès (employés, sous-traitants, autorités)
> 4. Comment demander leur suppression définitive
>
> Cette demande est faite en application du RGPD.
>
> Cordialement,
> [Votre nom]

---

### Ce que vous pouvez faire

1. **Posez au moins UNE question à un service que vous utilisez.** Ça vous apprendra beaucoup sur leur transparence.

2. **Gardez la checklist à portée de main.** Consultez-la avant d'adopter un nouvel outil IA.

3. **Partagez vos découvertes.** Si une entreprise a des pratiques douteuses, faites-le savoir.

4. **Votez avec vos pieds.** Si un service ne respecte pas vos droits, changez.

5. **Restez sceptique.** "Nous prenons votre vie privée au sérieux" est une phrase marketing, pas une garantie.

---

*Chapitre suivant : Questions à poser à votre employeur*
