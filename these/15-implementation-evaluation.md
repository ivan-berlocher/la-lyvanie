# Chapitre 15 — Implementation & Evaluation

## Abstract

This chapter addresses the critical gap between architectural vision and executable proof. We specify formal contracts, failure models, and evaluation metrics required for scientific validation of the AMI cognitive architecture.

---

## 15.1 UIL Formal Specification

### 15.1.1 Intent Schema (v0.1)

```typescript
interface Intent {
  // Core classification
  type: IntentType;
  
  // Semantic payload
  subject: Entity;
  predicate: Predicate;
  object?: Entity | Value;
  
  // Goal structure (optional)
  goal?: Goal;
  
  // Constraints and qualifiers
  constraints: Constraint[];
  qualifiers: Qualifier[];
  
  // Metadata
  confidence: number;        // [0.0, 1.0]
  provenance: Provenance;
  timestamp: ISO8601;
  
  // Lifecycle
  status: IntentStatus;
  parent?: IntentId;         // For decomposed intents
  children?: IntentId[];
}

enum IntentType {
  ACTION    = "ACTION",      // Execute something
  QUERY     = "QUERY",       // Retrieve information
  PLAN      = "PLAN",        // Generate multi-step strategy
  REFLECT   = "REFLECT",     // Meta-cognitive operation
  ASSERT    = "ASSERT",      // Declare a fact
  REVOKE    = "REVOKE"       // Retract previous intent
}

enum IntentStatus {
  PENDING   = "PENDING",
  ACTIVE    = "ACTIVE",
  BLOCKED   = "BLOCKED",
  COMPLETED = "COMPLETED",
  FAILED    = "FAILED",
  CANCELLED = "CANCELLED"
}

interface Provenance {
  agent: AgentId;
  model?: ModelId;
  source: "user" | "system" | "inference";
  timestamp: ISO8601;
  trace_id: UUID;
}
```

### 15.1.2 UIL Grammar (BNF)

```bnf
<intent>      ::= <type> "(" <subject> "," <predicate> ["," <object>] ")" 
                  ["[" <constraints> "]"] 
                  ["{" <metadata> "}"]

<type>        ::= "ACTION" | "QUERY" | "PLAN" | "REFLECT" | "ASSERT" | "REVOKE"

<subject>     ::= <entity> | <pronoun> | <reference>

<predicate>   ::= <verb> [":" <domain>]

<object>      ::= <entity> | <value> | <intent>

<constraints> ::= <constraint> ("," <constraint>)*

<constraint>  ::= <temporal> | <spatial> | <resource> | <priority>

<temporal>    ::= "before:" <time> | "after:" <time> | "within:" <duration>

<priority>    ::= "priority:" ("critical" | "high" | "normal" | "low" | "background")

<metadata>    ::= "confidence:" <float> ["," "source:" <source>]
```

### 15.1.3 UIL Examples

```yaml
# Simple action
ACTION(user, create:productivity, presentation)
  [within:2h, priority:high]
  {confidence:0.92, source:user}

# Complex query with decomposition
QUERY(system, analyze:research, cognitive_architectures)
  [depth:comprehensive]
  {confidence:0.85, source:inference}
  -> children: [
    QUERY(system, retrieve:memory, related_papers),
    QUERY(system, summarize:nlp, key_themes),
    ACTION(system, generate:output, structured_report)
  ]

# Meta-cognitive reflection
REFLECT(harmonia, evaluate:meta, current_plan)
  [trigger:confidence_drop]
  {confidence:0.78, source:system}
```

### 15.1.4 Type Safety Guarantees

| Property | Guarantee | Enforcement |
|----------|-----------|-------------|
| Type completeness | Every intent has valid type | Schema validation |
| Subject resolution | Subject must resolve to entity | Graph lookup |
| Temporal consistency | Constraints don't contradict | Constraint solver |
| Provenance integrity | Every intent has traceable origin | Immutable log |
| Confidence bounds | 0.0 ≤ confidence ≤ 1.0 | Type system |

---

## 15.2 Memory Lifecycle Specification

### 15.2.1 Memory Tiers

