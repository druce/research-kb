# Research Notes: a-practical-guide-to-building-agents (1)

**Source:** `a-practical-guide-to-building-agents (1)`  
**Processed:** research-kb

---

**Key Finding: Agents Automate Workflows with Independence**
Agents are systems that independently accomplish tasks on behalf of users, streamlining and automating workflows with a high degree of independence.

---
**Key Finding: Agents Suited for Complex, Ambiguous Workflows**
Agents are uniquely suited to workflows where traditional deterministic and rule-based approaches fall short, particularly those involving nuanced judgment, exceptions, or context-sensitive decisions.

---
**Key Finding: Incremental Approach to Agent Building**
Customers typically achieve greater success with an incremental approach to agent building, rather than immediately building a fully autonomous agent with complex architecture.

---
**Key Finding: Guardrails are Critical for Safe and Predictable Operation**
Guardrails are a critical component of any LLM-based deployment, helping ensure agents operate safely and predictably in production.

---
**Supporting Fact: Distinguishing Agents from Simple LLM Applications**
Applications that integrate LLMs but don’t use them to control workflow execution—think simple chatbots, single-turn LLMs, or sentiment classifiers—are not agents.

---
**Supporting Fact: Three Core Components of an Agent**
An agent consists of three core components: the LLM (Model), external functions or APIs (Tools), and explicit guidelines and guardrails (Instructions).

---
**Critical Capability: Model Selection**
Select models based on task complexity, latency, and cost, using a variety of models for different tasks in the workflow. Start with the most capable model to establish a performance baseline, then try swapping in smaller models to optimize for cost and latency.

---
**Critical Capability: Defining and Standardizing Tools**
Each tool should have a standardized definition, enabling flexible, many-to-many relationships between tools and agents. Well-documented, thoroughly tested, and reusable tools improve discoverability, simplify version management, and prevent redundant definitions.

---
**Critical Capability: Configuring Instructions**
High-quality instructions are essential for any LLM-powered app, but especially critical for agents. Clear instructions reduce ambiguity and improve agent decision-making, resulting in smoother workflow execution and fewer errors.

---
**Critical Capability: Orchestration Patterns**
Orchestration patterns fall into two categories: Single-agent systems, where a single model executes workflows in a loop, and multi-agent systems, where workflow execution is distributed across multiple coordinated agents.

---
**Decision: When to Create Multiple Agents**
Consider splitting tasks across multiple agents when prompts contain many conditional statements, or when there is tool overload (similarity or overlap of tools).

---
**Best Practice: Maximize Single Agent Capabilities First**
Maximize a single agent’s capabilities before introducing multiple agents, as more agents can introduce additional complexity and overhead.

---
**Best Practice: Use Prompt Templates for Single-Agent Systems**
Use a single flexible base prompt that accepts policy variables, rather than maintaining numerous individual prompts for distinct use cases. This template approach adapts easily to various contexts, significantly simplifying maintenance and evaluation.

---
**Best Practice: Layered Defense with Guardrails**
Use multiple, specialized guardrails together to create more resilient agents, combining LLM-based guardrails, rules-based guardrails such as regex, and moderation APIs.

---
**AI Roadmap: Iterative Development and Validation**
Start small, validate with real users, and grow capabilities over time.

---
**AI Roadmap: Focus on Data Privacy and Content Safety First**
When building guardrails, focus on data privacy and content safety first, then add new guardrails based on real-world edge cases and failures encountered.

---
**AI Roadmap: Optimistic Execution with Guardrails**
Implement guardrails using an optimistic execution approach, where the primary agent proactively generates outputs while guardrails run concurrently, triggering exceptions if constraints are breached.

---
**AI Roadmap: Plan for Human Intervention**
Implement a human intervention mechanism to allow the agent to gracefully transfer control when it can’t complete a task, triggered by exceeding failure thresholds or high-risk actions.

---
**Guardrails: Relevance Classifier**
A relevance classifier ensures agent responses stay within the intended scope by flagging off-topic queries.

---
**Guardrails: Safety Classifier**
A safety classifier detects unsafe inputs (jailbreaks or prompt injections) that attempt to exploit system vulnerabilities.

---
**Guardrails: PII Filter**
A PII filter prevents unnecessary exposure of personally identifiable information (PII) by vetting model output for any potential PII.

---
**Guardrails: Tool Safeguards**
Assess the risk of each tool available to your agent by assigning a rating—low, medium, or high—based on factors like read-only vs. write access, reversibility, required account permissions, and financial impact.