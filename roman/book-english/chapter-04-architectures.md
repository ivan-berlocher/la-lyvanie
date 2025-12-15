# Chapter 4

## Cognitive Architectures

---

### 4.1 Introduction

The previous chapters established the theoretical foundations: structured representation (Language of Thought) and transparency mechanisms. This chapter surveys **cognitive architectures** — computational frameworks that organize perception, reasoning, and action into unified systems.

A cognitive architecture is more than a collection of algorithms; it is a theory of how intelligent behavior is organized. We examine classical architectures, extract common principles, and develop a synthesis suitable for modern AI systems.

---

### 4.2 What is a Cognitive Architecture?

#### 4.2.1 Definition

**Definition 4.1 (Cognitive Architecture)**: A cognitive architecture is a specification of:
1. The structure of memory systems
2. The representation of knowledge
3. The mechanisms of reasoning
4. The interface between perception and cognition
5. The interface between cognition and action
6. The control of processing (what happens when)

A cognitive architecture provides the fixed structure within which specific knowledge and skills are acquired.

#### 4.2.2 Architecture vs. Knowledge

**Architecture** is what remains constant across different tasks and domains — the "hardware" of the mind.

**Knowledge** is what varies — the "software" loaded into the architecture.

This distinction mirrors computer science: the CPU architecture is fixed, programs vary.

#### 4.2.3 Levels of Analysis

Marr (1982) distinguished three levels:

1. **Computational**: What problem is being solved?
2. **Algorithmic**: What representations and algorithms are used?
3. **Implementational**: How is it realized in hardware/wetware?

Cognitive architectures operate primarily at the algorithmic level, with implications for both computational and implementational levels.

---

### 4.3 Classical Cognitive Architectures

#### 4.3.1 Soar

**Soar** (Laird, Newell, & Rosenbloom, 1987) is one of the oldest and most influential cognitive architectures.

**Core Principles**:

1. **Problem Space Hypothesis**: All goal-directed behavior is search through problem spaces
2. **Universal Subgoaling**: When knowledge is insufficient, create a subgoal to acquire it
3. **Chunking**: Compiled knowledge from problem-solving becomes rules

**Memory Systems**:
- Working memory: Current state, goals, operators
- Long-term memory: Procedural (production rules), semantic, episodic

**Processing Cycle**:
```
loop:
    1. Elaborate: Apply all matching rules to augment working memory
    2. Propose: Generate candidate operators
    3. Evaluate: Assess operators via preferences
    4. Decide: Select and apply operator
    5. If impasse: Create subgoal
```

**Representation**: Working memory elements are (identifier ^attribute value) triples. Example:
```
(S1 ^type state ^ball B1 ^goal G1)
(B1 ^color red ^location table)
(G1 ^type achieve ^desired (B1 ^location floor))
```

**Production Rules**:
```
sp {propose*pick-up
    (state <s> ^type state ^ball <b> ^goal <g>)
    (<g> ^type achieve ^desired (<b> ^location floor))
    (<b> ^location table)
-->
    (<s> ^operator <o>)
    (<o> ^name pick-up ^ball <b>)
}
```

#### 4.3.2 ACT-R

**ACT-R** (Anderson, 2007) is a cognitive architecture grounded in psychological theory.

**Core Principles**:

1. **Modular Architecture**: Separate modules for vision, motor, declarative memory, goal, imaginal (problem state)
2. **Buffers**: Modules communicate through limited-capacity buffers
3. **Production System**: Procedural knowledge as condition-action rules

**Memory Systems**:
- Declarative memory: Facts as chunks with activation levels
- Procedural memory: Production rules

**Activation Equation**:

$$A_i = B_i + \sum_j W_j S_{ji} + \epsilon$$

Where:
- $A_i$ = activation of chunk i
- $B_i$ = base-level activation (recency/frequency)
- $W_j$ = attentional weight on element j in goal
- $S_{ji}$ = association strength between j and i
- $\epsilon$ = noise

**Retrieval Probability**:

$$P(retrieve_i) = \frac{1}{1 + e^{-\frac{A_i - \tau}{s}}}$$

Where τ is retrieval threshold and s is noise parameter.

**Production Cycle**:
```
loop (50ms per cycle):
    1. Match: Find productions matching buffer contents
    2. Select: Choose production based on utility
    3. Fire: Execute production actions
    4. Update: Modify buffers, request retrievals
```

