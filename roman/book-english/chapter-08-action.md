# Chapter 8

## Action and Planning

---

### 8.1 Introduction

Intelligence is not contemplation alone — it is **action in the world**. An agent perceives, reasons, and then **acts** to achieve its goals.

This chapter examines:
- How intentions become actions
- Planning algorithms for goal achievement
- Execution and monitoring
- The relationship between reasoning and acting

We connect these to the cognitive architecture developed in previous chapters.

---

### 8.2 The Action Problem

#### 8.2.1 From Intention to Effect

**The Action Chain**:
```
Goal → Intention → Plan → Motor Commands → Physical Movement → World Change
```

Each step presents challenges:
- Goal formulation: What do we want?
- Planning: How do we get it?
- Execution: Carrying out the plan
- Monitoring: Did it work?

#### 8.2.2 Formal Model of Action

**Definition 8.1 (Action)**: An action is a function from states to states:
$$a: State \rightarrow State$$

More precisely, actions may be:
- **Deterministic**: $s' = a(s)$
- **Stochastic**: $P(s'|s, a)$
- **Partially observable**: Agent doesn't know full state

**Action Description** (STRIPS-style):
```
Action: pickup(X)
Preconditions: on_table(X), clear(X), hand_empty
Effects: holding(X), ¬on_table(X), ¬hand_empty
```

#### 8.2.3 Action and Causation

Actions are **interventions** in the causal structure of the world.

**Do-calculus** (Pearl, 2000): Distinguish observation from intervention:
- $P(Y|X = x)$: Probability of Y given we observe X = x
- $P(Y|do(X = x))$: Probability of Y given we set X = x

Actions correspond to $do()$ operations — they change the causal graph.

---

### 8.3 Classical Planning

#### 8.3.1 The Planning Problem

**Definition 8.2 (Planning Problem)**: Given:
- Initial state $s_0$
- Goal condition $G$
- Set of actions $A$

Find a sequence of actions $\langle a_1, ..., a_n \rangle$ such that:
$$G(a_n(...a_2(a_1(s_0))...))$$

#### 8.3.2 State-Space Search

**Forward Search** (progression):
```python
def forward_search(s0, goal, actions):
    frontier = [(s0, [])]
    visited = {s0}
    
    while frontier:
        state, plan = frontier.pop()
        
        if goal(state):
            return plan
        
        for action in applicable_actions(state, actions):
            new_state = apply(action, state)
            if new_state not in visited:
                visited.add(new_state)
                frontier.append((new_state, plan + [action]))
    
    return None  # No plan exists
```

**Backward Search** (regression):
Start from goal, work backward to initial state.

**Heuristic Search**: Use A* with admissible heuristics:
- $h^{add}$: Additive heuristic (sum of costs to achieve each goal)
- $h^{max}$: Max heuristic (max cost across goals)
- $h^{FF}$: FastForward heuristic (relaxed plan length)

#### 8.3.3 Plan-Space Search

Instead of searching through states, search through partial plans.

**Partial-Order Planning**:
- Plans are sets of actions with ordering constraints
- Causal links: $a_1 \xrightarrow{p} a_2$ means $a_1$ achieves precondition $p$ for $a_2$
- Threats: Actions that might undo causal links

**Algorithm Sketch**:
```
1. Start with initial and goal steps
2. If plan is complete (no open preconditions), return
3. Select open precondition
4. Find action that achieves it
5. Add action, add ordering constraints
6. Resolve any threats
7. Repeat
```

#### 8.3.4 Complexity

**Theorem 8.1**: STRIPS planning is PSPACE-complete.

**Implication**: General planning is intractable. Practical planners exploit problem structure.

**Tractable Cases**:
- Hierarchical planning (abstraction)
- Domain-specific heuristics
- Delete-free relaxations

---

### 8.4 Hierarchical Planning

#### 8.4.1 Abstraction

Real-world planning uses abstraction hierarchies:
```
Level 3: Go from home to airport
Level 2: Get to car, drive to airport, park
Level 1: Walk to garage, unlock car, open door, sit, start engine, ...
Level 0: Muscle activations, motor commands
```

**Principle**: Plan at abstract levels, refine as needed.

#### 8.4.2 Hierarchical Task Networks (HTN)

**Definition 8.3 (HTN)**: An HTN consists of:
- Primitive tasks: Directly executable actions
- Compound tasks: Decompose into subtasks
- Methods: Ways to decompose compound tasks

**Example**:
```
Task: travel(A, B)
Methods:
  - If same city: [taxi(A, B)]
  - If different cities: [travel(A, airport1), fly(airport1, airport2), travel(airport2, B)]
```

**HTN Planning**: Recursively decompose compound tasks until only primitives remain.

#### 8.4.3 Goal-Task Networks

**Goals vs. Tasks**:
- Goal: State to achieve (declarative)
- Task: Action to perform (procedural)

Planning involves translating goals into task networks.

---

### 8.5 Planning Under Uncertainty

#### 8.5.1 Stochastic Outcomes

**Markov Decision Process (MDP)**:
- States $S$
- Actions $A$  
- Transition function $P(s'|s, a)$
- Reward function $R(s, a)$
- Discount factor $\gamma$

**Objective**: Find policy $\pi: S \rightarrow A$ maximizing expected discounted reward:
$$V^\pi(s) = E\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, \pi(s_t)) | s_0 = s\right]$$

