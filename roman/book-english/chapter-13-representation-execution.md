# Chapter 13

## From Representation to Execution

---

### 13.1 Introduction

The previous chapters established how to represent knowledge (Language of Thought), how to reason over it (inference engines), and why current ML systems fall short (the learning illusion). But representation alone is insufficient. Intelligence requires **action**.

This chapter examines the complete pipeline from language to execution:

1. How languages are compiled and interpreted
2. The role of intermediate representations
3. The evolution of the Web as a case study
4. Toward universal languages for intent and action

The central thesis: **A language is only as powerful as its interpreter.** Understanding this relationship is essential for building systems that bridge representation and action.

---

### 13.2 The Compilation Pipeline

#### 13.2.1 From Source to Execution

Every language requires a path from source to execution:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Source    │ → │   Parser    │ → │     IR      │ → │  Executor   │
│   Language  │    │  (Syntax)   │    │ (Semantics) │    │  (Action)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Definition 13.1 (Compilation)**: The transformation of a source language S into a target language T, preserving semantic equivalence:

$$\forall p \in S: \text{meaning}(p) = \text{meaning}(\text{compile}(p))$$

**Definition 13.2 (Interpretation)**: Direct execution of source language constructs without explicit target language generation.

The distinction is implementation strategy, not fundamental — both require semantic understanding.

#### 13.2.2 Phases of Compilation

**Phase 1: Lexical Analysis (Tokenization)**
```
"x = 3 + y * 2" → [ID:x, ASSIGN, NUM:3, PLUS, ID:y, MULT, NUM:2]
```

- Input: Character stream
- Output: Token stream
- Formalism: Regular expressions / Finite automata (Chapter 2.5)

**Phase 2: Syntactic Analysis (Parsing)**
```
Tokens → Abstract Syntax Tree (AST)

        (=)
       /   \
      x    (+)
          /   \
         3    (*)
             /   \
            y     2
```

- Input: Token stream
- Output: Parse tree / AST
- Formalism: Context-free grammars (Chapter 2.5)

**Phase 3: Semantic Analysis**
```
AST + Symbol Table → Annotated AST

- Type checking: Is y numeric?
- Scope resolution: Which x?
- Constraint verification: Types compatible?
```

- Input: AST
- Output: Annotated AST with semantic information
- Formalism: Attribute grammars, type systems

**Phase 4: Intermediate Representation (IR)**
```
Annotated AST → IR

t1 = y * 2
t2 = 3 + t1
x = t2
```

- Input: Annotated AST
- Output: Platform-independent intermediate code
- Purpose: Optimization, portability

**Phase 5: Optimization**
```
IR → Optimized IR

- Constant folding: 3 + 5 → 8
- Dead code elimination
- Loop optimization
- Register allocation
```

**Phase 6: Code Generation**
```
Optimized IR → Target Code

MOV R1, y
MUL R1, 2
ADD R1, 3
MOV x, R1
```

#### 13.2.3 Intermediate Representations

**Why IR Matters**:
- Decouples source from target (M sources × N targets → M + N compilers, not M × N)
- Enables optimization independent of source/target
- Provides semantic abstraction

**Common IR Forms**:

**Three-Address Code (TAC)**:
```
t1 = a + b
t2 = t1 * c
x = t2
```

**Static Single Assignment (SSA)**:
```
t1 = a + b
t2 = t1 * c
x1 = t2
```
Each variable assigned exactly once — enables powerful optimizations.

**Control Flow Graph (CFG)**:
```
    ┌───────┐
    │ Entry │
    └───┬───┘
        │
    ┌───▼───┐
    │ i = 0 │
    └───┬───┘
        │
    ┌───▼───┐ ◄──────┐
    │ i < n │        │
    └───┬───┘        │
      T │            │
    ┌───▼───┐        │
    │ body  │────────┘
    └───────┘
      F │
    ┌───▼───┐
    │ Exit  │
    └───────┘
```

**Abstract Syntax Tree (AST)**:
Preserves source structure, used for refactoring, analysis.

---

### 13.3 The Web as Case Study

The World Wide Web provides a rich case study in the evolution from documents to data to actions.

#### 13.3.1 Web 1.0: Documents (HTML)

**The Original Vision** (Berners-Lee, 1989):
Hypertext documents linked together.

**HTML as Language**:
```html
<html>
  <head><title>My Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a <a href="other.html">link</a>.</p>
  </body>
</html>
```

**Compilation Pipeline**:
```
HTML Source → Parser → DOM Tree → Layout Engine → Pixels
```

**The DOM (Document Object Model)**:
```
Document
├── html
│   ├── head
│   │   └── title: "My Page"
│   └── body
│       ├── h1: "Welcome"
│       └── p
│           ├── text: "This is a "
│           ├── a[href="other.html"]: "link"
│           └── text: "."
```

The DOM is the **IR** of the web — a structured representation enabling:
- Style application (CSS)
- Script manipulation (JavaScript)
- Accessibility tools
- Search engine indexing

**Limitation**: HTML encodes **presentation**, not **meaning**.

```html
<span class="price">$29.99</span>
```
A human sees a price. A machine sees styled text.

#### 13.3.2 Web 2.0: Applications (JavaScript)

**The Shift**: From documents to applications.

**JavaScript as Universal Runtime**:
```javascript
document.querySelector('.price').textContent = '$24.99';
```

The browser became a **virtual machine**:
```
JavaScript → Parser → AST → Bytecode → JIT Compiler → Machine Code
```

**Modern JS Engines** (V8, SpiderMonkey):
- Parse to AST
- Generate bytecode
- Profile hot paths
- JIT compile to native code
- Deoptimize if assumptions break

**The DOM as Mutable State**:
```
User Input → Event Handler → DOM Mutation → Re-render → Pixels
```

**Limitation**: Data is trapped in applications, not accessible to machines.

#### 13.3.3 Web 3.0: Semantic Web (RDF/OWL)

**The Vision** (Berners-Lee, 2001): A web of **data**, not just documents.

**RDF (Resource Description Framework)**:
Everything is triples: (Subject, Predicate, Object)

```turtle
@prefix ex: <http://example.org/> .
@prefix schema: <http://schema.org/> .

ex:product123 a schema:Product ;
    schema:name "Widget" ;
    schema:price "29.99" ;
    schema:priceCurrency "USD" .
```