```typescript
interface MemoryTier {
  name: "STM" | "MTM" | "LTM";
  scope: TemporalScope;
  storage: StorageType;
  capacity: CapacityLimit;
  promotion_rules: PromotionRule[];
  eviction_rules: EvictionRule[];
}

const STM: MemoryTier = {
  name: "STM",
  scope: "session",                    // Current interaction
  storage: "in-memory",
  capacity: { max_items: 100, max_tokens: 50000 },
  promotion_rules: [
    { trigger: "referenced_3x", target: "MTM" },
    { trigger: "user_starred", target: "MTM" },
    { trigger: "goal_linked", target: "MTM" }
  ],
  eviction_rules: [
    { trigger: "session_end", action: "evaluate_promotion_then_discard" },
    { trigger: "capacity_exceeded", action: "evict_lowest_relevance" }
  ]
};

const MTM: MemoryTier = {
  name: "MTM",
  scope: "rolling_window",             // 7-30 days
  storage: "persistent_cache",
  capacity: { max_items: 10000, max_mb: 500 },
  promotion_rules: [
    { trigger: "referenced_10x", target: "LTM" },
    { trigger: "cross_session_relevance > 0.8", target: "LTM" },
    { trigger: "user_confirmed", target: "LTM" }
  ],
  eviction_rules: [
    { trigger: "age > 30d && relevance < 0.3", action: "archive_cold" },
    { trigger: "contradicted_by_newer", action: "mark_superseded" }
  ]
};

const LTM: MemoryTier = {
  name: "LTM",
  scope: "permanent",
  storage: "graph_db + vector_store",
  capacity: { max_items: "unlimited", compression: "enabled" },
  promotion_rules: [],                 // Terminal tier
  eviction_rules: [
    { trigger: "user_requested_deletion", action: "hard_delete" },
    { trigger: "privacy_policy", action: "anonymize_or_delete" }
  ]
};
```

### 15.2.2 Promotion Algorithm

```python
def evaluate_promotion(memory_item: MemoryItem, current_tier: MemoryTier) -> Optional[MemoryTier]:
    """
    Evaluate whether a memory item should be promoted to a higher tier.
    Returns target tier or None if no promotion warranted.
    """
    
    score = calculate_promotion_score(memory_item)
    
    # Scoring factors
    factors = {
        "reference_count": memory_item.references * 0.3,
        "recency_weighted_access": recency_decay(memory_item.last_accessed) * 0.2,
        "goal_relevance": goal_alignment_score(memory_item) * 0.25,
        "user_signals": explicit_user_value(memory_item) * 0.15,
        "cross_session": cross_session_persistence(memory_item) * 0.1
    }
    
    score = sum(factors.values())
    
    # Promotion thresholds
    if current_tier.name == "STM" and score > 0.6:
        return MTM
    if current_tier.name == "MTM" and score > 0.8:
        return LTM
    
    return None
```

### 15.2.3 Forgetting Rules

```typescript
interface ForgettingPolicy {
  // Passive decay
  decay_function: "exponential" | "power_law";
  half_life_days: number;
  
  // Active eviction
  contradiction_handling: "supersede" | "version" | "conflict_flag";
  
  // User control
  user_can_pin: boolean;
  user_can_delete: boolean;
  
  // Privacy compliance
  gdpr_right_to_forget: boolean;
  retention_limit_days?: number;
}

const DEFAULT_FORGETTING: ForgettingPolicy = {
  decay_function: "power_law",         // More realistic than exponential
  half_life_days: 14,
  contradiction_handling: "version",   // Keep history, mark superseded
  user_can_pin: true,
  user_can_delete: true,
  gdpr_right_to_forget: true,
  retention_limit_days: 365 * 2        // 2 years default
};
```

### 15.2.4 Conflict Resolution

```typescript
interface MemoryConflict {
  type: "contradiction" | "ambiguity" | "staleness";
  items: MemoryItem[];
  detected_at: ISO8601;
  resolution_strategy: ResolutionStrategy;
}

enum ResolutionStrategy {
  // Automatic
  PREFER_RECENT    = "prefer_recent",
  PREFER_CONFIDENT = "prefer_confident",
  PREFER_USER      = "prefer_user_sourced",
  
  // Requires intervention
  FLAG_FOR_REVIEW  = "flag_for_review",
  ASK_USER         = "ask_user",
  
  // Structural
  VERSION_BOTH     = "version_both",
  MERGE_PARTIAL    = "merge_partial"
}

function resolve_conflict(conflict: MemoryConflict): Resolution {
  switch (conflict.type) {
    case "contradiction":
      // Two facts directly oppose each other
      if (confidence_gap(conflict.items) > 0.3) {
        return apply_strategy(ResolutionStrategy.PREFER_CONFIDENT);
      }
      if (recency_gap(conflict.items) > days(7)) {
        return apply_strategy(ResolutionStrategy.PREFER_RECENT);
      }
      return apply_strategy(ResolutionStrategy.FLAG_FOR_REVIEW);
      
    case "staleness":
      // Information may be outdated
      return apply_strategy(ResolutionStrategy.PREFER_RECENT);
      
    case "ambiguity":
      // Multiple valid interpretations
      return apply_strategy(ResolutionStrategy.VERSION_BOTH);
  }
}
```

---

## 15.3 Failure Model

### 15.3.1 Failure Taxonomy

