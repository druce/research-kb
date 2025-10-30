# Research Notes: GPT-4.1 Prompting Guide _ OpenAI Cookbook

**Source:** `GPT-4.1 Prompting Guide _ OpenAI Cookbook`  
**Processed:** research-kb

---

```markdown
**Key Finding: GPT-4.1 Enhanced Capabilities**
GPT-4.1 represents a significant advancement over GPT-4o in coding, instruction following, and handling long contexts. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Key Finding: GPT-4.1 is Highly Steerable**
GPT-4.1 is trained to follow instructions more closely and literally than its predecessors, making it highly steerable with well-specified prompts. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Prompt Migration Required**
To maximize GPT-4.1's intelligence, prompt migration is necessary, as the model interprets instructions more literally. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Empirical AI Engineering**
AI engineering is inherently empirical; build informative evals and iterate often to ensure prompt engineering changes yield benefits. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Key Finding: GPT-4.1 for Agentic Workflows**
GPT-4.1 is well-suited for building agentic workflows due to its training on diverse problem-solving trajectories. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Critical Capability: Agent Prompt Reminders**
Include persistence, tool-calling, and planning reminders in agent prompts to fully utilize GPT-4.1's agentic capabilities. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: System Prompt Reminders for Agents**
Use system prompt reminders like "You are an agent - please keep going until the user’s query is completely resolved" to improve agent performance. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Tool Usage via API**
Use the OpenAI API's "tools" field to pass tools, rather than manually injecting tool descriptions into prompts, to minimize errors. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Supporting Fact & Figure: Tool Usage Improvement**
Using API-parsed tool descriptions resulted in a 2% increase in SWE-bench Verified pass rate compared to manual injection. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Tool Definition Clarity**
Name tools and parameters clearly, and provide detailed descriptions in the "description" field. Use an "# Examples" section for usage examples. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Inducing Planning in Prompts**
Induce explicit, step-by-step planning in prompts to have the model "think out loud," which can increase task completion rates. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Supporting Fact & Figure: Planning Improvement**
Inducing explicit planning in prompts increased the pass rate by 4% on the SWE-bench Verified agentic task. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Key Capability: Long Context Utilization**
GPT-4.1 has a performant 1M token input context window, useful for tasks like document parsing, re-ranking, and multi-hop reasoning. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Instruction Placement in Long Context**
Place instructions at both the beginning and end of long context prompts for better performance. If only once, place above the context. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Chain-of-Thought Prompting**
Use chain-of-thought prompting to break down problems into manageable pieces and improve output quality, starting with a basic instruction. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Refining Chain-of-Thought Prompts**
Improve chain-of-thought prompts by auditing failures and addressing systematic planning and reasoning errors with more explicit instructions. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Instruction Following Development**
Develop and debug instructions in prompts by starting with high-level guidance, adding specific details, and using ordered lists for workflow steps. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Conflict Resolution in Instructions**
Check for conflicting, underspecified, or wrong instructions. GPT-4.1 tends to follow the instruction closer to the end of the prompt. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Instruction Following Examples**
Add examples that demonstrate desired behavior, ensuring that any important behavior demonstrated in your examples are also cited in your rules. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Avoiding Unnecessary Incentives**
Avoid using all-caps or other incentives like bribes or tips unless necessary, as they can cause GPT-4.1 to pay attention to them too strictly. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Caveat: Tool Calling with Insufficient Information**
Instructing a model to always call a tool may lead to hallucinated inputs or null values if it lacks sufficient information; mitigate by instructing it to ask the user for needed information. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Varying Sample Phrases**
When providing sample phrases, instruct the model to vary them to avoid repetitive outputs. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Prompt Structure**
Use a clear prompt structure including Role and Objective, Instructions, Reasoning Steps, Output Format, and Examples. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Best Practice: Delimiter Selection**
Use Markdown or XML for delimiters, as JSON can be more verbose and require character escaping. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Caveat: Long, Repetitive Outputs**
In some cases, the model may resist producing very long, repetitive outputs; instruct it strongly to output information in full or break down the problem. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Caveat: Parallel Tool Calls**
Rare instances of incorrect parallel tool calls have been observed; test this and consider setting `parallel_tool_calls` to false if issues arise. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]

---

**Key Capability: Improved Diff Generation**
GPT-4.1 features substantially improved diff capabilities, critical for coding-related tasks. — [Noah MacCallum (OpenAI), Julian Lee (OpenAI)]
```