#### 4.3.3 CLARION

**CLARION** (Sun, 2002) emphasizes dual processing: explicit and implicit.

**Core Principles**:

1. **Dual Representation**: Both symbolic (explicit) and subsymbolic (implicit) knowledge
2. **Bottom-up Learning**: Implicit knowledge can be extracted into explicit rules
3. **Motivation**: Drives and goals influence processing

**Subsystems**:
- Action-Centered Subsystem (procedural knowledge)
- Non-Action-Centered Subsystem (declarative knowledge)
- Motivational Subsystem (drives and goals)
- Meta-Cognitive Subsystem (monitoring and control)

**Dual Processing**: Each subsystem has top (explicit/symbolic) and bottom (implicit/connectionist) levels that interact.

#### 4.3.4 Comparison

| Feature | Soar | ACT-R | CLARION |
|---------|------|-------|---------|
| Knowledge rep. | Symbolic | Hybrid | Dual |
| Learning | Chunking | Bayesian | Bottom-up |
| Timing | None | 50ms cycle | None |
| Psychological grounding | Moderate | High | High |
| Neural plausibility | Low | Moderate | Moderate |

---

### 4.4 Common Architectural Principles

Despite differences, cognitive architectures share common principles.

#### 4.4.1 Working Memory

**Principle**: A limited-capacity workspace holds current goals, context, and intermediate results.

**Formal Model**:
```
WorkingMemory = {
    capacity: N  (typically 4-7 items)
    contents: Set<Chunk>
    focus: Chunk (current attention)
    decay: Time → Activation
}
```

**Miller's Law**: Working memory capacity ≈ 7 ± 2 items (or 4 ± 1 chunks for complex items).

**Implications**:
- Reasoning must be incremental, building on limited active context
- Chunking extends effective capacity by grouping items
- Attention mechanisms select what enters working memory

#### 4.4.2 Production Systems

**Principle**: Procedural knowledge is represented as condition-action rules that match against working memory.

**Definition 4.2 (Production Rule)**: A production rule is a pair (C, A) where:
- C is a condition pattern over working memory
- A is a set of actions modifying working memory and/or external state

**Recognition-Action Cycle**:
```
loop:
    1. Match: Find all productions whose conditions are satisfied
    2. Conflict Resolution: Select one production
    3. Act: Execute the selected production's actions
```

**Advantages**:
- Modularity: Rules are independent
- Incremental: New rules can be added without restructuring
- Transparent: Each rule is inspectable

#### 4.4.3 Long-Term Memory

**Principle**: Persistent storage of declarative knowledge (facts) and procedural knowledge (skills).

**Types**:
- **Semantic memory**: General world knowledge (Paris is in France)
- **Episodic memory**: Specific experiences (I visited Paris in 2019)
- **Procedural memory**: Skills and procedures (how to ride a bike)

**Retrieval**: Memory access is typically via:
- Spreading activation (associative retrieval)
- Pattern matching (structured retrieval)
- Cued recall (probe → response)

#### 4.4.4 Goal Management

**Principle**: Behavior is directed by explicit goal structures.

**Goal Stack**: Goals can be hierarchical:
```
Goal Stack:
└── G1: Complete project
    ├── G1.1: Write report
    │   ├── G1.1.1: Gather data
    │   └── G1.1.2: Draft sections
    └── G1.2: Prepare presentation
```

**Goal Operations**:
- Push: Add subgoal
- Pop: Complete/abandon goal
- Suspend: Temporarily deprioritize
- Resume: Return attention to suspended goal

#### 4.4.5 Learning

**Principle**: Architecture must support knowledge acquisition from experience.

**Learning Mechanisms**:
- **Chunking** (Soar): Compile problem-solving traces into rules
- **Reinforcement** (ACT-R): Adjust utility based on outcomes
- **Explanation-based** (EBL): Generalize from explained examples
- **Instance-based**: Store and retrieve specific experiences

---

### 4.5 The Sense-Think-Act Cycle

#### 4.5.1 Overview

All cognitive architectures implement some variant of:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    ENVIRONMENT                                              │
│         │                                                   │
│         ▼                                                   │
│    ┌─────────┐         ┌─────────┐         ┌─────────┐     │
│    │  SENSE  │────────▶│  THINK  │────────▶│   ACT   │     │
│    └─────────┘         └─────────┘         └─────────┘     │
│                              │                    │         │
│                              │                    │         │
│                        ┌─────▼─────┐              │         │
│                        │  MEMORY   │◀─────────────┘         │
│                        └───────────┘                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**SENSE**: Transform environmental stimuli into internal representations
**THINK**: Process representations, make decisions
**ACT**: Transform decisions into environmental effects

