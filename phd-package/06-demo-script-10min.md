# Live Demo Script — 10 Minutes (PhD / Systems)

## Ce que le prof doit comprendre

1. Il y a un **kernel** (pas un prompt chain)
2. Il y a une **IR (UIL)** — intermediate representation typée
3. Il y a une **mémoire structurée** (graph-based)
4. Les **LLM sont remplaçables** (model-agnostic)
5. Le **raisonnement est visible et traçable**

---

## Pré-requis techniques (minimum)

**Tu dois avoir :**

- [ ] UIL lisible (JSON output)
- [ ] Trace visible (console / panel)
- [ ] 1 bouton "switch model"
- [ ] 1 graph memory view (même très simple)

**Pas besoin :**

- ❌ UI parfaite
- ❌ Design
- ❌ Performance optimisée

---

## ⏱️ Timeline Précise

### 0:00 – 1:00 — Contexte

**Tu parles. Pas d'écran complexe.**

**Dire exactement :**

> "I'll show you a running cognitive kernel. Not a prompt chain, but a system with an explicit intent language, memory, and execution pipeline."

**Annoncer ce que ce n'est PAS :**

- Not end-to-end LLM
- Not black box
- Not theoretical

**Do:** Écran simple, logo ou titre "Harmonia Kernel"

---

### 1:00 – 2:30 — Architecture

**Un seul schéma. Un seul slide.**

```
Input (text/voice)
       ↓
UIL (typed intent)
       ↓
Graph Memory + Goal
       ↓
Agent Routing
       ↓
Action
       ↓
Trace
```

**Dire exactement :**

> "UIL is the intermediate representation. Everything before and after goes through it."

**⚠️ NE PAS dire :** AGI, Language of Thought, vision long terme, révolutionnaire

---

### 2:30 – 4:30 — Action Simple Traçable (LIVE)

**Cas ultra simple, mais réel.**

**Input exemple :**

> "Plan a 3-day trip in Zurich next month, with a budget constraint."

**Montrer exactement 4 choses :**

1. Input utilisateur (texte)
2. UIL généré (JSON visible)
3. Graph Memory avant / après
4. Trace d'agents

**Dire exactement :**

> "This UIL is logged, typed, and replayable."

**JSON attendu (exemple) :**

```json
{
  "type": "PLAN",
  "subject": "user",
  "predicate": { "verb": "plan", "domain": "travel" },
  "object": { "type": "trip", "destination": "Zurich", "duration": "3 days" },
  "constraints": [
    { "type": "temporal", "value": "next month" },
    { "type": "budget", "value": "constrained" }
  ],
  "confidence": 0.91
}
```

---

### 4:30 – 6:30 — Changement de Modèle (MOMENT CLÉ)

**⚠️ Moment le plus important de la démo.**

**Actions :**

1. Même requête
2. Switch vers autre LLM (ou mode degraded)
3. Exécuter

**Dire exactement :**

> "Kernel logic unchanged. Only inference swapped."

**Ce qu'on montre :**

- Même UIL généré
- Même structure de résultat
- Texte peut varier, structure identique

**Pourquoi c'est fort :**

> Le prof comprend que ce n'est pas un prompt hack.

---

### 6:30 – 8:00 — Mémoire & Continuité

**Faire une 2e requête liée à la 1re.**

**Input exemple :**

> "Reduce the budget by 20% and remove museums."

**Montrer :**

1. Récupération du goal précédent (pas de re-prompt)
2. Modification du graph (delta visible)
3. Pas de context window hack

**Dire exactement :**

> "Continuity is handled by memory, not context length."

---

### 8:00 – 9:30 — Échec Contrôlé (TRÈS FORT)

**Montrer volontairement un échec.**

**Exemples de failure modes :**

- Agent conflict (deux agents proposent différent)
- Missing data (info non disponible)
- Low confidence (< 0.5)

**Dire exactement :**

> "Here the system does not hallucinate. It raises uncertainty."

**Montrer :**

- Confidence score bas
- Flag "uncertain" ou "needs_clarification"
- Pas de réponse inventée

**Pourquoi c'est fort :**

> Les profs adorent voir les limites. C'est PhD-compatible.

---

### 9:30 – 10:00 — Clôture

**Une seule phrase :**

> "The PhD would formalize, evaluate, and scale this architecture."

**Puis :**

> "I'd be happy to answer questions."

**Do:** Arrêter de parler. Attendre.

---

## 🧠 Questions Anticipées (Prépare-les)

### Q1: "How is UIL defined formally?"

> "UIL has a typed schema with Intent types (ACTION, QUERY, PLAN, REFLECT), a predicate structure (verb + domain), constraints, and provenance metadata. I have a BNF grammar in the technical documentation. The key property is that every intent is machine-parseable and replayable."

### Q2: "What is non-LLM here?"

> "The kernel itself: intent routing, memory operations, scheduling, conflict detection, and audit logging. LLMs are used for natural language understanding and generation, but the orchestration layer runs independently. I demonstrated this by swapping models without changing behavior."

### Q3: "How do you evaluate correctness?"

> "Three metrics I'm developing: Cognitive Load Reduction (fewer user interactions for same goal), Intention Continuity (goal persistence across sessions), and Temporal Coherence (no contradictions in memory over time). These are non-BLEU, non-accuracy metrics designed for cognitive systems."

### Q4: "What happens when agents disagree?"

> "There's an arbitration protocol. First: priority rules by domain. Second: confidence comparison. Third: if still ambiguous, an arbiter agent evaluates context. Fourth: if still uncertain, escalate to user. I showed a case where the system flagged uncertainty rather than choosing arbitrarily."

### Q5: "What is the PhD contribution vs engineering?"

> "The engineering is the prototype—it proves feasibility. The PhD contribution would be: (1) formalizing UIL semantics, (2) defining evaluation protocols for cognitive architectures, (3) studying scaling properties and failure modes systematically. The prototype enables the research, but the research is the formalization."

---

## Backup Plans

### Si quelque chose plante

**Dire :**

> "Let me restart that component—this happens in prototypes."

**Avoir prêt :**

- Backup recording of the demo
- Architecture diagram to pivot to
- JSON logs from previous run

### Si le temps manque

**Couper dans cet ordre :**

1. Réduire section architecture (montrer juste le schéma)
2. Skip section mémoire si nécessaire
3. GARDER : model swap + failure mode (les plus forts)

---

## Checklist Avant Démo

- [ ] Kernel running
- [ ] UIL output visible
- [ ] Graph memory view ready
- [ ] Model switch button functional
- [ ] Sample queries tested
- [ ] Failure scenario prepared
- [ ] Backup recording ready
- [ ] Timer visible (pour toi)
- [ ] Water bottle nearby