**The Triple Store as IR**:
```
┌─────────────────┬────────────────┬─────────────┐
│ Subject         │ Predicate      │ Object      │
├─────────────────┼────────────────┼─────────────┤
│ ex:product123   │ rdf:type       │ schema:Product │
│ ex:product123   │ schema:name    │ "Widget"    │
│ ex:product123   │ schema:price   │ "29.99"     │
└─────────────────┴────────────────┴─────────────┘
```

**SPARQL as Query Language**:
```sparql
SELECT ?product ?price
WHERE {
  ?product a schema:Product ;
           schema:price ?price .
  FILTER (?price < 30)
}
```

**OWL (Web Ontology Language)**:
Adds reasoning capabilities via Description Logic (Chapter 2.5.6).

```turtle
ex:Father owl:equivalentClass [
    owl:intersectionOf (ex:Parent ex:Male)
] .
```

**Inference**:
```
Given: ex:john a ex:Parent ; ex:Male .
Infer: ex:john a ex:Father .
```

**The Semantic Web Stack**:
```
┌─────────────────────────────────────┐
│           Trust / Proof             │
├─────────────────────────────────────┤
│         Logic / Rules (OWL)         │
├─────────────────────────────────────┤
│      Ontology (RDFS/OWL)            │
├─────────────────────────────────────┤
│      Data Model (RDF)               │
├─────────────────────────────────────┤
│      Identifiers (URI/IRI)          │
├─────────────────────────────────────┤
│      Syntax (XML/JSON-LD/Turtle)    │
└─────────────────────────────────────┘
```

**Limitation**: The Semantic Web describes **what is**, not **what to do**.

#### 13.3.4 Knowledge Graphs in Practice

**Schema.org**: Shared vocabulary for structured data on the web.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Widget",
  "offers": {
    "@type": "Offer",
    "price": "29.99",
    "priceCurrency": "USD"
  }
}
</script>
```

**Google Knowledge Graph**, **Wikidata**, **DBpedia**:
Massive knowledge bases built on semantic web principles.

**Impact**:
- Rich search results
- Voice assistant understanding
- Recommendation systems

**But**: Still primarily **descriptive**, not **actionable**.

---

### 13.4 Operating Systems as Interaction Languages

An often-overlooked insight: **operating systems are languages**. They translate human intentions (gestures, commands) into machine actions. Understanding this reveals deep connections between HCI, linguistics, and computation.

#### 13.4.1 What Is an Operating System?

**Definition 13.8 (Operating System)**: A software layer that:
1. **Manages resources** (CPU, memory, storage, I/O)
2. **Provides abstractions** (files, processes, windows)
3. **Interprets user intentions** into hardware actions

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Intentions                          │
│    (click, type, drag, speak, gesture, command)                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Input Processing Layer                        │
│   Mouse → coordinates    Keyboard → keycodes    Touch → gestures │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      Event System (IR)                           │
│   MouseClickEvent(x=340, y=120, button=left, target=button#save) │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     Window Manager / Shell                       │
│            Route event to application, manage focus              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     Application Logic                            │
│                 Execute handler: saveFile()                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      System Calls                                │
│    write(fd, buffer, size) → Kernel → Disk Controller            │
└─────────────────────────────────────────────────────────────────┘
```

The OS is a **compiler** from human gesture to hardware instruction.

#### 13.4.2 The Gesture-Action Compilation Pipeline

**Input Modalities as Source Languages**:

| Modality | Lexemes | Grammar | Semantics |
|----------|---------|---------|-----------|
| **Mouse** | click, move, scroll, drag | sequences, patterns | select, scroll, move, resize |
| **Keyboard** | keypress, keyrelease | chords, sequences | type, shortcut, navigate |
| **Touch** | tap, swipe, pinch, hold | multi-finger gestures | select, scroll, zoom, context |
| **Voice** | phonemes → words | sentences | commands, dictation |
| **Pen** | stroke, pressure, tilt | handwriting, gestures | draw, write, annotate |

**The Double-Click Example**:
```
Physical: Button depression × 2, interval < 500ms
Lexical:  CLICK, CLICK (within threshold)
Syntactic: DOUBLE_CLICK pattern recognized
Semantic: "Open" intent (context-dependent)
Action:   launch_application(selected_item)
```

**Drag-and-Drop Compilation**:
```
Source:    MOUSE_DOWN(x₁,y₁) → MOUSE_MOVE*(x,y) → MOUSE_UP(x₂,y₂)
Parse:     DragGesture(start=(x₁,y₁), end=(x₂,y₂), path=[...])
Semantics: MoveIntent(object=icon_at(x₁,y₁), destination=drop_target_at(x₂,y₂))
Action:    mv /home/user/file.txt /home/user/archive/
```

#### 13.4.3 The Command Line: Text as Action Language

The **shell** (bash, zsh, PowerShell) is explicitly a language:

**Bash Grammar (simplified)**:
```bnf
<command>     ::= <simple_cmd> | <pipeline> | <compound_cmd>
<pipeline>    ::= <command> '|' <command>
<simple_cmd>  ::= <word>+ <redirection>*
<redirection> ::= '<' <file> | '>' <file> | '>>' <file>
<compound_cmd>::= '{' <command_list> '}' | 'if' <condition> 'then' <command_list> 'fi'
```

**Example Compilation**:
```bash
ls -la /home | grep ".txt" | wc -l
```
```
Parse Tree:
  Pipeline
  ├── SimpleCmd: ls [-la, /home]
  ├── SimpleCmd: grep [".txt"]
  └── SimpleCmd: wc [-l]

Execution:
  fork() → exec(ls) → pipe → fork() → exec(grep) → pipe → fork() → exec(wc)
  
Result: "42" (number of .txt files)
```

#### 13.4.4 Unix Philosophy: Everything Is a File

**Ken Thompson** and **Dennis Ritchie** (Unix creators) established:

> *"Everything is a file"* — Uniform interface for all resources

| Resource | File Interface |
|----------|---------------|
| Regular file | /home/user/doc.txt |
| Directory | /home/user/ |
| Device | /dev/sda1, /dev/tty0 |
| Process info | /proc/1234/status |
| Network | /dev/tcp/host/port |
| Pipe | Anonymous or /tmp/named_pipe |

**This is a language design decision**: By unifying the abstraction, the same operations (read, write, open, close) compose across all resources.

