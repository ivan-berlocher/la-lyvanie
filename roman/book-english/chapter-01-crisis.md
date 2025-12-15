# Chapter 1

## The Representation Crisis

---

### 1.1 Introduction

Artificial intelligence has achieved remarkable successes. Systems now defeat world champions at Go, generate human-quality text, translate between languages in real-time, and recognize objects in images with superhuman accuracy. By many metrics, AI has exceeded expectations that seemed optimistic just a decade ago.

Yet something is wrong.

These same systems make errors that no human would make. They confidently assert falsehoods. They fail in ways that are difficult to predict, diagnose, or repair. And crucially, we often cannot explain *why* they behave as they do — even to ourselves, let alone to the humans who must trust and use them.

This chapter argues that these problems share a common root: a **representation crisis**. Modern AI systems, particularly deep neural networks, have optimized for performance while abandoning interpretable representation. The result is systems that work but cannot be understood.

Understanding this crisis is the first step toward addressing it.

---

### 1.2 The Black Box Problem

#### 1.2.1 Definition

**Definition 1.1 (Black Box System)**: A computational system is a *black box* with respect to property P if the internal states and processes that determine P are not accessible to external inspection in a form that supports human understanding, verification, or modification.

This definition is relative: a system may be transparent with respect to some properties (e.g., input-output behavior) while opaque with respect to others (e.g., the causal chain from input to output).

#### 1.2.2 Modern Neural Networks as Black Boxes

Consider a deep neural network trained for image classification. The network receives an image (a tensor of pixel values), propagates activations through layers of learned weights, and outputs a probability distribution over classes.

Mathematically, for a network with L layers:

$$\mathbf{h}^{(0)} = \mathbf{x}$$
$$\mathbf{h}^{(l)} = \sigma(\mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}) \quad \text{for } l = 1, \ldots, L-1$$
$$\mathbf{y} = \text{softmax}(\mathbf{W}^{(L)} \mathbf{h}^{(L-1)} + \mathbf{b}^{(L)})$$

Where:
- **x** is the input
- **h**^(l) is the hidden activation at layer l
- **W**^(l), **b**^(l) are learned parameters
- σ is a nonlinearity (ReLU, tanh, etc.)
- **y** is the output distribution

The computation is entirely specified. Every operation is a standard mathematical function. There are no hidden random processes or inaccessible states. Yet the system is a black box in a critical sense: the intermediate representations **h**^(l) do not correspond to human-interpretable concepts.

#### 1.2.3 Why Interpretability is Lost

The representations learned by neural networks are optimized for a single objective: minimizing loss on the training distribution. There is no constraint requiring that intermediate representations be human-interpretable.

In fact, interpretable representations may be *suboptimal* for loss minimization. A representation that entangles many features in a way humans cannot parse might nonetheless be highly effective for prediction.

**Theorem 1.1 (Representation-Performance Tradeoff, Informal)**: For many learning problems, the space of high-performing solutions includes both interpretable and uninterpretable representations. Gradient-based optimization provides no preference for interpretability.

This is not a bug in neural network training — it is a direct consequence of optimizing purely for predictive performance.

---

### 1.3 The Consequences of Opacity

The black box problem would be merely academic if opacity had no practical consequences. Unfortunately, it creates severe problems across multiple dimensions.

#### 1.3.1 Verification Failure

**Problem**: We cannot formally verify that a black box system satisfies desired properties.

Traditional software verification uses techniques like model checking, theorem proving, and testing to establish that code meets specifications. These techniques assume we can reason about program structure.

For a neural network, we can verify:
- That the architecture is correctly implemented
- That training converged (loss decreased)
- That test accuracy meets some threshold

We cannot easily verify:
- That the network has learned the "right" concept (rather than a spurious correlation)
- That performance will generalize to distribution shift
- That no adversarial inputs exist that cause catastrophic failure

**Example 1.1 (Spurious Correlation)**: A network trained to classify "wolf" vs "husky" achieves 95% test accuracy. Investigation reveals the network has learned to detect snow in the background (wolves photographed in snow, huskies in grass). The network has learned a spurious correlation rather than distinguishing the animals themselves (Ribeiro et al., 2016).

The test set, drawn from the same distribution as training, cannot reveal this failure. The opacity of internal representations prevents us from verifying what concept was actually learned.

#### 1.3.2 Correction Failure

**Problem**: We cannot precisely repair errors in systems we do not understand.

When a black box makes an error, we have limited options:
1. Add the failing case to training data and retrain
2. Collect more data in the failing region
3. Modify the architecture and retrain
4. Accept the error