```typescript
enum FailureClass {
  // Agent-level failures
  AGENT_TIMEOUT        = "agent_timeout",
  AGENT_ERROR          = "agent_error",
  AGENT_HALLUCINATION  = "agent_hallucination",
  AGENT_REFUSAL        = "agent_refusal",
  
  // Coordination failures
  CONFLICT_DEADLOCK    = "conflict_deadlock",
  ROUTING_AMBIGUITY    = "routing_ambiguity",
  RESOURCE_CONTENTION  = "resource_contention",
  
  // Memory failures
  GRAPH_INCONSISTENCY  = "graph_inconsistency",
  MEMORY_OVERFLOW      = "memory_overflow",
  RETRIEVAL_FAILURE    = "retrieval_failure",
  
  // System failures
  MODEL_UNAVAILABLE    = "model_unavailable",
  LATENCY_EXCEEDED     = "latency_exceeded",
  QUOTA_EXHAUSTED      = "quota_exhausted"
}

interface Failure {
  class: FailureClass;
  severity: "critical" | "degraded" | "minor";
  recoverable: boolean;
  context: FailureContext;
  timestamp: ISO8601;
}
```

### 15.3.2 Recovery Strategies

```typescript
interface RecoveryStrategy {
  failure_class: FailureClass;
  primary_action: RecoveryAction;
  fallback_actions: RecoveryAction[];
  max_retries: number;
  escalation_path: EscalationPath;
}

const RECOVERY_STRATEGIES: RecoveryStrategy[] = [
  {
    failure_class: FailureClass.AGENT_TIMEOUT,
    primary_action: { type: "retry", delay_ms: 1000 },
    fallback_actions: [
      { type: "route_to_fallback_agent" },
      { type: "degrade_to_simple_response" },
      { type: "return_partial_result" }
    ],
    max_retries: 3,
    escalation_path: { notify_user_after: 2, log_level: "warn" }
  },
  
  {
    failure_class: FailureClass.AGENT_HALLUCINATION,
    primary_action: { type: "verify_with_second_agent" },
    fallback_actions: [
      { type: "check_against_memory" },
      { type: "flag_uncertain", confidence_penalty: 0.3 },
      { type: "ask_user_confirmation" }
    ],
    max_retries: 1,
    escalation_path: { notify_user_after: 1, log_level: "warn" }
  },
  
  {
    failure_class: FailureClass.CONFLICT_DEADLOCK,
    primary_action: { type: "invoke_arbiter_agent" },
    fallback_actions: [
      { type: "apply_priority_rules" },
      { type: "random_tiebreak_with_logging" },
      { type: "escalate_to_user" }
    ],
    max_retries: 2,
    escalation_path: { notify_user_after: 1, log_level: "error" }
  },
  
  {
    failure_class: FailureClass.GRAPH_INCONSISTENCY,
    primary_action: { type: "run_consistency_check" },
    fallback_actions: [
      { type: "quarantine_conflicting_nodes" },
      { type: "rollback_to_checkpoint" },
      { type: "request_manual_review" }
    ],
    max_retries: 1,
    escalation_path: { notify_user_after: 0, log_level: "critical" }
  }
];
```

### 15.3.3 Agent Conflict Resolution

```typescript
interface AgentConflict {
  agents: AgentId[];
  conflict_type: "recommendation" | "resource" | "goal";
  proposals: AgentProposal[];
}

function resolve_agent_conflict(conflict: AgentConflict): Resolution {
  // Step 1: Check for clear priority
  const priority_winner = check_domain_priority(conflict);
  if (priority_winner) return { winner: priority_winner, method: "priority" };
  
  // Step 2: Confidence-based resolution
  const confidence_sorted = conflict.proposals
    .sort((a, b) => b.confidence - a.confidence);
  
  if (confidence_sorted[0].confidence - confidence_sorted[1].confidence > 0.2) {
    return { winner: confidence_sorted[0].agent, method: "confidence" };
  }
  
  // Step 3: Invoke arbiter
  const arbiter_decision = invoke_arbiter({
    proposals: conflict.proposals,
    context: get_current_context(),
    user_preferences: get_user_preferences()
  });
  
  if (arbiter_decision.confident) {
    return { winner: arbiter_decision.selected, method: "arbiter" };
  }
  
  // Step 4: User escalation
  return { 
    action: "ask_user",
    options: conflict.proposals.map(p => ({
      agent: p.agent,
      summary: p.summary,
      confidence: p.confidence
    })),
    method: "user_choice"
  };
}
```

---

## 15.4 Cognitive Scheduler

### 15.4.1 Architecture

```typescript
interface CognitiveScheduler {
  // Intent queue management
  intent_queue: PriorityQueue<Intent>;
  
  // Processing paths
  fast_path: FastPathProcessor;      // < 100ms
  standard_path: StandardProcessor;  // < 2s
  deep_path: DeepProcessor;          // < 30s
  background_path: BackgroundProcessor; // async
  
  // Resource management
  model_pool: ModelPool;
  memory_cache: MemoryCache;
  
  // Monitoring
  latency_tracker: LatencyTracker;
  budget_manager: BudgetManager;
}
```

### 15.4.2 Path Classification

