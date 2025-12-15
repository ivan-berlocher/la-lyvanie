# Chapter 2

## The Language of Thought

---

### 2.1 Introduction

The previous chapter identified the representation crisis: modern AI systems lack structured, interpretable internal representations. This chapter presents a theoretical framework for what such representations might look like: the **Language of Thought** (LoT) hypothesis.

Originally proposed by philosopher Jerry Fodor (1975), the Language of Thought hypothesis claims that cognition operates over structured symbolic representations with language-like properties. We will examine this hypothesis, formalize it for computational purposes, and show how it addresses the interpretability requirements identified in Chapter 1.

---

### 2.2 The Classical Hypothesis

#### 2.2.1 Fodor's Original Argument

Jerry Fodor argued that mental processes are computational operations over mental representations, and these representations have the structure of a language — what he called "Mentalese."

The argument proceeds:

1. **Thinking is productive**: We can think an unbounded number of distinct thoughts.

2. **Thinking is systematic**: The ability to think certain thoughts implies the ability to think related thoughts (if you can think "John loves Mary," you can think "Mary loves John").

3. **Thinking is compositional**: The meaning of a complex thought is determined by the meanings of its parts and how they are combined.

4. **Conclusion**: Mental representations must have combinatorial structure — a vocabulary of primitive concepts and rules for combining them.

This structure is what makes mental representation "language-like."

#### 2.2.2 Properties of Language-Like Representation

A Language of Thought has several defining properties:

**Discreteness**: Representations consist of discrete symbols, not continuous values.

**Constituency**: Complex representations are built from simpler constituents. The representation of "red square" contains the representations of "red" and "square."

**Compositionality**: The meaning of a complex expression is a function of the meanings of its parts and their mode of combination.

**Productivity**: A finite vocabulary and finite set of combinatorial rules can generate an infinite set of representations.

**Systematicity**: Representational capacities come in clusters. Any system that can represent *aRb* can also represent *bRa*.

#### 2.2.3 Formalization

We can formalize a Language of Thought as a formal language:

**Definition 2.1 (Language of Thought)**: A Language of Thought ℒ is a tuple (𝒱, 𝒞, 𝒫) where:
- 𝒱 is a vocabulary of primitive symbols (concepts)
- 𝒞 is a set of category labels (types)
- 𝒫 is a set of production rules specifying how symbols combine

**Example 2.1**: A simple propositional LoT:

Vocabulary 𝒱:
- Objects: *john*, *mary*, *ball*, ...
- Properties: *red*, *round*, *happy*, ...
- Relations: *loves*, *kicks*, *gives*, ...

Categories 𝒞:
- Entity, Property, Relation, Proposition

Productions 𝒫:
- Property(Entity) → Proposition
- Relation(Entity, Entity) → Proposition
- ¬Proposition → Proposition
- Proposition ∧ Proposition → Proposition

This generates expressions like:
- *happy(john)* — "John is happy"
- *loves(john, mary)* — "John loves Mary"
- *loves(john, mary) ∧ happy(mary)* — "John loves Mary and Mary is happy"

---

### 2.3 Computational Formalization

For AI systems, we need a more precise computational specification.

#### 2.3.1 Concept Representation

**Definition 2.2 (Concept)**: A concept C is represented as a structure:

```
Concept = {
    id: Identifier
    type: Category
    features: Map<Feature, Value>
    relations: Set<(Relation, Concept)>
    grounding: GroundingFunction
}
```

Where:
- *id* uniquely identifies the concept
- *type* specifies the ontological category
- *features* capture intrinsic properties
- *relations* link to other concepts
- *grounding* connects to perceptual representations

**Example 2.2**: The concept DOG:

```
DOG = {
    id: concept_dog
    type: NaturalKind
    features: {
        animate: true
        mammal: true
        domesticated: true
    }
    relations: {
        (is-a, ANIMAL),
        (has-part, TAIL),
        (makes-sound, BARK)
    }
    grounding: perceptual_dog_detector
}
```

#### 2.3.2 Propositional Representation

**Definition 2.3 (Proposition)**: A proposition P is a structured representation with truth conditions:

```
Proposition = {
    predicate: Concept
    arguments: List<Concept | Proposition>
    modality: {asserted, hypothetical, negated, ...}
    confidence: [0, 1]
    source: Provenance
}
```

**Example 2.3**:

"The red ball is on the table"

```
Proposition = {
    predicate: ON
    arguments: [
        {predicate: BALL, features: {color: RED}},
        TABLE
    ]
    modality: asserted
    confidence: 0.95
    source: visual_perception
}
```

