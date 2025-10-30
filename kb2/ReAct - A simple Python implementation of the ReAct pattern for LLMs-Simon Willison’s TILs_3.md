**Source:** `ReAct - A simple Python implementation of the ReAct pattern for LLMs _ Simon Willison’s TILs`

**Critical Capability: Secure Action Execution**
When implementing actions like `calculate`, it's crucial to use secure sandboxing techniques (e.g., WebAssembly) to prevent malicious code execution. The author notes the use of `eval()` is "dangerous".
