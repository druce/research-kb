# Research Notes: Building effective agents _ Anthropic

**Source:** `Building effective agents _ Anthropic`  
**Processed:** research-kb

---

**Successful LLM Agent Implementations**
The most successful LLM agent implementations use simple, composable patterns rather than complex frameworks or specialized libraries. — Anthropic

---

**Agent Definition**
Agents are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. — Anthropic

---

**Workflow Definition**
Workflows are systems where LLMs and tools are orchestrated through predefined code paths. — Anthropic

---

**When to Use Agentic Systems**
Agentic systems often trade latency and cost for better task performance, making them suitable when flexibility and model-driven decision-making are needed at scale. — Anthropic

---

**When to Use Workflows**
Workflows offer predictability and consistency for well-defined tasks. — Anthropic

---

**Framework Considerations**
Frameworks can simplify initial implementation but may obscure underlying prompts and responses, making debugging harder and tempting unnecessary complexity. — Anthropic

---

**Best Practice: Start Simple**
Developers should start by using LLM APIs directly, as many patterns can be implemented in a few lines of code. If using a framework, ensure a thorough understanding of the underlying code. — Anthropic

---

**Building Block: Augmented LLM**
The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. — Anthropic

---

**Key Implementation Aspects: Augmented LLM**
Focus on tailoring LLM capabilities to the specific use case and ensuring an easy, well-documented interface. — Anthropic

---

**Workflow: Prompt Chaining**
Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. — Anthropic

---

**When to Use Prompt Chaining**
Prompt chaining is ideal for tasks that can be easily decomposed into fixed subtasks, trading latency for higher accuracy. — Anthropic

---

**Workflow: Routing**
Routing classifies an input and directs it to a specialized follow-up task, enabling separation of concerns and specialized prompts. — Anthropic

---

**When to Use Routing**
Routing works well for complex tasks with distinct categories that are better handled separately, provided classification can be handled accurately. — Anthropic

---

**Workflow: Parallelization**
Parallelization involves LLMs working simultaneously on a task, with outputs aggregated programmatically, either through sectioning (independent subtasks) or voting (multiple attempts). — Anthropic

---

**When to Use Parallelization**
Parallelization is effective when subtasks can be parallelized for speed or when multiple perspectives are needed for higher confidence results. — Anthropic

---

**Workflow: Orchestrator-Workers**
In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. — Anthropic

---

**When to Use Orchestrator-Workers**
This workflow is well-suited for complex tasks where you can’t predict the subtasks needed, and subtasks aren't pre-defined, but determined by the orchestrator based on the specific input. — Anthropic

---

**Workflow: Evaluator-Optimizer**
In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. — Anthropic

---

**When to Use Evaluator-Optimizer**
This workflow is particularly effective when there are clear evaluation criteria, and when iterative refinement provides measurable value. — Anthropic

---

**Agent Characteristics**
Agents understand complex inputs, engage in reasoning and planning, use tools reliably, and recover from errors. — Anthropic

---

**Agent Execution**
During execution, agents gain "ground truth" from the environment at each step to assess progress, pausing for human feedback at checkpoints or when encountering blockers. — Anthropic

---

**Tool Design for Agents**
It is crucial to design toolsets and their documentation clearly and thoughtfully for agents. — Anthropic

---

**When to Use Agents**
Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. — Anthropic

---

**Agent Considerations**
The autonomous nature of agents means higher costs and the potential for compounding errors, necessitating extensive testing in sandboxed environments and appropriate guardrails. — Anthropic

---

**Key to Success with LLM Features**
The key to success is measuring performance and iterating on implementations, adding complexity only when it demonstrably improves outcomes. — Anthropic

---

**Core Principles for Implementing Agents**
Maintain simplicity in agent design, prioritize transparency by showing planning steps, and carefully craft the agent-computer interface (ACI) through thorough tool documentation and testing. — Anthropic

---

**Customer Support Application**
Customer support combines chatbot interfaces with enhanced capabilities through tool integration, making it a natural fit for open-ended agents. — Anthropic

---

**Coding Agents Application**
The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. — Anthropic

---

**Prompt Engineering for Tools**
Tool definitions and specifications should be given just as much prompt engineering attention as overall prompts. — Anthropic

---

**Tool Format Suggestions**
Give the model enough tokens to "think", keep the format close to what the model has seen naturally occurring in text, and ensure there's no formatting "overhead". — Anthropic

---

**Agent-Computer Interface (ACI)**
Invest as much effort in creating a good ACI as you would in human-computer interfaces (HCI). — Anthropic

---

**Tool Testing and Optimization**
Test how the model uses your tools, run many example inputs to see what mistakes the model makes, and iterate. Poka-yoke your tools by changing the arguments so that it is harder to make mistakes. — Anthropic