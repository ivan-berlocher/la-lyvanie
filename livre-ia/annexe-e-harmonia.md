# Annexe E
## L'architecture Harmonia — Pour aller plus loin

---

*Cette annexe présente une proposition d'architecture pour une IA gouvernable, développée dans le cadre de recherches académiques parallèles.*

---

## Pourquoi cette annexe ?

Tout au long de ce livre, nous avons vu les limites des IA actuelles : opacité, centralisation, perte de contrôle sur nos données. Cette annexe présente **Harmonia**, une architecture alternative qui tente de résoudre ces problèmes.

**Ce n'est pas un produit commercial.** C'est une proposition conceptuelle et technique, issue de travaux de recherche, qui illustre à quoi pourrait ressembler une IA conçue différemment — avec le citoyen au centre.

---

## Le problème que Harmonia cherche à résoudre

### Le modèle actuel

```
[Vous] → [API cloud] → [Modèle opaque] → [Réponse]
              ↓
    [Vos données stockées]
    [Entraînement futur ?]
    [Analyse comportementale ?]
```

**Problèmes :**
- Vous ne savez pas ce qui se passe avec vos données
- Le modèle est une boîte noire
- Aucun contrôle sur les règles qui gouvernent l'IA
- Dépendance à une entreprise privée

### Le modèle Harmonia

```
[Vous] → [Votre profil .life] → [Gouverneur local] → [Modèle]
              ↓                        ↓
    [Données sous votre contrôle]  [Règles vérifiables]
```

**Différences clés :**
- Vos données restent sous votre contrôle
- Les règles de l'IA sont explicites et vérifiables
- Séparation entre "comprendre" et "agir"
- Possibilité de supervision et d'audit

---

## Les trois couches d'Harmonia

### 1. Lumeria — La couche de raisonnement

**Rôle :** Traiter l'information, raisonner, générer du contenu.

C'est là qu'interviennent les LLM (GPT-4, Claude, etc.). Mais dans Harmonia, cette couche est **encadrée** par les deux autres.

**Principe :** Le LLM fait ce qu'il fait bien (comprendre le langage, générer du texte), mais il ne décide pas seul.

### 2. Trustia — La couche de confiance

**Rôle :** Gérer l'identité, les permissions, la traçabilité.

- Qui parle à l'IA ?
- Quels droits a cette personne ?
- Quelles actions sont autorisées ?
- Comment tracer ce qui s'est passé ?

**Principe :** Avant d'agir, l'IA vérifie qu'elle en a le droit.

### 3. Lumenia — La couche de gouvernance

**Rôle :** Définir les règles, les contraintes éthiques, les limites.

- Quelles sont les valeurs que l'IA doit respecter ?
- Quels contenus sont interdits ?
- Comment résoudre les conflits ?

**Principe :** Les règles sont explicites, pas cachées dans les poids du modèle.

---

## Le document .life — Reprendre le contrôle

### Concept