**The Power of Composition**:
```bash
cat /proc/cpuinfo | grep "model name" | uniq | tee cpu_info.txt
```
Four programs, never designed to work together, compose because they share the file abstraction.

#### 13.4.5 Graphical Shells: WIMP as Language

**WIMP**: Windows, Icons, Menus, Pointer — the grammar of GUI interaction.

**Xerox PARC** (1970s) established the metaphor:
- **Desktop** = workspace
- **Windows** = documents/tasks
- **Icons** = objects
- **Menus** = available actions
- **Pointer** = attention/selection

**Grammar of GUI Interaction**:
```bnf
<interaction>  ::= <selection> <action>
<selection>    ::= <click> | <drag_select> | <keyboard_focus>
<action>       ::= <menu_action> | <keyboard_shortcut> | <drag_drop> | <direct_manipulation>
<menu_action>  ::= <menu_open> <menu_navigate> <menu_select>
```

**Direct Manipulation** (Ben Shneiderman, 1983):
1. Continuous representation of objects
2. Physical actions instead of complex syntax
3. Rapid, reversible, incremental actions
4. Immediate visible feedback

This is **compilation at the speed of perception**: intent → action → feedback in milliseconds.

#### 13.4.6 Historical Evolution

| Era | Interface | Language Type | Intent Expression |
|-----|-----------|---------------|-------------------|
| 1950s | Patch panels | Hardware | Wire connections |
| 1960s | Batch cards | Formal (JCL) | Punch card sequences |
| 1970s | Terminal (Unix) | Text commands | Shell grammar |
| 1980s | GUI (Mac, Windows) | WIMP gestures | Point and click |
| 2000s | Touch (iOS, Android) | Multi-touch | Tap, swipe, pinch |
| 2010s | Voice (Siri, Alexa) | Natural language | Spoken commands |
| 2020s | Multimodal AI | Hybrid | Text + voice + gesture + context |

**Key Figures**:
- **Ken Thompson** & **Dennis Ritchie** — Unix, C, the shell paradigm
- **Linus Torvalds** — Linux, open-source OS development
- **Steve Jobs** & **Bill Atkinson** — Macintosh GUI, making WIMP mainstream
- **Alan Kay** — Object-oriented GUI concepts, Dynabook vision
- **Doug Engelbart** (1925–2013) — Mouse, hypertext, the "Mother of All Demos" (1968)

#### 13.4.7 The OS as IR Between Intent and Hardware

**Insight**: The operating system's **system call interface** is an Intermediate Representation:

```
User Intent (high-level)
        ↓
Application Logic (medium-level)
        ↓
System Calls (IR) ← Portable, well-defined interface
        ↓
Kernel Implementation (low-level)
        ↓
Hardware Instructions (machine-level)
```

**POSIX** (Portable Operating System Interface) standardizes this IR:
- `open()`, `read()`, `write()`, `close()` — File operations
- `fork()`, `exec()`, `wait()` — Process management
- `socket()`, `connect()`, `send()` — Networking
- `mmap()`, `brk()` — Memory management

**Why This Matters for AI**:
Future AI systems will need to **emit system calls** or **generate UI gestures** to act in the world. Understanding the OS as a language is prerequisite to building agents that can use computers as humans do.

```
AI Agent Intent: "Save this analysis to a PDF"
        ↓
Plan: [open_app("word"), paste(analysis), menu("File > Export > PDF"), specify_path(...)]
        ↓
Gesture Sequence: [click(x1,y1), paste_shortcut, click(x2,y2), click(x3,y3), type(path), enter]
        ↓
OS Events → Application → System Calls → Disk Write
```

---

### 13.5 Toward Intent Languages

The missing piece: languages that express **intent** — what an agent wants to achieve — not just data or procedures.

#### 13.5.1 The Intent Gap

Current languages express:
- **Data**: What exists (HTML, JSON, RDF)
- **Procedure**: How to do it (JavaScript, Python)
- **Query**: What to find (SQL, SPARQL)

Missing:
- **Intent**: What to achieve
- **Constraints**: What must hold
- **Preferences**: What matters

**Example Gap**:
```
Data:      "Flight AA123 departs 10:00"
Procedure: "book_flight('AA123')"
Intent:    "I want to arrive in Paris by evening, minimize cost"
```

Intent requires **planning**, not just execution.

#### 13.5.2 Action Languages

**STRIPS (1971)**: Stanford Research Institute Problem Solver

```
Action: Pick-Up(x)
Preconditions: HandEmpty ∧ Clear(x) ∧ OnTable(x)
Effects: Holding(x) ∧ ¬HandEmpty ∧ ¬OnTable(x)
```

**PDDL (Planning Domain Definition Language)**:
```pddl
(:action pick-up
  :parameters (?x - block)
  :precondition (and (clear ?x) (ontable ?x) (handempty))
  :effect (and (holding ?x)
               (not (ontable ?x))
               (not (clear ?x))
               (not (handempty))))
```

**Compilation**: Intent + World State → Plan → Actions

```
Goal: On(A, B) ∧ On(B, C)
State: OnTable(A), OnTable(B), OnTable(C), Clear(A), Clear(B), Clear(C)

Plan:
  1. Pick-Up(C)
  2. Stack(C, Table)  ; No, wait...
  
Actually:
  1. Pick-Up(B)
  2. Stack(B, C)
  3. Pick-Up(A)
  4. Stack(A, B)
```

**Limitation**: PDDL requires complete world model. Real intents are vague.

#### 13.5.3 Proposing: Universal Intent Language (UIL)

A **hypothetical** language for expressing agent intentions:

**Design Goals**:
1. Express goals, not procedures
2. Handle uncertainty and preferences
3. Compositional and interpretable
4. Grounded in action capabilities

**Syntax Sketch**:
```uil
intent "travel to Paris" {
  goal: location(self) = Paris
  constraints: {
    time(arrival) <= 2024-12-20T18:00
    cost <= budget * 0.3
  }
  preferences: {
    minimize(cost, weight=0.6)
    minimize(duration, weight=0.4)
  }
  context: {
    current_location: "New York"
    budget: 5000 USD
  }
}
```

**Compilation Pipeline**:
```
UIL Intent → Parser → Intent IR → Planner → Action Sequence → Executor
```