```typescript
function classify_processing_path(intent: Intent): ProcessingPath {
  // Fast path criteria (< 100ms target)
  if (
    intent.type === IntentType.QUERY &&
    is_cached(intent) &&
    intent.constraints.every(c => c.type !== "deep_reasoning")
  ) {
    return ProcessingPath.FAST;
  }
  
  // Background path criteria
  if (
    intent.constraints.some(c => c.priority === "background") ||
    intent.type === IntentType.PLAN && estimated_complexity(intent) > 0.8
  ) {
    return ProcessingPath.BACKGROUND;
  }
  
  // Deep path criteria
  if (
    intent.type === IntentType.REFLECT ||
    requires_multi_agent(intent) ||
    intent.constraints.some(c => c.type === "comprehensive")
  ) {
    return ProcessingPath.DEEP;
  }
  
  // Default: standard path
  return ProcessingPath.STANDARD;
}
```

### 15.4.3 Fast Path Implementation

```typescript
class FastPathProcessor {
  private cache: LRUCache<string, CachedResponse>;
  private simple_router: SimpleRouter;
  
  async process(intent: Intent): Promise<Response> {
    const cache_key = compute_cache_key(intent);
    
    // L1: Exact cache hit
    if (this.cache.has(cache_key)) {
      metrics.record("fast_path_cache_hit");
      return this.cache.get(cache_key);
    }
    
    // L2: Semantic cache (embedding similarity)
    const semantic_match = await this.semantic_cache_lookup(intent);
    if (semantic_match && semantic_match.similarity > 0.95) {
      metrics.record("fast_path_semantic_hit");
      return adapt_cached_response(semantic_match.response, intent);
    }
    
    // L3: Simple single-agent routing (no orchestration)
    const agent = this.simple_router.route(intent);
    const response = await agent.process_simple(intent, { timeout_ms: 100 });
    
    // Cache for future
    this.cache.set(cache_key, response);
    
    return response;
  }
}
```

### 15.4.4 Latency Budget

```typescript
interface LatencyBudget {
  total_ms: number;
  phases: {
    perception: number;    // UIL parsing
    routing: number;       // Agent selection
    retrieval: number;     // Memory access
    reasoning: number;     // Agent processing
    generation: number;    // Output creation
    delivery: number;      // Response transmission
  };
}

const LATENCY_BUDGETS: Record<ProcessingPath, LatencyBudget> = {
  FAST: {
    total_ms: 100,
    phases: { perception: 10, routing: 5, retrieval: 20, reasoning: 40, generation: 20, delivery: 5 }
  },
  STANDARD: {
    total_ms: 2000,
    phases: { perception: 50, routing: 50, retrieval: 200, reasoning: 1200, generation: 400, delivery: 100 }
  },
  DEEP: {
    total_ms: 30000,
    phases: { perception: 100, routing: 200, retrieval: 2000, reasoning: 24000, generation: 3000, delivery: 700 }
  },
  BACKGROUND: {
    total_ms: Infinity,  // No hard limit
    phases: { /* adaptive */ }
  }
};
```

---

## 15.5 Graph Compression

### 15.5.1 Compression Strategies

```typescript
interface CompressionStrategy {
  name: string;
  trigger: CompressionTrigger;
  algorithm: CompressionAlgorithm;
  preservation_guarantee: PreservationGuarantee;
}

const COMPRESSION_STRATEGIES: CompressionStrategy[] = [
  {
    name: "semantic_deduplication",
    trigger: { type: "similarity_threshold", threshold: 0.95 },
    algorithm: {
      type: "merge_similar_nodes",
      merge_function: "preserve_most_recent_with_provenance"
    },
    preservation_guarantee: { semantic_loss: 0.0, structural_loss: 0.05 }
  },
  
  {
    name: "hierarchical_summarization",
    trigger: { type: "cluster_size", min_nodes: 50 },
    algorithm: {
      type: "create_summary_node",
      summary_model: "gpt-4-turbo",
      preserve_links: true
    },
    preservation_guarantee: { semantic_loss: 0.1, structural_loss: 0.3 }
  },
  
  {
    name: "cold_archival",
    trigger: { type: "access_recency", days_since_access: 90 },
    algorithm: {
      type: "move_to_cold_storage",
      keep_stub: true,
      rehydration_available: true
    },
    preservation_guarantee: { semantic_loss: 0.0, access_latency_increase: "high" }
  },
  
  {
    name: "temporal_rollup",
    trigger: { type: "temporal_density", events_per_day: 100 },
    algorithm: {
      type: "aggregate_by_period",
      period: "day",
      aggregation: "summarize_activities"
    },
    preservation_guarantee: { semantic_loss: 0.15, structural_loss: 0.5 }
  }
];
```

### 15.5.2 Hierarchical Summary Generation

```typescript
interface GraphSummary {
  level: "session" | "day" | "week" | "month" | "year";
  node_count_original: number;
  node_count_compressed: number;
  summary_text: string;
  key_entities: Entity[];
  key_events: Event[];
  preserved_links: Link[];
}

async function generate_hierarchical_summary(
  nodes: GraphNode[],
  level: SummaryLevel
): Promise<GraphSummary> {
  // Extract key information
  const entities = extract_key_entities(nodes, { top_k: 10 });
  const events = extract_key_events(nodes, { top_k: 5 });
  const themes = cluster_by_theme(nodes);
  
  // Generate natural language summary
  const summary_prompt = build_summary_prompt({
    entities,
    events,
    themes,
    level,
    node_count: nodes.length
  });
  
  const summary_text = await llm.generate(summary_prompt, {
    max_tokens: 500,
    model: "gpt-4-turbo"
  });
  
  // Create summary node
  const summary_node: GraphSummary = {
    level,
    node_count_original: nodes.length,
    node_count_compressed: 1,
    summary_text,
    key_entities: entities,
    key_events: events,
    preserved_links: extract_external_links(nodes)
  };
  
  return summary_node;
}
```

