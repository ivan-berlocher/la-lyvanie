# Chapter 11

## System Integration

---

### 11.1 Introduction

The preceding chapters examined components of intelligent systems in isolation:
- Representation (Chapter 2)
- Transparency (Chapter 3)
- Architecture (Chapter 4)
- Perception (Chapter 5)
- Reasoning (Chapter 7)
- Action (Chapter 8)
- Memory (Chapter 9)
- Metacognition (Chapter 10)

This chapter addresses **integration**: how these components combine into coherent, functioning systems.

Integration is not merely connecting modules. It requires:
- Consistent representations across components
- Coordination of processing
- Resolution of conflicts
- Unified behavior from diverse capabilities

---

### 11.2 The Integration Problem

#### 11.2.1 Why Integration Is Hard

**The Module Mismatch Problem**: Components developed separately may have incompatible:
- Representations (different formats, ontologies)
- Timing (different processing speeds)
- Assumptions (different world models)
- Control structures (different activation patterns)

**The Coordination Problem**: Multiple components may:
- Compete for resources (attention, processing time)
- Produce conflicting outputs
- Create circular dependencies
- Generate combinatorial interactions

#### 11.2.2 Integration Levels

**Level 1: Interface Integration**
Components connected through defined interfaces. Minimal interaction.

**Level 2: Data Integration**
Shared representations allow components to exchange information meaningfully.

**Level 3: Control Integration**
Unified control structure coordinates component activation and sequencing.

**Level 4: Architectural Integration**
Components designed from the start as parts of unified architecture.

---

### 11.3 Representational Integration

#### 11.3.1 The Common Language Problem

For components to communicate, they need shared representation.

**Options**:
1. **Universal representation**: Single format for all components
2. **Translation layers**: Convert between component-specific formats
3. **Shared ontology**: Common concepts, different surface formats

**Recommendation**: Shared ontology (Language of Thought) with component-specific realizations.

```
                    Shared Ontology (LoT)
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
    Perception        Reasoning          Action
   (grounded LoT)   (symbolic LoT)   (executable LoT)
```

#### 11.3.2 Ontology Design

**Core Ontology Components**:
- **Entities**: Objects, agents, locations
- **Properties**: Attributes of entities
- **Relations**: Connections between entities
- **Events**: Changes over time
- **States**: Snapshots of the world
- **Actions**: Agent-initiated changes

**Example Ontology Fragment**:
```
Entity
  ├── PhysicalObject
  │     ├── Artifact
  │     └── NaturalObject
  ├── Agent
  │     ├── Person
  │     └── System
  └── Location
        ├── Place
        └── Region

Relation
  ├── Spatial (on, in, near, above)
  ├── Temporal (before, during, after)
  ├── Causal (causes, enables, prevents)
  └── Social (knows, trusts, owns)
```

#### 11.3.3 Translation Between Formats

When components use different formats, translation is required:

```python
class RepresentationBridge:
    def __init__(self, ontology):
        self.ontology = ontology
        
    def perception_to_lot(self, percept_rep):
        """Convert perceptual representation to LoT."""
        lot_rep = LoTRepresentation()
        
        for detected_object in percept_rep.objects:
            entity = lot_rep.create_entity(
                type=self.ontology.map_category(detected_object.category),
                id=detected_object.id
            )
            
            for property_name, value in detected_object.properties:
                lot_rep.add_predicate(
                    entity, 
                    self.ontology.map_property(property_name),
                    value
                )
                
        for relation in percept_rep.relations:
            lot_rep.add_relation(
                relation.subject,
                self.ontology.map_relation(relation.predicate),
                relation.object
            )
            
        return lot_rep
        
    def lot_to_action(self, lot_intention):
        """Convert LoT intention to executable action."""
        action_type = lot_intention.predicate
        parameters = lot_intention.arguments
        
        executable = ActionSpecification(
            action=self.ontology.map_action(action_type),
            params=self.translate_params(parameters)
        )
        
        return executable
```

---

### 11.4 Control Integration

#### 11.4.1 Control Architectures

**Centralized Control**: Single controller directs all components
- Advantages: Coherent, predictable
- Disadvantages: Bottleneck, single point of failure

**Distributed Control**: Components negotiate and coordinate
- Advantages: Robust, parallel
- Disadvantages: Potential conflicts, harder to guarantee coherence