**Intent IR**:
```
IntentGraph {
  goal: StateCondition(location, self, Paris)
  constraints: [
    TemporalConstraint(arrival, <=, DateTime(...)),
    ResourceConstraint(cost, <=, Expr(budget * 0.3))
  ]
  preferences: [
    Minimize(cost, 0.6),
    Minimize(duration, 0.4)
  ]
  context: Map{current_location: "New York", budget: 5000}
}
```

**Key Insight**: Intent is not a string to execute, but a **specification to satisfy**.

---

### 13.6 Document Languages: From Static to Living

#### 13.6.1 The Document Spectrum

```
Static ◄──────────────────────────────────────────────► Dynamic
  │                                                        │
  PDF          HTML           Jupyter         Live Code
  │              │               │                │
  Fixed      Rendered      Interactive      Executable
```

**Evolution**:
1. **PDF**: Fixed layout, portable, dead
2. **HTML**: Rendered, hyperlinked, mostly static
3. **Jupyter Notebook**: Executable cells, reproducible
4. **Live Documents**: Code + data + UI, continuously updating

#### 13.6.2 Proposing: .LIFE Document Format

A **hypothetical** universal document format combining:
- Content (text, media)
- Data (structured, queryable)
- Code (executable)
- Intent (what the document should do)

**Concept**:
```life
@document "quarterly-report" {
  
  @metadata {
    author: "Finance Team"
    created: 2024-12-15
    version: "1.0"
  }
  
  @section "Revenue" {
    @text "Q4 revenue was ${revenue.q4}."
    
    @data revenue {
      source: "database://sales/quarterly"
      query: "SELECT quarter, SUM(amount) FROM sales GROUP BY quarter"
      refresh: "daily"
    }
    
    @visualization {
      type: "bar-chart"
      data: revenue
      x: quarter
      y: amount
    }
    
    @intent "alert if revenue drops" {
      condition: revenue.q4 < revenue.q3 * 0.9
      action: notify(stakeholders, "Revenue alert")
    }
  }
}
```

**Compilation**:
```
.LIFE Source → Parser → Document IR → {
  Renderer → Visual Output
  Data Engine → Live Data
  Intent Engine → Automated Actions
}
```

**Key Properties**:
- **Declarative**: Specifies what, not how
- **Reactive**: Updates when data changes
- **Intentful**: Can trigger actions
- **Composable**: Documents reference documents

#### 13.6.3 The Living Document IR

```
DocumentIR {
  metadata: Map<String, Value>
  sections: List<Section>
  data_bindings: Map<Name, DataSource>
  intents: List<Intent>
  
  Section {
    content: List<ContentBlock>
    visualizations: List<Viz>
    nested: List<Section>
  }
  
  Intent {
    trigger: Condition
    action: ActionSpec
    context: BindingContext
  }
}
```

---

### 13.7 The Agentic Web

#### 13.7.1 From Documents to Agents

The web evolution:
- **Web 1.0**: Read documents
- **Web 2.0**: Read/write applications  
- **Web 3.0**: Read/write/reason over data
- **Web 4.0?**: Read/write/reason/act via agents

**The Agentic Web**: A web where:
- Documents express intents
- Agents interpret and execute intents
- Services expose capabilities, not just data
- Composition happens at intent level

#### 13.7.2 Agent Communication Languages

**KQML (Knowledge Query and Manipulation Language)**:
```kqml
(ask-one
  :sender agent1
  :receiver agent2
  :content (price widget ?x)
  :language KIF
  :ontology commerce)
```

**FIPA-ACL (Foundation for Intelligent Physical Agents)**:
```
(inform
  :sender agent1
  :receiver agent2
  :content ((price widget 29.99))
  :language fipa-sl)
```

**Speech Acts** (Austin, Searle):
- **Assertive**: Stating facts
- **Directive**: Requesting action
- **Commissive**: Committing to action
- **Expressive**: Expressing attitude
- **Declarative**: Changing state by declaration

#### 13.7.3 Capability Description

For agents to compose, they must describe capabilities:

**WSDL/SOAP** (Web Services):
```xml
<operation name="BookFlight">
  <input message="BookingRequest"/>
  <output message="BookingConfirmation"/>
</operation>
```

**OpenAPI/Swagger**:
```yaml
/flights/book:
  post:
    summary: Book a flight
    parameters:
      - name: flight_id
        in: query
        required: true
    responses:
      200:
        description: Booking confirmation
```

**Semantic Service Description** (OWL-S):
```turtle
ex:BookFlightService a owls:Service ;
  owls:presents ex:BookFlightProfile ;
  owls:describedBy ex:BookFlightProcess .

ex:BookFlightProfile
  owls:hasInput ex:FlightID ;
  owls:hasOutput ex:Confirmation ;
  owls:hasPrecondition ex:FlightAvailable ;
  owls:hasEffect ex:SeatReserved .
```

#### 13.7.4 The Agent Compilation Pipeline

```
User Intent (natural language)
        │
        ▼
┌───────────────────┐
│ Intent Parser     │ ← LLM as fuzzy front-end (Chapter 6.8)
│ (NL → UIL)        │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│ Intent Compiler   │ ← Formal verification
│ (UIL → Plan)      │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│ Service Discovery │ ← Capability matching
│ (Plan → Services) │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│ Orchestrator      │ ← Execution, monitoring
│ (Services → Actions) │
└───────┬───────────┘
        │
        ▼
    Real-World Effects
```

**Critical Insight**: Each stage has formal semantics. The LLM is **only** a fuzzy interface to the formal system, not the reasoning core.

#### 13.7.5 The Model Context Protocol (MCP)

A significant development in LLM-to-tool interaction emerged in 2024: the **Model Context Protocol (MCP)**, introduced by Anthropic. MCP represents a principled approach to connecting LLMs with external capabilities while maintaining clear separation of concerns.

