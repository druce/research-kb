# Research Notes: What We’ve Learned From A Year of Building with LLMs – Applied LLMs

**Source:** `What We’ve Learned From A Year of Building with LLMs – Applied LLMs`  
**Processed:** research-kb

---

Okay, I've analyzed the document and extracted the following notes. Here they are:

**LLMs are "Good Enough" for Real-World Applications**
LLMs have become sufficiently advanced and accessible for practical use, driving an estimated $200B investment in AI by 2025. Provider APIs have lowered the barrier to entry, enabling broader adoption beyond ML specialists. — Applied LLMs

---

**Tactical, Operational, and Strategic Considerations**
Building successful LLM products requires addressing tactical (prompting, RAG), operational (team, deployment), and strategic (long-term vision) aspects. — Applied LLMs

---

**Key Finding: Prompting is Underestimated and Overestimated**
Prompting is underestimated because the right techniques can be powerful, but overestimated because significant engineering around the prompt is still required. — Applied LLMs

---

**Prompting Technique: N-Shot Prompts and In-Context Learning**
Provide LLMs with examples (n ≥ 5) demonstrating the task and desired outputs, ensuring examples are representative of the production distribution. — Applied LLMs

---

**Prompting Technique: Chain-of-Thought (CoT)**
Encourage the LLM to explain its reasoning process before providing the final answer, adding specificity to reduce hallucination rates. — Applied LLMs

---

**Prompting Technique: Providing Relevant Resources**
Use Retrieval Augmented Generation (RAG) to provide the model with snippets of text it can directly use in its response, prioritizing their use and acknowledging when resources are insufficient. — Applied LLMs

---

**Structured Input and Output Improves LLM Performance**
Structured input (e.g., SQL schema) clarifies tasks and resembles training data, while structured output simplifies integration with downstream systems. Use Instructor for LLM APIs and Outlines for self-hosted models. — Applied LLMs

---

**Avoid "God Object" Prompts**
Break down complex tasks into smaller, focused prompts that are easier to understand, iterate, and evaluate individually. — Applied LLMs

---

**Craft Your Context Tokens Carefully**
Rethink the amount of context sent to the agent, removing superfluous material and structuring the context to underscore relationships between parts. — Applied LLMs

---

**Key Finding: RAG is Dependent on Document Quality**
The quality of RAG output depends on the relevance, density, and level of detail in the retrieved documents. — Applied LLMs

---

**Don't Forget Keyword Search**
Use keyword search (e.g., BM25) as a baseline and in hybrid search approaches, as vector embeddings may struggle with specific keyword-based queries. — Applied LLMs

---

**Prefer RAG Over Finetuning for New Knowledge**
RAG often outperforms finetuning for incorporating new information, is easier to keep up-to-date, and provides finer-grained control over document retrieval. — Applied LLMs

---

**Long-Context Models Won't Make RAG Obsolete**
Even with large context windows, retrieval is still needed to select relevant context, avoid overwhelming the model with distractors, and manage inference costs. — Applied LLMs

---

**Step-by-Step "Flows" Can Boost Performance**
Decomposing a single complex task into multiple simpler tasks (multi-turn flows) can achieve better results. — Applied LLMs

---

**Prioritize Deterministic Workflows**
For reliable agent deployment, have agent systems produce deterministic plans that are then executed in a structured, reproducible way. — Applied LLMs

---

**Getting More Diverse Outputs Beyond Temperature**
Adjust elements within the prompt (e.g., shuffling the order of items), keep a list of recent outputs to avoid redundancy, and vary the phrasing used in prompts. — Applied LLMs

---

**Caching is Underrated**
Caching saves cost, eliminates generation latency, and allows serving vetted responses, reducing the risk of harmful content. — Applied LLMs

---

**When to Finetune**
Finetune when prompting falls short, but consider the costs of data annotation, model training, and self-hosting. Generate synthetic data or bootstrap on open-source data to reduce costs. — Applied LLMs

---

**Create Assertion-Based Unit Tests**
Create unit tests with input/output samples and expectations based on at least three criteria, triggered by any pipeline changes. — Applied LLMs

---

**LLM-as-Judge Can Work (Somewhat)**
LLM-as-Judge can help build priors about prompt performance, especially with pairwise comparisons, controlling for position bias, allowing for ties, and using Chain-of-Thought. — Applied LLMs

---

**The "Intern Test" for Evaluating Generations**
Ask: Could an average college student in the relevant major succeed at the task given the input and context? If not, enrich the context or reduce task complexity. — Applied LLMs

---

**Overemphasizing Certain Evals Can Hurt Overall Performance**
Overemphasis on specific evals (e.g., Needle-in-a-Haystack) can reduce performance on other tasks like extraction and summarization. — Applied LLMs

---

**Simplify Annotation to Binary Tasks or Pairwise Comparisons**
Simplify annotation tasks to binary classifications (yes/no) or pairwise comparisons (A is better than B) for faster and more reliable annotations. — Applied LLMs

---

**(Reference-Free) Evals and Guardrails Can Be Used Interchangeably**
Reference-free evals can assess output quality based solely on the input prompt and model's response, and can be used as guardrails to filter undesired output. — Applied LLMs

---

