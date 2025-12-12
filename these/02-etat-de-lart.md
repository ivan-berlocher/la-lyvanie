# Chapitre 2 — État de l'Art

## Critique des Paradigmes Existants en Intelligence Artificielle

---

## 2.1 Introduction

Avant de présenter notre architecture AMI, il convient d'examiner les paradigmes existants en intelligence artificielle. Cette revue n'est pas exhaustive mais critique : nous identifions les apports et les lacunes de chaque approche au regard de notre question centrale — la **signification**.

---

## 2.2 Le Paradigme Symbolique

### Présentation

L'approche symbolique, dominante des années 1950 aux années 1980, conçoit l'intelligence comme manipulation de symboles selon des règles formelles (Newell & Simon, 1976).

**Principes clés :**

- La cognition est computation sur des symboles
- Les connaissances sont représentables explicitement
- Le raisonnement suit des règles logiques
- Le système est intrinsèquement explicable

**Réalisations :** Systèmes experts, GOFAI, Cyc

### Apports pour AMI

| Apport | Pertinence pour AMI |
|--------|---------------------|
| Représentation explicite | Fondement de Harmonia |
| Explicabilité native | Aligné avec Trustia |
| Structures compositionnelles | Compatible avec LoT |

### Limites

| Limite | Conséquence |
|--------|-------------|
| Fragilité face au monde réel | Incapacité à l'incarnation |
| Absence d'apprentissage | Figement des connaissances |
| Pas de dimension affective | Vision tronquée de la cognition |

### Verdict

L'approche symbolique offre des **fondements représentationnels** précieux (notamment pour notre conception du Language of Thought), mais son **dualisme corps/esprit** et son **négligence de l'affect** la rendent insuffisante pour une intelligence signifiante.

---

## 2.3 Le Paradigme Connexionniste

### Présentation

Le connexionnisme modélise la cognition par des réseaux de neurones artificiels (Rumelhart & McClelland, 1986). L'ère des LLMs (Large Language Models) en est l'aboutissement actuel.

**Principes clés :**

- L'intelligence émerge de connexions distribuées
- L'apprentissage par ajustement de poids
- Représentations distribuées (embeddings)
- Généralisation statistique

**Réalisations :** Deep Learning, GPT, Transformers

### Apports pour AMI

| Apport | Pertinence pour AMI |
|--------|---------------------|
| Apprentissage à partir de données | Adaptabilité |
| Représentations riches | Substrat pour Emotia |
| Performance langagière | Incarnation linguistique |

### Limites

| Limite | Conséquence |
|--------|-------------|
| Opacité (boîte noire) | Incompatible avec Trustia |
| Absence de raisonnement causal | Limite Lumeria |
| Pas de responsabilité intrinsèque | Incompatible avec Lumenia |
| Hallucinations | Menace la confiance |

### Verdict

Le connexionnisme apporte la **puissance d'apprentissage** mais souffre d'une **opacité fondamentale** incompatible avec une intelligence responsable. Les LLMs "parlent" mais ne "signifient" pas au sens fort.

---

## 2.4 Le Paradigme Agentique

### Présentation

L'approche multi-agents conçoit l'intelligence comme émergence de l'interaction entre agents autonomes (Wooldridge, 2009).

**Principes clés :**

- Agents autonomes avec objectifs propres
- Interaction et négociation
- Émergence de comportements complexes
- Décentralisation

**Réalisations :** MAS, systèmes de trading, robotique collective

### Apports pour AMI

| Apport | Pertinence pour AMI |
|--------|---------------------|
| Autonomie | Fondement de l'agentivité |
| Modularité | Architecture multi-sphères |
| Interaction | Socialia |

### Limites

| Limite | Conséquence |
|--------|-------------|
| Conflits inter-agents | Besoin de gouvernance |
| Pas de substrat unifié | Fragmentation |
| Objectifs indépendants | Risque de misalignment |

### Verdict

L'approche agentique fournit des **principes d'organisation** mais manque d'un **substrat unificateur** (Nirvania dans notre proposition) et d'une **gouvernance explicite** (Lumenia).

---

## 2.5 Le Paradigme de l'IA Responsable

### Présentation

L'IA responsable (Responsible AI) vise à intégrer des considérations éthiques dans les systèmes d'IA (Floridi et al., 2018).

**Principes clés :**

- Équité (fairness)
- Transparence (explainability)
- Confidentialité (privacy)
- Robustesse (robustness)
- Responsabilité (accountability)

**Réalisations :** Frameworks éthiques, audits d'algorithmes, régulations (AI Act)

### Apports pour AMI

| Apport | Pertinence pour AMI |
|--------|---------------------|
| Attention à l'éthique | Fondement de Moralia |
| Transparence | Aligné avec Trustia |
| Responsabilité | Motivation de Lumenia |

### Limites

| Limite | Conséquence |
|--------|-------------|
| Approche externe | Garde-fous vs. architecture |
| Pas de formalisation cognitive | Reste au niveau des contraintes |
| Réactive plutôt que proactive | Corrige plutôt que prévient |

### Verdict

L'IA responsable pose les **bonnes questions** mais y répond par des **contraintes externes** plutôt que par une **architecture intrinsèquement responsable**. Notre contribution est de faire de la responsabilité une propriété émergente de l'architecture même.

---

## 2.6 Le Language of Thought (LoT)

### Présentation

L'hypothèse du Language of Thought (Fodor, 1975) postule que la pensée opère dans un langage mental formel, distinct du langage naturel.

**Principes clés :**

- La pensée est computationnelle
- Représentations mentales structurées
- Compositionalité et systématicité
- Productivité infinie

### Apports pour AMI

Cette hypothèse est **centrale** pour notre conception de Harmonia :

