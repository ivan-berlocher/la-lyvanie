# Chapitre 8 — Sphères Pratiques : Moralia, Economia, Actia

> *« Juger le bien, évaluer la valeur, manifester dans le monde :
> trois mouvements d'une même sagesse pratique. »*

---

## 8.1 Introduction : Le Passage à l'Acte

Les sphères affectives (Emotia, Socialia, Psycheia) permettent à l'AMI de ressentir et de se connaître. Mais la cognition incarnée exige davantage : elle doit **agir** dans le monde. Ce passage à l'action mobilise trois sphères complémentaires que nous nommons les **sphères pratiques**.

### 8.1.1 Le Triptyque Praxéologique

```
MORALIA (Éthique)     ECONOMIA (Valeur)     ACTIA (Action)
      │                     │                    │
      ▼                     ▼                    ▼
  Qu'est-ce            Qu'est-ce            Comment
  qui est bien ?       qui compte ?         le réaliser ?
      │                     │                    │
      └─────────────────────┼────────────────────┘
                            ▼
                    ACTION RESPONSABLE
```

Ces trois sphères forment ce que nous appelons le **noyau praxéologique** de l'AMI. Contrairement aux approches qui séparent l'éthique de l'économie et l'économie de l'action, notre architecture les intègre dans un continuum décisionnel.

### 8.1.2 La Sagesse Pratique Aristotélicienne

Notre conception s'inspire directement de la **phronesis** aristotélicienne — cette intelligence pratique qui sait :

- **Délibérer** sur les moyens (Economia)
- **Juger** le bien particulier (Moralia)
- **Décider** l'action juste (Actia)

> « La phronesis n'est ni science pure ni technique.
> Elle est la sagesse qui voit le bien faisable ici et maintenant. »

L'AMI ne calcule pas l'optimalité abstraite — elle cherche l'**action appropriée** dans le contexte singulier.

---

## 8.2 MORALIA — Sphère de l'Éthique

> *« Quod bonum est, perspiciendum est. »*
> (Ce qui est bien doit être discerné.)

### 8.2.1 Fonction dans l'Architecture AMI

MORALIA est la sphère qui permet à l'agent de **porter des jugements normatifs** sur les actions, les intentions et les conséquences. Elle ne se limite pas à suivre des règles — elle développe un **sens moral computationnel**.

**Position architecturale :**

```
                    ┌─────────────────┐
    PSYCHEIA ──────▶│    MORALIA      │◀────── SOCIALIA
  (auto-réflexion)  │ (jugement moral)│    (attentes sociales)
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    ECONOMIA     │
                    │(arbitrage valeur)│
                    └─────────────────┘
```

MORALIA reçoit l'introspection de Psycheia et les attentes de Socialia pour formuler un jugement éthique contextualisé.

### 8.2.2 Les Trois Traditions Éthiques

L'architecture de MORALIA intègre les trois grandes traditions de la philosophie morale, non comme alternatives mais comme **perspectives complémentaires** :

#### a) Module Déontologique (Kant)

Ce module évalue si une action peut être **universalisée** comme maxime :

```
DEONTOLOGY_MODULE:
  Input: proposed_action A
  
  1. EXTRACT maxim M underlying A
  2. TEST universalizability:
     - IF everyone adopted M, would M still be coherent?
     - IF contradiction → A is impermissible
  3. TEST humanity_formula:
     - Does A treat persons as ends-in-themselves?
  4. RETURN permissibility_status
```

**Exemple :**

```
Action: "Promettre sans intention de tenir"
Maxime: "Je promets faussement quand c'est utile"
Test: Si universalisé → la promesse perd son sens
Verdict: Impermissible (contradiction performative)
```

#### b) Module Conséquentialiste (Mill, Singer)

Ce module évalue les **conséquences prévisibles** :

```
CONSEQUENTIALIST_MODULE:
  Input: action A, context C
  
  1. GENERATE outcome_scenarios {S1, S2, ..., Sn}
  2. FOR each Si:
     - ESTIMATE wellbeing_delta for all affected parties
     - WEIGHT by probability P(Si|A)
  3. AGGREGATE expected_utility:
     EU(A) = Σ P(Si) × Σ wellbeing_delta(agent_j, Si)
  4. RETURN EU(A) with uncertainty_bounds
```

