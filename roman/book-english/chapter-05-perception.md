# Chapter 5

## Perception and Grounding

---

### 5.1 Introduction

The preceding chapters developed structured representations (Language of Thought) and architectural frameworks. This chapter addresses a fundamental question: **How do symbolic representations connect to the world?**

This is the **symbol grounding problem** (Harnad, 1990). Pure symbols are arbitrary; "CAT" has no intrinsic connection to cats. Yet human concepts are grounded in experience — we know what cats look, sound, and feel like.

For AI systems, grounding is both a theoretical necessity (symbols must mean something) and a practical requirement (systems must perceive their environment).

---

### 5.2 The Symbol Grounding Problem

#### 5.2.1 Statement of the Problem

**Definition 5.1 (Symbol Grounding Problem)**: How can the semantic interpretation of a formal symbol system be made intrinsic to the system, rather than parasitic on external interpretation?

**The Chinese Room Argument** (Searle, 1980): A person following rules to manipulate Chinese characters can produce correct outputs without understanding Chinese. By analogy, a computer manipulating symbols may not "understand" them.

**Harnad's Formulation**: Symbols must be grounded in something other than more symbols. An infinite regress of symbolic definitions provides no grounding.

#### 5.2.2 Types of Grounding

**Perceptual grounding**: Connecting symbols to sensory patterns
```
Symbol "RED" ← grounded in → pattern of photoreceptor activations
```

**Motor grounding**: Connecting symbols to action capabilities
```
Symbol "GRASP" ← grounded in → motor program for grasping
```

**Social grounding**: Connecting symbols to shared conventions
```
Symbol "MONEY" ← grounded in → social practices involving currency
```

**Embodied grounding**: Connecting symbols to bodily states
```
Symbol "TIRED" ← grounded in → physiological fatigue states
```

#### 5.2.3 Formal Model of Grounding

**Definition 5.2 (Grounding Function)**: A grounding function is a mapping:
$$G: Symbols \rightarrow Groundings$$

where $Groundings$ is a domain of non-symbolic entities (patterns, actions, states).

**Compositionality**: Grounding should respect compositional structure:
$$G(\text{RED} \land \text{CAR}) = G(\text{RED}) \cap G(\text{CAT})$$

**Invariance**: Grounding should be robust to irrelevant variation:
$$G(\text{CAT}) \ni \text{persian-cat-image}$$
$$G(\text{CAT}) \ni \text{tabby-cat-image}$$

---

### 5.3 Perceptual Systems

#### 5.3.1 Architecture of Perception

```
Raw Input → Preprocessing → Feature Extraction → Recognition → Representation
   │              │                │                  │              │
 pixels        filtered        features          category         symbol
 samples       signals         vectors           labels            LoT
```

**Stage 1: Preprocessing**
- Noise reduction
- Normalization
- Signal conditioning

**Stage 2: Feature Extraction**
- Low-level: edges, textures, frequencies
- Mid-level: parts, contours, patterns
- High-level: objects, scenes

**Stage 3: Recognition**
- Pattern matching
- Classification
- Detection

**Stage 4: Representation**
- Map to symbolic structures
- Integrate with context
- Store in working memory

#### 5.3.2 Visual Perception

**The Visual Pipeline**:
```
Image → Conv layers → Feature maps → RoI → Object proposals → Classification
                                                                      ↓
                                                              Symbol binding
                                                                      ↓
                                                             LoT representation
```

**From Features to Symbols**:

Let $f: Image \rightarrow \mathbb{R}^d$ be a feature extractor (e.g., CNN).
Let $c: \mathbb{R}^d \rightarrow Categories$ be a classifier.
Let $b: Categories \times BoundingBox \rightarrow LoT$ be a symbol binder.

The grounded representation is:
$$R = b(c(f(I)), bbox)$$

**Example**:
```
Input: Image with red ball on table
Features: CNN activation vector
Classification: {ball: 0.97, table: 0.95, person: 0.02}
Binding: (E1 ^type ball ^color red ^location on ^support E2)
         (E2 ^type table)
```

#### 5.3.3 Auditory Perception