#### 2.3.3 Schema Representation

Beyond individual propositions, cognition requires organized knowledge structures.

**Definition 2.4 (Schema)**: A schema S is a parameterized structure representing a class of situations:

```
Schema = {
    name: Identifier
    roles: Map<Role, TypeConstraint>
    constraints: Set<Proposition>
    defaults: Map<Role, Value>
    procedures: Map<Event, Action>
}
```

**Example 2.4**: A RESTAURANT schema:

```
RESTAURANT_SCHEMA = {
    name: dining_experience
    roles: {
        customer: PERSON
        server: PERSON  
        food: FOOD_ITEM
        bill: MONETARY_VALUE
        location: RESTAURANT
    }
    constraints: {
        works_at(server, location),
        orders(customer, food),
        serves(server, food, customer),
        pays(customer, bill)
    }
    defaults: {
        tip: 0.15 * bill
    }
    procedures: {
        on_arrival: [be_seated, receive_menu],
        on_ordering: [wait, receive_food],
        on_finishing: [request_bill, pay, leave]
    }
}
```

---

### 2.4 Formal Semantics

A Language of Thought requires a semantic theory specifying what representations *mean*.

#### 2.4.1 Denotational Semantics

**Definition 2.5 (Interpretation)**: An interpretation I maps LoT expressions to denotations:

- For concepts: I(C) ⊆ D (extension in domain D)
- For relations: I(R) ⊆ D^n (n-ary relations over D)
- For propositions: I(P) ∈ {T, F} (truth values)

**Truth Conditions**:

For atomic propositions:
- I(P(a)) = T iff I(a) ∈ I(P)
- I(R(a,b)) = T iff (I(a), I(b)) ∈ I(R)

For complex propositions:
- I(¬P) = T iff I(P) = F
- I(P ∧ Q) = T iff I(P) = T and I(Q) = T
- I(P ∨ Q) = T iff I(P) = T or I(Q) = T
- I(∀x.P(x)) = T iff for all d ∈ D, I(P(d)) = T
- I(∃x.P(x)) = T iff for some d ∈ D, I(P(d)) = T

#### 2.4.2 Compositional Semantics

**Principle of Compositionality**: The meaning of a complex expression is determined by:
1. The meanings of its constituent parts
2. The mode of syntactic combination

Formally, if expression E = f(E₁, ..., Eₙ) is formed by combining E₁...Eₙ via operation f, then:

I(E) = g(I(E₁), ..., I(Eₙ))

where g is a semantic operation corresponding to syntactic operation f.

**Example 2.5**:

Expression: *loves(john, mary)*
Composition: Relation + Entity + Entity → Proposition

I(*loves(john, mary)*) = T iff (I(*john*), I(*mary*)) ∈ I(*loves*)

The meaning of the whole is computed from meanings of parts.

#### 2.4.3 Grounded Semantics

Pure denotational semantics connects symbols to abstract sets. For AI systems, we also need **grounding** — connecting symbols to perception and action.

**Definition 2.6 (Perceptual Grounding)**: A grounding function G maps concepts to perceptual procedures:

G: Concept → (Percept → Probability)

The grounding of DOG is a function that takes a perceptual input and returns the probability that it is an instance of DOG.

**Definition 2.7 (Action Grounding)**: For action concepts, grounding maps to motor procedures:

G: ActionConcept → (State × Parameters → Trajectory)

The grounding of GRASP is a function that takes current state and parameters and returns a motor trajectory.

---

### 2.5 Formal Language Theory

Before describing operations over LoT, we must establish the mathematical foundations of formal languages. This section introduces the essential theory that underlies all structured representation.

#### 2.5.1 The Chomsky Hierarchy

**Definition 2.8 (Formal Language)**: A formal language L is a set of strings over an alphabet Σ. Languages are classified by the grammars that generate them.

**The Chomsky Hierarchy** (1956) classifies languages by generative power:

| Type | Name | Grammar Restriction | Recognizer | Example |
|------|------|---------------------|------------|---------|
| 3 | Regular | A → aB or A → a | Finite Automaton | `a*b+` |
| 2 | Context-Free | A → γ | Pushdown Automaton | Balanced parentheses |
| 1 | Context-Sensitive | αAβ → αγβ | Linear-Bounded Automaton | aⁿbⁿcⁿ |
| 0 | Recursively Enumerable | α → β | Turing Machine | Any computable language |

Each level strictly contains all levels below it: Type 3 ⊂ Type 2 ⊂ Type 1 ⊂ Type 0.