None of these is *targeted repair*. We cannot identify the specific internal state responsible for the error and modify it directly. Retraining may fix the observed error while introducing new ones — a phenomenon sometimes called "whack-a-mole debugging."

**Contrast**: In a symbolic system with explicit knowledge representation, if the system makes an error because of an incorrect rule, we can identify and modify that specific rule. The repair is local and its effects are predictable.

#### 1.3.3 Trust Failure

**Problem**: We cannot establish justified trust in systems whose reasoning we cannot follow.

Trust requires more than track record. We trust human experts not only because they are usually right, but because:
- They can explain their reasoning
- We can evaluate whether their reasoning is sound
- We can identify when they are operating outside their competence
- We can update our models of their reliability based on new information

Black box systems cannot provide these justifications. A system's confidence score (softmax probability) does not necessarily correlate with actual reliability, especially under distribution shift.

**Example 1.2 (Overconfidence)**: Neural networks are often highly confident in their predictions, even when wrong. A network may assign 99% probability to an incorrect class. This makes calibrated trust impossible (Guo et al., 2017).

#### 1.3.4 Alignment Failure

**Problem**: We cannot verify that a system pursues intended objectives.

The alignment problem asks: how do we ensure an AI system's behavior aligns with human intentions? This is difficult even when we can inspect the system's goals and reasoning. It becomes nearly impossible when we cannot.

A black box may be optimizing for an objective subtly different from what we intended. Without interpretable internals, we can only observe this through behavioral testing — which may not cover the situations where misalignment matters.

---

### 1.4 Historical Context: Symbolic vs. Subsymbolic

The representation crisis is not new. It recapitulates a debate that has structured AI since its founding.

#### 1.4.1 The Symbolic Tradition

Classical AI, dominant from the 1950s through the 1980s, was built on explicit symbolic representation:

- **McCarthy's Advice Taker (1958)**: Knowledge as logical sentences, reasoning as theorem proving
- **Newell & Simon's GPS (1959)**: Problems represented as state spaces, solved by search
- **Expert Systems (1970s-80s)**: Domain knowledge encoded as if-then rules

These systems were interpretable by design. Every inference could be traced, every conclusion justified by explicit rules.

**Advantages**:
- Transparent reasoning
- Easy to verify and debug
- Knowledge could be inspected and modified
- Strong formal foundations

**Disadvantages**:
- Knowledge acquisition bottleneck (humans must encode all rules)
- Brittleness (performance degrades outside narrow domains)
- Poor handling of uncertainty and perception
- Computational inefficiency for many problems

#### 1.4.2 The Connectionist Revolution

Starting in the 1980s and accelerating dramatically in the 2010s, neural networks offered an alternative:

- **Perceptrons and Backpropagation (1980s)**: Learning from examples rather than programming
- **Deep Learning (2010s)**: Hierarchical learned representations
- **Transformers (2017+)**: Attention-based architectures scaling to billions of parameters

**Advantages**:
- Learn directly from data
- Handle perception and pattern recognition
- Scale with compute and data
- State-of-the-art performance on many benchmarks

**Disadvantages**:
- Opaque internal representations
- Difficult to verify, correct, or explain
- Require massive data
- Unpredictable failure modes

#### 1.4.3 The Current Impasse

Modern AI is dominated by the connectionist paradigm. Deep learning has achieved results that symbolic methods never could on perception, language, and many other tasks.

But the problems of opacity have not been solved — they have been *accepted*. The field has traded interpretability for performance.

This trade-off may be acceptable for low-stakes applications (recommendation systems, image filters). It is not acceptable for high-stakes applications (medical diagnosis, autonomous vehicles, legal decisions) where verification, trust, and correction matter.

---

### 1.5 The Interpretability Research Program

Recognition of the black box problem has spawned a research program in "interpretability" or "explainable AI" (XAI). We survey the main approaches and their limitations.

#### 1.5.1 Post-Hoc Explanation Methods

**Approach**: Leave the model unchanged; generate explanations after the fact.

**Saliency Methods**: Highlight which input features most influenced the output.
- Gradient-based: compute ∂y/∂x to find influential inputs
- Perturbation-based: observe output changes when inputs are masked
- Examples: GradCAM, LIME, SHAP

**Limitations**:
- Explanations may not reflect actual model reasoning (Adebayo et al., 2018)
- Different methods give different explanations for the same prediction
- Explanations are local (per-prediction) not global (understanding the model)

#### 1.5.2 Concept-Based Explanations