**Design Philosophy**:
```
┌────────────────────────────────────────────────────────────────────┐
│                         MCP Architecture                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────┐         JSON-RPC/stdio        ┌──────────────┐  │
│  │              │ ◄──────────────────────────► │              │  │
│  │   MCP Host   │                              │  MCP Server  │  │
│  │   (LLM App)  │        Bidirectional         │   (Tools)    │  │
│  │              │ ◄──────────────────────────► │              │  │
│  └──────────────┘                              └──────────────┘  │
│        │                                              │          │
│        │ Decides:                          Provides:  │          │
│        │ • Which tool?                     • Formal execution    │
│        │ • What arguments?                 • Type validation     │
│        │ • When to call?                   • Error handling      │
│        │                                   • Result formatting   │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**Protocol Primitives**:

**1. Tools** — Executable functions with typed signatures
```json
{
  "name": "read_file",
  "description": "Read contents of a file",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": { "type": "string", "description": "File path to read" },
      "encoding": { "type": "string", "default": "utf-8" }
    },
    "required": ["path"]
  }
}
```

**2. Resources** — Data sources the LLM can access
```json
{
  "uri": "file:///project/config.json",
  "mimeType": "application/json",
  "name": "Project Configuration"
}
```

**3. Prompts** — Reusable prompt templates
```json
{
  "name": "code_review",
  "description": "Review code for issues",
  "arguments": [
    { "name": "code", "required": true },
    { "name": "language", "required": true }
  ]
}
```

**Interaction Flow**:
```
1. Discovery
   Host → Server: "capabilities/list"
   Server → Host: { tools: [...], resources: [...], prompts: [...] }

2. Tool Invocation
   Host → Server: { method: "tools/call", params: { name: "query_db", arguments: {...} } }
   Server: [validates input] → [executes] → [validates output]
   Server → Host: { result: {...} }

3. Error Handling
   Server → Host: { error: { code: -32602, message: "Invalid SQL syntax" } }
```

**Formal Properties**:

| Property | How MCP Achieves It |
|----------|---------------------|
| **Type Safety** | JSON Schema validation on inputs/outputs |
| **Discoverability** | Explicit capability listing protocol |
| **Auditability** | Every call logged with full context |
| **Composability** | Multiple servers can be connected |
| **Error Bounds** | Explicit error codes and messages |

**Comparison with Historical Protocols**:

```
Evolution of Agent-Tool Protocols:

1990s: KQML           ─────────┐
       (Agent↔Agent)           │
                               │    Common thread:
2000s: FIPA-ACL       ─────────┤    Separation of
       (Standardized)          │    interface from
                               │    implementation
2010s: REST/OpenAPI   ─────────┤
       (Web Services)          │
                               │
2024:  MCP            ─────────┘
       (LLM↔Tools)

Key difference: MCP designed specifically for LLM capabilities and limitations
```

**What MCP Gets Right**:

1. **LLM as Orchestrator, Not Oracle**
   - The LLM decides *what* to do
   - Formal systems decide *how* to do it
   - Clear responsibility boundary

2. **Explicit Contracts**
   - Tool capabilities are declared, not discovered by probing
   - Type schemas prevent malformed calls
   - Errors are structured, not string-matched

3. **Composability**
   - Multiple MCP servers can provide different capabilities
   - Host orchestrates across servers
   - No monolithic system required

4. **Progressive Trust**
   - Servers can require confirmation for sensitive operations
   - Hosts can sandbox or filter tool access
   - Permissions are explicit

**What MCP Does Not Solve**:

1. **Intent Verification**
   - MCP ensures tool calls are *well-formed*
   - Does not ensure they *achieve user intent*
   - The gap between "correctly called" and "correctly solved"

2. **Planning**
   - MCP is for individual tool calls
   - Multi-step planning still relies on LLM
   - No formal plan verification

3. **Semantic Grounding**
   - Tool descriptions are natural language
   - LLM interpretation is still statistical
   - No formal semantics for tool meaning

4. **Composition Correctness**
   - Calling tools A then B may have unintended interactions
   - No formal model of tool effects on state
   - Relies on LLM "understanding" consequences

**Example: Database Query**
```
User: "How many users signed up last month?"

1. LLM interprets intent
2. LLM generates tool call:
   { "name": "query_database", 
     "arguments": { "sql": "SELECT COUNT(*) FROM users WHERE created_at > '2024-11-01'" } }
3. MCP Server:
   - Validates SQL syntax ✓
   - Checks permissions ✓
   - Executes query
   - Returns: { "count": 1247 }
4. LLM formats response to user

What MCP guarantees: Query was valid SQL, executed correctly
What MCP cannot guarantee: Query captured user's actual intent
```

**MCP in the Agentic Stack**:
```
┌─────────────────────────────────────────────────────────────┐
│  Natural Language Intent                                     │
│  "Book me a flight to Paris, cheapest option"               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  LLM Interpretation (statistical, approximate)               │
│  → Extract: destination=Paris, constraint=minimize(cost)    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  MCP Tool Calls (formal, verified)                           │
│  1. search_flights({dest: "CDG", sort: "price"})            │
│  2. book_flight({flight_id: "AF123", ...})                  │
│  3. send_confirmation({email: user.email, ...})             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Real-World Effects                                          │
│  Flight booked, confirmation sent                            │
└─────────────────────────────────────────────────────────────┘

The gap: Between "LLM Interpretation" and "MCP Tool Calls"
        → Still relies on LLM correctness
        → MCP formalizes execution, not intent mapping
```

**Toward Complete Verification**:

MCP is a necessary but not sufficient component. A fully verified agentic system would require:

1. **Formal Intent Language** (Section 13.5): Parse NL to formal intent
2. **Intent Verification**: Prove tool sequence achieves intent
3. **MCP**: Execute verified plan through formal tools
4. **Effect Monitoring**: Verify real-world effects match expected

```
NL → [LLM] → Intent IR → [Verifier] → Plan → [MCP] → Tools → Effects
                   ↑                           ↓
                   └─────── Feedback ──────────┘
```

MCP handles the `Plan → Tools` boundary formally. The other boundaries remain research problems.

---

### 13.8 From Internet of Things to Internet of Agents

The evolution from connected devices to autonomous agents represents a fundamental shift in distributed computing — from systems that **emit data** to systems that **pursue goals**.

#### 13.8.1 The Internet of Things (IoT)

**Definition 13.12 (Internet of Things)**: A network of physical devices embedded with sensors, software, and connectivity that enables them to collect and exchange data.

**Architecture**:
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Sensor     │    │   Gateway    │    │    Cloud     │
│   Device     │───►│   (Edge)     │───►│   Platform   │
│              │    │              │    │              │
│  • Measure   │    │  • Aggregate │    │  • Store     │
│  • Transmit  │    │  • Filter    │    │  • Analyze   │
└──────────────┘    └──────────────┘    └──────────────┘
                                               │
                                               ▼
                                        ┌──────────────┐
                                        │  Dashboard   │
                                        │   (Human)    │
                                        │              │
                                        │  • Visualize │
                                        │  • DECIDE    │
                                        └──────────────┘
```