---

## 15.6 Model Governance

### 15.6.1 Routing Policy

```typescript
interface ModelRoutingPolicy {
  // Model tiers
  tiers: {
    fast: ModelConfig[];      // < 50ms, cheap
    standard: ModelConfig[];  // < 500ms, balanced
    powerful: ModelConfig[];  // < 5s, expensive
  };
  
  // Routing rules
  routing_rules: RoutingRule[];
  
  // Budget constraints
  budget: BudgetConfig;
  
  // Fallback chain
  fallback_chain: ModelId[];
}

interface RoutingRule {
  condition: RoutingCondition;
  target_tier: "fast" | "standard" | "powerful";
  override_model?: ModelId;
}

const DEFAULT_ROUTING_POLICY: ModelRoutingPolicy = {
  tiers: {
    fast: [
      { id: "gpt-4o-mini", latency_p50_ms: 30, cost_per_1k_tokens: 0.00015 },
      { id: "claude-3-haiku", latency_p50_ms: 40, cost_per_1k_tokens: 0.00025 }
    ],
    standard: [
      { id: "gpt-4o", latency_p50_ms: 200, cost_per_1k_tokens: 0.005 },
      { id: "claude-3.5-sonnet", latency_p50_ms: 250, cost_per_1k_tokens: 0.003 }
    ],
    powerful: [
      { id: "gpt-4-turbo", latency_p50_ms: 800, cost_per_1k_tokens: 0.01 },
      { id: "claude-3-opus", latency_p50_ms: 1000, cost_per_1k_tokens: 0.015 }
    ]
  },
  
  routing_rules: [
    { condition: { intent_type: "QUERY", complexity: "low" }, target_tier: "fast" },
    { condition: { intent_type: "ACTION", domain: "simple" }, target_tier: "fast" },
    { condition: { intent_type: "PLAN" }, target_tier: "powerful" },
    { condition: { intent_type: "REFLECT" }, target_tier: "powerful" },
    { condition: { requires_reasoning: true }, target_tier: "standard" }
  ],
  
  budget: {
    daily_limit_usd: 10.0,
    per_request_limit_usd: 0.50,
    alert_threshold_percent: 80
  },
  
  fallback_chain: ["gpt-4o-mini", "claude-3-haiku", "local-llama"]
};
```

### 15.6.2 Auditability

```typescript
interface ModelAuditLog {
  request_id: UUID;
  timestamp: ISO8601;
  
  // Request details
  intent: Intent;
  selected_model: ModelId;
  routing_reason: string;
  
  // Execution details
  latency_ms: number;
  tokens_in: number;
  tokens_out: number;
  cost_usd: number;
  
  // Quality signals
  user_feedback?: "positive" | "negative" | "neutral";
  confidence_score: number;
  hallucination_detected: boolean;
  
  // Compliance
  pii_detected: boolean;
  content_flags: string[];
}

class AuditLogger {
  async log(entry: ModelAuditLog): Promise<void> {
    // Immutable append-only log
    await this.audit_store.append(entry);
    
    // Real-time anomaly detection
    if (entry.hallucination_detected || entry.latency_ms > threshold) {
      await this.alert_system.notify(entry);
    }
    
    // Budget tracking
    await this.budget_tracker.record(entry.cost_usd);
  }
  
  async query(filters: AuditFilters): Promise<ModelAuditLog[]> {
    return this.audit_store.query(filters);
  }
  
  async generate_report(period: DateRange): Promise<AuditReport> {
    const logs = await this.query({ date_range: period });
    
    return {
      total_requests: logs.length,
      total_cost_usd: sum(logs.map(l => l.cost_usd)),
      avg_latency_ms: avg(logs.map(l => l.latency_ms)),
      model_distribution: group_by(logs, l => l.selected_model),
      error_rate: logs.filter(l => l.hallucination_detected).length / logs.length,
      user_satisfaction: calculate_satisfaction(logs)
    };
  }
}
```

---

## 15.7 Complete Traceable Scenario

### 15.7.1 Scenario: User Planning Request

**Input:** "Plan my presentation about cognitive architectures for the ETH meeting next Tuesday"

### 15.7.2 Full Execution Trace (JSON)