**Theorem 2.5 (Chomsky)**: Natural languages require at least context-free power, and some constructions (cross-serial dependencies in Swiss German) suggest mildly context-sensitive power.

#### 2.5.2 Regular Expressions and Finite Automata

**Definition 2.9 (Regular Expression)**: Regular expressions over alphabet Σ are defined inductively:
- ∅ (empty set) and ε (empty string) are regular expressions
- For each a ∈ Σ, a is a regular expression
- If r and s are regular expressions, so are:
  - (r|s) — alternation (union)
  - (rs) — concatenation
  - (r*) — Kleene star (zero or more)

**Example 2.7**: The regex `[a-z]+@[a-z]+\.[a-z]{2,3}` matches simple email addresses.

**Definition 2.10 (Deterministic Finite Automaton)**: A DFA is a tuple M = (Q, Σ, δ, q₀, F) where:
- Q is a finite set of states
- Σ is the input alphabet
- δ: Q × Σ → Q is the transition function
- q₀ ∈ Q is the start state
- F ⊆ Q is the set of accepting states

**Theorem 2.6 (Kleene)**: A language is regular iff it is recognized by some finite automaton iff it is generated by some regular expression.

```
     ┌─────────────────────────────────────────┐
     │         Equivalence of Formalisms       │
     │                                         │
     │  Regular    ←─────→   DFA/NFA           │
     │ Expression            Automaton         │
     │      ↑                    ↑             │
     │      └────────→ ←─────────┘             │
     │           Regular Grammar               │
     └─────────────────────────────────────────┘
```

#### 2.5.3 Context-Free Grammars

**Definition 2.11 (Context-Free Grammar)**: A CFG is a tuple G = (N, Σ, P, S) where:
- N is a finite set of non-terminal symbols
- Σ is a finite set of terminal symbols (N ∩ Σ = ∅)
- P is a finite set of production rules: A → α where A ∈ N and α ∈ (N ∪ Σ)*
- S ∈ N is the start symbol

**Example 2.8**: Grammar for arithmetic expressions:

```
E → E + T | E - T | T
T → T * F | T / F | F
F → ( E ) | number | variable
```

This grammar captures operator precedence (* binds tighter than +) and associativity.

**Backus-Naur Form (BNF)**: Standard notation for CFGs:

```bnf
<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
<term>       ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
<factor>     ::= "(" <expression> ")" | <number> | <identifier>
```

**Extended BNF (EBNF)** adds convenience:
- `[...]` for optional elements
- `{...}` for zero or more repetitions
- `(...)` for grouping

#### 2.5.4 Parsing Algorithms

Parsing transforms a string into a structured representation (parse tree or AST).

**Definition 2.12 (Parse Tree)**: A parse tree for string w under grammar G is a tree where:
- The root is labeled with the start symbol
- Each internal node is labeled with a non-terminal
- Each leaf is labeled with a terminal
- For each internal node A with children X₁...Xₙ, there is a production A → X₁...Xₙ

**Top-Down Parsing** (Predictive, LL):
- Start from start symbol, predict productions
- LL(k): Left-to-right, Leftmost derivation, k lookahead tokens
- Recursive descent is the simplest implementation

```python
def parse_expression(tokens):
    """Recursive descent parser for expressions"""
    left = parse_term(tokens)
    while tokens.peek() in ['+', '-']:
        op = tokens.consume()
        right = parse_term(tokens)
        left = BinaryOp(op, left, right)
    return left
```

**Bottom-Up Parsing** (Shift-Reduce, LR):
- Start from input, reduce to start symbol
- LR(k): Left-to-right, Rightmost derivation (reversed), k lookahead
- More powerful than LL parsers

**Chart Parsing** (Earley, CYK):
- Handle ambiguous grammars
- Earley: O(n³) general, O(n²) unambiguous, O(n) for LR grammars
- CYK: O(n³), requires Chomsky Normal Form

**Theorem 2.7**: Every context-free language can be parsed in O(n³) time using the CYK or Earley algorithm.

#### 2.5.5 Semantic Analysis

Parsing produces syntax; semantic analysis assigns meaning.

**Definition 2.13 (Attribute Grammar)**: An attribute grammar extends a CFG with:
- Attributes attached to grammar symbols
- Semantic rules computing attribute values

**Synthesized attributes**: Computed from children (bottom-up)
**Inherited attributes**: Computed from parent/siblings (top-down)

**Example 2.9**: Type checking as attribute grammar:

```
Production: E → E₁ + E₂
Semantic rule: E.type = 
    if E₁.type == E₂.type == INT then INT
    else if E₁.type == FLOAT or E₂.type == FLOAT then FLOAT
    else ERROR
```

**Compositional Semantics** (Montague):
- Each syntactic rule has a corresponding semantic rule
- Meaning is computed compositionally during parsing

$$⟦\text{John loves Mary}⟧ = ⟦\text{loves}⟧(⟦\text{John}⟧, ⟦\text{Mary}⟧)$$

#### 2.5.6 Ontologies and Knowledge Representation

**Definition 2.14 (Ontology)**: An ontology O is a formal specification of a conceptualization, consisting of:
- **Concepts** (classes): Categories of entities
- **Relations** (properties): Connections between concepts
- **Instances** (individuals): Specific entities
- **Axioms**: Logical constraints on concepts and relations

**Description Logic (DL)**: The logical foundation for ontologies.

Basic constructors:
- ⊤ (top/universal concept), ⊥ (bottom/empty concept)
- ¬C (complement), C ⊓ D (intersection), C ⊔ D (union)
- ∀R.C (universal restriction), ∃R.C (existential restriction)
- ≤n R.C, ≥n R.C (number restrictions)

**Example 2.10**: OWL-style ontology fragment:

```
Class: Person
Class: Parent ≡ Person ⊓ ∃hasChild.Person
Class: Father ≡ Parent ⊓ Male
Class: Mother ≡ Parent ⊓ Female

ObjectProperty: hasChild
    Domain: Person
    Range: Person

DisjointClasses: Male, Female
```

**Theorem 2.8**: Description Logic SHIQ is decidable with EXPTIME complexity. OWL-DL corresponds to SHOIN(D) with decidable reasoning.

**The Open World Assumption**: Unlike databases (closed-world), ontologies assume that unknown facts might be true. This affects reasoning.

#### 2.5.7 Formal Languages and Cognitive Architecture

The Language of Thought must be **at least** context-free to support:
- Recursive structure (sentences containing sentences)
- Compositional semantics
- Systematic productivity

**Practical LoT systems** typically use:
- Type 2 (CFG) for basic syntax
- Type 1 extensions for cross-references and agreement
- Description Logic for taxonomic knowledge
- First-order logic for rules and inference

```
┌──────────────────────────────────────────────────┐
│              Language Stack in LoT               │
├──────────────────────────────────────────────────┤
│  First-Order Logic / Horn Clauses     (Rules)   │
├──────────────────────────────────────────────────┤
│  Description Logic / OWL              (Ontology) │
├──────────────────────────────────────────────────┤
│  Context-Free Grammar                 (Syntax)   │
├──────────────────────────────────────────────────┤
│  Regular Expressions                  (Lexicon)  │
└──────────────────────────────────────────────────┘
```

---

### 2.6 Fractal Structure of Language and Cognition

A profound property of natural language and cognitive systems is their **fractal structure** — the same organizational patterns repeat at multiple scales. This self-similarity is not coincidental; it reflects deep principles about how compositional systems must be organized.

#### 2.6.1 Self-Similarity Across Scales

**Definition 2.15 (Fractal Structure)**: A system exhibits fractal structure if similar patterns or organizational principles recur at different scales of observation.

**Linguistic Hierarchy**:
```
┌─────────────────────────────────────────────────────────────────────────┐
│ DISCOURSE    │  Introduction → Body → Conclusion  (macro-structure)    │
├──────────────┼──────────────────────────────────────────────────────────┤
│ PARAGRAPH    │  Topic → Support → Transition      (text-structure)     │
├──────────────┼──────────────────────────────────────────────────────────┤
│ SENTENCE     │  Subject → Predicate → Object      (syntactic)          │
├──────────────┼──────────────────────────────────────────────────────────┤
│ PHRASE       │  Specifier → Head → Complement     (X-bar)              │
├──────────────┼──────────────────────────────────────────────────────────┤
│ WORD         │  Prefix → Root → Suffix            (morphological)      │
├──────────────┼──────────────────────────────────────────────────────────┤
│ SYLLABLE     │  Onset → Nucleus → Coda            (phonological)       │
└──────────────┴──────────────────────────────────────────────────────────┘
```

At each level, we observe:
- A **head** or central element
- Optional **modifiers** or dependents
- **Recursive embedding** of lower-level structures
- **Compositional semantics** (meaning from parts)

This is self-similarity: the same structural template (head + dependents + recursion) applies at every scale.

#### 2.6.2 Mathematical Foundations

**Zipf's Law** (1935): In natural language, word frequency follows a power law:

$$f(r) \propto \frac{1}{r^\alpha}$$

Where $r$ is the rank of a word by frequency and $\alpha \approx 1$.

**Mandelbrot's Extension** (1953): Benoît Mandelbrot showed this is a characteristic of self-similar, information-efficient coding systems:

$$f(r) \propto \frac{1}{(r + \beta)^\alpha}$$

**Power Laws as Fractal Signature**: Power-law distributions (found throughout language) indicate scale-invariance — a hallmark of fractal structure.

| Linguistic Phenomenon | Distribution | Exponent |
|-----------------------|--------------|----------|
| Word frequency | Power law | α ≈ 1.0 |
| Sentence length | Log-normal | — |
| Parse tree depth | Power law | α ≈ 1.5 |
| Clause embedding | Exponential decay | — |
| Semantic associations | Power law | α ≈ 0.7 |

**Definition 2.16 (Scale Invariance)**: A property P is scale-invariant if:

$$P(λx) = λ^k P(x)$$

for some constant $k$ and all scaling factors $λ > 0$.

Language exhibits statistical scale invariance: the same distributional patterns appear whether we analyze corpora of 10K, 100K, or 100M words.

#### 2.6.3 Recursion as Fractal Generator

**Chomsky's Insight**: The recursive nature of syntax is what generates fractal structure.

**Recursive Rule**:
```
S → NP VP
VP → V S    (embedded clause)
```

This allows:
- "John thinks [Mary believes [Tom knows [...]]]"
- Unbounded depth, same structure at each level

**The Embedding Pattern**:
```
                    S
                   / \
                 NP   VP
                 |   /  \
               John V    S
                   |    / \
               thinks NP  VP
                      |  /  \
                    Mary V   S
                         |  / \
                   believes...
```

Each embedded S has the same structure as the root S — self-similarity through recursion.

**Formal Connection**: A Context-Free Grammar generates fractal parse trees when it contains recursive productions. The "fractal dimension" of the parse tree relates to the grammar's recursive depth.

#### 2.6.4 Cognitive Fractality

The fractal principle extends beyond language to cognition itself.

**Hierarchical Processing**:
```
┌─────────────────────────────────────────────────────────────────────────┐
│ METACOGNITION │  Monitor → Evaluate → Adjust     (thinking about thinking)│
├───────────────┼─────────────────────────────────────────────────────────┤
│ REASONING     │  Premise → Inference → Conclusion (logical)             │
├───────────────┼─────────────────────────────────────────────────────────┤
│ COMPREHENSION │  Perceive → Parse → Interpret    (understanding)        │
├───────────────┼─────────────────────────────────────────────────────────┤
│ PERCEPTION    │  Detect → Group → Recognize      (bottom-up)            │
├───────────────┼─────────────────────────────────────────────────────────┤
│ SENSATION     │  Transduce → Filter → Encode     (sensory)              │
└───────────────┴─────────────────────────────────────────────────────────┘
```

At each level: **input → processing → output**, with the output becoming input to the next level.

**Minsky's Society of Mind** (1986): Intelligence emerges from societies of simpler agents, where each agent itself may be a society of even simpler agents — fractal decomposition of cognition.

```
         Agent (high-level)
        /       |        \
    Agent    Agent     Agent
    / \      / \       / \
   a   a    a   a     a   a  ... (micro-agents)
```

**Hofstadter's Strange Loops** (1979): Self-referential structures in cognition create "tangled hierarchies" where high levels reach back to influence low levels — a different kind of fractal recursion.

#### 2.6.5 Implications for Language of Thought

**Why LoT Must Be Fractal**:

1. **Productivity**: Finite resources generating infinite outputs requires recursive structure
2. **Compositionality**: Meaning composition follows the same pattern at all scales
3. **Learnability**: Same structural patterns can be learned once, applied everywhere
4. **Efficiency**: Fractal compression — describe complex structures with simple recursive rules

**Design Principle**: A Language of Thought should exhibit self-similar structure:

```
LoT Expression
├── Head concept
├── Modifier expressions
│   └── [Each modifier is itself a LoT Expression]
└── Embedded expressions
    └── [Each embedding is itself a LoT Expression]
```

**The Fractal Signature in LoT**:

| Property | Manifestation |
|----------|---------------|
| Self-similarity | Same composition rules at all levels |
| Scale invariance | Statistical patterns hold across expression sizes |
| Recursive generation | Expressions contain expressions of same type |
| Power-law distributions | Concept frequency, expression complexity |
| Hierarchical organization | Concepts embed in larger concepts |