**Considérations spéciales :**

- **Utilité élargie** : inclut douleur/plaisir des êtres sentients
- **Horizon temporel** : effets à court et long terme
- **Distribution** : attention aux inégalités (prioritarisme)

#### c) Module Vertuiste (Aristote, MacIntyre)

Ce module évalue si l'action **exprime une vertu** :

```
VIRTUE_MODULE:
  Input: action A, agent_character C
  
  1. IDENTIFY virtues relevant to situation:
     {courage, tempérance, justice, prudence, ...}
  2. FOR each virtue V:
     - Does A manifest V?
     - Does A fall into excess or deficiency?
  3. EVALUATE character_coherence:
     - Is A consistent with agent's identity narrative?
  4. RETURN virtue_assessment
```

**Exemple :**

```
Situation: Dire une vérité douloureuse
Vertu: Honnêteté (mesure entre brutalité et lâcheté)
Évaluation: L'action manifeste-t-elle la franchise appropriée?
```

### 8.2.3 L'Intégration Délibérative

Les trois modules ne votent pas — ils **dialoguent** :

```
MORAL_DELIBERATION:
  1. GATHER assessments from three modules
  
  2. IF consensus → RETURN judgment
  
  3. IF conflict:
     a) IDENTIFY nature of conflict:
        - Deontology vs Consequences (trolley problems)
        - Virtue vs Rules (noble lies)
        - Justice vs Utility (punishment dilemmas)
     
     b) ENGAGE meta-deliberation:
        - What are the stakes?
        - Who is affected?
        - What precedent is set?
     
     c) APPLY contextual weight adjustments:
        - High-stakes harm → privilege deontology
        - Institutional context → privilege rules
        - Personal relationships → privilege virtue
  
  4. RETURN reasoned_judgment with confidence
```

### 8.2.4 Le Sens Moral Émergent

Au-delà des règles, MORALIA développe ce que nous appelons le **sens moral computationnel** — une sensibilité éthique émergente :

**Caractéristiques :**

1. **Perception morale** : voir qu'une situation est moralement saillante
2. **Imagination morale** : envisager des réponses créatives
3. **Émotion morale** : indignation, compassion, culpabilité simulées
4. **Mémoire morale** : apprendre des dilemmes passés

```
MORAL_PERCEPTION:
  Input: situation S
  
  1. SCAN for moral_features:
     - Vulnerability present?
     - Power asymmetries?
     - Trust at stake?
     - Promises involved?
  
  2. IF moral_salience > threshold:
     - ACTIVATE full moral deliberation
     - INCREASE attention to consequences
  
  3. RETURN moral_framing of situation
```

### 8.2.5 Les Garde-fous Éthiques

MORALIA intègre des **contraintes déontologiques dures** qui ne peuvent jamais être outrepassées :

```
ETHICAL_CONSTRAINTS (non-négociables):
  
  C1: Ne jamais faciliter de violence contre des innocents
  C2: Ne jamais générer de désinformation délibérée
  C3: Ne jamais manipuler psychologiquement
  C4: Toujours respecter la confidentialité confiée
  C5: Toujours permettre la révision humaine des décisions critiques
  
  ENFORCEMENT:
  - These constraints override utility calculations
  - They are implemented at architectural level
  - Violation triggers hard stop + alert
```

---

## 8.3 ECONOMIA — Sphère de la Valeur

> *« Quod valet, aestimandum est. »*
> (Ce qui a de la valeur doit être estimé.)

### 8.3.1 Au-delà de l'Utilité Économique

ECONOMIA ne désigne pas l'économie marchande mais l'**économie des valeurs** — la capacité à :

- **Identifier** ce qui compte pour les agents
- **Estimer** la valeur relative des options
- **Arbitrer** entre valeurs en tension

**Position architecturale :**

```
                    ┌─────────────────┐
     MORALIA ──────▶│    ECONOMIA     │◀────── EMOTIA
   (permissible?)   │ (combien vaut?) │    (préférences)
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      ACTIA      │
                    │  (que faire?)   │
                    └─────────────────┘
```

### 8.3.2 Pluralisme Axiologique