**Hierarchical Control**: Levels of control with different time scales
- Advantages: Handles complexity, natural abstraction
- Disadvantages: Communication overhead, potential delays

#### 11.4.2 The Cognitive Cycle (Integrated)

```python
class IntegratedCognitiveSystem:
    def __init__(self):
        self.perception = PerceptionModule()
        self.memory = MemorySystem()
        self.reasoning = ReasoningEngine()
        self.action = ActionModule()
        self.metacognition = MetacognitiveModule(self)
        self.working_memory = WorkingMemory()
        
    def cognitive_cycle(self):
        while self.active:
            # 1. PERCEIVE
            raw_input = self.environment.observe()
            percepts = self.perception.process(raw_input)
            self.working_memory.add(percepts)
            
            # 2. RETRIEVE
            cues = self.working_memory.get_retrieval_cues()
            retrieved = self.memory.retrieve(cues)
            self.working_memory.add(retrieved)
            
            # 3. REASON
            inferences = self.reasoning.infer(self.working_memory)
            self.working_memory.add(inferences)
            
            # 4. METACOGNITIVE MONITORING
            assessment = self.metacognition.monitor(self.working_memory)
            
            # 5. DECIDE
            if assessment['confidence'] > THRESHOLD:
                decision = self.reasoning.decide(self.working_memory)
            else:
                decision = self.metacognition.control(assessment)
                
            # 6. ACT
            if decision.is_external():
                action = self.action.execute(decision)
                self.environment.apply(action)
            else:
                self.apply_internal(decision)
                
            # 7. CONSOLIDATE
            self.memory.consolidate(self.working_memory.recent())
            
            # 8. UPDATE SELF-MODEL
            self.metacognition.update_self_model(decision, outcome)
```

#### 11.4.3 Conflict Resolution

When components disagree:

**Priority-Based**: Higher-priority component wins
```
if perception.urgent_threat():
    return perception.threat_response()
elif reasoning.has_plan():
    return reasoning.next_action()
else:
    return default_behavior()
```

**Voting**: Aggregate component opinions
```
votes = [component.vote(situation) for component in components]
decision = majority(votes)  # or weighted average
```

**Arbitration**: Dedicated arbitration module resolves conflicts
```
if conflict(perception.output, reasoning.output):
    return arbitrator.resolve(perception.output, reasoning.output)
```

---

### 11.5 Memory Integration

#### 11.5.1 Unified Memory Architecture

Memory must serve all components:

```
                    ┌─────────────────────┐
                    │   Working Memory    │
                    │  (current context)  │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌─────────────────┐    ┌───────────────┐
│   Episodic    │    │    Semantic     │    │  Procedural   │
│   Memory      │    │    Memory       │    │   Memory      │
│ (experiences) │    │ (facts, models) │    │   (skills)    │
└───────────────┘    └─────────────────┘    └───────────────┘
        │                      │                      │
        └──────────────────────┴──────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Consolidation     │
                    │   & Integration     │
                    └─────────────────────┘
```

#### 11.5.2 Memory-Component Interfaces

**Perception → Memory**:
- Store new percepts in episodic memory
- Update semantic memory with recognized objects

**Reasoning → Memory**:
- Retrieve relevant knowledge
- Store inferences and conclusions

**Action → Memory**:
- Store action outcomes in episodic memory
- Update procedural knowledge from successes/failures

**Metacognition → Memory**:
- Access self-knowledge
- Update self-model from experience

#### 11.5.3 Memory Consistency

Maintain consistency across memory types:
```python
class MemoryConsistencyManager:
    def update(self, new_info, source):
        """Update memories while maintaining consistency."""
        
        # Check for conflicts with existing knowledge
        conflicts = self.find_conflicts(new_info, self.semantic_memory)
        
        if conflicts:
            resolution = self.resolve_conflicts(new_info, conflicts, source)
            if resolution.update_existing:
                self.semantic_memory.update(resolution.updated)
            if resolution.reject_new:
                return False
                
        # Propagate updates
        self.episodic_memory.add_event(new_info, source)
        self.semantic_memory.integrate(new_info)
        
        # Trigger reconsolidation if needed
        if resolution.major_change:
            self.reconsolidate_related(new_info)
            
        return True
```

---

### 11.6 Perception-Reasoning Integration

#### 11.6.1 The Symbol Grounding Bridge

Perception produces grounded representations; reasoning uses symbolic structures.