```json
{
  "trace_id": "tr_a1b2c3d4e5f6",
  "timestamp": "2025-01-15T10:30:00Z",
  "duration_ms": 2847,
  
  "1_input": {
    "raw_text": "Plan my presentation about cognitive architectures for the ETH meeting next Tuesday",
    "modality": "text",
    "source": "chat_input",
    "user_id": "usr_ivan"
  },
  
  "2_perception": {
    "phase": "PERCEPTION",
    "duration_ms": 45,
    "operations": [
      { "op": "tokenize", "result": "18 tokens" },
      { "op": "entity_extract", "entities": ["presentation", "cognitive architectures", "ETH", "next Tuesday"] },
      { "op": "temporal_resolve", "next_tuesday": "2025-01-21" }
    ]
  },
  
  "3_uil_parsing": {
    "phase": "SENSEMAKING",
    "duration_ms": 120,
    "intent": {
      "type": "PLAN",
      "subject": { "type": "user", "id": "usr_ivan" },
      "predicate": { "verb": "plan", "domain": "productivity" },
      "object": { "type": "artifact", "class": "presentation", "topic": "cognitive architectures" },
      "constraints": [
        { "type": "temporal", "deadline": "2025-01-21T00:00:00Z" },
        { "type": "context", "event": "ETH meeting" }
      ],
      "confidence": 0.94,
      "provenance": {
        "agent": "uil_parser",
        "model": "gpt-4o-mini",
        "source": "user",
        "timestamp": "2025-01-15T10:30:00.045Z"
      }
    }
  },
  
  "4_memory_retrieval": {
    "phase": "SENSEMAKING",
    "duration_ms": 230,
    "queries": [
      {
        "query": "cognitive architectures research",
        "tier": "LTM",
        "results": 12,
        "top_relevance": 0.89
      },
      {
        "query": "ETH presentations past",
        "tier": "MTM",
        "results": 3,
        "top_relevance": 0.76
      },
      {
        "query": "user presentation preferences",
        "tier": "LTM",
        "results": 5,
        "top_relevance": 0.82
      }
    ],
    "graph_state_before": {
      "relevant_nodes": 20,
      "active_goals": ["phd_preparation", "eth_contact"]
    }
  },
  
  "5_agent_routing": {
    "phase": "MODELING",
    "duration_ms": 85,
    "routing_decision": {
      "primary_agent": "productivity_crew",
      "supporting_agents": ["research_crew", "writing_crew"],
      "routing_reason": "PLAN intent + productivity domain + research context",
      "confidence": 0.91
    }
  },
  
  "6_agent_execution": {
    "phase": "MODELING",
    "duration_ms": 1950,
    "agents": [
      {
        "agent": "productivity_crew",
        "model": "gpt-4o",
        "task": "generate_presentation_outline",
        "latency_ms": 1200,
        "tokens_in": 2400,
        "tokens_out": 850,
        "cost_usd": 0.0163,
        "output": {
          "outline": [
            "1. Introduction to Cognitive Architectures",
            "2. Language of Thought (LoT) Foundations",
            "3. UIL: Universal Intent Language",
            "4. Harmonia Kernel Architecture",
            "5. PSMR Cognitive Pipeline",
            "6. Demo & Implementation Status",
            "7. Research Agenda & Collaboration"
          ],
          "estimated_duration_minutes": 15,
          "suggested_visuals": 12
        }
      },
      {
        "agent": "research_crew",
        "model": "gpt-4o-mini",
        "task": "gather_supporting_references",
        "latency_ms": 450,
        "output": {
          "references": [
            { "title": "Language of Thought Hypothesis", "author": "Fodor", "relevance": 0.92 },
            { "title": "Cognitive Architectures Survey", "author": "Langley et al.", "relevance": 0.88 }
          ]
        }
      }
    ],
    "conflict_resolution": null
  },
  
  "7_thinking_panel": {
    "phase": "MODELING",
    "visible_reasoning": [
      "Analyzing request: presentation planning with academic context",
      "Retrieved 12 relevant memory nodes about cognitive architectures",
      "Identified ETH meeting as high-stakes context → formal structure recommended",
      "User preference: visual presentations, 15-20 min duration",
      "Generating 7-section outline with demo emphasis",
      "Cross-referencing with PhD preparation goal"
    ],
    "meta_decisions": [
      { "decision": "include_demo_section", "reason": "user has working prototype" },
      { "decision": "emphasize_formal_foundations", "reason": "academic audience" }
    ]
  },
  
  "8_memory_write": {
    "phase": "RESPONSE",
    "duration_ms": 180,
    "operations": [
      {
        "op": "create_node",
        "node_type": "artifact",
        "node_id": "node_pres_eth_2025_01",
        "tier": "STM",
        "links": ["goal_eth_contact", "goal_phd_preparation"]
      },
      {
        "op": "update_node",
        "node_id": "goal_eth_contact",
        "update": { "progress": 0.3, "last_activity": "2025-01-15" }
      }
    ],
    "graph_state_after": {
      "new_nodes": 1,
      "updated_nodes": 1,
      "new_edges": 2
    }
  },
  
  "9_output_generation": {
    "phase": "RESPONSE",
    "duration_ms": 220,
    "outputs": [
      {
        "type": "text",
        "content": "I've created a presentation outline for your ETH meeting...",
        "tokens": 450
      },
      {
        "type": "structured_data",
        "format": "presentation_outline",
        "sections": 7
      }
    ],
    "delivery": {
      "channel": "chat",
      "tts_enabled": false,
      "avatar_enabled": false
    }
  },
  
  "10_feedback_loop": {
    "phase": "COMPLETE",
    "awaiting_feedback": true,
    "follow_up_suggestions": [
      "Would you like me to draft the introduction?",
      "Should I create speaker notes for each section?",
      "Want me to generate slide mockups?"
    ]
  },
  
  "summary": {
    "success": true,
    "total_latency_ms": 2847,
    "total_cost_usd": 0.0189,
    "models_used": ["gpt-4o", "gpt-4o-mini"],
    "agents_activated": 2,
    "memory_operations": 3,
    "confidence_final": 0.91
  }
}
```