#### 4.5.2 Sense Module

**Input**: Raw sensory data (pixels, audio samples, text characters)
**Output**: Structured representations in working memory

**Subprocesses**:
1. **Preprocessing**: Noise reduction, normalization
2. **Feature extraction**: Identify relevant features
3. **Pattern recognition**: Match to known concepts
4. **Grounding**: Connect percepts to symbols
5. **Attention**: Select relevant information

**Formal Model**:
```
Sense: Percept → LoTRepresentation

Sense(p) = Ground(Recognize(Extract(Preprocess(p))))
```

#### 4.5.3 Think Module

**Input**: Working memory state (percepts, goals, context)
**Output**: Updated working memory, decisions, plans

**Subprocesses**:
1. **Comprehension**: Integrate percepts with context
2. **Retrieval**: Access relevant long-term memory
3. **Reasoning**: Draw inferences, evaluate options
4. **Planning**: Construct action sequences
5. **Decision**: Select action

**Formal Model**:
```
Think: WorkingMemory × LongTermMemory → WorkingMemory × Decision

Think(wm, ltm) = 
    let context = Retrieve(wm, ltm) in
    let inferences = Reason(wm, context) in
    let plan = Plan(wm.goal, inferences) in
    let decision = Select(plan) in
    (Update(wm, inferences), decision)
```

#### 4.5.4 Act Module

**Input**: Decision/plan from thinking
**Output**: Actions affecting environment

**Subprocesses**:
1. **Motor planning**: Translate intention to motor commands
2. **Execution**: Carry out motor commands
3. **Monitoring**: Track execution progress
4. **Adjustment**: Correct for deviations

**Formal Model**:
```
Act: Decision × State → Action × State'

Act(d, s) = 
    let motor_plan = MotorPlan(d, s) in
    let result = Execute(motor_plan) in
    Monitor(result, d)
```

---

### 4.6 A Unified Architecture Framework

Based on the common principles, we can specify a generic cognitive architecture.

#### 4.6.1 Core Specification

```
CognitiveArchitecture = {
    // Memory Systems
    working_memory: WorkingMemory
    declarative_memory: DeclarativeMemory
    procedural_memory: ProceduralMemory
    
    // Processing Components
    perception: Percept → Representation
    reasoning: State → State
    action: Decision → Effect
    
    // Control
    goal_manager: GoalStack
    attention: Focus
    conflict_resolution: Set<Production> → Production
    
    // Learning
    consolidation: Experience → Memory
    adaptation: Feedback → Updated Parameters
}
```

#### 4.6.2 The Main Loop

```python
def cognitive_cycle(architecture, environment):
    while active:
        # 1. SENSE
        percept = environment.observe()
        representation = architecture.perception(percept)
        architecture.working_memory.add(representation)
        
        # 2. RETRIEVE
        context = architecture.declarative_memory.retrieve(
            query=architecture.working_memory.focus
        )
        architecture.working_memory.add(context)
        
        # 3. MATCH
        applicable = architecture.procedural_memory.match(
            architecture.working_memory
        )
        
        # 4. SELECT
        production = architecture.conflict_resolution(applicable)
        
        # 5. EXECUTE
        if production.is_internal():
            architecture.working_memory = production.apply(
                architecture.working_memory
            )
        else:
            action = production.get_action()
            effect = architecture.action(action)
            environment.apply(effect)
        
        # 6. LEARN
        architecture.consolidation(
            experience=architecture.working_memory.recent()
        )
        
        # 7. GOAL MANAGEMENT
        architecture.goal_manager.update(
            architecture.working_memory
        )
```

#### 4.6.3 Mathematical Formalization

Let:
- $S$ = set of possible states
- $A$ = set of possible actions
- $P$ = set of production rules
- $M$ = memory contents

**Cognitive State**: $\sigma = (wm, g, ltm) \in S$
- $wm$ = working memory contents
- $g$ = goal stack
- $ltm$ = long-term memory

**Transition Function**: $\delta: S \times Percept \rightarrow S \times Action$

