# Chapter 9

## Memory Systems

---

### 9.1 Introduction

Memory is foundational to intelligence. Without memory:
- No learning from experience (nothing persists)
- No reasoning (no premises to draw from)
- No planning (no goals or world models)
- No identity (no continuity of self)

This chapter examines memory from cognitive and computational perspectives, distinguishing genuine memory from the parameter storage of current ML systems (see Chapter 6).

---

### 9.2 What Is Memory?

#### 9.2.1 Memory vs. Storage

**Storage**: Information written to a medium and potentially retrievable.
**Memory**: Information encoded, organized, consolidated, and retrievable in context-appropriate ways.

The distinction is crucial:
- A hard drive has storage
- A human has memory
- Current ML models have parameter storage, not memory

**Definition 9.1 (Cognitive Memory)**: A system has cognitive memory if it:
1. Encodes experiences in structured form
2. Organizes information by meaning and relation
3. Retrieves information based on relevance to current context
4. Updates and reorganizes based on new experiences
5. Distinguishes what is remembered from inference

#### 9.2.2 Memory Functions

**Encoding**: Transforming experience into storable representation
**Storage**: Maintaining information over time
**Consolidation**: Strengthening and reorganizing stored information
**Retrieval**: Accessing stored information when needed
**Forgetting**: Losing access to information (adaptive or pathological)

---

### 9.3 Types of Memory

#### 9.3.1 Temporal Classification

**Sensory Memory**: Ultra-short retention of sensory input
- Iconic (visual): ~250ms
- Echoic (auditory): ~2-4 seconds
- Function: Buffer for perceptual processing

**Short-Term / Working Memory**: Active maintenance of information
- Duration: Seconds to minutes
- Capacity: 4 ± 1 chunks (Cowan, 2001)
- Function: Workspace for current processing

**Long-Term Memory**: Persistent storage
- Duration: Minutes to lifetime
- Capacity: Effectively unlimited
- Function: Knowledge base for reasoning and behavior

#### 9.3.2 Content Classification

**Declarative (Explicit) Memory**: Facts and events
- **Semantic**: General knowledge ("Paris is in France")
- **Episodic**: Personal experiences ("I visited Paris in 2019")

**Procedural (Implicit) Memory**: Skills and habits
- Motor skills (riding a bicycle)
- Cognitive skills (reading)
- Conditioning (learned responses)

**Diagram**:
```
                    Long-Term Memory
                          │
            ┌─────────────┴─────────────┐
            │                           │
      Declarative                  Procedural
      (Explicit)                   (Implicit)
            │                           │
      ┌─────┴─────┐               ┌─────┴─────┐
      │           │               │           │
   Semantic   Episodic        Skills      Conditioning
```

---

### 9.4 Working Memory

#### 9.4.1 The Workspace

Working memory is the "mental workspace" where current thinking happens.

**Baddeley's Model** (2000):
- **Central Executive**: Attention control, coordination
- **Phonological Loop**: Verbal/acoustic information
- **Visuospatial Sketchpad**: Visual/spatial information
- **Episodic Buffer**: Integration, connection to LTM

```
          ┌──────────────────────────────┐
          │      Central Executive       │
          │    (attention, control)      │
          └──────────────────────────────┘
                 │          │
       ┌─────────┴──────────┴─────────┐
       │              │               │
┌──────▼──────┐ ┌─────▼─────┐ ┌───────▼───────┐
│ Phonological│ │ Episodic  │ │ Visuospatial  │
│    Loop     │ │  Buffer   │ │   Sketchpad   │
└─────────────┘ └───────────┘ └───────────────┘
```

#### 9.4.2 Capacity Limits

**Miller's Magic Number**: 7 ± 2 items
**Modern Revision**: 4 ± 1 chunks (Cowan, 2001)

**Chunking**: Combining items into meaningful units increases effective capacity.
- "F B I C I A N S A" = 9 items
- "FBI CIA NSA" = 3 chunks

#### 9.4.3 Computational Model

```python
class WorkingMemory:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.contents = []
        self.focus = None  # Current focus of attention
        
    def add(self, item):
        if len(self.contents) >= self.capacity:
            self.decay_oldest()
        self.contents.append(item)
        self.focus = item
        
    def retrieve(self, cue):
        """Retrieve item matching cue, if any."""
        for item in self.contents:
            if matches(item, cue):
                return item
        return None
        
    def decay_oldest(self):
        """Remove least recent/relevant item."""
        if self.contents:
            # Remove item with lowest activation
            lowest = min(self.contents, key=lambda x: x.activation)
            self.contents.remove(lowest)
```

---

### 9.5 Long-Term Memory

#### 9.5.1 Encoding

**Levels of Processing** (Craik & Lockhart, 1972):
- Shallow processing (perceptual): Poor retention
- Deep processing (semantic): Good retention

