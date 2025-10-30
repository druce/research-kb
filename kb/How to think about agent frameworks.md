# Research Notes: How to think about agent frameworks

**Source:** `How to think about agent frameworks`  
**Processed:** research-kb

---

```markdown
**Key Finding: Context is Critical for Reliable Agents**
The most challenging aspect of building dependable agentic systems is ensuring the LLM receives the appropriate context at each step, including controlling content and generating relevant information.

---

**Agentic Systems: Workflows and Agents Combined**
Most "agentic systems" in production are a blend of predefined workflows and dynamically controlled agents, rather than purely one or the other.

---

**Agent Abstractions Can Obscure Context**
Agent abstractions can simplify initial development, but they often make it difficult to control and understand the context being passed to the LLM, hindering reliability.

---

**Frameworks Should Support Both Agents and Workflows**
A production-ready agentic framework needs to support both predefined workflows and dynamic agents, allowing developers to choose the right approach for each task.

---

**Key Quote: Simplicity First**
"When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all." — Anthropic

---

**Key Quote: Validate Agent Use Cases**
"Before committing to building an agent, validate that your use case can meet these criteria clearly. Otherwise, a deterministic solution may suffice." — OpenAI

---

**Agent Performance Quality is a Major Limitation**
A survey of agent builders revealed that "performance quality" is the biggest limitation in deploying more agents to production.

---

**Reasons for Poor Agent Performance**
LLM errors often stem from incomplete context, vague input, lack of access to tools, poor tool descriptions, or poorly formatted tool responses.

---

**LangGraph: An Orchestration Framework**
LangGraph is an orchestration framework with both declarative and imperative APIs, offering agent abstractions built on top.

---

**Predictability vs. Agency Trade-off**
As systems become more agentic, they become less predictable, which can impact user trust and regulatory compliance.

---

**Framework Floors and Ceilings**
Workflow frameworks have a high floor (require more initial effort) but a high ceiling (offer extensive capabilities), while agent frameworks have a low floor but a low ceiling.

---

**Agent Abstractions: Keras Analogy**
Agent abstractions are like Keras: they provide higher-level abstractions for easy starting, but should be built on a lower-level framework for advanced use cases.

---

**Multi-Agent Systems: Communication is Key**
In multi-agent systems, effective communication between agents is crucial, and workflows can sometimes be the best way to facilitate this.

---

**Value of an Agentic Framework**
Frameworks provide useful abstractions, short-term/long-term memory, human-in-the-loop/on-the-loop capabilities, streaming, debugging/observability, and fault tolerance.

---

**Key Capability: Debugging and Observability**
Being able to inspect the exact steps taken by an agent and the inputs/outputs at each step is crucial for building reliable agents.

---

**Frameworks: Understand the Underlying Code**
"If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error." — Anthropic

---

**Future of Agents vs. Workflows**
Even as models improve, controlling the context passed to the LLM will remain important, and production systems will likely combine workflows and agents.

---

**Unique Tasks May Require Custom Models**
If a task is unique, firms may need to train/finetune/RL their own models to achieve optimal agent performance, making workflow control less critical.

---

**Agent Frameworks: Focus on Orchestration**
The main value of a framework should be a reliable orchestration layer that provides explicit control over context and handles production concerns.

---

**OpenAI's Take on Agent Frameworks: Misses the Mark**
OpenAI's perspective conflates declarative vs. imperative approaches with agent abstractions and workflows vs. agents, ultimately missing the importance of a reliable orchestration layer.
```