**LLMs Will Return Output Even When They Shouldn't**
LLMs may confidently return values even when they don't exist, necessitating robust guardrails to detect and filter undesired output. — Applied LLMs

---

**Hallucinations are a Stubborn Problem**
Factual inconsistencies occur at a baseline rate of 5-10% and are challenging to reduce below 2%, requiring a combination of prompt engineering and factual inconsistency guardrails. — Applied LLMs

---

**Check for Development-Prod Skew**
Measure skew between LLM input/output pairs, including structural (formatting) and content-based (semantic) skew, to ensure production accuracy. — Applied LLMs

---

**Look at Samples of LLM Inputs and Outputs Every Day**
Regularly review data samples to develop an intuitive understanding of how LLMs perform and adapt to new patterns or failure modes. — Applied LLMs

---

**Generate Structured Output to Ease Downstream Integration**
Generate structured output (e.g., JSON, YAML) to ease integration with downstream applications, using Instructor for LLM APIs and Outlines for self-hosted models. — Applied LLMs

---

**Migrating Prompts Across Models is a Pain**
Expect prompt migration across models to take time, requiring reliable evals to measure task performance before and after migration. — Applied LLMs

---

**Version and Pin Your Models**
Pin specific model versions in production to avoid unexpected changes in behavior, and maintain a shadow pipeline with the latest versions for testing. — Applied LLMs

---

**Choose the Smallest Model That Gets the Job Done**
Experiment with smaller models, as techniques like chain-of-thought and finetuning can help them achieve comparable results with lower latency and cost. — Applied LLMs

---

**Involve Design Early and Often**
Involve designers early to rethink how the user experience can be improved, focusing on the job to be done, not just the technology. — Applied LLMs

---

**Design Your UX for Human-In-The-Loop**
Design the user experience for Human-In-The-Loop (HITL) to collect valuable data and improve models, balancing user effort and control. — Applied LLMs

---

**Prioritize Your Hierarchy of Needs Ruthlessly**
Prioritize requirements (reliability, harmlessness, factual consistency, usefulness, scalability, cost) ruthlessly to identify the minimum lovable product and iterate. — Applied LLMs

---

**Calibrate Your Risk Tolerance Based on the Use Case**
Calibrate risk tolerance based on the use case, setting a higher bar for safety and accuracy for customer-facing applications offering critical advice. — Applied LLMs

---

**Focus on the Process, Not Tools**
Focus on understanding the problem-solving methodology and process before adopting tools, avoiding accidental complexity and underspecified solutions. — Applied LLMs

---

**Always Be Experimenting**
Position your team to experiment frequently, teaching everyone the basics of prompt engineering and setting aside time for building evals and running multiple experiments. — Applied LLMs

---

**Empower Everyone to Use New AI Technology**
Educate and empower the entire team to use new AI technology, providing opportunities for hands-on experimentation and exploration. — Applied LLMs

---

**Don't Fall Into the Trap of "AI Engineering is All I Need"**
Building AI products requires a broad array of specialized roles, including AI Engineers, platform/data engineers, and MLEs, hired at the right time. — Applied LLMs

---

**Training From Scratch (Almost) Never Makes Sense**
For most organizations, pretraining an LLM from scratch is an impractical distraction from building products. — Applied LLMs

---

**Don't Finetune Until You've Proven It's Necessary**
Organizations invest in finetuning too early, trying to beat the “just another wrapper” allegations. In reality, finetuning is heavy machinery, to be deployed only after you’ve collected plenty of examples that convince you other approaches won’t suffice. — Applied LLMs

---

**Start With Inference APIs, But Don't Be Afraid of Self-Hosting**
Start with LLM APIs, but consider self-hosting for data privacy, circumventing limitations, gaining control, and potentially reducing costs at scale. — Applied LLMs

---

**The Model Isn't the Product, the System Around It Is**
Focus on building lasting value through evals, guardrails, caching, and a data flywheel, rather than chasing the latest model releases. — Applied LLMs

---

**Build Trust By Starting Small**
Focus on specific domains and use cases, narrowing the scope by going deep rather than wide to create domain-specific tools that resonate with users. — Applied LLMs

---

**Build LLMOps, But Build It for the Right Reason: Faster Iteration**
Build LLMOps to shorten the feedback gap between models and their inferences and interactions in production, enabling faster iteration. — Applied LLMs

---

**Don't Build LLM Features You Can Buy**
Focus on LLM applications that truly align with your product goals and enhance your core operations, avoiding general problems being tackled en masse by software companies. — Applied LLMs

---

**AI in the Loop; Humans at the Center**
Center humans in the workflow, using LLMs as a resource to support their rapid utilization, increasing productivity and happiness. — Applied LLMs

---

**Prompt Engineering Comes First**
Start with prompt engineering, using techniques like chain-of-thought, n-shot examples, and structured input/output, before considering finetuning. — Applied LLMs

---

**Build Evals and Kickstart a Data Flywheel**
Build evals specific to your tasks and use cases, starting with unit testing and human evaluation, to create a positive feedback loop for model improvement. — Applied LLMs

---

**The High-Level Trend of Low-Cost Cognition**
The cost of running models with equivalent performance is rapidly decreasing, making previously infeasible applications economical. — Applied LLMs