#### 2.6.6 Formal Definition

**Definition 2.17 (Fractal LoT)**: A Language of Thought ℒ is fractal if:

1. **Recursive Closure**: For any well-formed expression E ∈ ℒ, there exists a production rule that can embed E in a larger expression E' ∈ ℒ

2. **Structural Self-Similarity**: The composition operations at any level of embedding are isomorphic to those at any other level

3. **Scale-Invariant Statistics**: The distribution of expression properties (depth, breadth, concept frequency) follows power laws

**Theorem 2.3 (Fractal Compositionality)**: If a LoT is fractal, then its compositional semantics can be defined by a single recursive semantic function:

$$⟦E⟧ = f(⟦E_1⟧, ⟦E_2⟧, ..., ⟦E_n⟧, \text{combinator})$$

where $E_1, ..., E_n$ are the immediate constituents of $E$ and $f$ is the same function at all levels.

*Proof sketch*: Self-similarity ensures that the semantic combination rule does not depend on the depth of embedding. The same f applies whether E is at the root or arbitrarily deep in the structure. □

#### 2.6.7 Connections to Other Chapters

The fractal principle connects to themes throughout this book:

- **Chapter 4 (Cognitive Architectures)**: Hierarchical organization of cognitive modules
- **Chapter 7 (Reasoning)**: Recursive inference rules
- **Chapter 9 (Memory)**: Hierarchical memory organization (episodic ⊃ events ⊃ actions)
- **Chapter 10 (Metacognition)**: Cognition about cognition — the ultimate self-reference
- **Chapter 13 (Execution)**: Compilation pipelines repeat at multiple scales

**Key Insight**: The fractal structure of language is not a curiosity — it is a **design requirement** for any system that must be simultaneously expressive, learnable, and efficient. A Language of Thought inherits this requirement.

---

### 2.7 Operations Over LoT

A Language of Thought is not just a representational format — it supports cognitive operations.

#### 2.6.1 Logical Inference

**Deduction**: Deriving conclusions that follow necessarily from premises.

Rule: Modus Ponens
```
P, P → Q
─────────
    Q
```

**Example**: From *loves(john, mary)* and *∀x,y. loves(x,y) → cares_about(x,y)*, derive *cares_about(john, mary)*.

#### 2.6.2 Unification and Pattern Matching

**Definition 2.15 (Unification)**: Two expressions E₁ and E₂ unify under substitution σ if σ(E₁) = σ(E₂).

**Algorithm**: Robinson's Unification Algorithm

```
UNIFY(E₁, E₂) → substitution or FAIL:
    if E₁ = E₂: return {}
    if E₁ is variable: return {E₁ ↦ E₂}
    if E₂ is variable: return {E₂ ↦ E₁}
    if E₁ = f(a₁...aₙ) and E₂ = f(b₁...bₙ):
        σ = {}
        for i = 1 to n:
            σᵢ = UNIFY(σ(aᵢ), σ(bᵢ))
            if σᵢ = FAIL: return FAIL
            σ = compose(σ, σᵢ)
        return σ
    else: return FAIL
```

Unification enables matching patterns against knowledge structures and deriving variable bindings.

#### 2.6.3 Analogical Mapping

**Definition 2.16 (Analogical Mapping)**: Given source structure S and target structure T, an analogical mapping is a set of correspondences M: S → T preserving structural relations.

**Structure Mapping Engine (SME)** algorithm (Gentner, 1983):

1. Find local matches between relations
2. Combine into structurally consistent mappings
3. Prefer mappings that preserve higher-order structure (systematicity)

**Example 2.6**: Analogy between solar system and atom:

Source (Solar System):
- ORBITS(planet, sun)
- MORE_MASSIVE(sun, planet)
- ATTRACTS(sun, planet)

Target (Atom):
- ORBITS(electron, nucleus)
- ??? (nucleus, electron)
- ATTRACTS(nucleus, electron)

Mapping: {sun → nucleus, planet → electron, ORBITS → ORBITS, ATTRACTS → ATTRACTS}

Analogical inference: MORE_MASSIVE(nucleus, electron)

---

### 2.8 Computational Complexity

Language of Thought representations enable powerful inference but at computational cost.

#### 2.7.1 Complexity of Logical Inference

**Theorem 2.9**: Propositional satisfiability (SAT) is NP-complete.

**Theorem 2.10**: First-order logic entailment is undecidable in general (Church-Turing).

**Implication**: Unrestricted logical inference over LoT representations is computationally intractable. Practical systems must use:
- Restricted languages (e.g., Horn clauses)
- Heuristic search with incomplete inference
- Approximate reasoning methods

