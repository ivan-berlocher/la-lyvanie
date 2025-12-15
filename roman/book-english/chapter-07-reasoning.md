# Chapter 7

## Reasoning and Inference

---

### 7.1 Introduction

Having established what genuine learning requires (Chapter 6), we now examine **reasoning** — the process by which an agent derives new knowledge from existing knowledge.

Reasoning is central to intelligence. It enables:
- Drawing conclusions not explicitly stated
- Planning actions toward goals
- Explaining observations
- Making decisions under uncertainty

This chapter develops a formal treatment of reasoning, distinguishing types of inference, examining their computational properties, and connecting them to cognitive architecture.

---

### 7.2 Types of Inference

#### 7.2.1 Deduction

**Definition 7.1 (Deductive Inference)**: Deriving conclusions that necessarily follow from premises.

$$\frac{P \rightarrow Q, \quad P}{Q} \quad \text{(Modus Ponens)}$$

**Properties**:
- **Truth-preserving**: If premises are true, conclusion is true
- **Monotonic**: Adding premises never invalidates conclusions
- **Certain**: Conclusions are guaranteed (given premises)

**Example**:
```
Premise 1: All humans are mortal
Premise 2: Socrates is human
Conclusion: Socrates is mortal
```

**Formal System**: First-order logic with inference rules (see Chapter 2).

#### 7.2.2 Induction

**Definition 7.2 (Inductive Inference)**: Deriving general rules from specific observations.

$$\frac{F(a_1), F(a_2), ..., F(a_n)}{\forall x. F(x)} \quad \text{(with uncertainty)}$$

**Properties**:
- **Ampliative**: Conclusion goes beyond premises
- **Uncertain**: Conclusion may be false even if premises are true
- **Defeasible**: New evidence can overturn conclusions

**Example**:
```
Observation 1: Swan_1 is white
Observation 2: Swan_2 is white
...
Observation n: Swan_n is white
Conclusion: All swans are white (uncertain — black swans exist)
```

**The Problem of Induction** (Hume): No finite set of observations logically entails a universal generalization. Induction requires assumptions (uniformity of nature, simplicity priors).

#### 7.2.3 Abduction

**Definition 7.3 (Abductive Inference)**: Inferring the best explanation for observations.

$$\frac{O, \quad H \text{ explains } O}{H} \quad \text{(Inference to Best Explanation)}$$

**Properties**:
- **Explanatory**: Seeks causes or reasons
- **Uncertain**: Multiple hypotheses may explain observations
- **Creative**: Generates new hypotheses

**Example**:
```
Observation: The grass is wet
Hypothesis 1: It rained
Hypothesis 2: The sprinkler ran
Hypothesis 3: Heavy dew formed
Best Explanation: It rained (given background knowledge)
```