---

## 15.8 Anti-LLM Demonstration

### 15.8.1 What Works Without LLM

| Component | LLM Required | Function Without LLM |
|-----------|--------------|---------------------|
| UIL Parser | No* | Rule-based parsing for common patterns |
| Intent Router | No | Keyword + embedding similarity routing |
| Memory Store | No | Full CRUD, graph traversal, retrieval |
| Scheduler | No | Priority queue, path classification |
| Audit Logger | No | Complete logging and reporting |
| Cache Layer | No | LRU caching, semantic dedup |
| Conflict Detector | No | Rule-based conflict identification |

*UIL parsing can fall back to rule-based for simple intents

### 15.8.2 Kernel Isolation Test

```typescript
async function run_anti_llm_demo(): Promise<DemoResult> {
  // Disable all LLM calls
  const kernel = new HarmoniaKernel({ llm_enabled: false });
  
  // Test 1: UIL Parsing (rule-based)
  const intent1 = kernel.parse("create reminder for tomorrow 9am");
  assert(intent1.type === IntentType.ACTION);
  assert(intent1.predicate.verb === "create");
  // ✓ Works without LLM
  
  // Test 2: Memory Operations
  await kernel.memory.store({
    content: "Meeting with ETH professor",
    timestamp: new Date(),
    tags: ["meeting", "eth", "phd"]
  });
  const retrieved = await kernel.memory.query("ETH meetings");
  assert(retrieved.length > 0);
  // ✓ Works without LLM
  
  // Test 3: Routing (embedding-based)
  const route = kernel.router.classify(intent1);
  assert(route.domain === "productivity");
  // ✓ Works with pre-computed embeddings
  
  // Test 4: Scheduling
  const path = kernel.scheduler.classify(intent1);
  assert(path === ProcessingPath.FAST);
  // ✓ Works without LLM
  
  // Test 5: What FAILS without LLM
  try {
    await kernel.execute_deep_reasoning(intent1);
  } catch (e) {
    assert(e.message === "LLM required for deep reasoning");
    // ✓ Expected failure - proves isolation
  }
  
  return {
    components_working_without_llm: 4,
    components_requiring_llm: 1,
    kernel_isolation_verified: true
  };
}
```

### 15.8.3 Value Without LLM

The Harmonia kernel provides value even with a "dumb" model:

1. **Structured Intent Representation** — Every interaction becomes machine-readable UIL
2. **Persistent Memory Graph** — Context accumulates across sessions
3. **Transparent Audit Trail** — Every decision is logged and traceable
4. **Cognitive Scheduling** — Fast path optimization regardless of model quality
5. **Conflict Detection** — System-level inconsistencies are caught

**Thesis claim:** The architecture is the contribution, not the LLM capability.

---

## 15.9 Non-AI Evaluation Metrics

### 15.9.1 Cognitive Load Reduction (CLR)

```typescript
interface CognitiveLoadMetric {
  name: "CLR";
  definition: "Reduction in user cognitive effort to achieve a goal";
  measurement: {
    baseline: "steps_without_system";
    with_system: "steps_with_system";
    formula: "(baseline - with_system) / baseline";
  };
  target: "> 0.4 (40% reduction)";
}

// Measurement protocol
async function measure_cognitive_load(task: Task, user: User): Promise<CLRResult> {
  // Baseline: User performs task without system
  const baseline_session = await run_baseline_session(task, user);
  
  // Treatment: User performs equivalent task with system
  const treatment_session = await run_treatment_session(task, user);
  
  return {
    baseline_steps: baseline_session.interaction_count,
    baseline_time_s: baseline_session.duration_s,
    baseline_errors: baseline_session.error_count,
    
    treatment_steps: treatment_session.interaction_count,
    treatment_time_s: treatment_session.duration_s,
    treatment_errors: treatment_session.error_count,
    
    clr_steps: 1 - (treatment_session.interaction_count / baseline_session.interaction_count),
    clr_time: 1 - (treatment_session.duration_s / baseline_session.duration_s),
    clr_errors: 1 - (treatment_session.error_count / baseline_session.error_count)
  };
}
```

### 15.9.2 Intention Continuity (IC)