**Soundness**: The architecture should only derive conclusions that follow from knowledge:
$$\forall \sigma, p. \text{Let } (\sigma', a) = \delta(\sigma, p). \text{ Then } \sigma'.wm \models \sigma.ltm$$

---

### 4.7 Modern Extensions

Classical architectures were developed before deep learning. Modern architectures incorporate neural components.

#### 4.7.1 Hybrid Architectures

**Strategy**: Use neural networks for perception and neural-symbolic integration for reasoning.

```
Environment
    ↓
[Neural Perception] → Feature vectors
    ↓
[Symbol Grounding] → LoT representations
    ↓
[Symbolic Reasoning] → Conclusions/Plans
    ↓
[Neural Motor Control] → Actions
```

#### 4.7.2 Differentiable Reasoning

**Strategy**: Implement symbolic operations in differentiable form for end-to-end learning.

**Neural Turing Machines** (Graves et al., 2014):
- External memory matrix
- Differentiable read/write operations
- Learned memory access patterns

**Differentiable Theorem Provers** (Rocktäschel & Riedel, 2017):
- Embed logical rules in vector space
- Perform "soft" unification via similarity
- Backpropagate through inference chains

#### 4.7.3 Large Language Models as Cognitive Components

**Observation**: LLMs exhibit some cognitive capabilities (reasoning, knowledge retrieval) but lack architecture.

**Integration Strategy**:
- Use LLM as knowledge retrieval component
- Use LLM for natural language understanding/generation
- Provide structured architecture for planning, goal management, memory
- Maintain explicit LoT representations for transparency

---

### 4.8 Evaluation and Validation

#### 4.8.1 Cognitive Metrics

Cognitive architectures should be evaluated against human cognition:

**Behavioral fit**: Does the model produce human-like responses?
**Timing fit**: Does it match human response time patterns?
**Error fit**: Does it make human-like errors?
**Learning curves**: Does it learn at human-like rates?
**Transfer**: Does it transfer knowledge appropriately?

#### 4.8.2 Engineering Metrics

For AI applications:

**Accuracy**: Task performance
**Efficiency**: Computational cost
**Transparency**: Interpretability of reasoning
**Robustness**: Performance under distribution shift
**Adaptability**: Learning rate on new tasks

#### 4.8.3 Ablation Studies

Systematically remove architectural components to assess contributions:

| Removed Component | Effect |
|------------------|--------|
| Working memory limits | Loss of focus, inefficiency |
| Long-term retrieval | Failure to use prior knowledge |
| Goal stack | Loss of hierarchical behavior |
| Production rules | Loss of procedural knowledge |

---

### 4.9 Summary

Cognitive architectures provide organizational frameworks for intelligent systems. Key insights:

1. **Working memory** provides limited-capacity workspace for current processing
2. **Production systems** represent procedural knowledge as modular condition-action rules
3. **Long-term memory** stores declarative and procedural knowledge with associative retrieval
4. **Goal management** directs behavior hierarchically
5. **Sense-Think-Act** cycle organizes processing

Modern architectures integrate neural and symbolic components while preserving these organizational principles.

---

### Key Concepts

- **Cognitive architecture**: Fixed organizational structure for intelligent processing
- **Working memory**: Limited-capacity active workspace
- **Production system**: Knowledge as condition-action rules
- **Goal stack**: Hierarchical organization of objectives
- **Sense-Think-Act**: The fundamental cognitive cycle

---

### Exercises

**4.1** Implement a simplified production system in your language of choice. Include working memory, rule matching, and conflict resolution.

**4.2** Compare Soar and ACT-R on a specific task (e.g., the Tower of Hanoi). What differences emerge from architectural differences?

**4.3** Design a hybrid architecture that uses a neural network for perception and a symbolic system for planning. Specify the interfaces.

**4.4** Prove or disprove: A production system with N rules can simulate any finite-state machine.

**4.5** Propose metrics for evaluating cognitive architectures on a new domain. What baselines would you use?

---

### Further Reading

- Anderson, J. R. (2007). *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press.
- Laird, J. E. (2012). *The Soar Cognitive Architecture*. MIT Press.
- Sun, R. (2002). *Duality of the Mind*. Lawrence Erlbaum Associates.
- Kotseruba, I., & Tsotsos, J. K. (2020). "40 years of cognitive architectures: Core cognitive abilities and practical applications." *Artificial Intelligence Review*, 53, 17-94.

---

*End of Chapter 4*