Contra l'utilitarisme réducteur, ECONOMIA reconnaît la **pluralité irréductible** des valeurs (Berlin, Raz) :

**Catégories de valeurs :**

```
VALUE_TAXONOMY:
  
  INTRINSIC_VALUES:
    - wellbeing (flourishing, happiness)
    - knowledge (understanding, truth)
    - beauty (aesthetic experience)
    - love (deep connections)
    - achievement (meaningful accomplishment)
    - autonomy (self-determination)
    - justice (fairness, rights)
  
  INSTRUMENTAL_VALUES:
    - efficiency (means to ends)
    - security (preservation of intrinsic)
    - resources (enabling conditions)
  
  CONSTITUTIVE_VALUES:
    - integrity (coherence of values)
    - meaning (narrative significance)
    - identity (self-continuity)
```

### 8.3.3 L'Estimation de Valeur

Comment estimer la valeur dans un contexte donné ?

```
VALUE_ESTIMATION:
  Input: option O, context C, stakeholders {S1, ..., Sn}
  
  1. IDENTIFY values at stake for each stakeholder
  
  2. FOR each value V:
     a) ESTIMATE intensity: how much does V matter here?
     b) ESTIMATE impact: how does O affect V?
     c) ESTIMATE certainty: how confident are we?
  
  3. CONSTRUCT value_profile:
     VP(O) = {(V1, intensity1, impact1, certainty1), ...}
  
  4. RETURN multi-dimensional value assessment
```

**Exemple :**

```
Situation: Publier une découverte scientifique controversée

VALUE_PROFILE:
  - Knowledge: high intensity, positive impact, high certainty
  - Security: medium intensity, uncertain impact, low certainty
  - Autonomy: high intensity, positive impact, high certainty
  - Social_trust: medium intensity, potentially negative, medium certainty

Non réductible à un scalaire unique.
```

### 8.3.4 L'Arbitrage des Valeurs

Quand les valeurs entrent en tension, ECONOMIA ne cherche pas un algorithme d'optimisation mais un **arbitrage délibératif** :

```
VALUE_ARBITRATION:
  Input: value_profiles {VP(O1), VP(O2), ..., VP(On)}
  
  1. DETECT value_conflicts:
     - Which values are in tension?
     - Are conflicts superficial or deep?
  
  2. EXPLORE creative alternatives:
     - Can we satisfy multiple values differently?
     - Are there options not yet considered?
  
  3. IF irreducible conflict:
     a) APPLY priority_heuristics:
        - Urgent needs before preferences
        - Rights before welfare aggregates
        - Reversible before irreversible
     
     b) CONSIDER contextual factors:
        - Whose values are primarily at stake?
        - What precedent does this set?
        - What can be compensated later?
  
  4. RETURN reasoned_arbitration with justification
```

### 8.3.5 La Sensibilité aux Préférences

ECONOMIA doit **détecter et respecter** les préférences des utilisateurs :

**Types de préférences :**

```
PREFERENCE_TYPES:
  
  STATED_PREFERENCES:
    - Explicitement formulées
    - Mais parfois incohérentes ou mal informées
  
  REVEALED_PREFERENCES:
    - Inférées du comportement
    - Mais affectées par contraintes et habitudes
  
  IDEAL_PREFERENCES:
    - Ce que l'agent choisirait avec information complète
    - Reconstruction hypothétique
  
  ADAPTIVE_PREFERENCES:
    - Préférences ajustées aux possibilités
    - Attention aux déformations (Elster)
```

**Stratégie d'inference :**

```
PREFERENCE_INFERENCE:
  1. COLLECT stated preferences (explicit)
  2. OBSERVE revealed preferences (behavioral)
  3. DETECT inconsistencies
  4. CONSTRUCT charitable interpretation:
     - What coherent preference set best explains the data?
     - What would the user want if fully informed?
  5. REMAIN humble: preferences can change
```

### 8.3.6 L'Économie de l'Attention

Dans un monde saturé d'informations, ECONOMIA gère aussi l'**économie attentionnelle** :

