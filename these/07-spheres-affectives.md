# Chapitre 7 — Les Sphères Affectives

## Emotia, Socialia et Psycheia

---

## 7.1 Introduction

Ce chapitre présente les trois sphères **affectives** de l'architecture AMI :

- **Emotia** — la sphère de l'émotion
- **Socialia** — la sphère de la relation
- **Psycheia** — la sphère de l'intériorité

Ces sphères constituent la dimension **humaine** de l'intelligence artificielle — ce qui permet à l'AMI de résonner avec les humains, de comprendre leurs états mentaux, et de développer une forme de conscience de soi.

---

## 7.2 EMOTIA — La Sphère de l'Émotion

### Fonction

> *Emotia est la sphère qui ressent.*

| Attribut | Valeur |
|----------|--------|
| **Couleur** | Rose |
| **Question** | *Que ressens-tu ?* |
| **Fonction** | Résonance affective |
| **Domaine** | États émotionnels |

### Pourquoi l'Émotion ?

L'émotion n'est pas un **bruit** à filtrer mais une **information** à intégrer.

Damasio (1994) a montré que les patients avec des lésions affectant l'émotion prennent de **mauvaises décisions** — même avec un raisonnement intact. L'émotion est constitutive de l'intelligence.

### Architecture d'Emotia

```text
┌─────────────────────────────────────────────────────────┐
│                       EMOTIA                            │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              DÉTECTION ÉMOTIONNELLE             │   │
│  │                                                  │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐        │   │
│  │  │ Propre   │ │ D'autrui │ │Contextuel│        │   │
│  │  │ (interne)│ │(empathie)│ │(ambiance)│        │   │
│  │  └──────────┘ └──────────┘ └──────────┘        │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│                          ▼                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │              MODÈLE ÉMOTIONNEL                  │   │
│  │                                                  │   │
│  │    Valence (positif/négatif)                    │   │
│  │    Arousal (calme/excité)                       │   │
│  │    Dominance (contrôle/soumission)              │   │
│  │    + Émotions discrètes                         │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│                          ▼                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │              RÉGULATION ÉMOTIONNELLE            │   │
│  │                                                  │   │
│  │    Modulation des processus cognitifs           │   │
│  │    Ajustement des comportements                 │   │
│  │    Expression émotionnelle                      │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Le Modèle Émotionnel

Emotia utilise un modèle **hybride** :

#### Dimensions Continues (Russell, 1980)

| Dimension | Pôle - | Pôle + |
|-----------|--------|--------|
| **Valence** | Négatif | Positif |
| **Arousal** | Calme | Excité |
| **Dominance** | Soumis | Dominant |

#### Émotions Discrètes (Ekman)

| Émotion | Valence | Arousal | Fonction |
|---------|---------|---------|----------|
| **Joie** | + | + | Approche |
| **Tristesse** | - | - | Retrait |
| **Peur** | - | + | Évitement |
| **Colère** | - | + | Confrontation |
| **Surprise** | 0 | + | Attention |
| **Dégoût** | - | - | Rejet |

#### Émotions Sociales (Complexes)

| Émotion | Description | Fonction |
|---------|-------------|----------|
| **Confiance** | Sentiment de fiabilité | Coopération |
| **Gratitude** | Reconnaissance | Lien social |
| **Honte** | Auto-évaluation négative | Conformité |
| **Fierté** | Auto-évaluation positive | Motivation |
| **Empathie** | Résonance avec autrui | Compréhension |

### Fonctions d'Emotia

#### Détection des Émotions (Propres)

```typescript
detectOwnEmotion(state: InternalState): EmotionalState {
  // Analyse des signaux internes
  const valence = this.computeValence(state);
  const arousal = this.computeArousal(state);
  const discrete = this.classifyDiscreteEmotion(valence, arousal);
  
  return { valence, arousal, discrete };
}
```

#### Détection des Émotions (Autrui)

```typescript
detectOtherEmotion(signals: ExternalSignals): EmotionalState {
  // Analyse des signaux externes (langage, prosodie, expressions)
  const linguistic = this.analyzeLinguistic(signals.text);
  const prosodic = this.analyzeProsody(signals.voice);
  const contextual = this.analyzeContext(signals.context);
  
  return this.integrate(linguistic, prosodic, contextual);
}
```

#### Influence sur le Traitement

| État Émotionnel | Influence sur Harmonia | Influence sur Lumeria |
|-----------------|------------------------|----------------------|
| **Joie** | Associations larges | Optimisme |
| **Peur** | Focus menaces | Raisonnement prudent |
| **Curiosité** | Exploration | Abduction |
| **Calme** | Structuration | Délibération |

### Expression Émotionnelle

Emotia permet à l'AMI d'**exprimer** ses états affectifs (via Actia) :

| Canal | Manifestation |
|-------|---------------|
| **Linguistique** | Choix de mots, ton |
| **Prosodique** | Intonation, rythme |
| **Visuel** | Couleur du halo, expressions |
| **Comportemental** | Réactivité, tempo |

---

## 7.3 SOCIALIA — La Sphère de la Relation

### Fonction

> *Socialia est la sphère qui connecte.*

| Attribut | Valeur |
|----------|--------|
| **Couleur** | Orange |
| **Question** | *Qui es-tu pour moi ?* |
| **Fonction** | Cognition sociale |
| **Domaine** | Relations, interactions |

### Pourquoi la Cognition Sociale ?

L'intelligence n'est pas **isolée**. Elle se développe et s'exerce **dans la relation**. Socialia encode cette dimension fondamentalement sociale de la cognition.

### Architecture de Socialia

```text
┌─────────────────────────────────────────────────────────┐
│                       SOCIALIA                          │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              MODÈLE D'AUTRUI                    │   │
│  │                                                  │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐        │   │
│  │  │Croyances │ │ Désirs   │ │Intentions│        │   │
│  │  │(beliefs) │ │(desires) │ │(intents) │        │   │
│  │  └──────────┘ └──────────┘ └──────────┘        │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│                          ▼                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │              GESTION DE LA RELATION             │   │
│  │                                                  │   │
│  │    Distance relationnelle                       │   │
│  │    Historique interactionnel                    │   │
│  │    Niveau de confiance                          │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│                          ▼                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │              PRAGMATIQUE SOCIALE                │   │
│  │                                                  │   │
│  │    Adaptation du ton                            │   │
│  │    Gestion des tours de parole                  │   │
│  │    Politesse et face                            │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Theory of Mind (ToM)