```typescript
interface IntentionContinuityMetric {
  name: "IC";
  definition: "Degree to which system maintains user's goal across interruptions";
  measurement: {
    method: "session_analysis";
    signals: [
      "goal_resumption_after_break",
      "context_preservation_accuracy",
      "proactive_reminder_relevance"
    ];
  };
  target: "> 0.8 (80% continuity)";
}

function calculate_intention_continuity(sessions: Session[]): number {
  let continuity_score = 0;
  let opportunities = 0;
  
  for (const session of sessions) {
    // Check if session correctly resumed previous goals
    if (session.has_prior_context) {
      opportunities++;
      
      const resumed_correctly = session.resumed_goals.filter(
        g => session.prior_goals.includes(g)
      ).length;
      
      const resumption_rate = resumed_correctly / session.prior_goals.length;
      continuity_score += resumption_rate;
    }
    
    // Check proactive reminders
    for (const reminder of session.proactive_reminders) {
      opportunities++;
      if (reminder.user_found_relevant) {
        continuity_score += 1;
      }
    }
  }
  
  return continuity_score / opportunities;
}
```

### 15.9.3 Temporal Coherence (TC)

```typescript
interface TemporalCoherenceMetric {
  name: "TC";
  definition: "Consistency of system's world model over time";
  measurement: {
    method: "contradiction_detection";
    signals: [
      "fact_consistency_over_sessions",
      "preference_stability",
      "goal_progress_monotonicity"
    ];
  };
  target: "> 0.9 (90% coherence)";
}

async function measure_temporal_coherence(
  memory_graph: MemoryGraph,
  time_window: DateRange
): Promise<TCResult> {
  const snapshots = await memory_graph.get_snapshots(time_window);
  
  let contradictions = 0;
  let total_facts = 0;
  
  for (let i = 1; i < snapshots.length; i++) {
    const prev = snapshots[i - 1];
    const curr = snapshots[i];
    
    // Check for contradictions
    const conflicts = detect_contradictions(prev, curr);
    contradictions += conflicts.length;
    
    // Count facts
    total_facts += curr.fact_count;
  }
  
  const coherence = 1 - (contradictions / total_facts);
  
  return {
    coherence_score: coherence,
    contradictions_found: contradictions,
    total_facts_checked: total_facts,
    time_window: time_window
  };
}
```

### 15.9.4 Evaluation Protocol Summary

| Metric | Method | Sample Size | Success Criterion |
|--------|--------|-------------|-------------------|
| CLR | A/B user study | n=30 | > 40% reduction |
| IC | Session log analysis | 500 sessions | > 80% continuity |
| TC | Graph consistency check | 10,000 facts | > 90% coherence |

---

## 15.10 MVP Development Trajectory

### Phase 1: Foundation (Months 0–2)

**Deliverables:**
- UIL v0.1 formal specification ✓
- Graph Memory minimal implementation
- 3 agents maximum (router, executor, memory)
- 1 task type: personal planning

**Success criteria:**
- UIL parses 90% of planning intents correctly
- Memory persists across sessions
- End-to-end trace for simple planning task

### Phase 2: Lifecycle (Months 2–4)

**Deliverables:**
- Memory promotion/eviction rules
- Agent conflict arbitration
- Thinking Panel (trace viewer)
- 3 additional agents (research, writing, scheduling)

**Success criteria:**
- Memory correctly promotes high-value items
- Conflicts resolved without user intervention 80% of time
- Visible reasoning traces for all operations

### Phase 3: Multimodal (Months 4–6)

**Deliverables:**
- Voice input (STT integration)
- Limited autonomous loop (proactive reminders)
- Robust persistence (crash recovery)
- 10 specialist crews

**Success criteria:**
- Voice commands parsed at 85% accuracy
- Autonomous reminders rated helpful > 70%
- Zero data loss on crash

### Phase 4: Validation (Months 6–9)

**Deliverables:**
- Scale test (1000+ memory nodes)
- User study (n=30)
- Academic paper draft
- Demo video + live presentation

**Success criteria:**
- CLR > 40%
- IC > 80%
- TC > 90%
- Paper accepted at workshop/venue

---

## 15.11 Conclusion

This chapter transforms architectural vision into executable specification. The formal contracts (UIL schema, memory lifecycle, failure model) provide the rigor required for scientific evaluation. The traceable scenario demonstrates that the system is not theoretical but implementable.

**Key contributions of this chapter:**

1. **UIL Formal Specification** — Type-safe intent representation with BNF grammar
2. **Memory Lifecycle Rules** — Explicit promotion, eviction, and conflict resolution
3. **Failure Model** — Comprehensive error taxonomy with recovery strategies
4. **Cognitive Scheduler** — Latency-aware processing path classification
5. **Anti-LLM Proof** — Demonstration that the kernel provides value independent of model capability
6. **Non-AI Metrics** — Evaluation framework beyond traditional ML benchmarks

The discipline of implementation—not the grandeur of vision—determines whether AMI succeeds as a scientific contribution.