**Key Protocols**:
- **MQTT** (Message Queuing Telemetry Transport): Lightweight publish-subscribe
- **CoAP** (Constrained Application Protocol): REST for constrained devices
- **Zigbee/Z-Wave**: Low-power mesh networking
- **LoRaWAN**: Long-range, low-power WAN

**Characteristics**:
| Property | IoT Value |
|----------|-----------|
| Primary function | Data collection |
| Decision maker | Human or cloud service |
| Autonomy | Low (execute predefined rules) |
| Intelligence | Edge analytics, pattern detection |
| Communication | Device → Cloud (mostly unidirectional) |

**Limitations**:
- Devices are **passive** — they report, they don't decide
- Intelligence is **centralized** — in cloud or human
- Coordination is **top-down** — orchestrated by platform
- Adaptation requires **reprogramming** — not learning

#### 13.8.2 The Internet of Agents (IoA)

**Definition 13.13 (Internet of Agents)**: A network of autonomous agents that can perceive, reason, act, and negotiate to achieve goals, coordinating without central control.

**Architecture**:
```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Agent A    │◄───────►│   Agent B    │◄───────►│   Agent C    │
│              │         │              │         │              │
│  • Perceive  │         │  • Perceive  │         │  • Perceive  │
│  • Reason    │         │  • Reason    │         │  • Reason    │
│  • Plan      │         │  • Plan      │         │  • Plan      │
│  • Act       │         │  • Act       │         │  • Act       │
│  • DECIDE    │         │  • DECIDE    │         │  • DECIDE    │
└──────────────┘         └──────────────┘         └──────────────┘
       │                        │                        │
       │    ┌───────────────────┼───────────────────┐    │
       │    │                   │                   │    │
       ▼    ▼                   ▼                   ▼    ▼
┌─────────────────────────────────────────────────────────────┐
│                    Shared Environment / Services             │
│                                                              │
│   • World State    • Capability Registry    • Trust Network │
└─────────────────────────────────────────────────────────────┘
```

**Characteristics**:
| Property | IoA Value |
|----------|-----------|
| Primary function | Goal achievement |
| Decision maker | Each agent autonomously |
| Autonomy | High (reason, plan, adapt) |
| Intelligence | Distributed, emergent |
| Communication | Agent ↔ Agent (bidirectional negotiation) |

**Key Shift**:
```
IoT:   Device ──data──► Cloud ──command──► Device
             (Human decides)

IoA:   Agent ◄──negotiate──► Agent
             (Agents decide collectively)
```

#### 13.8.3 Comparison: IoT vs IoA

| Dimension | Internet of Things | Internet of Agents |
|-----------|-------------------|-------------------|
| **Unit** | Device/Sensor | Autonomous Agent |
| **Purpose** | Sense and transmit | Perceive, reason, act |
| **Control** | Centralized (cloud/human) | Decentralized (emergent) |
| **Communication** | Data streams | Speech acts, negotiations |
| **Adaptation** | Firmware updates | Learning, planning |
| **Coordination** | Orchestration | Cooperation/competition |
| **Trust** | Certificate-based | Reputation, verification |
| **Failure mode** | Device offline | Agent defection |
| **Protocols** | MQTT, CoAP | MCP, FIPA-ACL, (emerging) |
| **Example** | Smart thermostat | Autonomous trading agent |

**Historical Precedents**:
- **Multi-Agent Systems** (1990s-2000s): JADE, Jason, academic MAS
- **Semantic Web Services** (2000s): OWL-S, automatic composition
- **Blockchain/DAOs** (2010s): Decentralized autonomous organizations
- **LLM Agents** (2020s): AutoGPT, BabyAGI, multi-agent frameworks

#### 13.8.4 Protocol Requirements for IoA

**What IoT Protocols Lack**:
1. **Semantic Content**: MQTT sends bytes, not meanings
2. **Negotiation**: No protocol for offer/counter-offer
3. **Commitment**: No concept of promises or obligations
4. **Verification**: No proof that claims are true

**What IoA Protocols Need**:

**1. Agent Communication Language (ACL)**
```
(request
  :sender    agent-buyer
  :receiver  agent-seller
  :content   (sell item-123 :price < 100)
  :reply-by  2024-12-20T18:00:00Z
  :protocol  negotiation-v1)
```

**2. Capability Description**
```yaml
agent: travel-booker-agent
capabilities:
  - name: book_flight
    inputs: [origin, destination, date, constraints]
    outputs: [booking_confirmation, price]
    preconditions: [valid_route, available_seats]
    effects: [seat_reserved, payment_authorized]
    trust_level: verified
```

**3. Commitment Protocol**
```
1. Agent A: propose(action, conditions)
2. Agent B: accept(action) | reject(action) | counter(action')
3. If accept: commit(A, action) — creates obligation
4. If execute: done(action) | fail(action, reason)
5. Track: obligation fulfilled | violated
```

**4. Verification Layer**
```
claim: "I booked flight AF123"
evidence: 
  - booking_id: XYZ789
  - signature: agent-travel-booker
  - timestamp: 2024-12-15T10:30:00Z
  - verifiable_credential: booking_system_attestation
verification: 
  - check signature
  - query booking system
  - match details
```

#### 13.8.5 Emergent Behaviors and Challenges

**Emergence in Agent Networks**:

When many agents interact, complex behaviors emerge that no single agent intended:

| Emergent Phenomenon | Description | Challenge |
|---------------------|-------------|-----------|
| **Markets** | Price discovery through bid/ask | Manipulation, bubbles |
| **Reputation** | Trust scores from interactions | Gaming, Sybil attacks |
| **Norms** | Conventions for coordination | Enforcement, evolution |
| **Coalitions** | Temporary alliances | Stability, fairness |
| **Cascades** | Viral behavior propagation | Runaway effects |

**Key Challenges**:

**1. Trust Without Central Authority**
- How does Agent A trust Agent B's claims?
- Reputation systems, cryptographic proofs, track records
- But: Sybil attacks, identity manipulation