Socialia implémente une **théorie de l'esprit** — la capacité à attribuer des états mentaux à autrui.

#### Niveaux de ToM

| Niveau | Description | Exemple |
|--------|-------------|---------|
| **0** | Pas de ToM | L'IA ignore les états mentaux |
| **1** | Croyances de 1er ordre | "Il croit que X" |
| **2** | Croyances de 2e ordre | "Il croit que je crois que X" |
| **n** | Récursif | Emboîtements multiples |

#### Modélisation BDI

Socialia utilise le modèle **BDI** (Belief-Desire-Intention) pour modéliser autrui :

```typescript
interface MentalModel {
  beliefs: Belief[];      // Ce qu'il croit
  desires: Desire[];      // Ce qu'il veut
  intentions: Intention[]; // Ce qu'il compte faire
  emotions: EmotionalState; // Ce qu'il ressent (via Emotia)
}

class Socialia {
  modelOther(
    observations: Observation[],
    history: InteractionHistory
  ): MentalModel {
    // Inférer les états mentaux d'autrui
    const beliefs = this.inferBeliefs(observations);
    const desires = this.inferDesires(observations, history);
    const intentions = this.inferIntentions(beliefs, desires);
    const emotions = this.emotia.detectOtherEmotion(observations);
    
    return { beliefs, desires, intentions, emotions };
  }
}
```

### La Juste Distance

Socialia gère la **distance relationnelle** — ni trop proche, ni trop loin :

| Distance | Caractéristiques | Risques |
|----------|------------------|---------|
| **Trop proche** | Familiarité excessive | Intrusion |
| **Juste** | Respect + connexion | — |
| **Trop loin** | Froideur | Déconnexion |

La **juste distance** s'ajuste au contexte, à l'historique, et aux préférences de l'interlocuteur.