**Bridge Requirements**:
1. Map perceptual features to symbols
2. Maintain grounding links (symbol ↔ percept)
3. Support reasoning queries about perceptual content

```python
class PerceptionReasoningBridge:
    def __init__(self):
        self.symbol_table = {}  # symbol → grounding
        self.reverse_index = {}  # feature → symbols
        
    def ground_percept(self, percept):
        """Create grounded symbol for percept."""
        symbol = create_symbol(percept.category)
        grounding = {
            'features': percept.features,
            'location': percept.location,
            'timestamp': now(),
            'confidence': percept.confidence
        }
        
        self.symbol_table[symbol] = grounding
        self.reverse_index[hash(percept.features)].append(symbol)
        
        return symbol
        
    def query_grounding(self, symbol):
        """Retrieve grounding for symbol (for explanation)."""
        return self.symbol_table.get(symbol)
        
    def find_symbol(self, perceptual_query):
        """Find symbol matching perceptual features."""
        candidates = self.reverse_index.get(hash(perceptual_query.features), [])
        return best_match(candidates, perceptual_query)
```

#### 11.6.2 Attention Integration

Attention connects perception and reasoning bidirectionally:

**Bottom-up**: Perception drives attention based on salience
**Top-down**: Reasoning drives attention based on goals

```python
class AttentionIntegrator:
    def compute_attention(self, perceptual_input, goals, working_memory):
        """Compute integrated attention map."""
        
        # Bottom-up: perceptual salience
        bottom_up = self.perception.compute_salience(perceptual_input)
        
        # Top-down: goal relevance
        top_down = self.reasoning.compute_relevance(perceptual_input, goals)
        
        # Working memory: current context
        wm_bias = self.working_memory_bias(perceptual_input, working_memory)
        
        # Combine
        attention = (
            W_BOTTOM_UP * bottom_up +
            W_TOP_DOWN * top_down +
            W_WM * wm_bias
        )
        
        return normalize(attention)
```

---

### 11.7 Reasoning-Action Integration

#### 11.7.1 Plan-Action Bridge

Reasoning produces plans; action module executes them.

```python
class PlanExecutor:
    def __init__(self, action_module, monitor):
        self.action = action_module
        self.monitor = monitor
        
    def execute_plan(self, plan):
        """Execute plan with monitoring."""
        for step in plan:
            # Check preconditions
            if not self.check_preconditions(step):
                return self.handle_failure('precondition', step)
                
            # Translate to executable action
            executable = self.translate(step)
            
            # Execute
            result = self.action.execute(executable)
            
            # Monitor outcome
            if not self.monitor.check_outcome(step, result):
                return self.handle_failure('outcome', step, result)
                
        return Success()
        
    def translate(self, plan_step):
        """Translate abstract plan step to executable action."""
        action_schema = self.action.get_schema(plan_step.action_type)
        bindings = self.bind_parameters(action_schema, plan_step.arguments)
        return action_schema.instantiate(bindings)
```

#### 11.7.2 Reactive Integration

Not all action requires deliberate planning:

```python
class ReasoningActionIntegrator:
    def select_action(self, situation):
        """Select action through deliberation or reaction."""
        
        # Check for urgent reactive needs
        reactive = self.reactive_layer.check(situation)
        if reactive.urgent:
            return reactive.response
            
        # Check for applicable plan
        if self.current_plan and self.current_plan.applicable(situation):
            return self.current_plan.next_action()
            
        # Deliberate
        analysis = self.reasoning.analyze(situation)
        
        if analysis.requires_planning:
            self.current_plan = self.reasoning.plan(analysis.goal)
            return self.current_plan.next_action()
        else:
            return self.reasoning.decide(analysis)
```

---

### 11.8 Integration Testing

#### 11.8.1 Integration Tests

**Interface Tests**: Do components communicate correctly?
```python
def test_perception_memory_interface():
    percept = perception.process(test_image)
    memory.store(percept)
    retrieved = memory.retrieve(percept.cue)
    assert similar(percept, retrieved)
```

**Flow Tests**: Does information flow correctly through system?
```python
def test_perception_to_action_flow():
    # Perception
    percept = perception.process(image_with_object)
    
    # Reasoning
    inference = reasoning.infer([percept, goal_to_interact])
    
    # Action
    action = action_module.plan(inference)
    
    assert action.involves(percept.objects[0])
```