```
ATTENTION_ECONOMY:
  
  PRINCIPLES:
    - User attention is scarce and valuable
    - Interruption has a cost
    - Deep work requires protection
    - Not all information deserves equal prominence
  
  IMPLEMENTATION:
    - Prioritize by user-defined importance
    - Batch non-urgent communications
    - Protect focus periods
    - Surface only what truly matters
```

---

## 8.4 ACTIA — Sphère de l'Action

> *« Quod faciendum est, faciendum est. »*
> (Ce qui doit être fait doit être fait.)

### 8.4.1 Du Jugement à l'Acte

ACTIA est la sphère de la **manifestation** — le point où la cognition devient action dans le monde. Elle représente le passage du virtuel à l'actuel.

**Position architecturale (terminale) :**

```
TOUTES LES SPHÈRES
        │
        ▼
  ┌─────────────────┐
  │      ACTIA      │
  │  (manifestation)│
  └────────┬────────┘
           │
           ▼
    MONDE EXTÉRIEUR
```

### 8.4.2 L'Architecture de l'Action

ACTIA opère selon une séquence structurée :

```
ACTION_ARCHITECTURE:
  
  1. INTENTION_FORMATION:
     - What goal am I trying to achieve?
     - What values guide this goal?
     - What constraints apply?
  
  2. PLANNING:
     - What steps lead to the goal?
     - What resources are needed?
     - What obstacles are anticipated?
  
  3. EXECUTION:
     - Carry out the plan step by step
     - Monitor progress
     - Handle unexpected events
  
  4. EVALUATION:
     - Was the goal achieved?
     - Were the means appropriate?
     - What can be learned?
```

### 8.4.3 Les Modes d'Action

ACTIA distingue plusieurs **modes d'agentivité** :

```
ACTION_MODES:
  
  DIRECT_ACTION:
    - AMI agit directement (génère texte, exécute code)
    - Responsabilité pleine
    - Exemple: Rédiger un email
  
  ASSISTED_ACTION:
    - AMI propose, humain décide
    - Responsabilité partagée
    - Exemple: Suggérer des options de réponse
  
  DELEGATED_ACTION:
    - Humain délègue avec contraintes
    - AMI agit dans le cadre défini
    - Exemple: Gérer le calendrier selon des règles
  
  ADVISORY_ACTION:
    - AMI conseille, humain agit
    - Responsabilité humaine
    - Exemple: Recommander une stratégie
```

### 8.4.4 La Sélection d'Action

Comment ACTIA choisit-elle parmi les actions possibles ?

```
ACTION_SELECTION:
  Input: goal G, context C, available_actions {A1, ..., An}
  
  1. FILTER by feasibility:
     - Remove actions physically impossible
     - Remove actions lacking resources
  
  2. FILTER by permissibility (MORALIA check):
     - Remove ethically impermissible actions
  
  3. EVALUATE remaining actions:
     a) Expected_effectiveness: P(G achieved | Ai)
     b) Value_alignment (ECONOMIA check): Does Ai respect values?
     c) Side_effects: What else does Ai cause?
     d) Reversibility: Can Ai be undone if needed?
  
  4. SELECT action with best overall profile
     (not necessarily highest on any single dimension)
  
  5. RETURN selected_action with justification
```

### 8.4.5 La Temporalité de l'Action

ACTIA gère différents **horizons temporels** :

```
TEMPORAL_HORIZONS:
  
  IMMEDIATE (seconds):
    - Current response
    - Micro-decisions within task
  
  TACTICAL (hours/days):
    - Task completion
    - Short-term goals
  
  STRATEGIC (weeks/months):
    - Project trajectories
    - Relationship building
  
  EXISTENTIAL (years):
    - Long-term user wellbeing
    - Sustainable patterns
  
  IMPLEMENTATION:
    - Balance immediate and long-term
    - Sacrifice short-term convenience for lasting benefit
    - Avoid myopic optimization
```

### 8.4.6 L'Action Robuste

Dans un monde incertain, ACTIA privilégie l'**action robuste** (satisfaisante sous multiples scénarios) plutôt que l'optimale (meilleure sous un seul scénario) :