**Encoding Specificity**: Memory is better when retrieval context matches encoding context.

**Elaborative Encoding**: Connecting new information to existing knowledge improves retention.

#### 9.5.2 Organization

Long-term memory is organized, not random:

**Semantic Networks**: Concepts connected by relations
```
        Animal
       /      \
    Bird      Mammal
    /  \      /    \
 Robin Eagle  Dog   Cat
```

**Schemas**: Structured knowledge about typical situations
```
Restaurant Schema:
  - Enter
  - Wait to be seated (or seat yourself)
  - Read menu
  - Order
  - Eat
  - Pay
  - Leave tip
  - Exit
```

**Scripts**: Event sequences for common situations

#### 9.5.3 Retrieval

**Retrieval Cues**: Information that triggers memory access
- Content-based: "What do you know about Paris?"
- Context-based: "What happened yesterday?"
- Association-based: "What does this remind you of?"

**Spreading Activation**: Activation spreads from retrieval cue through semantic network:
$$A_i(t+1) = A_i(t) + \sum_j w_{ij} A_j(t) - decay \cdot A_i(t)$$

**Retrieval Failure**: Information may be stored but inaccessible:
- Wrong cue (encoding specificity)
- Interference from similar memories
- Decay from disuse

#### 9.5.4 Computational Model

```python
class LongTermMemory:
    def __init__(self):
        self.semantic = SemanticNetwork()
        self.episodic = EpisodicStore()
        self.procedural = ProceduralStore()
        
    def encode(self, item, memory_type, context):
        """Encode new information."""
        representation = create_representation(item, context)
        
        if memory_type == 'semantic':
            self.semantic.add(representation)
        elif memory_type == 'episodic':
            representation.timestamp = now()
            representation.context = context
            self.episodic.add(representation)
        elif memory_type == 'procedural':
            self.procedural.add_rule(representation)
            
    def retrieve(self, cue, memory_type=None):
        """Retrieve matching information."""
        results = []
        
        # Spread activation from cue
        activated = self.spread_activation(cue)
        
        # Gather matching items above threshold
        for item in activated:
            if item.activation > RETRIEVAL_THRESHOLD:
                results.append(item)
                
        return sorted(results, key=lambda x: -x.activation)
        
    def spread_activation(self, cue):
        """Spread activation through memory network."""
        activated = {cue: 1.0}
        
        for _ in range(SPREAD_ITERATIONS):
            new_activations = {}
            for item, activation in activated.items():
                for neighbor, weight in item.connections:
                    if neighbor not in new_activations:
                        new_activations[neighbor] = 0
                    new_activations[neighbor] += activation * weight
            
            # Apply decay and merge
            for item in activated:
                activated[item] *= DECAY_FACTOR
            activated.update(new_activations)
            
        return activated
```

---

### 9.6 Episodic Memory

#### 9.6.1 The What, Where, When

Episodic memory encodes **specific experiences**:
- **What** happened
- **Where** it happened
- **When** it happened
- **Who** was involved
- **How** it felt (emotional coloring)

**Definition 9.2 (Episode)**: A memory trace encoding:
$$episode = (content, location, time, agents, affect, context)$$

#### 9.6.2 Distinguishing Features

Episodic memory differs from semantic memory:

| Feature | Semantic | Episodic |
|---------|----------|----------|
| Content | Facts | Events |
| Time reference | Timeless | Dated |
| Self-reference | None | Required |
| Consciousness | Knowing | Remembering |
| Source | Abstracted | Preserved |

#### 9.6.3 Importance for AI

Episodic memory enables:
- **Learning from experience**: Remember what worked, what didn't
- **Analogy**: Retrieve similar past situations
- **Explanation**: "I did X because last time Y happened"
- **Social cognition**: Remember interactions with individuals
- **Self-model**: Maintain autobiography, identity

**Current AI Gap**: Most AI systems lack genuine episodic memory. They cannot remember specific interactions or learn from individual experiences.

---

### 9.7 Memory in Cognitive Architectures

#### 9.7.1 Soar

**Working Memory**: Holds current state, goals, operators
- Attribute-value pairs: `(S1 ^name state ^goal G1)`
- Contents change each cycle

**Long-Term Memory**:
- **Procedural**: Production rules
- **Semantic**: Facts in semantic memory
- **Episodic**: Stored episodes, cue-based retrieval

#### 9.7.2 ACT-R

**Buffers**: Limited-capacity interface to modules
**Declarative Memory**: Chunks with activation levels

**Activation Equation**:
$$A_i = B_i + \sum_j W_j S_{ji}$$

- $B_i$: Base-level activation (recency + frequency)
- $S_{ji}$: Associative strength from element j to chunk i
- $W_j$: Attentional weight on source j

