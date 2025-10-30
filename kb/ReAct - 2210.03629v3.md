# Research Notes: ReAct - 2210.03629v3

**Source:** `ReAct - 2210.03629v3`  
**Processed:** research-kb

---

Okay, I've analyzed the document and extracted the following notes:

**ReAct: Synergizing Reasoning and Acting in Language Models**
ReAct is a novel prompting paradigm that combines reasoning and acting in language models by interleaving verbal reasoning traces and task-specific actions. This allows for dynamic reasoning to create and adjust plans, and interaction with external environments to incorporate information into reasoning. — [Yao et al., 2023]
---

**Key Finding: ReAct Outperforms Baselines**
ReAct demonstrates effectiveness over state-of-the-art baselines in question answering, fact verification, and interactive decision-making tasks. It shows improved human interpretability and trustworthiness. — [Yao et al., 2023]
---

**ReAct Addresses Hallucination and Error Propagation**
By interacting with external sources like a Wikipedia API, ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning. — [Yao et al., 2023]
---

**ReAct Improves Interactive Decision Making**
On interactive decision-making benchmarks like ALFWorld and WebShop, ReAct outperforms imitation and reinforcement learning methods with significant improvements in success rates. — [Yao et al., 2023]
---

**Key Quote: Synergy Between Acting and Reasoning**
"This tight synergy between 'acting' and 'reasoning' allows humans to learn new tasks quickly and perform robust decision making or reasoning, even under previously unseen circumstances or facing information uncertainties." — [Yao et al., 2023]
---

**Critical Capability: Designing ReAct Prompts**
Designing ReAct prompts involves creating human trajectories of actions, thoughts, and environment observations to solve a task instance, which are then used as few-shot examples for the LLM. — [Yao et al., 2023]
---

**Critical Capability: Combining Internal and External Knowledge**
Combining ReAct with Chain-of-Thought Self-Consistency (CoT-SC) leverages both internal knowledge and externally obtained information, improving performance in knowledge-intensive reasoning tasks. — [Yao et al., 2023]
---

**AI Roadmap: Finetuning for Improved Performance**
While ReAct performs well with prompting, finetuning with generated trajectories can further improve performance, especially for smaller language models. — [Yao et al., 2023]
---

**Measuring Success: Performance Metrics**
Performance is measured using metrics like exact match (EM) for question answering, accuracy (Acc) for fact verification, and success rate (SR) and score for interactive decision-making tasks. — [Yao et al., 2023]
---

**Supporting Fact: ALFWorld Performance Improvement**
ReAct achieves an absolute success rate improvement of 34% on ALFWorld compared to imitation or reinforcement learning methods. — [Yao et al., 2023]
---

**Supporting Fact: WebShop Performance Improvement**
ReAct achieves an absolute success rate improvement of 10% on WebShop compared to imitation learning and imitation + reinforcement learning methods. — [Yao et al., 2023]
---

**Key Finding: ReAct's Groundedness and Trustworthiness**
ReAct's problem-solving trajectory is more factual and grounded compared to Chain-of-Thought reasoning, thanks to its access to an external knowledge base. — [Yao et al., 2023]
---

**Limitation: Reasoning Error in ReAct**
ReAct can sometimes exhibit a higher reasoning error rate than CoT due to the structural constraint of interleaving reasoning, action, and observation steps, which can reduce flexibility. — [Yao et al., 2023]
---

**Critical Capability: Human-in-the-Loop Interaction**
ReAct allows for human-in-the-loop interaction, enabling users to inspect and edit reasoning traces to correct or guide the model's behavior. — [Yao et al., 2023]
---

**Best Practice: Sparse Reasoning in Decision Making**
Sparse, versatile reasoning in decision making tasks is more effective than dense, external feedback-driven approaches like Inner Monologue (IM). — [Yao et al., 2023]
---

**AI Roadmap: Scaling Up ReAct**
Future directions include scaling up ReAct with multi-task training and combining it with reinforcement learning to unlock further potential of LLMs. — [Yao et al., 2023]
---

**Ethics Statement: Risk Awareness**
Researchers should be aware of potential risks when hooking up LLMs with action spaces to interact with external environments, such as accessing inappropriate information or taking harmful actions. — [Yao et al., 2023]
---

**Key Quote: Easy to Design**
"Designing ReAct prompts is straightforward as human annotators just type down their thoughts in language on top of their actions taken. No ad-hoc format choice, thought design, or example selection is used in this paper." — [Yao et al., 2023]