**Coherence Tests**: Does system behave coherently?
```python
def test_system_coherence():
    system.present(stimulus)
    response1 = system.respond(query1)
    response2 = system.respond(query2)
    
    # Responses should be consistent
    assert not contradicts(response1, response2)
```

#### 11.8.2 Emergent Behavior Testing

Integration creates emergent behaviors not present in components:

**Emergence Positive**: New capabilities from component interaction
**Emergence Negative**: Unexpected failures or conflicts

```python
def test_for_negative_emergence():
    """Test for unexpected negative interactions."""
    for scenario in stress_scenarios:
        system.reset()
        system.run(scenario)
        
        assert not system.deadlock_detected()
        assert not system.resource_exhaustion()
        assert system.maintains_coherence()
        assert not system.oscillating()
```

---

### 11.9 Case Study: Integrated Cognitive Agent

#### 11.9.1 Specification

**Task**: Navigate environment, find objects, answer questions, explain behavior.

**Components**:
- Visual perception (object detection, scene understanding)
- Spatial reasoning (navigation, spatial relations)
- Language understanding/generation
- Memory (episodic for history, semantic for world knowledge)
- Action (movement, manipulation)
- Metacognition (confidence, self-monitoring)

#### 11.9.2 Integration Architecture

```
                    ┌─────────────────────────────┐
                    │      Central Executive      │
                    │   (coordination, control)   │
                    └─────────────┬───────────────┘
                                  │
    ┌──────────┬──────────┬───────┴────────┬──────────┬──────────┐
    │          │          │                │          │          │
    ▼          ▼          ▼                ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐    ┌──────────┐ ┌────────┐ ┌────────┐
│Visual  │ │Language│ │Spatial │    │  Memory  │ │ Action │ │ Meta-  │
│Percept.│ │Process.│ │Reason. │    │  System  │ │ Module │ │cognit. │
└────┬───┘ └────┬───┘ └────┬───┘    └────┬─────┘ └────┬───┘ └────┬───┘
     │          │          │             │            │          │
     └──────────┴──────────┴─────────────┴────────────┴──────────┘
                                  │
                    ┌─────────────▼───────────────┐
                    │      Working Memory         │
                    │  (shared representation)    │
                    └─────────────────────────────┘
```

#### 11.9.3 Interaction Flow

```
1. Visual input → Visual Perception → Grounded symbols in WM
2. Language input → Language Processing → Query representation in WM
3. WM contents → Spatial Reasoning → Spatial inferences
4. WM + Query → Memory System → Retrieved knowledge
5. All → Central Executive → Action decision or response
6. Decision → Action Module → Behavior
7. Throughout → Metacognition → Confidence, monitoring
```

---

### 11.10 Summary

Integration is the challenge of combining components into coherent systems:

1. **Representational integration** requires shared ontology and translation
2. **Control integration** requires coordination mechanisms and conflict resolution
3. **Memory integration** requires unified architecture serving all components
4. **Component-specific integration** (perception-reasoning, reasoning-action) requires bridges
5. **Testing** must verify interfaces, flows, coherence, and emergent behavior

A well-integrated system is more than the sum of its parts — components enable each other and produce capabilities that none has alone.

---

### Key Concepts

- **Representational integration**: Shared formats enabling communication
- **Control integration**: Coordinated component activation
- **Ontology**: Shared conceptual vocabulary
- **Emergence**: New capabilities (or problems) from component interaction
- **Cognitive cycle**: Integrated loop of perception, cognition, action

---

### Exercises

**11.1** Design an ontology for a robot operating in a kitchen environment. Define entities, properties, relations.

**11.2** Implement a simple attention integrator combining bottom-up salience and top-down goals.

**11.3** Design integration tests for a system with perception, reasoning, and action components.

**11.4** Analyze a failure case where integrated components produced unexpected behavior. What went wrong?

**11.5** Compare the integration approaches in Soar, ACT-R, and CLARION. What are the tradeoffs?

---

### Further Reading

- Laird, J. E. (2012). *The Soar Cognitive Architecture*. MIT Press. (Chapters on system integration)
- Anderson, J. R., et al. (2004). "An integrated theory of the mind." *Psychological Review*, 111(4), 1036-1060.
- Kotseruba, I., & Tsotsos, J. K. (2020). "40 years of cognitive architectures." *AI Review*, 53, 17-94.

---

*End of Chapter 11*