**Criteria for Best Explanation**:
- Simplicity (Occam's Razor)
- Explanatory scope (explains more observations)
- Coherence with background knowledge
- Predictive power

#### 7.2.4 Analogy

**Definition 7.4 (Analogical Inference)**: Transferring knowledge from a source domain to a target domain based on structural similarity.

$$\frac{Similar(S, T), \quad P(S)}{P(T)} \quad \text{(with uncertainty)}$$

**Example**:
```
Source: The atom has a nucleus with electrons orbiting
Target: The solar system has a sun with planets orbiting
Transfer: Perhaps atomic structure follows similar laws to orbital mechanics
```

**Structure Mapping Theory** (Gentner, 1983):
- Identify relational structure in source
- Find corresponding structure in target
- Transfer inferences along the mapping

#### 7.2.5 Comparison

| Type | Direction | Certainty | Ampliative |
|------|-----------|-----------|------------|
| Deduction | General → Specific | Certain | No |
| Induction | Specific → General | Uncertain | Yes |
| Abduction | Effect → Cause | Uncertain | Yes |
| Analogy | Domain → Domain | Uncertain | Yes |

---

### 7.3 Formal Reasoning Systems

#### 7.3.1 Propositional Logic

**Syntax**:
- Propositions: $P, Q, R, ...$
- Connectives: $\neg, \land, \lor, \rightarrow, \leftrightarrow$

**Semantics**: Truth tables define meaning of connectives.

**Inference Rules**:
```
Modus Ponens:     P → Q, P ⊢ Q
Modus Tollens:    P → Q, ¬Q ⊢ ¬P
Conjunction:      P, Q ⊢ P ∧ Q
Disjunction:      P ⊢ P ∨ Q
Resolution:       P ∨ Q, ¬P ∨ R ⊢ Q ∨ R
```

**Completeness**: Every valid inference can be derived.
**Decidability**: Satisfiability is decidable (but NP-complete).

#### 7.3.2 First-Order Logic

**Syntax**:
- Terms: constants, variables, functions
- Predicates: $P(t_1, ..., t_n)$
- Quantifiers: $\forall, \exists$

**Example**:
$$\forall x. Human(x) \rightarrow Mortal(x)$$

**Inference**: Extends propositional rules with:
- Universal instantiation: $\forall x. P(x) \vdash P(a)$
- Existential generalization: $P(a) \vdash \exists x. P(x)$
- Unification for matching

**Semi-decidability**: Valid formulas can be proven, but invalid formulas may loop forever.

#### 7.3.3 Probabilistic Reasoning

**Bayesian Inference**:
$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$

**Components**:
- $P(H)$: Prior probability of hypothesis
- $P(E|H)$: Likelihood of evidence given hypothesis
- $P(H|E)$: Posterior probability after observing evidence

**Bayesian Networks**: Directed acyclic graphs representing conditional dependencies.

```
       Weather
       /     \
      ↓       ↓
  Sprinkler   Rain
       \     /
        ↓   ↓
      Wet Grass
```

$$P(W, S, R, G) = P(W) \cdot P(S|W) \cdot P(R|W) \cdot P(G|S,R)$$

**Inference**: Compute posterior probabilities given evidence.

#### 7.3.4 Non-Monotonic Reasoning

**Problem**: Classical logic is monotonic — adding premises never retracts conclusions. But common-sense reasoning is non-monotonic.

**Example**:
```
Birds typically fly.
Tweety is a bird.
→ Tweety flies (default conclusion)

Tweety is a penguin.
→ Tweety does not fly (retract previous conclusion)
```

**Approaches**:
- Default logic (Reiter, 1980)
- Circumscription (McCarthy, 1980)
- Answer Set Programming

**Default Rule**:
$$\frac{Bird(x) : Flies(x)}{Flies(x)}$$
"If x is a bird, and it's consistent to assume x flies, then conclude x flies."

---

### 7.4 Reasoning in Cognitive Architectures

#### 7.4.1 Production System Reasoning

In architectures like Soar and ACT-R, reasoning emerges from production rule firing.

**Forward Chaining** (data-driven):
```
Working Memory: {A, B}
Rules:
  R1: A, B → C
  R2: C → D

Fire R1: {A, B, C}
Fire R2: {A, B, C, D}
```

**Backward Chaining** (goal-driven):
```
Goal: D
Rules:
  R2: C → D  (need C)
  R1: A, B → C (need A, B)

Check: A? Yes. B? Yes.
Fire R1, R2: Goal achieved.
```

#### 7.4.2 Reasoning with Uncertainty

**ACT-R Activation-Based Retrieval**:

Memory chunks have activation levels. Retrieval probability depends on activation:
$$P(retrieve_i) = \frac{e^{A_i / s}}{\sum_j e^{A_j / s}}$$

This implements a form of probabilistic reasoning — more relevant (higher activation) knowledge is more likely to influence conclusions.

#### 7.4.3 Meta-Reasoning

**Definition 7.5 (Meta-Reasoning)**: Reasoning about one's own reasoning processes.

**Functions**:
- Monitoring: Is reasoning on track?
- Strategy selection: Which reasoning approach?
- Resource allocation: How much effort to invest?
- Confidence assessment: How certain is the conclusion?

**Example**:
```
Task: Prove theorem
Meta-level: 
  - Current approach not making progress
  - Try different proof strategy
  - If still stuck, reduce confidence in provability
```

---

### 7.5 Rule Engines and Production Systems

Rule engines are the computational foundation for automated reasoning. They provide efficient algorithms for pattern matching and inference over large rule bases.

#### 7.5.1 Production System Architecture

**Definition 7.6 (Production System)**: A production system consists of:
- **Working Memory (WM)**: Current facts (working memory elements, WMEs)
- **Production Memory (PM)**: Rules of form condition → action
- **Inference Engine**: Matches rules against WM and fires them

**The Recognize-Act Cycle**:
```
while not done:
    1. MATCH: Find all rules whose conditions match WM
    2. CONFLICT RESOLUTION: Select one rule to fire
    3. ACT: Execute the rule's actions (modify WM)
```

**Conflict Resolution Strategies**:
- **Specificity**: Prefer more specific rules (more conditions)
- **Recency**: Prefer rules matching recently added facts
- **Refraction**: Don't fire same rule on same data twice
- **Priority**: Explicit rule ordering

#### 7.5.2 Forward Chaining (Data-Driven Inference)

**Definition 7.7 (Forward Chaining)**: Starting from known facts, repeatedly apply rules until goal is reached or no more rules apply.

**Algorithm**:
```
ForwardChain(facts, rules, goal):
    WM = facts
    while goal not in WM and rules can fire:
        for rule in rules:
            if rule.conditions satisfied by WM:
                WM = WM ∪ rule.conclusions
    return goal in WM
```

**Example**: Medical diagnosis
```
Facts: {fever, cough, fatigue}
Rules:
    R1: fever ∧ cough → possible_flu
    R2: possible_flu ∧ fatigue → likely_flu
    R3: likely_flu → recommend_rest

Trace:
    Match R1: fever ∧ cough ✓ → add possible_flu
    Match R2: possible_flu ∧ fatigue ✓ → add likely_flu
    Match R3: likely_flu ✓ → add recommend_rest
```

**When to Use**: When you have data and want to derive all consequences. Good for monitoring, alerting, data-driven decisions.

#### 7.5.3 Backward Chaining (Goal-Driven Inference)

**Definition 7.8 (Backward Chaining)**: Starting from goal, recursively find rules that conclude the goal, and try to prove their conditions.

**Algorithm**:
```
BackwardChain(goal, facts, rules):
    if goal in facts:
        return True
    for rule in rules where rule.conclusion == goal:
        if all(BackwardChain(c, facts, rules) for c in rule.conditions):
            return True
    return False
```

**Example**: Proving ancestry
```
Goal: ancestor(abraham, jacob)?
Rules:
    R1: parent(X, Y) → ancestor(X, Y)
    R2: parent(X, Z) ∧ ancestor(Z, Y) → ancestor(X, Y)
Facts: parent(abraham, isaac), parent(isaac, jacob)

Trace:
    Goal: ancestor(abraham, jacob)
    Try R1: need parent(abraham, jacob) → not in facts
    Try R2: need parent(abraham, Z) ∧ ancestor(Z, jacob)
        Z = isaac: parent(abraham, isaac) ✓
        Subgoal: ancestor(isaac, jacob)
            Try R1: parent(isaac, jacob) ✓
        → ancestor(abraham, jacob) proven
```

**When to Use**: When you have a specific question. Good for query answering, proof systems, expert systems.

#### 7.5.4 The Rete Algorithm

**Problem**: Naive forward chaining re-evaluates all rules on every cycle. With thousands of rules and facts, this is O(R × F^C) per cycle.

**Rete** (Forgy, 1982): An efficient algorithm that avoids redundant pattern matching.

**Key Insight**: Most WM changes affect few rules. Maintain a network that incrementally propagates changes.

**Rete Network Structure**:
```
                [Root]
                   |
        ┌─────────┼─────────┐
        ↓         ↓         ↓
    [α-node]  [α-node]  [α-node]    ← Single-condition tests
        |         |         |
    [α-mem]   [α-mem]   [α-mem]    ← Alpha memories
        |         |         |
        └────┬────┴────┬────┘
             ↓         ↓
         [β-node]  [β-node]         ← Join conditions
             |         |
         [β-mem]   [β-mem]         ← Beta memories
             |         |
             └────┬────┘
                  ↓
            [Production]            ← Rule actions
```

**Components**:
- **Alpha Network**: Tests single conditions. Each α-node tests one attribute.
- **Alpha Memories**: Store WMEs matching partial conditions.
- **Beta Network**: Joins multiple conditions.
- **Beta Memories**: Store partial matches (tokens).
- **Production Nodes**: Rules ready to fire.

**Complexity**:
- Build time: O(R × C) where R = rules, C = average conditions
- Update time: O(affected matches) — typically small
- Space: O(partial matches stored)

**Example**:
```
Rule: person(X) ∧ age(X, A) ∧ A > 65 → senior(X)

Rete Network:
    Root
      |
    ┌─┴─┬────────────┐
    ↓   ↓            ↓
  [person?] [age?] [>65?]
    |       |        |
    α₁      α₂       α₃
    |       |        |
    └───┬───┘        |
        ↓            |
    [X = X]          |
        |            |
        β₁           |
        |            |
        └─────┬──────┘
              ↓
          [A = A, A > 65]
              |
              β₂
              |
          [Production: senior(X)]
```

When `person(john)` is added:
1. Propagates through α₁ → α₁-mem
2. Joins with α₂-mem (looking for age(john, _))
3. If found, propagates to β₁, then checks age constraint

**Rete Variants**:
- **TREAT**: Removes beta memories (less space, more recomputation)
- **LEAPS**: Lazy evaluation (compute matches on demand)
- **Rete/UL**: Supports unification (Prolog-style variables)

#### 7.5.5 Comparison: Forward vs. Backward

| Aspect | Forward Chaining | Backward Chaining |
|--------|------------------|-------------------|
| Direction | Data → Conclusions | Goal → Subgoals |
| Trigger | New data arrives | Query asked |
| Exploration | Derives everything derivable | Only relevant inferences |
| Best for | Monitoring, alerting, ETL | Query answering, diagnosis |
| Completeness | Finds all consequences | Finds one proof (if exists) |
| Control | May derive irrelevant facts | Goal-directed |

**Hybrid Systems**: Many systems combine both:
- Forward chain to maintain derived facts
- Backward chain to answer specific queries

#### 7.5.6 Logic Programming: Prolog

**Prolog** implements backward chaining with unification over Horn clauses.

**Syntax**:
```prolog
% Facts
parent(abraham, isaac).
parent(isaac, jacob).

% Rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Query
?- ancestor(abraham, jacob).
% Yes
```

**Execution Model**:
1. Match goal against rule heads (unification)
2. Replace goal with rule body (resolution)
3. Recursively prove body goals
4. Backtrack on failure

**Negation as Failure**: `\+ Goal` succeeds if Goal cannot be proven.

**Cut (!)**:  Commits to current choice, prevents backtracking.

**Limitations**:
- Left-to-right, depth-first search can loop
- Negation as failure is not classical negation
- No built-in uncertainty handling

#### 7.5.7 Modern Rule Engines

**Production Rule Systems**:
- **Drools** (Java): Enterprise rule engine with Rete
- **CLIPS** (C): NASA-developed expert system shell
- **Jess** (Java): Expert system with Rete

**Logic Programming**:
- **Prolog**: Classic backward chaining
- **Datalog**: Restricted Prolog (no function symbols), guaranteed termination
- **Answer Set Programming (ASP)**: Non-monotonic reasoning

**Hybrid/Neural-Symbolic**:
- **Problog**: Probabilistic Prolog
- **DeepProblog**: Neural predicates + probabilistic logic
- **Neural Theorem Provers**: Differentiable backward chaining

---

### 7.6 Computational Complexity

#### 7.6.1 Complexity Classes

| Problem | Complexity |
|---------|------------|
| Propositional satisfiability | NP-complete |
| First-order validity | Semi-decidable |
| Probabilistic inference | #P-hard |
| Planning (general) | PSPACE-complete |

**Implication**: General reasoning is computationally intractable. Intelligent systems must use heuristics, approximations, and bounded rationality.

#### 7.6.2 Tractable Subclasses

**Horn Clauses**: Propositional clauses with at most one positive literal. Linear-time inference.

**Polytrees**: Bayesian networks without undirected cycles. Linear-time inference.

**Bounded Treewidth**: Many NP-hard problems become tractable when graph structure has bounded treewidth.

#### 7.6.3 Anytime Algorithms

**Definition 7.9 (Anytime Algorithm)**: An algorithm that can return a result at any time, with quality improving given more time.

**Properties**:
- Interruptible: Can stop at any time
- Monotonic: Quality never decreases with time
- Bounded: Known quality bounds at any time

**Example**: Iterative deepening search, beam search, MCMC sampling.

---

### 7.7 Neural Approaches to Reasoning

#### 7.7.1 The Challenge

Neural networks excel at pattern recognition but struggle with systematic reasoning.

**Failures**:
- Compositionality: "John loves Mary" ≠ "Mary loves John"
- Systematicity: Knowing "X above Y" should transfer to new X, Y
- Variable binding: Tracking which entity fills which role

#### 7.7.2 Neural Theorem Provers

**Approach**: Embed logical rules and facts in vector space. Perform "soft" reasoning via similarity.

**Example** (Rocktäschel & Riedel, 2017):
- Rules and facts are embedded as vectors
- Unification becomes similarity computation
- Backpropagate through proof structure

**Limitation**: Approximates logical reasoning but may not preserve soundness.

#### 7.7.3 Chain-of-Thought Prompting

**Observation**: LLMs perform better on reasoning tasks when prompted to show intermediate steps.

```
Q: Roger has 5 tennis balls. He buys 2 more cans of 3. How many does he have?
A: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. 
   The answer is 11.
```

**Interpretation**: Decomposing reasoning into steps keeps intermediate results in the context window, simulating working memory.

**Limitation**: This is reasoning *simulation*, not genuine reasoning. The model has no understanding of why the steps work.

#### 7.7.4 Neuro-Symbolic Reasoning

**Hybrid Approach**:
- Neural networks for perception and pattern recognition
- Symbolic systems for reasoning
- Interface layer for translation

```
Percept → [Neural Encoder] → Symbols → [Symbolic Reasoner] → Conclusion
                                              ↓
                                    [Explanation Generator]
```

**Advantages**:
- Preserves reasoning soundness
- Enables explanation
- Leverages neural perception

---

### 7.8 Reasoning Under Uncertainty

#### 7.8.1 Sources of Uncertainty

**Aleatoric**: Inherent randomness in the world
**Epistemic**: Uncertainty from incomplete knowledge
**Model uncertainty**: Uncertainty about which model is correct

#### 7.8.2 Representing Uncertainty

**Probabilities**: $P(A) \in [0, 1]$
**Confidence intervals**: $A \in [low, high]$ with probability $p$
**Fuzzy sets**: Degree of membership $\mu_A(x) \in [0, 1]$
**Dempster-Shafer**: Belief functions over sets of hypotheses

#### 7.8.3 Decision Making Under Uncertainty

**Expected Utility**:
$$EU(action) = \sum_{outcome} P(outcome | action) \cdot U(outcome)$$

**Maximum Expected Utility Principle**: Choose action with highest expected utility.

**Bounded Rationality**: In practice, agents cannot compute optimal decisions. They satisfice — find "good enough" solutions with limited computation.

---

### 7.9 Reasoning and Transparency

#### 7.9.1 Explainable Reasoning

A transparent reasoning system can explain its inferences:

```
Conclusion: Tweety cannot fly
Explanation:
  1. Tweety is a penguin (given)
  2. Penguins are birds (knowledge base)
  3. Penguins cannot fly (knowledge base)
  4. By rule application: Tweety cannot fly
```

#### 7.9.2 Reasoning Traces

**Definition 7.10 (Reasoning Trace)**: A record of inference steps leading to a conclusion.

```
Trace = {
    conclusion: Proposition
    steps: List<{
        rule: InferenceRule
        premises: List<Proposition>
        result: Proposition
    }>
    confidence: Float
}
```

#### 7.9.3 Auditable Inference

For high-stakes decisions, reasoning must be auditable:
- Each step justified
- Sources cited
- Assumptions explicit
- Uncertainty quantified

---

### 7.10 Summary

Reasoning derives new knowledge from existing knowledge:

1. **Deduction** guarantees truth preservation but is not ampliative
2. **Induction** generalizes from observations but is uncertain
3. **Abduction** explains observations by hypothesizing causes
4. **Analogy** transfers knowledge across domains

Key challenges:
- Computational intractability of general reasoning
- Integration of uncertain evidence
- Neural networks' difficulty with systematic reasoning
- Maintaining transparency and explainability

The solution lies in hybrid architectures combining neural perception with symbolic reasoning, within cognitive frameworks that support genuine understanding.

---

### Key Concepts

- **Deduction**: Certain inference from general to specific
- **Induction**: Uncertain inference from specific to general
- **Abduction**: Inference to best explanation
- **Forward chaining**: Data-driven inference from facts to conclusions
- **Backward chaining**: Goal-driven inference from query to supporting facts
- **Rete algorithm**: Efficient pattern matching for production systems
- **Non-monotonic reasoning**: Conclusions can be retracted
- **Meta-reasoning**: Reasoning about reasoning

---

### Exercises

**7.1** Formalize the following argument in first-order logic and check its validity:
"All professors are academics. Some academics are not wealthy. Therefore, some professors are not wealthy."

**7.2** Given a Bayesian network with structure A → B → C, derive the formula for P(A|C).

**7.3** Design a default logic theory for common-sense reasoning about birds and flight. Handle eagles, penguins, and wounded birds.

**7.4** Implement a simple forward-chaining reasoner. Test it on a rule base encoding family relationships.

**7.5** Analyze a chain-of-thought prompt response from an LLM. Identify where it simulates reasoning vs. where it relies on pattern matching.

**7.6** Implement a backward-chaining reasoner in Prolog (or a similar language). Define rules for the transitive closure of a relation.

**7.7** Draw the Rete network for the following rules:
```
R1: employee(X) ∧ department(X, D) ∧ manager(D, M) → reports_to(X, M)
R2: reports_to(X, Y) ∧ reports_to(Y, Z) → indirect_reports(X, Z)
```

**7.8** Compare the memory and time complexity of forward chaining with and without the Rete algorithm on a rule base with 100 rules and 10,000 facts.

---

### Further Reading

**Classical Logic and Reasoning:**
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*, 4th ed. Chapters 7-15.
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann.

**Non-Monotonic Reasoning:**
- Reiter, R. (1980). "A logic for default reasoning." *Artificial Intelligence*, 13, 81-132.
- McCarthy, J. (1980). "Circumscription — a form of non-monotonic reasoning." *Artificial Intelligence*, 13, 27-39.

**Rule Engines and Production Systems:**
- Forgy, C. (1982). "Rete: A fast algorithm for the many pattern/many object pattern match problem." *Artificial Intelligence*, 19(1), 17-37.
- Brownston, L., et al. (1985). *Programming Expert Systems in OPS5*. Addison-Wesley.

**Logic Programming:**
- Sterling, L., & Shapiro, E. (1994). *The Art of Prolog*. 2nd ed. MIT Press.
- Clocksin, W., & Mellish, C. (2003). *Programming in Prolog*. 5th ed. Springer.

**Analogy and Structure Mapping:**
- Gentner, D. (1983). "Structure-mapping: A theoretical framework for analogy." *Cognitive Science*, 7, 155-170.

---

*End of Chapter 7*