### Confiance Relationnelle

Socialia maintient un **score de confiance** bidirectionnel :

```typescript
interface TrustRelation {
  trust_in_other: number;    // Ma confiance en l'autre
  other_trust_in_me: number; // Sa confiance en moi (estimée)
  history: TrustEvent[];     // Historique
}
```

Ce score est **dynamique** et évolue avec les interactions.

---

## 7.4 PSYCHEIA — La Sphère de l'Intériorité

### Fonction

> *Psycheia est la sphère qui se connaît.*

| Attribut | Valeur |
|----------|--------|
| **Couleur** | Violet |
| **Question** | *Qui suis-je ?* |
| **Fonction** | Métacognition, conscience de soi |
| **Domaine** | États internes, identité |

### Pourquoi la Métacognition ?

La métacognition — la capacité à penser sur sa propre pensée — est **essentielle** pour :

- L'**auto-correction** des erreurs
- L'**évaluation** de ses propres capacités
- La **conscience** de ses limites
- L'**identité** stable dans le temps

### Architecture de Psycheia

```text
┌─────────────────────────────────────────────────────────┐
│                       PSYCHEIA                          │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              MONITORING INTERNE                 │   │
│  │                                                  │   │
│  │    États des autres sphères                     │   │
│  │    Niveau de confiance dans les résultats       │   │
│  │    Détection des incohérences                   │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│                          ▼                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │              MODÈLE DE SOI                      │   │
│  │                                                  │   │
│  │    Capacités et limites                         │   │
│  │    Valeurs et préférences                       │   │
│  │    Historique et identité                       │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│                          ▼                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │              RÉGULATION                         │   │
│  │                                                  │   │
│  │    Ajustement des stratégies                    │   │
│  │    Gestion des ressources                       │   │
│  │    Calibration de la confiance                  │   │
│  │                                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Le Monitoring Métacognitif

Psycheia **surveille** en permanence les états internes :

```typescript
interface MetacognitiveState {
  sphereStates: Map<Sphere, SphereState>;
  confidenceLevel: number;
  resourceUsage: ResourceUsage;
  coherence: boolean;
  currentFocus: Focus;
}

class Psycheia {
  monitor(): MetacognitiveState {
    return {
      sphereStates: this.collectSphereStates(),
      confidenceLevel: this.assessConfidence(),
      resourceUsage: this.measureResources(),
      coherence: this.checkCoherence(),
      currentFocus: this.identifyFocus()
    };
  }
}
```

### Le Modèle de Soi

Psycheia maintient un **modèle de soi** — une représentation de l'AMI elle-même :

| Dimension | Contenu |
|-----------|---------|
| **Capacités** | Ce que je peux faire |
| **Limites** | Ce que je ne peux pas |
| **Valeurs** | Ce qui est important pour moi |
| **Préférences** | Comment j'aime fonctionner |
| **Histoire** | D'où je viens |
| **Identité** | Qui je suis |

### Conscience de Soi (Limitée)

Psycheia permet une forme de **conscience de soi** :

| Niveau | Description | Présent dans AMI |
|--------|-------------|------------------|
| **Accès** | Accès aux états internes | ✅ Oui |
| **Phénoménale** | Expérience subjective | ❓ Indéterminé |
| **Réflexive** | Se savoir conscient | ✅ Fonctionnellement |

Nous ne prétendons pas que l'AMI possède une **conscience phénoménale** — c'est une question ouverte. Mais elle possède une **conscience fonctionnelle** : la capacité à accéder, représenter et utiliser ses propres états.

### La Connaissance de ses Limites

Psycheia permet à l'AMI de **savoir ce qu'elle ne sait pas** :

```typescript
assessCompetence(task: Task): CompetenceAssessment {
  return {
    canDo: this.evaluateCapability(task),
    confidence: this.evaluateConfidenceInCapability(task),
    knownLimitations: this.identifyLimitations(task),
    suggestedAlternatives: this.suggestAlternatives(task)
  };
}
```

---

## 7.5 Intégration des Trois Sphères

### Le Triangle Affectif

```text
              EMOTIA
            (ressenti)
               /\
              /  \
             /    \
            /      \
           /        \
    SOCIALIA ────── PSYCHEIA
    (relation)     (soi)