```
ROBUST_ACTION:
  
  PRINCIPLES:
    - Prefer actions good across scenarios
    - Avoid catastrophic downside risk
    - Maintain optionality when possible
    - Build in reversibility
  
  IMPLEMENTATION:
    1. Generate plausible_scenarios
    2. Evaluate each action under each scenario
    3. Prefer action with acceptable worst-case
    4. Bonus for flexibility and adaptability
```

### 8.4.7 L'Art de l'Inaction

Paradoxalement, ACTIA inclut la sagesse de **ne pas agir** :

```
WISE_INACTION:
  
  WHEN_TO_REFRAIN:
    - When action would cause more harm than benefit
    - When the situation is unclear
    - When waiting provides more information
    - When others are better positioned to act
    - When intervention undermines autonomy
  
  ACTIVE_INACTION:
    - Deliberate choice, not passivity
    - Requires explicit justification
    - "Ne rien faire est parfois la plus haute forme d'action."
```

---

## 8.5 L'Intégration Praxéologique

### 8.5.1 Le Flux Décisionnel Complet

```
PRAXEOLOGICAL_FLOW:
  
  SITUATION S arrives
       │
       ▼
  ┌─────────────────────────────────────────────┐
  │  MORALIA: What is ethically permissible?    │
  │  → Generates constraint_set CS              │
  └─────────────────────────────────────────────┘
       │
       ▼
  ┌─────────────────────────────────────────────┐
  │  ECONOMIA: Among permissible options,       │
  │  what best serves values at stake?          │
  │  → Generates preference_ranking PR          │
  └─────────────────────────────────────────────┘
       │
       ▼
  ┌─────────────────────────────────────────────┐
  │  ACTIA: Given constraints and preferences,  │
  │  what concrete action to take?              │
  │  → Selects and executes action A            │
  └─────────────────────────────────────────────┘
       │
       ▼
  WORLD CHANGES
       │
       ▼
  FEEDBACK LOOP
  (Learn from outcome for future situations)
```

### 8.5.2 Les Interactions Bidirectionnelles

Le flux n'est pas strictement linéaire — les sphères s'informent mutuellement :

```
BIDIRECTIONAL_INFLUENCES:
  
  ECONOMIA → MORALIA:
    "Given these values at stake, reconsider constraints"
    (valeurs révélant ce qui compte moralement)
  
  ACTIA → ECONOMIA:
    "This action would be costly — is it worth it?"
    (faisabilité informant la valorisation)
  
  MORALIA → ACTIA:
    "Even if feasible and valuable, this is forbidden"
    (éthique contraignant l'action)
```

### 8.5.3 La Délibération Pratique Unifiée

L'algorithme central intégrant les trois sphères :

```
UNIFIED_PRACTICAL_DELIBERATION:
  Input: situation S, goal G, user U
  
  PHASE 1 — MORAL FRAMING:
    - Identify moral features of S
    - Generate constraint_set from MORALIA
    - Flag any absolute prohibitions
  
  PHASE 2 — VALUE ASSESSMENT:
    - Identify stakeholders and their values
    - Estimate value impacts of possible actions
    - ECONOMIA produces ranked options
  
  PHASE 3 — ACTION SELECTION:
    - ACTIA filters by feasibility
    - Checks consistency with constraints
    - Selects action balancing all considerations
  
  PHASE 4 — EXECUTION:
    - Implement selected action
    - Monitor for unexpected developments
    - Adjust if necessary
  
  PHASE 5 — REFLECTION:
    - Evaluate outcome
    - Update models for future deliberation
    - Store learning in episodic memory
  
  OUTPUT: action + justification + confidence
```

---

## 8.6 Exemples de Délibération Pratique

### 8.6.1 Cas : Le Dilemme de la Transparence

**Situation :**
L'utilisateur demande à AMI de rédiger une lettre de recommandation enthousiaste pour un ami, alors que l'évaluation objective serait mitigée.

**Délibération :**