**Approach**: Identify intermediate representations that correspond to human concepts.

**Probing Classifiers**: Train classifiers on hidden states to predict concept presence.

**Concept Activation Vectors (CAVs)**: Identify directions in activation space corresponding to concepts (Kim et al., 2018).

**Limitations**:
- Concepts found may be spurious (not causally relevant to behavior)
- Coverage is limited to concepts we think to probe for
- Representations may not be organized around human concepts at all

#### 1.5.3 Inherently Interpretable Models

**Approach**: Constrain model architecture to be interpretable by design.

**Examples**:
- Decision trees
- Sparse linear models
- Generalized additive models (GAMs)
- Rule lists

**Limitations**:
- Often lower performance than deep networks
- May not scale to complex perceptual tasks
- "Interpretable" architectures may still be complex enough to resist understanding

#### 1.5.4 Assessment

The XAI research program has produced useful tools but has not solved the fundamental problem. Post-hoc explanations may not reflect true reasoning. Probed concepts may be spurious. Interpretable models may sacrifice too much performance.

The core issue remains: optimizing purely for prediction does not produce interpretable systems, and retrofitting interpretability onto opaque systems is unreliable.

---

### 1.6 Toward a Solution: Structured Representation

This book proposes a different approach: rather than interpreting opaque systems, we should design systems that are interpretable by construction.

The key insight is that interpretability requires **structured representation** — internal states organized around discrete, compositional, human-aligned concepts.

#### 1.6.1 Desiderata for Interpretable Representation

**D1. Discreteness**: Representations should decompose into identifiable units (concepts, propositions, relations) rather than continuous activations.

**D2. Compositionality**: Complex representations should be built systematically from simpler components with predictable semantics.

**D3. Grounding**: Symbolic representations should be connected to perception and action in principled ways.

**D4. Accessibility**: Internal states should be externally inspectable in human-understandable form.

**D5. Modifiability**: It should be possible to change specific beliefs or rules without wholesale retraining.

These desiderata describe what classical symbolic AI had and modern neural AI lacks.

#### 1.6.2 The Path Forward

Achieving these desiderata while retaining the strengths of modern AI requires new architectures that integrate:

1. **Learned perception**: Neural networks excel at mapping raw input to useful features
2. **Structured representation**: Intermediate representations organized as discrete symbolic structures
3. **Explicit reasoning**: Inference over symbolic structures using interpretable operations
4. **Grounded action**: Mapping from symbolic plans to concrete actions

This integration is the subject of the remaining chapters.

---

### 1.7 Summary

Modern AI systems achieve impressive performance but suffer from a representation crisis: their internal representations are opaque, making verification, correction, trust, and alignment difficult or impossible.

This crisis reflects a historical choice: the field optimized for performance at the cost of interpretability. Post-hoc interpretability methods provide some insight but do not solve the fundamental problem.

A solution requires systems designed for interpretability from the ground up, with structured representations that satisfy desiderata of discreteness, compositionality, grounding, accessibility, and modifiability.

The next chapter introduces the theoretical foundation for such representations: the Language of Thought hypothesis.

---

### Key Concepts

- **Black box system**: A system whose internal processes are not accessible to human understanding
- **Representation crisis**: The systematic loss of interpretability in modern AI
- **Verification failure**: Inability to formally verify system properties
- **Correction failure**: Inability to make targeted repairs to reasoning
- **Structured representation**: Internal states organized as discrete, compositional, human-aligned concepts

---

### Exercises

**1.1** Give a formal definition of "interpretability" for AI systems. What are the challenges in making this precise?

**1.2** Consider a deep neural network trained for sentiment analysis. Describe three specific questions about its behavior that cannot be answered by examining its weights and architecture.

**1.3** Compare the failure modes of symbolic expert systems (1980s) with deep neural networks (2020s). What do they share? What differs?

**1.4** Analyze a published XAI technique (e.g., LIME, SHAP, GradCAM). What guarantees does it provide? What are its limitations?

**1.5** Design an experiment to test whether a neural network has learned a concept (e.g., "dog") versus a spurious correlation (e.g., "grass background"). What are the methodological challenges?

---

### Further Reading

- Lipton, Z. C. (2018). "The mythos of model interpretability." *Queue*, 16(3), 31-57.
- Rudin, C. (2019). "Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead." *Nature Machine Intelligence*, 1(5), 206-215.
- Adebayo, J., et al. (2018). "Sanity checks for saliency maps." *NeurIPS*.
- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?: Explaining the predictions of any classifier." *KDD*.

---

*End of Chapter 1*