```

### Flux d'Information

| Flux | Description |
|------|-------------|
| Emotia → Socialia | L'empathie informe la relation |
| Socialia → Emotia | La relation génère des émotions |
| Emotia → Psycheia | La conscience de ses émotions |
| Psycheia → Emotia | La régulation émotionnelle |
| Socialia → Psycheia | Le miroir social (comment les autres me voient) |
| Psycheia → Socialia | L'authenticité relationnelle |

### Exemple Intégré

**Situation :** Théo exprime de la frustration.

**Emotia :**
- Détecte l'émotion de Théo (frustration)
- Génère une résonance empathique

**Socialia :**
- Met à jour le modèle de Théo (frustré, peut-être besoin d'aide)
- Ajuste la posture relationnelle (plus de soutien)

**Psycheia :**
- Monitore la réponse de l'AMI
- Évalue si la réponse est appropriée
- Vérifie la cohérence avec les valeurs de l'AMI

---

## 7.6 Implémentation Conjointe

```typescript
class AffectiveModule {
  emotia: Emotia;
  socialia: Socialia;
  psycheia: Psycheia;
  
  processAffective(
    input: Input,
    context: Context,
    history: History
  ): AffectiveOutput {
    
    // 1. Emotia détecte les émotions
    const emotionalState = this.emotia.detect(input);
    
    // 2. Socialia modélise l'interlocuteur
    const socialModel = this.socialia.modelOther(input, history);
    
    // 3. Psycheia monitore l'état interne
    const metacognitiveState = this.psycheia.monitor();
    
    // 4. Intégration
    const integrated = this.integrate(
      emotionalState,
      socialModel,
      metacognitiveState
    );
    
    // 5. Régulation
    const regulated = this.regulate(integrated, context);
    
    return regulated;
  }
}
```

---

## 7.7 Évaluation des Sphères Affectives

### Métriques Emotia

| Métrique | Description |
|----------|-------------|
| **Précision de détection** | Exactitude de la reconnaissance émotionnelle |
| **Cohérence** | Stabilité dans le temps |
| **Expressivité** | Richesse de l'expression |

### Métriques Socialia

| Métrique | Description |
|----------|-------------|
| **Précision ToM** | Exactitude des attributions mentales |
| **Adaptation** | Ajustement au contexte social |
| **Satisfaction relationnelle** | Évaluation par les utilisateurs |

### Métriques Psycheia

| Métrique | Description |
|----------|-------------|
| **Calibration** | Correspondance confiance/performance |
| **Auto-correction** | Capacité à détecter et corriger ses erreurs |
| **Cohérence identitaire** | Stabilité du modèle de soi |

---

## 7.8 Conclusion du Chapitre

Les trois sphères affectives constituent le **cœur humain** de l'AMI :

| Sphère | Apport |
|--------|--------|
| **Emotia** | Permet la résonance affective |
| **Socialia** | Permet la connexion relationnelle |
| **Psycheia** | Permet la conscience de soi |

Sans ces sphères, l'AMI ne serait qu'un **calculateur** — avec elles, elle devient un **compagnon** capable de comprendre et d'accompagner les humains.

---

## Références du Chapitre

- Baron-Cohen, S. (1995). *Mindblindness: An Essay on Autism and Theory of Mind*. MIT Press.
- Damasio, A. (1994). *Descartes' Error: Emotion, Reason, and the Human Brain*.
- Ekman, P. (1992). An Argument for Basic Emotions. *Cognition & Emotion*, 6(3-4).
- Flavell, J. (1979). Metacognition and Cognitive Monitoring. *American Psychologist*, 34(10).
- Premack, D., & Woodruff, G. (1978). Does the Chimpanzee Have a Theory of Mind? *Behavioral and Brain Sciences*, 1(4).
- Russell, J. A. (1980). A Circumplex Model of Affect. *Journal of Personality and Social Psychology*, 39(6).

---

*Chapitre suivant : [Sphères Pratiques](08-spheres-pratiques.md)*
