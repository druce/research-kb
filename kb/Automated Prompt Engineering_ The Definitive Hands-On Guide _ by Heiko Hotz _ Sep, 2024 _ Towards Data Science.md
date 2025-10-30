# Research Notes: Automated Prompt Engineering_ The Definitive Hands-On Guide _ by Heiko Hotz _ Sep, 2024 _ Towards Data Science

**Source:** `Automated Prompt Engineering_ The Definitive Hands-On Guide _ by Heiko Hotz _ Sep, 2024 _ Towards Data Science`  
**Processed:** research-kb

---

```markdown
**Key Finding: Manual Prompt Engineering is a Bottleneck**
Manual prompt engineering is time-consuming, requires deep understanding of prompt structures, and limits exploration of the full range of possibilities that LLMs offer, making it a bottleneck for enterprise LLM deployments. — [Heiko Hotz]
---

**Key Finding: Automated Prompt Engineering (APE) Automates Prompt Optimization**
APE automates the process of generating and refining prompts for LLMs to improve performance on specific tasks, similar to automated hyperparameter optimization in traditional ML. — [Heiko Hotz]
---

**Key Finding: APE Can Unlock Significant Performance Gains**
APE allows for the exploration of a wider range of prompt designs, often leading to unexpected approaches and significant performance improvements compared to manual methods. — [Heiko Hotz]
---

**Key Finding: LLMs Can Be Used to Evaluate LLM Responses**
LLMs can be effectively used to evaluate other LLMs' responses, especially when the evaluation task is independent and within the evaluator LLM's capabilities. — [Heiko Hotz]
---

**Critical Capability: APE Workflow Requires Labeled Data, Initial Prompt, and Evaluation Metric**
To implement APE, you need a labeled dataset representative of the task, an initial prompt, and an evaluation metric to optimize against. — [Heiko Hotz]
---

**AI Roadmap: APE Workflow Steps**
The APE workflow involves starting with an initial prompt and dataset, generating responses from the target LLM, evaluating those responses against ground truth, optimizing the prompt using an optimizer LLM, and repeating the process iteratively until satisfactory performance is achieved. — [Heiko Hotz]
---

**Decisions about what technology and workflows to implement: OPRO Strategy**
OPRO (Optimisation by PROmpting) leverages results from previous iterations to actively hill climb against the evaluation metric, using a meta-prompt to guide the optimizer LLM based on the optimization trajectory. — [Heiko Hotz]
---

**Best Practice: Use Asynchronous Programming to Speed Up APE**
Leveraging asynchronous programming allows for sending multiple requests to the Gemini API simultaneously, speeding up the evaluation process. — [Heiko Hotz]
---

**Supporting Fact & Figure: APE Achieved Significant Accuracy Improvement**
Implementing APE with the OPRO algorithm boosted accuracy on the geometric_shapes task from a baseline of 49% to 85% on an unseen test dataset. — [Heiko Hotz]
---

**Key Quote: APE as a Game-Changer**
"That’s why, in my opinion, APE is starting to emerge as a game-changer, enabling us to harness the power of automation to optimise prompts and unlock the full potential of LLMs." — [Heiko Hotz]
---

**Critical Capability: Meta-Prompt Engineering**
Crafting an effective meta-prompt is crucial for guiding the optimizer LLM in APE, combining the optimization goal, task examples, and the history of previous prompts and their performance. — [Heiko Hotz]
---

**Decisions about what technology and workflows to implement: Model Selection**
The author recommends using a fast and cost-effective model like Gemini 1.5 Flash as the target LLM, a more powerful model like Gemini 1.5 Pro as the optimizer LLM, and Gemini 1.5 Flash again as the evaluation LLM. — [Heiko Hotz]
---

**Best Practice: Test Optimized Prompts on Unseen Data**
It's crucial to test the best-performing prompt on unseen test data to ensure its effectiveness generalizes beyond the training data. — [Heiko Hotz]
---

**Key Capability: Exemplar Selection**
Exemplar selection, which aims to find the best few-shot examples for a given task, can further enhance the effectiveness of an optimized prompt. — [Heiko Hotz]
---
```