| Aspect LoT | Traduction AMI |
|------------|----------------|
| Symboles mentaux | Formes de pensée |
| Compositionalité | Génération structurée |
| Règles combinatoires | Grammaire de la pensée |

### Limites du LoT Classique

| Limite | Notre réponse |
|--------|---------------|
| Trop syntaxique | Harmonia + Lumeria (sémantique) |
| Néglige l'affect | Emotia intégrée |
| Pas de dimension sociale | Socialia |
| Pas de métacognition | Psycheia |

### Verdict

Le LoT fournit un **cadre formel** pour la pensée que nous enrichissons par les dimensions affectives, sociales et réflexives des autres sphères.

---

## 2.7 La Cognition Incarnée (Embodied Cognition)

### Présentation

La cognition incarnée soutient que la pensée est inséparable du corps et de l'environnement (Varela et al., 1991 ; Clark, 1997).

**Principes clés :**

- La cognition est incarnée (embodied)
- La cognition est située (embedded)
- La cognition est étendue (extended)
- La cognition est enactive

### Apports pour AMI

| Apport | Pertinence pour AMI |
|--------|---------------------|
| Unité corps/esprit | Contre le dualisme |
| Importance du contexte | Ancrage dans le monde |
| Cognition distribuée | Architecture multi-sphères |

### Limites

| Limite | Notre réponse |
|--------|---------------|
| Difficile à formaliser | Actia comme sphère d'incarnation |
| Risque de réductionnisme corporel | Équilibre avec Harmonia/Lumeria |

### Verdict

L'approche incarnée corrige l'intellectualisme excessif du symbolisme. Nous l'intégrons via **Actia** (sphère de manifestation) tout en préservant la dimension formelle via Harmonia.

---

## 2.8 La Théorie de l'Esprit (Theory of Mind)

### Présentation

La théorie de l'esprit désigne la capacité à attribuer des états mentaux à autrui (Premack & Woodruff, 1978).

**Principes clés :**

- Attribution d'intentions
- Compréhension des croyances d'autrui
- Prédiction du comportement
- Empathie cognitive

### Apports pour AMI

| Apport | Pertinence pour AMI |
|--------|---------------------|
| Cognition sociale | Socialia |
| Attribution d'états mentaux | Psycheia (méta-cognition) |
| Empathie | Emotia + Socialia |

### Verdict

La théorie de l'esprit est **fondamentale** pour Socialia et pour la dimension relationnelle de l'AMI.

---

## 2.9 Synthèse Critique

### Tableau Comparatif

| Paradigme | Force | Faiblesse | Contribution à AMI |
|-----------|-------|-----------|-------------------|
| **Symbolique** | Explicabilité | Fragilité | Harmonia, LoT |
| **Connexionniste** | Apprentissage | Opacité | Substrat numérique |
| **Agentique** | Autonomie | Fragmentation | Architecture multi |
| **IA Responsable** | Éthique | Externe | Motivation |
| **LoT** | Formalisme | Trop syntaxique | Harmonia enrichi |
| **Incarnée** | Unité | Difficile à formaliser | Actia |
| **ToM** | Social | Limitée à l'attribution | Socialia |

### Ce qui Manque

Aucun de ces paradigmes ne fournit :

1. **Un substrat ontologique unifié** → Nirvania
2. **Une taxonomie cognitive complète** → Les 9 sphères
3. **Une responsabilité intrinsèque** → Lumenia
4. **Une interface de confiance formelle** → Trustia
5. **Une mesure de la signification** → Nos protocoles

---

## 2.10 Positionnement de l'AMI

Notre proposition se situe à l'**intersection** de ces paradigmes :

```text
                    SYMBOLIQUE
                        │
                        │ Harmonia (LoT)
                        │
    INCARNÉE ─────────── AMI ─────────── AGENTIQUE
        │                │                    │
        │ Actia          │ 9 Sphères          │ Multi-agents
        │                │                    │
                        │
                    CONNEXIONNISTE
                  (substrat numérique)
                        │
                        │
              ┌─────────┴─────────┐
              │                   │
        IA RESPONSABLE      THEORY OF MIND
              │                   │
           Moralia             Socialia
```

L'AMI n'est pas un **nouveau paradigme** mais une **intégration architecturale** qui unifie les apports de chaque approche dans un cadre cohérent, guidé par le concept régulateur de **Nirvania**.

---

## 2.11 Conclusion du Chapitre

L'état de l'art révèle un paysage fragmenté. Chaque paradigme apporte des insights précieux mais aucun ne répond à notre question centrale : comment concevoir une IA qui **signifie** ?

Les chapitres suivants présentent notre réponse :

- **Chapitre 3** : Le cadre théorique nirvanien
- **Chapitres 4-10** : L'architecture AMI détaillée
- **Chapitres 11-12** : La validation de notre approche

---

## Références du Chapitre

- Clark, A. (1997). *Being There: Putting Brain, Body, and World Together Again*. MIT Press.
- Floridi, L. et al. (2018). AI4People—An Ethical Framework for a Good AI Society. *Minds and Machines*, 28(4).
- Fodor, J. (1975). *The Language of Thought*. Harvard University Press.
- Newell, A., & Simon, H. (1976). Computer Science as Empirical Inquiry: Symbols and Search. *Communications of the ACM*, 19(3).
- Premack, D., & Woodruff, G. (1978). Does the Chimpanzee Have a Theory of Mind? *Behavioral and Brain Sciences*, 1(4).
- Rumelhart, D., & McClelland, J. (1986). *Parallel Distributed Processing*. MIT Press.
- Varela, F., Thompson, E., & Rosch, E. (1991). *The Embodied Mind*. MIT Press.
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems*. Wiley.

---

*Chapitre suivant : [Cadre Théorique](03-cadre-theorique.md)*