#### 2.7.2 Complexity of Unification

**Theorem 2.11**: First-order unification is O(n) for most practical cases (linear unification algorithms exist).

**Theorem 2.12**: Unification with "occurs check" is O(n²) in the worst case but O(n) amortized.

Unification is tractable, making pattern-matching operations efficient.

#### 2.7.3 Handling Complexity

Practical cognitive architectures address complexity through:

1. **Chunking**: Compiling frequent inference patterns into single-step operations
2. **Spreading activation**: Limiting search to contextually relevant knowledge
3. **Resource bounds**: Hard limits on inference depth/breadth
4. **Approximate inference**: Trading completeness for tractability

---

### 2.9 LoT and Neural Representations

How does Language of Thought relate to neural network representations?

#### 2.8.1 The Integration Challenge

Neural networks learn distributed representations — vectors in high-dimensional space. LoT requires discrete, symbolic structures. Bridging this gap is a central challenge.

**Options**:

1. **Neural → Symbolic**: Use neural networks for perception, then extract discrete symbols
2. **Symbolic → Neural**: Embed discrete structures in continuous space
3. **Hybrid**: Different representations for different cognitive functions
4. **Neurosymbolic**: Architectures that compute over symbols using neural operations

#### 2.8.2 Neural Encoding of Symbolic Structures

Recent research has explored whether neural networks implicitly learn LoT-like representations.

**Findings**:
- Transformers develop attention patterns resembling syntactic structure
- Some neurons respond to interpretable concepts
- Vector arithmetic can capture analogical relations (king - man + woman ≈ queen)

**Limitations**:
- These structures are discovered post-hoc, not designed
- They are incomplete and inconsistent
- They lack the systematicity of true LoT

#### 2.8.3 Tensor Product Representations

**Smolensky (1990)** proposed representing symbolic structures as tensor products:

For structure *R(a, b)*:
- Encode role-filler pairs: role₁ ⊗ a + role₂ ⊗ b
- Where ⊗ is the outer product of vectors

This allows symbolic structures to be represented in continuous vector spaces while preserving compositional structure.

**Definition 2.17 (Tensor Product Representation)**:

For structure S with roles {r₁, ..., rₙ} and fillers {f₁, ..., fₙ}:

$$\mathbf{S} = \sum_{i=1}^{n} \mathbf{r}_i \otimes \mathbf{f}_i$$

where **r**ᵢ and **f**ᵢ are vectors representing roles and fillers.

---

### 2.10 Evidence and Objections

#### 2.9.1 Evidence for LoT

**Productivity**: Humans can understand sentences they have never heard before. This requires compositional processing.

**Systematicity**: Humans who understand "John loves Mary" also understand "Mary loves John." This suggests shared structural components.

**Inferential Coherence**: Human reasoning respects logical relationships in ways consistent with propositional structure.

#### 2.9.2 Objections to LoT

**Objection 1**: *Concepts may not have classical definitional structure.*

Response: LoT is compatible with prototype or exemplar theories of concepts. The compositional structure is at the level of propositions, not necessarily concepts.

**Objection 2**: *Much cognition is subsymbolic (perception, motor control).*

Response: LoT may coexist with subsymbolic processes. The claim is that high-level cognition uses LoT, not all cognition.

**Objection 3**: *Neural networks work without LoT.*

Response: Neural networks excel at pattern recognition but struggle with systematic reasoning. LoT addresses exactly these limitations.

---

### 2.11 Summary

The Language of Thought hypothesis proposes that cognition operates over structured symbolic representations with compositional semantics. This framework provides:

- **Interpretability**: Discrete, human-aligned concepts with clear semantics
- **Compositionality**: Complex representations built systematically from primitives
- **Systematic reasoning**: Formal operations over structured representations
- **Grounding**: Connections between symbols and perception/action

These properties address the interpretability requirements identified in Chapter 1. The challenge is implementing LoT in computational systems that retain the strengths of modern neural approaches.

The next chapter examines how LoT representations can be made accessible through transparency mechanisms.

---

### Key Concepts