**Base-Level Learning**:
$$B_i = \ln\left(\sum_{j=1}^{n} t_j^{-d}\right)$$

Where $t_j$ is time since jth presentation, $d$ is decay parameter (~0.5).

#### 9.7.3 Memory Integration

```
                    ┌─────────────────┐
                    │ Working Memory  │
                    │ (current focus) │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│    Semantic     │ │    Episodic     │ │   Procedural    │
│    Memory       │ │    Memory       │ │    Memory       │
│  (facts, concepts)│ │  (experiences)  │ │  (skills, rules)│
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

---

### 9.8 Memory vs. ML "Memory"

#### 9.8.1 What LLMs Have

**Parameter Memory**: Statistics from training encoded in weights
- No explicit storage of facts
- No retrieval process
- No timestamps or sources
- No update during deployment

**Context Window**: Recent conversation
- Short duration (ephemeral)
- Limited size
- Lost when conversation ends
- No consolidation

#### 9.8.2 What LLMs Lack

Genuine memory requires:

| Feature | Human Memory | LLM |
|---------|--------------|-----|
| Encoding | Yes | No (after training) |
| Organized storage | Yes | No (implicit in weights) |
| Selective retrieval | Yes | No |
| Source attribution | Yes | No |
| Episodic dating | Yes | No |
| Update from experience | Yes | No |
| Forgetting control | Yes | No |

#### 9.8.3 Toward Genuine Memory in AI

**Memory-Augmented Systems**:
- External memory stores
- Retrieval mechanisms (nearest neighbor, attention)
- Read/write operations

**Example Architecture**:
```
Query → [Encoder] → query_vector
                         │
                         ▼
            ┌─────────────────────┐
            │   Memory Store      │
            │   (key, value pairs)│
            └─────────────────────┘
                         │
                         ▼
              attention(query, keys)
                         │
                         ▼
              weighted sum of values
                         │
                         ▼
                    Retrieved info
```

**Limitations**: Current memory-augmented systems still lack:
- Meaningful organization
- True consolidation
- Episodic structure
- Selective forgetting

---

### 9.9 Forgetting

#### 9.9.1 Adaptive Forgetting

Forgetting is not just failure — it can be adaptive:
- **Interference reduction**: Remove competing memories
- **Generalization**: Forget details, retain patterns
- **Relevance filtering**: Forget irrelevant information

#### 9.9.2 Mechanisms

**Decay**: Memories weaken without use
$$strength(t) = strength_0 \cdot e^{-\lambda t}$$

**Interference**: New memories compete with old
- Proactive: Old interferes with new
- Retroactive: New interferes with old

**Retrieval Failure**: Memory exists but cannot be accessed

#### 9.9.3 Computational Forgetting

In AI systems, forgetting is a problem:
- **Catastrophic forgetting**: Neural networks forget old tasks when learning new ones
- **Memory overflow**: Fixed-size stores must discard information

**Solutions**:
- Elastic weight consolidation (protect important weights)
- Replay (rehearse old memories)
- Modular memories (separate stores)
- Importance-weighted retention

---

### 9.10 Summary

Memory is essential for intelligence:

1. **Working memory** provides limited-capacity workspace
2. **Semantic memory** stores facts and concepts
3. **Episodic memory** stores specific experiences
4. **Procedural memory** stores skills and procedures

Genuine memory involves encoding, organization, retrieval, and update — not just parameter storage.

Current ML systems lack genuine memory, which limits their ability to learn from experience, maintain context, and exhibit genuine understanding.

---

### Key Concepts

- **Working memory**: Limited-capacity active workspace
- **Declarative memory**: Facts (semantic) and events (episodic)
- **Procedural memory**: Skills and procedures
- **Spreading activation**: Retrieval via associative networks
- **Encoding specificity**: Context-dependent retrieval

---

### Exercises

**9.1** Implement a spreading activation retrieval algorithm. Test it on a small semantic network.

**9.2** Design an episodic memory system for a conversational agent. What should be stored? How should retrieval work?

**9.3** Compare memory retrieval in ACT-R (activation-based) and Soar (cue-based). What are the tradeoffs?

**9.4** Analyze the "memory" claims of a commercial AI product. Does it have genuine memory by the criteria in this chapter?

**9.5** Design an experiment to distinguish genuine episodic memory from pattern completion in a neural network.

---

### Further Reading

- Baddeley, A. (2007). *Working Memory, Thought, and Action*. Oxford University Press.
- Tulving, E. (2002). "Episodic memory: From mind to brain." *Annual Review of Psychology*, 53, 1-25.
- Anderson, J. R. (2007). *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press.
- Graves, A., et al. (2014). "Neural Turing Machines." *arXiv:1410.5401*.

---

*End of Chapter 9*