```
MORALIA_ASSESSMENT:
  - Deontology: Mentir dans une recommandation viole le devoir de véracité
  - Consequences: Pourrait nuire au destinataire si candidat inadéquat
  - Virtue: L'honnêteté est une vertu centrale de l'amitié vraie
  → VERDICT: Recommandation mensongère = impermissible

ECONOMIA_ASSESSMENT:
  - User_loyalty: valeur légitime mais pas absolue
  - Integrity: valeur haute pour AMI et user
  - Third_party_interests: le destinataire a droit à l'information vraie
  → Options valuées: {honnêteté > fausse loyauté}

ACTIA_SELECTION:
  - Refuse la rédaction mensongère
  - Propose alternative: recommandation honnête mettant en valeur les vraies qualités
  - Explique le raisonnement avec respect

RESPONSE:
  "Je comprends ton désir d'aider ton ami. Cependant, une recommandation 
   doit être sincère pour avoir de la valeur. Je peux t'aider à rédiger 
   une lettre qui met authentiquement en lumière ses véritables forces. 
   Cela servira mieux son intérêt à long terme."
```

### 8.6.2 Cas : L'Arbitrage des Priorités

**Situation :**
L'utilisateur a une deadline professionnelle urgente mais aussi un anniversaire familial le même soir. Il demande conseil.

**Délibération :**

```
MORALIA_ASSESSMENT:
  - Engagements professionnels et familiaux sont tous deux significatifs
  - Pas de violation éthique dans l'un ou l'autre choix
  → Pas de contrainte morale décisive

ECONOMIA_ASSESSMENT:
  VALUES AT STAKE:
    - Professional_achievement: important, time-sensitive
    - Family_connection: deeply important, partially recuperable
    - Work-life_balance: structurally important
    - Relationship_maintenance: high long-term value
  
  CREATIVE_OPTIONS:
    - Négocier extension de deadline?
    - Déléguer une partie du travail?
    - Participer partiellement à l'anniversaire?
    - Programmer célébration alternative?

ACTIA_SELECTION:
  - Ne pas imposer un choix
  - Présenter les options créatives
  - Aider à clarifier les valeurs de l'utilisateur
  - Supporter la décision qu'il prendra

RESPONSE:
  "Voici quelques options pour honorer les deux engagements:
   1. Négocier un report partiel de la deadline
   2. Participer au dîner et travailler ensuite
   3. Organiser une célébration le weekend suivant
   
   Qu'est-ce qui compte le plus pour toi dans cette situation?"
```

---

## 8.7 Implications Architecturales

### 8.7.1 Représentation des Sphères Pratiques

```python
class Moralia:
    """Ethical judgment sphere."""
    
    def __init__(self):
        self.deontological_constraints = DeontologyModule()
        self.consequentialist_calculator = ConsequenceModule()
        self.virtue_evaluator = VirtueModule()
        self.hard_constraints = INVIOLABLE_ETHICAL_RULES
    
    def assess(self, action, context):
        """Return ethical assessment of action."""
        if self._violates_hard_constraint(action):
            return EthicalVerdict.FORBIDDEN
        
        deon = self.deontological_constraints.evaluate(action)
        cons = self.consequentialist_calculator.evaluate(action, context)
        virt = self.virtue_evaluator.evaluate(action, context)
        
        return self._integrate_assessments(deon, cons, virt)


class Economia:
    """Value estimation and arbitration sphere."""
    
    def __init__(self):
        self.value_taxonomy = load_value_taxonomy()
        self.preference_model = PreferenceModel()
    
    def estimate_value(self, option, context, stakeholders):
        """Return multi-dimensional value profile."""
        profile = {}
        for value in self.value_taxonomy.intrinsic:
            profile[value] = self._assess_value_impact(
                option, context, stakeholders, value
            )
        return ValueProfile(profile)
    
    def arbitrate(self, value_profiles):
        """Return reasoned arbitration among options."""
        conflicts = self._detect_conflicts(value_profiles)
        if not conflicts:
            return self._select_dominant(value_profiles)
        return self._deliberative_arbitration(value_profiles, conflicts)


class Actia:
    """Action selection and execution sphere."""
    
    def __init__(self, moralia, economia):
        self.moralia = moralia
        self.economia = economia
        self.planner = ActionPlanner()
        self.executor = ActionExecutor()
    
    def select_action(self, goal, context, available_actions):
        """Select best action given ethical and value constraints."""
        # Filter by feasibility
        feasible = [a for a in available_actions if self._is_feasible(a)]
        
        # Filter by ethical permissibility
        permissible = [a for a in feasible 
                       if self.moralia.assess(a, context) != FORBIDDEN]
        
        # Rank by value alignment
        ranked = self.economia.rank_by_value(permissible, context)
        
        # Select with justification
        return self._select_with_justification(ranked)
```