**The Audio Pipeline**:
```
Waveform → Spectrogram → Phonemes/Features → Words/Sounds → Symbols
```

**Speech Recognition**:
$$text = argmax_t P(t | spectrogram)$$

Modern systems use end-to-end models (Transformer, CTC) mapping audio directly to text.

**Sound Recognition**:
Similar architecture to image classification, operating on spectrograms or raw waveforms.

#### 5.3.4 Multimodal Integration

Real perception is multimodal — we see AND hear.

**Binding Problem**: How are features from different modalities unified into coherent percepts?

**Temporal Binding**: Concurrent events are bound
**Spatial Binding**: Collocated features are bound
**Semantic Binding**: Congruent meanings are bound

**Example**:
```
Visual: Person with moving lips
Audio: Speech sounds
Binding: (SPEAKING ^agent P1 ^content "hello")
```

---

### 5.4 Attention Mechanisms

#### 5.4.1 Why Attention?

**The Capacity Problem**: Perception generates vast amounts of information. Working memory has limited capacity. Attention selects what enters processing.

**Definition 5.3 (Attention)**: Attention is a mechanism that allocates limited processing resources to a subset of available information.

#### 5.4.2 Types of Attention

**Bottom-up (exogenous)**: Driven by stimulus salience
- Bright flashes
- Loud sounds
- Movement

**Top-down (endogenous)**: Driven by goals and expectations
- Looking for your keys
- Listening for your name
- Searching for red things

**Model**:
$$attention(x) = softmax(salience(x) + relevance(x, goal))$$

#### 5.4.3 Attention in Neural Networks

**Scaled Dot-Product Attention** (Vaswani et al., 2017):