**Bellman Equation**:
$$V^*(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^*(s') \right]$$

#### 8.5.2 Partial Observability

**POMDP**: States not fully observable. Agent maintains belief state:
$$b(s) = P(s | observations)$$

Planning in belief space is even harder (PSPACE-complete for finite horizon).

**Approximations**:
- Point-based methods (sample belief points)
- Online planning (plan from current belief)
- Assumption of maximum likelihood state

#### 8.5.3 Contingency Planning

**Conditional Plans**: Include branches for different observations.

```
Plan:
  do(check_weather)
  if sunny then:
    do(go_to_park)
  else:
    do(stay_home)
    do(read_book)
```

---

### 8.6 Execution and Monitoring

#### 8.6.1 The Execution Problem

Plans are made with assumptions. Reality may differ.

**Sources of Failure**:
- Action doesn't have intended effect
- Unexpected events change state
- Preconditions become false
- Time constraints violated

#### 8.6.2 Execution Monitoring

**Definition 8.4 (Execution Monitor)**: A process that tracks plan execution and detects deviations.

```python
def execute_with_monitoring(plan, initial_state):
    state = initial_state
    
    for action in plan:
        # Check preconditions
        if not preconditions_met(action, state):
            return replan(state, goal)
        
        # Execute
        state = execute(action, state)
        
        # Check postconditions
        expected = expected_effects(action)
        actual = observe(state)
        
        if significant_deviation(expected, actual):
            return replan(state, goal)
        
        # Check goal
        if goal_achieved(state):
            return SUCCESS
    
    return COMPLETED
```

#### 8.6.3 Replanning

When execution fails, options include:
- **Local repair**: Fix the plan minimally
- **Full replanning**: Generate new plan from current state
- **Plan library**: Retrieve pre-computed plan for situation

**Reactive Planning**: Interleave planning and execution, plan only next few steps.

---

### 8.7 Action in Cognitive Architecture

#### 8.7.1 Soar's Action Model

In Soar, action selection is part of the decision cycle:
1. Propose operators (candidate actions)
2. Evaluate operators (preferences)
3. Select operator
4. Apply operator

**Operator Application**:
- Internal: Modify working memory
- External: Issue motor commands

#### 8.7.2 ACT-R's Motor Module

ACT-R has explicit motor module with:
- Movement preparation time
- Movement execution time
- Fitts' Law timing for pointing: $MT = a + b \cdot \log_2(2D/W)$

**Motor Buffer**: Contains current motor command or state.

#### 8.7.3 The Intention-Action Gap

**Problem**: How does intention (goal representation) become action (motor command)?

**Solution Components**:
- **Action schemas**: Parameterized action patterns
- **Parameter binding**: Fill in specific values
- **Motor planning**: Translate to motor primitives
- **Execution**: Send motor commands

---

### 8.8 Planning and Reasoning Integration

#### 8.8.1 Planning as Reasoning

Planning can be viewed as reasoning about actions:
- **Situation calculus**: Axiomatize action effects in logic
- **Planning as deduction**: Prove that goal is reachable
- **Planning as satisfiability**: Encode as SAT problem

**Situation Calculus Example**:
```
holds(on(A, B), s) ∧ ¬holds(on(C, A), s) → 
    holds(on(A, table), do(putdown(A), s))
```

#### 8.8.2 Reasoning During Execution

**Deliberative Control**: Full reasoning for each decision (slow but thorough)

**Reactive Control**: Direct stimulus-response (fast but inflexible)

**Hybrid**: Reactive layer handles urgent situations, deliberative layer handles complex planning.

```
        Goals
          ↓
    [Deliberative Layer] ← Slow, thoughtful
          ↓
     High-level plan
          ↓
    [Reactive Layer] ← Fast, reflexive
          ↓
        Actions
```

---

### 8.9 Learning and Planning

#### 8.9.1 Learning Action Models

**Model-Based Reinforcement Learning**:
1. Learn transition model $\hat{P}(s'|s,a)$ from experience
2. Learn reward model $\hat{R}(s,a)$ from experience
3. Plan using learned models

**Advantages**: Sample efficient, can reason about novel situations
**Disadvantages**: Model errors compound

#### 8.9.2 Learning Heuristics

Learn heuristic functions from solved problems:
$$h_\theta(s) \approx \text{true distance to goal}$$

Neural networks can learn effective heuristics for specific domains.

#### 8.9.3 Case-Based Planning

Store successful plans, retrieve and adapt for similar problems.

```
retrieve(current_problem, plan_library) → similar_case
adapt(similar_case.plan, current_problem) → adapted_plan
```

This is closer to how humans often plan — by analogy to past experience.

---

### 8.10 Summary

Action connects intelligence to the world:

1. **Classical planning** searches for action sequences to achieve goals
2. **Hierarchical planning** uses abstraction to manage complexity
3. **Planning under uncertainty** handles stochastic outcomes and partial observability
4. **Execution monitoring** detects and responds to plan failures
5. **Cognitive architectures** integrate planning with perception and reasoning

Planning is reasoning about the future — it requires models of actions, states, and goals. The quality of planning depends on the quality of these models.

---

### Key Concepts

- **Planning problem**: Find action sequence from initial state to goal
- **Heuristic search**: Use estimates to guide search efficiently
- **Hierarchical task network**: Decompose complex tasks into subtasks
- **MDP**: Model for planning under stochastic uncertainty
- **Execution monitoring**: Track plan execution, detect failures

---

### Exercises

**8.1** Define a STRIPS domain for the blocks world (stacking blocks on a table). Write operators for `pickup`, `putdown`, `stack`, and `unstack`.

**8.2** Implement A* search for a planning problem. Compare different heuristics ($h^{add}$, $h^{max}$) on problem instances.

**8.3** Design an HTN for the task "prepare dinner." Define compound tasks, primitive tasks, and methods.

**8.4** Model a simple robot navigation problem as an MDP. Compute the optimal policy using value iteration.

**8.5** Analyze a case where a plan failed during execution. What monitoring could have detected the failure? What replanning options exist?

---

### Further Reading

- Ghallab, M., Nau, D., & Traverso, P. (2016). *Automated Planning and Acting*. Cambridge University Press.
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*, 4th ed. Chapters 10-11.
- Sutton, R., & Barto, A. (2018). *Reinforcement Learning*, 2nd ed. MIT Press.

---

*End of Chapter 8*
