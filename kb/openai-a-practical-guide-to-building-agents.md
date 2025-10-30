# Research Notes: openai-a-practical-guide-to-building-agents

**Source:** `openai-a-practical-guide-to-building-agents`  
**Processed:** research-kb

---

**Key Finding: Agents Automate End-to-End Workflows**
Agents represent a new era in workflow automation, reasoning through ambiguity, acting across tools, and handling multi-step tasks autonomously, unlike simpler LLM applications.

---

**Key Finding: Agents Suited for Complex, Unstructured Tasks**
Agents are well-suited for use cases involving complex decisions, unstructured data, or brittle rule-based systems.

---

**Agent Definition**
Agents are systems that independently accomplish tasks on your behalf, leveraging an LLM to manage workflow execution and make decisions.

---

**Non-Agent Examples**
Simple chatbots, single-turn LLMs, or sentiment classifiers are not agents because they don't use LLMs to control workflow execution.

---

**Agent Core Characteristics**
Agents leverage an LLM for decision-making, recognize workflow completion, proactively correct actions, and halt execution to transfer control to the user if needed.

---

**Agent Components: Model, Tools, Instructions**
An agent consists of an LLM (Model), external functions/APIs (Tools), and explicit guidelines/guardrails (Instructions).

---

**Critical Capability: Tool Access and Selection**
Agents need access to various tools to interact with external systems, dynamically selecting appropriate tools based on the workflow's current state, within defined guardrails.

---

**When to Build an Agent: Prioritize Difficult-to-Automate Workflows**
Prioritize workflows that have previously resisted automation, especially where traditional deterministic and rule-based methods encounter friction.

---

**Use Case Criteria for Agents: Complex Decisions, Rules Maintenance, Unstructured Data**
Consider agents for workflows involving nuanced judgment, difficult-to-maintain rulesets, or heavy reliance on unstructured data.

---

**Model Selection: Start with Capable Model, Optimize Later**
Build your agent prototype with the most capable model to establish a performance baseline, then try swapping in smaller models to optimize for cost and latency.

---

**Model Selection: Performance Baseline**
Set up evals to establish a performance baseline for model performance.

---

**Model Selection: Accuracy Target**
Focus on meeting your accuracy target with the best models available.

---

**Model Selection: Cost and Latency Optimization**
Optimize for cost and latency by replacing larger models with smaller ones where possible.

---

**Tool Types: Data, Action, Orchestration**
Agents need tools for data retrieval, action execution (e.g., sending emails), and orchestration (using other agents as tools).

---

**Best Practice: Standardized Tool Definitions**
Each tool should have a standardized definition, enabling flexible, many-to-many relationships between tools and agents, improving discoverability and version management.

---

**Best Practice: Use Existing Documents for Instructions**
Use existing operating procedures, support scripts, or policy documents to create LLM-friendly routines.

---

**Best Practice: Prompt Agents to Break Down Tasks**
Providing smaller, clearer steps from dense resources helps minimize ambiguity and helps the model better follow instructions.

---

**Best Practice: Define Clear Actions**
Make sure every step in your routine corresponds to a specific action or output.

---

**Best Practice: Capture Edge Cases**
A robust routine anticipates common variations and includes instructions on how to handle them with conditional steps or branches.

---

**AI Roadmap: Incremental Approach to Agent Building**
Customers typically achieve greater success with an incremental approach, rather than immediately building a fully autonomous agent with complex architecture.

---

**Orchestration Patterns: Single-Agent vs. Multi-Agent**
Orchestration patterns fall into single-agent systems (one model executing workflows in a loop) and multi-agent systems (workflow execution distributed across coordinated agents).

---

**Single-Agent Systems: Manage Complexity with Prompt Templates**
Use a single flexible base prompt that accepts policy variables to adapt easily to various contexts, significantly simplifying maintenance and evaluation.

---

**When to Consider Multiple Agents: Complex Logic or Tool Overload**
Consider splitting tasks across multiple agents when prompts contain many conditional statements or when tool similarity/overlap hinders performance.

---

**Multi-Agent Patterns: Manager vs. Decentralized**
Multi-agent systems can be Manager (central agent orchestrates specialized agents) or Decentralized (agents hand off tasks to one another).

---

**Manager Pattern: Centralized Control**
The manager pattern empowers a central LLM to orchestrate a network of specialized agents seamlessly through tool calls.

---

**Decentralized Pattern: Agent Handoffs**
In a decentralized pattern, agents can ‘handoff’ workflow execution to one another, optimal when you don’t need a single agent maintaining central control or synthesis.

---

**Critical Capability: Guardrails for Safety and Predictability**
Guardrails are critical at every stage, from input filtering and tool use to human-in-the-loop intervention, helping ensure agents operate safely and predictably in production.

---

**Guardrails: Layered Defense Mechanism**
Using multiple, specialized guardrails together creates more resilient agents.

---

**Guardrail Types: Relevance, Safety, PII, Moderation, Tool Safeguards, Rules-Based, Output Validation**
Examples include relevance classifiers, safety classifiers, PII filters, moderation, tool safeguards, rules-based protections, and output validation.

---

**Guardrail Implementation: Focus on Data Privacy and Content Safety**
Set up guardrails that address the risks you’ve already identified for your use case and layer in additional ones as you uncover new vulnerabilities.

---

**Guardrail Implementation: Add New Guardrails Based on Real-World Edge Cases**
Add new guardrails based on real-world edge cases and failures you encounter.

---

**Guardrail Implementation: Optimize for Security and User Experience**
Optimize for both security and user experience, tweaking your guardrails as your agent evolves.

---

**Critical Capability: Human Intervention**
Human intervention is a critical safeguard enabling you to improve an agent’s real-world performance without compromising user experience.

---

**Human Intervention Triggers: Failure Thresholds and High-Risk Actions**
Two primary triggers typically warrant human intervention: exceeding failure thresholds and high-risk actions.

---

**AI Roadmap: Start Small, Validate, and Grow**
The path to successful deployment isn’t all-or-nothing. Start small, validate with real users, and grow capabilities over time.