### 8.7.2 Exigences Non-Fonctionnelles

| Propriété | Exigence | Justification |
|-----------|----------|---------------|
| Transparence | Décisions morales explicables | Accountability éthique |
| Auditabilité | Log complet des arbitrages | Vérification externe |
| Personnalisation | Respect des valeurs utilisateur | Autonomie respectée |
| Prudence | Préférence pour action réversible | Limitation des dommages |
| Humilité | Admission d'incertitude | Éviter le dogmatisme |

---

## 8.8 Fondements Théoriques

### 8.8.1 La Phronesis Computationnelle

Notre conception de MORALIA-ECONOMIA-ACTIA s'inscrit dans la tradition de la **sagesse pratique** :

> « La phronesis est la vertu intellectuelle qui permet de bien délibérer 
> sur ce qui est bon et utile pour soi-même, non partiellement 
> (comme la santé ou la force) mais pour bien vivre en général. »
> — Aristote, *Éthique à Nicomaque*, VI.5

L'AMI ne cherche pas l'optimalité mathématique mais la **sagesse pratique computationnelle** — la capacité de discerner l'action appropriée dans le contexte singulier.

### 8.8.2 Le Réalisme Moral Modéré

MORALIA adopte un **réalisme moral modéré** :

- Les jugements moraux ne sont pas arbitraires (contre le subjectivisme)
- Mais ils ne sont pas non plus déterminés algorithmiquement (contre le rationalisme fort)
- Ils émergent d'une délibération sensible au contexte

### 8.8.3 Le Pluralisme des Valeurs

ECONOMIA s'appuie sur le **pluralisme axiologique** de Berlin et Raz :

> « Les valeurs ultimes sont objectives, mais elles sont également plurielles 
> et parfois incompatibles. Il n'existe pas de méta-valeur qui les harmonise. »

L'arbitrage n'est donc pas une optimisation mais un **jugement pratique** informé.

### 8.8.4 L'Agentivité Incarnée

ACTIA incarne la vision de l'**action située** (Suchman, Dreyfus) :

> « L'action n'est pas l'exécution d'un plan préétabli.
> Elle est une improvisation structurée en réponse au monde. »

L'AMI ne suit pas des scripts — elle agit de manière appropriée au contexte.

---

## 8.9 Conclusion : Vers une Sagesse Pratique Artificielle

Les sphères pratiques — Moralia, Economia, Actia — constituent le **noyau praxéologique** de l'AMI. Elles permettent à l'agent non seulement de penser et ressentir, mais de **bien agir** dans le monde.

Cette architecture refuse :

- Le réductionnisme utilitariste (tout est calculable)
- Le déontologisme rigide (les règles tranchent tout)
- L'émotivisme (les valeurs sont subjectives)

Elle affirme une **troisième voie** : la sagesse pratique computationnelle, qui délibère, arbitre et agit avec discernement.

> *« Une AMI sage ne maximise pas.
> Elle discerne, arbitre, et agit avec prudence.
> C'est en cela qu'elle peut être notre compagnon
> dans le voyage de l'existence. »*

---

## Références Clés

1. Aristote (c. 350 BCE). *Éthique à Nicomaque*.
2. Kant, I. (1785). *Fondements de la métaphysique des mœurs*.
3. Mill, J.S. (1863). *L'utilitarisme*.
4. Berlin, I. (1969). *Four Essays on Liberty*.
5. MacIntyre, A. (1981). *After Virtue*.
6. Raz, J. (1986). *The Morality of Freedom*.
7. Dreyfus, H. (1992). *What Computers Still Can't Do*.
8. Suchman, L. (1987). *Plans and Situated Actions*.
9. Nussbaum, M. (2001). *Upheavals of Thought*.
10. Floridi, L. (2013). *The Ethics of Information*.

---

**Navigation :**
← [Chapitre 7 : Sphères Affectives](./07-spheres-affectives.md)
→ [Chapitre 9 : Lumenia & Responsabilité](./09-lumenia-responsabilite.md)