$$Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:
- $Q$ = queries (what we're looking for)
- $K$ = keys (what's available)
- $V$ = values (what to retrieve)
- $d_k$ = key dimension

**Multi-head attention** allows attending to different aspects simultaneously:
$$MultiHead(Q,K,V) = Concat(head_1, ..., head_h)W^O$$

#### 5.4.4 Attention for Grounding

Attention can ground symbols by focusing on relevant percepts:

```
Query: Symbol "BALL"
Keys: Visual features from image regions
Values: Feature vectors

→ Attention focuses on image regions containing balls
→ Grounding: BALL ↔ attended region features
```

---

### 5.5 Symbol Binding

#### 5.5.1 The Binding Problem

**Problem**: Given percepts of features (color, shape, location), how do we bind them into coherent objects?

If we perceive:
- Red color
- Square shape
- Left location
- Blue color
- Circle shape
- Right location

We should perceive "red square on left" and "blue circle on right", not "red circle on left".

**Definition 5.4 (Binding)**: Binding is the process of associating features into coherent object representations.

#### 5.5.2 Mechanisms of Binding

**Spatial binding**: Features at the same location are bound
$$bind(features) = \{F : F.location \approx target\}$$

**Temporal binding**: Features at the same time are bound
$$bind(features) = \{F : F.time \approx target\}$$

**Attention-based binding**: Attended features are bound
$$bind(features) = \{F : attention(F) > \theta\}$$

#### 5.5.3 Neural Binding

**Synchrony hypothesis**: Bound features are represented by neurons firing in synchrony.

**Vector binding**: Features are bound by combining their vectors:

**Tensor Product** (Smolensky, 1990):
$$bind(role, filler) = role \otimes filler$$

**Holographic Reduced Representations** (Plate, 1995):
$$bind(a, b) = a \circledast b \text{ (circular convolution)}$$

**Properties**:
- Recoverable: Can retrieve components from bound representation
- Associative: $(a \circledast b) \circledast c = a \circledast (b \circledast c)$
- Distributed: Binding creates new distributed pattern

#### 5.5.4 Formal Binding Specification

```
BindingSystem = {
    // Inputs
    features: List<Feature>
    spatial_map: Feature → Location
    temporal_map: Feature → Time
    
    // Binding process
    bind: List<Feature> → List<Object>
    
    // Where each Object contains bound features:
    Object = {
        features: Set<Feature>
        location: Location
        time: Time
        id: Identifier  // for reference
    }
}
```

---

### 5.6 From Percepts to Symbols

#### 5.6.1 The Grounding Pipeline

```
Raw Percept
    ↓
Feature Extraction
    ↓
Attention (selection)
    ↓
Binding (grouping)
    ↓
Recognition (classification)
    ↓
Symbol Creation
    ↓
LoT Integration
```

#### 5.6.2 Algorithm: Percept-to-Symbol

```python
def ground_percept(percept, knowledge_base, goals):
    """
    Convert raw percept to grounded LoT representation.
    """
    # 1. Extract features
    features = extract_features(percept)
    
    # 2. Apply attention
    attended = apply_attention(
        features, 
        goals=goals,
        salience=compute_salience(features)
    )
    
    # 3. Bind features into objects
    objects = []
    for group in cluster_features(attended, spatial=True, temporal=True):
        obj = Object(
            features=group,
            location=compute_location(group),
            id=generate_id()
        )
        objects.append(obj)
    
    # 4. Recognize and classify
    for obj in objects:
        obj.category = classify(obj.features, knowledge_base)
        obj.properties = extract_properties(obj.features)
    
    # 5. Generate LoT representation
    lot_rep = create_lot_representation(objects)
    
    return lot_rep

def create_lot_representation(objects):
    """
    Convert bound objects to LoT format.
    """
    rep = LoTRepresentation()
    
    for obj in objects:
        # Create entity node
        entity = rep.create_entity(obj.id)
        
        # Add type
        rep.add_predicate(entity, 'type', obj.category)
        
        # Add properties
        for prop_name, prop_value in obj.properties:
            rep.add_predicate(entity, prop_name, prop_value)
        
        # Add location
        rep.add_predicate(entity, 'location', obj.location)
    
    # Add relations between objects
    for obj1, obj2 in pairs(objects):
        relations = compute_relations(obj1, obj2)
        for rel in relations:
            rep.add_relation(obj1.id, rel, obj2.id)
    
    return rep
```

#### 5.6.3 Example: Visual Scene Grounding

**Input**: Image of a red ball on a wooden table

**Step 1: Feature Extraction**
```
CNN features: 
  - Region R1: ball-like, red, round
  - Region R2: table-like, brown, flat, textured
  - Region R3: background, uniform
```

**Step 2: Attention**
```
Goals: Find objects
Salience: R1 high (distinct), R2 high (distinct), R3 low
Attended: R1, R2
```

**Step 3: Binding**
```
Object O1: features={red, round, ball-like}, location=(120, 80)
Object O2: features={brown, flat, table-like}, location=(200, 150)
```

**Step 4: Recognition**
```
O1: category=ball, properties={color=red, shape=sphere}
O2: category=table, properties={material=wood}
```

**Step 5: LoT Representation**
```
(O1 ^type ball ^color red ^shape sphere)
(O2 ^type table ^material wood)
(RELATION ^subject O1 ^predicate on ^object O2)
```

---

### 5.7 Language Grounding

#### 5.7.1 The Challenge

Language provides symbolic descriptions: "The red ball is on the table."

Grounding language requires connecting linguistic symbols to perceptual/motor experience.

**Definition 5.5 (Language Grounding)**: Mapping from linguistic expressions to their referents in the world or in perception.

#### 5.7.2 Reference Resolution

**Definite Descriptions**: "The red ball" → find unique entity matching description
$$ref(\text{"the red ball"}) = \{e : ball(e) \land red(e) \land unique(e)\}$$

**Anaphora**: "Put it on the table" → resolve "it"
$$ref(\text{"it"}) = resolve\_anaphor(\text{"it"}, context)$$

**Deixis**: "This one" + pointing → combine language with gesture
$$ref(\text{"this one"} + gesture) = attended\_entity(gesture)$$

#### 5.7.3 Compositional Grounding

Language is compositional. Grounding should respect this.

**Principle**: The meaning of a phrase is determined by the meanings of its parts and how they combine.

$$G(\text{"red ball"}) = G(\text{"red"}) \cap G(\text{"ball"})$$
$$G(\text{"ball on table"}) = \{(b,t) : G(\text{"ball"})(b) \land G(\text{"table"})(t) \land on(b,t)\}$$

#### 5.7.4 Vision-Language Models

Modern systems (CLIP, ALIGN, etc.) learn joint representations:

$$similarity = f_{visual}(image) \cdot f_{text}(description)$$

These can be used for grounding:
```
Given: Image I, phrase "red ball"
Find: Region R such that similarity(crop(I, R), "red ball") is maximized
```

---

### 5.8 Embodied Grounding

#### 5.8.1 Beyond Passive Perception

**Embodied cognition thesis**: Cognition is shaped by having a body that acts in the world.

Grounding is not just perception — it involves action and interaction.

#### 5.8.2 Affordances

**Definition 5.6 (Affordance)** (Gibson, 1979): An affordance is an action possibility offered by the environment to an agent.

**Examples**:
- A chair affords sitting
- A handle affords grasping
- A ball affords throwing

**Formal Model**:
$$affordance(object, agent) = \{a \in Actions : canPerform(agent, a, object)\}$$

#### 5.8.3 Grounding Through Interaction

**Active Perception**: Explore to disambiguate
- Turn object to see other side
- Poke object to assess rigidity
- Lift object to assess weight

**Learning from Interaction**:
```
loop:
    action = policy(state)
    new_state, feedback = environment.step(action)
    update_grounding(symbol, feedback)
```

**Example**: Learning what "heavy" means
```
For each object O:
    Attempt to lift O
    Measure force required
    If force > threshold:
        O ∈ extension("heavy")
```

---

### 5.9 Grounding and Transparency

#### 5.9.1 Connection to Chapter 3

Grounded representations support transparency:

**Explanation**: "I classified this as a cat because it has features F1, F2, F3 matching my grounded concept CAT."

**Verification**: External observers can check if features F1, F2, F3 are actually present.

**Correction**: If incorrect, adjust the grounding: "When F4 is present without F5, it's not a cat."

#### 5.9.2 Grounding Provenance

Track how symbols became grounded:

```
GroundedSymbol = {
    symbol: Symbol
    grounding: Grounding
    provenance: {
        source: Percept | Interaction | Learning
        timestamp: Time
        confidence: Float
        evidence: List<Evidence>
    }
}
```

---

### 5.10 Summary

Symbol grounding connects formal representations to the world:

1. **Perceptual grounding** connects symbols to sensory patterns
2. **Attention** selects relevant information for processing
3. **Binding** groups features into coherent object representations
4. **Recognition** maps percepts to categories and symbols
5. **Language grounding** connects linguistic expressions to referents
6. **Embodied grounding** involves action and interaction, not just passive perception

Grounding is essential for meaning — without it, symbols are empty.

---

### Key Concepts

- **Symbol grounding problem**: How symbols get intrinsic meaning
- **Attention**: Selective allocation of processing resources
- **Binding**: Grouping features into coherent objects
- **Affordance**: Action possibility offered by environment
- **Language grounding**: Connecting language to world

---

### Exercises

**5.1** Design a grounding system for the concept "fragile". What percepts, actions, and experiences would contribute to grounding this symbol?

**5.2** Implement an attention mechanism that combines bottom-up salience with top-down goals. Test on a visual search task.

**5.3** The word "bank" is ambiguous (river bank vs. financial bank). How would a grounding system disambiguate based on context?

**5.4** Prove: If grounding respects compositionality and intersective adjectives, then G(Adj(N)) = G(Adj) ∩ G(N).

**5.5** Design experiments to evaluate whether a vision-language model has "true" grounding vs. superficial correlations.

---

### Further Reading

- Harnad, S. (1990). "The symbol grounding problem." *Physica D*, 42, 335-346.
- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin.
- Barsalou, L. W. (2008). "Grounded cognition." *Annual Review of Psychology*, 59, 617-645.
- Radford, A., et al. (2021). "Learning transferable visual models from natural language supervision." *ICML*.

---

*End of Chapter 5*