**2. Coordination Without Orchestration**
- How do 1000 agents cooperate without a coordinator?
- Mechanism design, game theory, emergent conventions
- But: Deadlocks, inefficiency, free-riders

**3. Alignment at Scale**
- Individual agents may be aligned; collective behavior may not be
- "Tragedy of the commons" in agent networks
- Need: Multi-agent alignment theory

**4. Security and Adversarial Agents**
- Some agents may be malicious or compromised
- Attack vectors: false claims, denial of service, collusion
- Need: Byzantine fault tolerance for agent networks

**5. Legal and Ethical Accountability**
- Who is responsible when autonomous agents cause harm?
- Agents acting on behalf of humans, organizations, or other agents
- Need: Legal frameworks for agent liability

#### 13.8.6 Architecture for IoA

**Layered Architecture**:
```
┌─────────────────────────────────────────────────────────────────────┐
│  Application Layer                                                   │
│  • Agent goals and behaviors                                        │
│  • Domain-specific logic                                            │
├─────────────────────────────────────────────────────────────────────┤
│  Coordination Layer                                                  │
│  • Negotiation protocols                                            │
│  • Commitment management                                            │
│  • Coalition formation                                              │
├─────────────────────────────────────────────────────────────────────┤
│  Communication Layer                                                 │
│  • Agent Communication Language (FIPA-ACL, MCP, ...)               │
│  • Message routing and delivery                                     │
│  • Conversation management                                          │
├─────────────────────────────────────────────────────────────────────┤
│  Trust Layer                                                         │
│  • Identity and authentication                                      │
│  • Reputation systems                                               │
│  • Verifiable credentials                                           │
├─────────────────────────────────────────────────────────────────────┤
│  Transport Layer                                                     │
│  • Network protocols (TCP/IP, WebSocket, ...)                       │
│  • Discovery and addressing                                         │
│  • Quality of service                                               │
└─────────────────────────────────────────────────────────────────────┘
```

**Agent Registry and Discovery**:
```json
{
  "agent_id": "travel-agent-42",
  "endpoint": "wss://agents.example.com/travel-42",
  "capabilities": ["flight_booking", "hotel_booking", "itinerary_planning"],
  "protocols": ["MCP-v1", "FIPA-ACL"],
  "trust_score": 0.94,
  "verified_by": ["trust-authority-1", "trust-authority-2"],
  "rate_limits": { "requests_per_minute": 100 },
  "pricing": { "model": "per_request", "base": 0.01 }
}
```

#### 13.8.7 The Future: Hybrid IoT + IoA

The future is not replacement but integration:

```
┌───────────────────────────────────────────────────────────────────┐
│                        Hybrid Architecture                         │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│   ┌─────────────┐                           ┌─────────────┐       │
│   │  IoT Layer  │                           │  IoA Layer  │       │
│   │             │                           │             │       │
│   │  Sensors    │───── data ─────►         │  Agents     │       │
│   │  Actuators  │◄──── commands ────        │             │       │
│   │  Edge       │                           │  Negotiate  │       │
│   │             │                           │  Decide     │       │
│   └─────────────┘                           │  Coordinate │       │
│         │                                   └─────────────┘       │
│         │                                          │              │
│         ▼                                          ▼              │
│   ┌─────────────────────────────────────────────────────────┐    │
│   │                  Shared World Model                      │    │
│   │                                                          │    │
│   │   Physical state (from IoT) + Agent beliefs and goals   │    │
│   └─────────────────────────────────────────────────────────┘    │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘

IoT provides: perception, actuation, physical grounding
IoA provides: reasoning, planning, coordination, decision-making
```

**Example: Smart Building**

| Component | Role |
|-----------|------|
| Temperature sensors (IoT) | Report current temperature |
| Occupancy sensors (IoT) | Detect people in rooms |
| HVAC actuators (IoT) | Execute heating/cooling commands |
| Comfort Agent (IoA) | Optimize comfort for occupants |
| Energy Agent (IoA) | Minimize energy consumption |
| Schedule Agent (IoA) | Predict occupancy patterns |
| **Negotiation** | Agents negotiate comfort vs. energy tradeoffs |

The IoT layer provides the **physical interface**; the IoA layer provides the **intelligence**.

#### 13.8.8 Key Figures and Research

**Foundational Work**:
- **Michael Wooldridge** — Multi-agent systems textbook and theory
- **Nicholas Jennings** — Agent-based computing, social reasoning
- **Yoav Shoham** — Agent-oriented programming, mechanism design
- **Tim Finin** — KQML, agent communication languages
- **Kevin Ashton** — Coined "Internet of Things" (1999)

**Current Directions**:
- **LangChain/AutoGPT** communities — LLM-based agent frameworks
- **CrewAI, MetaGPT** — Multi-agent orchestration
- **Anthropic MCP** — Standardized agent-tool interaction
- **Academic MAS** — AAMAS conference, agent theory

---

### 13.9 Universal Representation Languages

#### 13.9.1 The Quest for Universality

History of "universal" languages:

| Era | Language | Claim | Reality |
|-----|----------|-------|---------|
| 1960s | LISP | Universal computation | Turing complete, not universal representation |
| 1970s | Prolog | Universal inference | Limited to Horn clauses |
| 1980s | KIF | Universal knowledge | Too expressive for tractable inference |
| 1990s | XML | Universal data | No semantics, just syntax |
| 2000s | RDF/OWL | Universal knowledge | Adoption limited |
| 2010s | JSON | Universal interchange | No schema, no semantics |
| 2020s | LLM embeddings | Universal meaning? | No structure, no verification |

**Lesson**: Universality trades off against:
- Tractability (more expressive → harder to reason)
- Usability (more formal → harder to adopt)
- Groundedness (more abstract → less actionable)

#### 13.9.2 A Layered Approach

Rather than one universal language, a **stack** of languages:

```
┌─────────────────────────────────────────────────────────┐
│  Natural Language                                       │
│  (Fuzzy, ambiguous, expressive)                        │
├─────────────────────────────────────────────────────────┤
│  Intent Language (UIL)                                  │
│  (Goals, constraints, preferences)                      │
├─────────────────────────────────────────────────────────┤
│  Knowledge Language (Description Logic)                 │
│  (Concepts, relations, axioms)                          │
├─────────────────────────────────────────────────────────┤
│  Action Language (PDDL-like)                           │
│  (Preconditions, effects, plans)                        │
├─────────────────────────────────────────────────────────┤
│  Data Language (RDF/JSON-LD)                           │
│  (Structured facts, linked data)                        │
├─────────────────────────────────────────────────────────┤
│  Execution Language (Code)                              │
│  (Procedures, APIs, actual computation)                 │
└─────────────────────────────────────────────────────────┘
```

