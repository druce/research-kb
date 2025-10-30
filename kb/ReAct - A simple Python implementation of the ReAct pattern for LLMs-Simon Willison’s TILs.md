# Research Notes: ReAct - A simple Python implementation of the ReAct pattern for LLMs _ Simon Willison’s TILs

**Source:** `ReAct - A simple Python implementation of the ReAct pattern for LLMs _ Simon Willison’s TILs`  
**Processed:** research-kb

---

**ReAct Pattern Enables LLM Tool Use**
The ReAct pattern allows LLMs to interact with external tools (e.g., search engines, calculators) by reasoning about actions, executing them, and incorporating the results back into their reasoning process.

---

**Key Capability: Implementing Actions for LLMs**
Buy-side firms can enhance LLMs by implementing custom actions tailored to financial tasks, such as accessing market data, running financial models, or querying internal databases.

---

**Example Actions for ReAct Pattern**
The author implemented actions like `wikipedia`, `simon_blog_search`, and `calculate` to demonstrate how an LLM can be extended with new capabilities.

---

**Critical Capability: Secure Action Execution**
When implementing actions like `calculate`, it's crucial to use secure sandboxing techniques (e.g., WebAssembly) to prevent malicious code execution. The author notes the use of `eval()` is "dangerous".

---

**AI Roadmap: Iterative Development and Refinement**
The author's implementation is described as a "very rough implementation" with "a ton of room for improvement," highlighting the iterative nature of AI development.

---

**Key Quote: Ease of Implementation**
"It really does just take a few dozen lines of Python to make these extra capabilities available to the LLM and have it start to use them." — Simon Willison

---

**Decisions about what technology and workflows to implement**
The author chose to build the ReAct pattern from scratch using a tiny Python wrapper for the ChatGPT API, rather than using a framework like Langchain.

---