- **Language of Thought**: Structured symbolic representation with language-like properties
- **Compositionality**: Meaning of whole determined by meanings of parts and combination
- **Productivity**: Finite resources generate infinite representational capacity
- **Systematicity**: Representational capacities come in clusters
- **Chomsky Hierarchy**: Classification of formal languages by generative power
- **Context-Free Grammar**: Grammar where each production has single non-terminal on left
- **Parser**: Algorithm that converts strings to structured representations
- **Ontology**: Formal specification of conceptualization with concepts, relations, and axioms
- **Description Logic**: Logical foundation for ontologies, subset of FOL
- **Grounding**: Connection between symbols and perception/action
- **Tensor product representation**: Encoding symbolic structures in vector spaces
- **Fractal structure**: Self-similar patterns recurring at different scales
- **Scale invariance**: Statistical properties unchanged under scaling
- **Zipf's Law**: Power-law distribution of word frequencies

---

### Exercises

**2.1** Prove that a compositional semantics satisfies systematicity: any system that can represent *R(a,b)* can represent *R(b,a)*.

**2.2** Design a LoT vocabulary and production rules for representing spatial relationships (on, in, near, between, etc.).

**2.3** Implement Robinson's unification algorithm and test it on the examples in this chapter.

**2.4** Consider the concept BACHELOR. Can it be represented with necessary and sufficient features? What does this suggest about concept representation?

**2.5** Design a tensor product encoding for simple predicate-argument structures. How would you extract the filler of a given role?

**2.6** Write a regular expression that matches valid identifiers in a programming language (letter followed by letters, digits, or underscores). Prove it cannot match balanced parentheses.

**2.7** Write a context-free grammar for a simple programming language with if-then-else, while loops, and assignment statements. Show that it is ambiguous and fix the ambiguity.

**2.8** Implement a recursive descent parser for arithmetic expressions with +, -, *, /, parentheses, and operator precedence.

**2.9** Design an ontology for a simple domain (family relationships, or a library system). Express it in Description Logic notation. What inferences can be drawn?

**2.10** Prove that the language aⁿbⁿ is context-free but aⁿbⁿcⁿ is not. What does this imply about natural language?

---

### Further Reading

**Language of Thought:**
- Fodor, J. (1975). *The Language of Thought*. Harvard University Press.
- Fodor, J. & Pylyshyn, Z. (1988). "Connectionism and cognitive architecture: A critical analysis." *Cognition*, 28, 3-71.
- Marcus, G. (2001). *The Algebraic Mind*. MIT Press.

**Formal Language Theory:**
- Chomsky, N. (1956). "Three models for the description of language." *IRE Transactions on Information Theory*, 2(3), 113-124.
- Hopcroft, J., Motwani, R., & Ullman, J. (2006). *Introduction to Automata Theory, Languages, and Computation*. 3rd ed. Pearson.
- Sipser, M. (2012). *Introduction to the Theory of Computation*. 3rd ed. Cengage Learning.

**Parsing:**
- Aho, A., Lam, M., Sethi, R., & Ullman, J. (2006). *Compilers: Principles, Techniques, and Tools*. 2nd ed. Pearson. (The "Dragon Book")
- Earley, J. (1970). "An efficient context-free parsing algorithm." *Communications of the ACM*, 13(2), 94-102.

**Ontologies and Knowledge Representation:**
- Baader, F., et al. (2003). *The Description Logic Handbook*. Cambridge University Press.
- Gruber, T. (1993). "A translation approach to portable ontology specifications." *Knowledge Acquisition*, 5(2), 199-220.
- Horrocks, I. (2008). "Ontologies and the Semantic Web." *Communications of the ACM*, 51(12), 58-67.

**Compositional Semantics:**
- Montague, R. (1973). "The proper treatment of quantification in ordinary English." In *Approaches to Natural Language*. Reidel.
- Partee, B. (1995). "Lexical semantics and compositionality." In *An Invitation to Cognitive Science*, Vol. 1. MIT Press.

**Fractal Structure and Power Laws:**
- Zipf, G. K. (1935). *The Psycho-Biology of Language*. Houghton Mifflin.
- Mandelbrot, B. (1953). "An informational theory of the statistical structure of language." In *Communication Theory*. Butterworth.
- Mandelbrot, B. (1982). *The Fractal Geometry of Nature*. W.H. Freeman.
- Minsky, M. (1986). *The Society of Mind*. Simon & Schuster.
- Hofstadter, D. (1979). *Gödel, Escher, Bach: An Eternal Golden Braid*. Basic Books.

**Neural-Symbolic Integration:**
- Smolensky, P. (1990). "Tensor product variable binding and the representation of symbolic structures in connectionist systems." *Artificial Intelligence*, 46, 159-216.
- Garcez, A., et al. (2019). "Neural-symbolic computing: An effective methodology for principled integration of machine learning and reasoning." *arXiv:1905.06088*.

---

*End of Chapter 2*