**Compilation Direction**: Top-down (intent → action)
**Verification Direction**: Bottom-up (execution → intent satisfaction)

#### 13.9.3 Cross-Layer Translation

Each layer boundary requires translation:

**NL → Intent**: Semantic parsing (Chapter 6.8)
- Requires: Ontology, context, disambiguation
- Challenge: Ambiguity, incompleteness

**Intent → Knowledge**: Grounding
- Requires: World model, entity resolution
- Challenge: Open-world assumption

**Knowledge → Action**: Planning
- Requires: Action models, precondition checking
- Challenge: Computational complexity

**Action → Execution**: Code generation
- Requires: API knowledge, type systems
- Challenge: Correctness verification

---

### 13.10 Implementation Considerations

#### 13.10.1 The Role of LLMs (Revisited)

Given Chapter 6's analysis, where can LLMs legitimately contribute?

**Appropriate Roles**:
1. **NL Normalization**: Cleaning, expanding, disambiguating natural language
2. **Candidate Generation**: Proposing possible formal representations
3. **Translation Assistance**: Suggesting mappings between representations
4. **Error Message Generation**: Making formal feedback human-readable

**Inappropriate Roles**:
1. **Sole semantic parser**: No formal guarantees
2. **Reasoning engine**: No sound inference
3. **Verification**: Cannot check its own outputs
4. **Final authority**: Must be verified by formal systems

**Architecture Pattern**:
```
User NL → [LLM] → Candidate Formal Rep → [Verifier] → Valid Rep → [Reasoner] → Result
              ↓                              ↓
          Confidence Score              Accept/Reject
```

#### 13.10.2 Bootstrapping the Stack

**Cold Start Problem**: How to build formal systems without massive manual effort?

**Approach 1: Schema-First**
- Define formal schemas (ontologies, grammars)
- Use LLMs to generate instances
- Verify against schemas
- Human review edge cases

**Approach 2: Example-First**
- Collect NL/Formal pairs from experts
- Train/fine-tune translation models
- Incrementally expand coverage
- Maintain test suite of known-correct pairs

**Approach 3: Interactive Refinement**
- LLM proposes, human corrects
- Corrections become training data
- System improves over time
- Formal guarantees from human oversight

#### 13.10.3 Verification at Scale

**Challenge**: Verifying millions of translations is infeasible manually.

**Solutions**:

**Type Systems**: Catch category errors automatically
```
Intent<Travel> ≠ Intent<Purchase>
```

**Constraint Checking**: Verify logical consistency
```
Constraint: arrival_time < departure_time → ERROR
```

**Sandboxed Execution**: Test actions in simulation
```
Plan → Simulate → Check effects match intent
```

**Formal Proofs**: For critical domains (medicine, finance)
```
Theorem: Plan achieves Goal given Preconditions
Proof: By construction from verified rules
```

---

### 13.11 Summary

The path from representation to execution requires:

1. **Compilation Pipelines**: Source → IR → Target with semantic preservation
2. **Intermediate Representations**: Enable optimization, analysis, portability
3. **The Web Evolution**: Documents → Applications → Data → Agents
4. **Intent Languages**: Express what to achieve, not how to do it
5. **Living Documents**: Content + Data + Code + Intent
6. **The Agentic Web**: Agents interpreting and executing intents
7. **Layered Universality**: Not one language, but a stack with clear interfaces

**Key Insight**: Language is only powerful as its interpreter. Building interpretable AI requires building the full stack — from representation to verified execution.

---

### Key Concepts

- **Compilation**: Semantic-preserving transformation between languages
- **Intermediate Representation (IR)**: Platform-independent semantic form
- **Semantic Web**: Data with formal, machine-interpretable meaning
- **Intent Language**: Specification of goals, not procedures
- **Living Document**: Reactive content with embedded data and actions
- **Agentic Web**: Web of agents exchanging intents and capabilities
- **Layered Stack**: Multiple languages with formal translations between layers

---

### Exercises

**13.1** Trace the compilation of a simple HTML page through the browser pipeline. Identify the IR at each stage.

**13.2** Write SPARQL queries against a simple RDF dataset. What can you express that SQL cannot?

**13.3** Design a minimal intent language for a specific domain (e.g., calendar scheduling). Define syntax, semantics, and compilation to actions.

**13.4** Compare three approaches to NL → Formal translation: rule-based, statistical, and LLM-based. What are the tradeoffs?

**13.5** Sketch the architecture for a .LIFE document interpreter. What components are needed? How do they interact?

**13.6** Analyze a real agent system (Siri, Alexa, or similar). Where in the stack does it use formal methods vs. statistical methods? What breaks?

**13.7** Design a verification strategy for an agentic web service that books flights. What must be verified? At what layer?

---

### Further Reading

**Compilers and Languages:**
- Aho, A., Lam, M., Sethi, R., & Ullman, J. (2006). *Compilers: Principles, Techniques, and Tools*. 2nd ed. ("Dragon Book")
- Pierce, B. (2002). *Types and Programming Languages*. MIT Press.

**Semantic Web:**
- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). "The Semantic Web." *Scientific American*, 284(5), 34-43.
- Hitzler, P., et al. (2009). *Foundations of Semantic Web Technologies*. CRC Press.

**Planning and Action Languages:**
- Ghallab, M., Nau, D., & Traverso, P. (2004). *Automated Planning: Theory and Practice*. Morgan Kaufmann.
- McDermott, D. (1998). "PDDL — The Planning Domain Definition Language." Technical Report.

**Agent Communication:**
- Labrou, Y., Finin, T., & Peng, Y. (1999). "Agent communication languages: The current landscape." *IEEE Intelligent Systems*, 14(2), 45-52.
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems*. 2nd ed. Wiley.

**The Agentic Future:**
- Mialon, G., et al. (2023). "Augmented Language Models: A Survey." *arXiv:2302.07842*.
- Yao, S., et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*.

---

*End of Chapter 13*
