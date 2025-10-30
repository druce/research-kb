# Research Notes: Cognitive architectures for llm agents

**Source:** `Cognitive architectures for llm agents`  
**Processed:** research-kb

---

**CoALA: Cognitive Architectures for Language Agents**
CoALA is a conceptual framework to characterize and design general-purpose language agents, drawing parallels with cognitive science and symbolic AI. It organizes agents along three key dimensions: information storage (memory), action space (internal/external), and decision-making procedure.

---
**Key Finding: Language Agents as a Synthesis**
Language agents synthesize advances in LLMs with traditional agent design, mitigating LLMs' limitations in knowledge and reasoning by connecting them to memory and environments, while leveraging LLMs' commonsense priors to adapt to novel tasks.

---
**Key Finding: CoALA as a Theoretical Framework**
CoALA combines theoretical framework with empirical work, grounding theory in existing practices and identifying short-term and long-term directions for future work in language agent design.

---
**Key Capability: Memory Modules**
Language agents should explicitly organize information into multiple memory modules, including short-term working memory and long-term episodic, semantic, and procedural memories, to enable multi-step interaction with the world.

---
**Key Capability: Action Space Structure**
Agents' action spaces should be structured into internal (retrieval, reasoning, learning) and external (grounding) actions, allowing for both interaction with internal memory and external environments.

---
**Key Capability: Decision-Making Procedure**
Language agents need a well-defined decision-making procedure, structured as an interactive loop with planning and execution, to choose actions based on reasoning and retrieval, affecting the outside world or the agent's long-term memory.

---
**Key Quote: Reasoning Actions**
"Yet the incorporation of an LLM leads to the addition of 'reasoning' actions, which can flexibly produce new knowledge and heuristics for various purposes – replacing hand-written rules in traditional cognitive architectures."

---
**Key Quote: Text as Internal Representation**
"It also makes text the de facto internal representation, streamlining agents’ memory modules. Finally, recent advances in vision-language models (VLMs; Alayrac et al., 2022) can simplify grounding by providing a straightforward translation of perceptual data into text (Zeng et al., 2022)."

---
**Critical Capability: Grounding Actions**
Grounding procedures should execute external actions and process environmental feedback into working memory as text, simplifying the agent's interaction with the outside world.

---
**Critical Capability: Retrieval Actions**
Retrieval procedures should read information from long-term memories into working memory, implemented in various ways (rule-based, sparse, or dense retrieval), to support adaptive and context-specific recall.

---
**Critical Capability: Reasoning Actions**
Reasoning actions should allow language agents to process the contents of working memory to generate new information, supporting learning and decision-making.

---
**Critical Capability: Learning Actions**
Learning actions should write information to long-term memory, including updating episodic memory with experience, semantic memory with knowledge, LLM parameters, and agent code.

---
**Critical Capability: Planning Stage**
During the planning stage of decision-making, reasoning and retrieval can be flexibly applied to propose, evaluate, and select actions, and these sub-stages could interleave or iterate to build up multi-step simulations before taking an external action.

---
**Best Practice: Modular Agent Design**
Agents should be structured and modular, with standardized terms and open-source implementations to facilitate plug-and-play and re-use, reducing technical debt and standardizing the customer experience.

---
**Best Practice: Balancing Code and LLMs**
Use code sparingly to implement generic algorithms that complement LLM limitations, such as implementing tree search to mitigate myopia induced by autoregressive generation.

---
**Best Practice: Structured Reasoning**
Implement a more structured reasoning procedure to update working memory variables, using prompting frameworks and structural output parsing solutions.

---
**AI Roadmap: Beyond Retrieval Augmentation**
Move beyond traditional retrieval-augmented language models by enabling memory-augmented language agents to both read and write self-generated content autonomously, opening up possibilities for efficient lifelong learning.

---
**AI Roadmap: Meta-Learning**
Explore meta-learning by modifying agent code to allow agents to learn more effectively, such as learning better retrieval procedures.

---
**AI Roadmap: Action Space Safety**
Specify and ablate the agent’s action space for worst-case scenario prediction and prevention, especially for "learning" and "grounding" actions that could cause internal or external harm.

---
**AI Roadmap: Deliberative Decision-Making**
Investigate more complex decision-making employing iterative proposal and evaluation to consider multiple actions, modeled after classical planning algorithms.

---
**AI Roadmap: Metareasoning**
Develop mechanisms to estimate the utility of planning and modify the decision procedure accordingly, either via amortization, routing among decision sub-procedures, or updates to the decision-making procedure.

---
**Measuring Success: Performance and Generalization**
Trade-off between performance and generalization when defining the decision-making procedure; more complex procedures can better fit a particular problem, while simpler ones are more domain-agnostic and generalizable.

---
**Measuring Success: Safety and Alignment**
Address issues such as over-confidence, miscalibration, misalignment with human values, hallucinations in self-evaluation, and lack of human-in-the-loop mechanisms to improve LLMs' utilities as agent backbones.