Le fichier `.life` est un document structuré qui contient :
- Votre profil (préférences, contexte, besoins)
- Vos règles personnelles (ce que l'IA peut/ne peut pas faire)
- Votre historique (ce que vous avez partagé, et avec qui)

**Vous êtes propriétaire de ce fichier.** Il est stocké localement ou dans un espace que vous contrôlez.

### Structure simplifiée

```yaml
# Exemple de document .life (simplifié)

identity:
  name: "Marie Dupont"
  preferred_language: "fr"
  timezone: "Europe/Paris"

preferences:
  communication_style: "direct"  # ou "gentle", "formal"
  verbosity: "concise"           # ou "detailed"
  
boundaries:
  share_health_data: false
  share_location: false
  allow_marketing: false
  
values:
  priorities:
    - family
    - learning
    - privacy
    
permissions:
  openai_chatgpt:
    read_calendar: false
    send_emails: false
    access_history: "session_only"  # pas de persistance
    
audit_log:
  enabled: true
  retention_days: 30
```

### Principes clés

**1. Portabilité**
Votre .life fonctionne avec n'importe quelle IA compatible. Pas de vendor lock-in.

**2. Lisibilité**
Le format est compréhensible par un humain, pas juste par une machine.

**3. Granularité**
Vous décidez permission par permission, service par service.

**4. Révocabilité**
Vous pouvez retirer une permission à tout moment.

---

## Le Gouverneur — Des règles vérifiables

### Problème des LLM actuels

Les "garde-fous" des LLM actuels sont :
- Entraînés dans le modèle (RLHF) → impossible à vérifier
- Ajoutés en post-traitement → contournables
- Définis par l'entreprise → vous n'avez pas votre mot à dire

### Solution Harmonia

Un **Gouverneur** externe au modèle qui :
- Intercepte les entrées et sorties
- Applique des règles formelles vérifiables
- Peut être audité par un tiers
- Peut être personnalisé par l'utilisateur

### Exemple de règle

```
RÈGLE: protection_mineurs
SI contexte.user.age < 18
ALORS:
  - BLOQUER contenu.violence == "explicite"
  - BLOQUER contenu.adult == true
  - ALERTER si conversation.topic in ["automutilation", "suicide"]
AUDIT: obligatoire
```

Cette règle est :
- **Explicite** : on sait exactement ce qu'elle fait
- **Vérifiable** : on peut tester qu'elle fonctionne
- **Auditable** : on peut prouver qu'elle a été appliquée

---

## L'Alter Ego — Une IA qui vous connaît (avec permission)

### Concept

L'Alter Ego est une couche de personnalisation qui :
- Apprend vos préférences au fil du temps
- Adapte les réponses à votre contexte
- Mémorise ce que vous lui avez partagé

**Différence avec le modèle actuel :** Les données restent les vôtres. Elles ne servent pas à entraîner le modèle pour d'autres.

### Fonctionnement

```
[Votre question]
      ↓
[Alter Ego] → "Marie préfère des réponses concises,
               elle travaille dans l'éducation,
               elle est sensible aux questions de vie privée"
      ↓
[Prompt enrichi envoyé au LLM]
      ↓
[Réponse adaptée à vous]
```

### Garanties

- **Consentement explicite** : L'Alter Ego ne collecte rien sans votre accord
- **Transparence** : Vous pouvez voir tout ce qu'il "sait" sur vous
- **Oubli** : Vous pouvez effacer tout ou partie à tout moment
- **Localité** : Les données peuvent rester sur votre appareil

---

## Cas d'usage illustratifs

### Cas 1 : IA d'entreprise gouvernée

Une entreprise déploie un assistant IA pour ses employés.

**Sans Harmonia :**
- L'entreprise fait confiance à OpenAI
- Pas de contrôle sur ce qui est dit aux employés
- Données sensibles potentiellement exposées

**Avec Harmonia :**
- Gouverneur d'entreprise avec règles RH et légales
- Données restent sur infrastructure de l'entreprise
- Audit trail complet pour conformité

### Cas 2 : IA éducative pour enfants

Une école utilise une IA pour aider les élèves.

**Sans Harmonia :**
- Dépendance aux garde-fous de l'éditeur
- Pas de personnalisation au contexte scolaire
- Données des mineurs sur serveurs tiers

**Avec Harmonia :**
- Règles adaptées à l'âge et au programme
- Profil .life contrôlé par les parents
- Données sur infrastructure scolaire

### Cas 3 : IA de santé

Un patient utilise une IA pour comprendre ses symptômes.

**Sans Harmonia :**
- Données de santé chez un géant tech
- Risque de conseils médicaux inappropriés
- Pas de lien avec le dossier médical

**Avec Harmonia :**
- Données de santé dans un espace certifié (HDS)
- Règles strictes sur les conseils médicaux
- Intégration contrôlée avec le parcours de soin

---

## État d'avancement

**Ce qui existe (décembre 2025) :**
- Spécification conceptuelle complète
- Prototype de recherche (Harmonia Kernel)
- Publications académiques en cours

**Ce qui reste à faire :**
- Implémentation industrielle
- Standardisation des formats
- Écosystème d'outils compatibles
- Adoption par des acteurs

**Où suivre les développements :**
- GitHub : [lien à ajouter]
- Papiers : [référence académique]

---

## Pour aller plus loin

### Documentation technique

La spécification complète d'Harmonia fait l'objet de publications académiques distinctes :

**"From Rational Agents to Governed Cognitive Systems"**
- Cadre théorique complet
- Formalisation mathématique
- Validation expérimentale

### Participer

Harmonia est un projet ouvert. Vous pouvez :
- Lire et commenter les spécifications
- Contribuer au code (open source)
- Proposer des cas d'usage
- Critiquer et améliorer

**L'objectif n'est pas de vendre un produit, mais de montrer qu'une autre IA est possible.**

---

## Conclusion

Harmonia n'est pas une utopie. C'est une démonstration de faisabilité.

Elle montre que les problèmes actuels de l'IA — opacité, centralisation, perte de contrôle — ne sont pas des fatalités techniques. Ce sont des choix de conception. Et d'autres choix sont possibles.

Le jour où suffisamment de citoyens exigeront une IA gouvernable, les outils existeront pour la construire.

Ce jour dépend de vous.

---

*Cette annexe présente une vue simplifiée d'Harmonia. La documentation technique complète est disponible séparément.*
