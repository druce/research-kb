# Research Notes: Emerging Architectures for LLM Applications _ Andreessen Horowitz

**Source:** `Emerging Architectures for LLM Applications _ Andreessen Horowitz`  
**Processed:** research-kb

---

**LLMs as a New Software Primitive**
Large language models (LLMs) represent a powerful new primitive for building software, but their novel behavior requires new approaches to development. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Reference Architecture for LLM Apps**
A reference architecture is emerging for LLM applications, encompassing systems, tools, and design patterns used by AI startups and sophisticated tech companies. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**In-Context Learning is a Common Starting Point**
The reference architecture is based on in-context learning, a design pattern where LLMs are used off-the-shelf and controlled through prompting and contextual data. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**In-Context Learning Solves Scalability Issues**
In-context learning addresses the limitations of directly feeding large datasets into LLMs by sending only the most relevant documents with each prompt. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**In-Context Learning Workflow: Data Preprocessing/Embedding**
The first stage of in-context learning involves storing private data by breaking it into chunks, passing it through an embedding model, and storing it in a vector database. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**In-Context Learning Workflow: Prompt Construction/Retrieval**
The second stage involves constructing prompts that combine a template, few-shot examples, external API information, and relevant documents from the vector database. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**In-Context Learning Workflow: Prompt Execution/Inference**
The final stage involves submitting the compiled prompts to a pre-trained LLM for inference, with optional operational systems like logging, caching, and validation. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**In-Context Learning vs. Fine-Tuning**
In-context learning can be easier than training or fine-tuning LLMs, requiring less specialized expertise and infrastructure, and can outperform fine-tuning for small datasets. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Context Window Limitations and Costs**
While increasing the context window is possible, it comes with tradeoffs, as cost and time of inference can scale quadratically with prompt length, making it cost-prohibitive for many applications. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Data Pipelines: ETL Tools and Document Loaders**
Data loading and transformation for LLM apps often use traditional ETL tools like Databricks or Airflow, as well as document loaders built into orchestration frameworks like LangChain and LlamaIndex. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Embeddings: OpenAI API is Popular**
Most developers use the OpenAI API (text-embedding-ada-002 model) for embeddings due to its ease of use, reasonable results, and decreasing cost. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Embeddings: Alternatives to OpenAI**
Alternatives to OpenAI for embeddings include Cohere, which focuses on embeddings and performs better in certain scenarios, and the open-source Sentence Transformers library from Hugging Face. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Vector Databases: Pinecone is a Common Choice**
Pinecone is a popular vector database choice due to its cloud-hosted nature, ease of use, and enterprise-level features like performance at scale, SSO, and uptime SLAs. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Vector Databases: Open Source Options**
Open-source vector databases like Weaviate, Vespa, and Qdrant offer excellent single-node performance and customization options for experienced AI teams. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Vector Databases: Local Libraries and OLTP Extensions**
Local vector management libraries like Chroma and Faiss provide great developer experience for small apps, while OLTP extensions like pgvector offer vector support within existing database systems. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Future of Vector Databases**
The future of vector databases may involve cloud offerings from open-source systems, but achieving strong performance in the cloud across various use cases is challenging. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Embedding Pipeline May Become More Important**
Despite larger context windows, the embedding pipeline may become more important, with different embedding models trained for model relevancy and vector databases designed to take advantage of this. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Prompting Strategies: From Simple to Advanced**
Prompting strategies range from simple zero-shot or few-shot prompting to more advanced techniques designed to ground model responses in a source of truth. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Orchestration Frameworks: LangChain and LlamaIndex**
Orchestration frameworks like LangChain and LlamaIndex abstract away prompt chaining, API interfacing, contextual data retrieval, and memory management across LLM calls. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**LangChain: Popular but Evolving**
LangChain is widely used among hobbyists and startups, but some developers switch to raw Python in production to avoid dependencies. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**ChatGPT as an Orchestration Tool**
ChatGPT can be considered a substitute for orchestration frameworks, abstracting away bespoke prompts, maintaining state, and retrieving contextual data via plugins or APIs. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**LLM APIs: OpenAI is the Leader**
OpenAI is the leading LLM API provider, with developers starting new apps using gpt-4 or gpt-4-32k for best-case performance and ease of use. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**LLM APIs: Production Considerations**
As projects scale, options like switching to gpt-3.5-turbo (cheaper and faster), experimenting with Anthropic's Claude models, and triaging requests to open-source models come into play. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Open Source LLMs: Closing the Gap**
Open-source models are closing the gap with proprietary offerings, with models like LLaMa setting a new bar for accuracy and driving the development of alternative base models. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Fine-Tuning Open Source Models**
Fine-tuning open-source base models is becoming more common, with platforms like Databricks, Anyscale, Mosaic, Modal, and RunPod supporting engineering teams. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Inference Options for Open Source Models**
Inference options for open-source models include simple API interfaces from Hugging Face and Replicate, raw compute resources from cloud providers, and opinionated cloud offerings. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Future of Open Source LLMs**
When open-source LLMs reach accuracy levels comparable to GPT-3.5, a "Stable Diffusion-like moment" is expected, with massive experimentation and productionizing of fine-tuned models. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Operational Tooling: Caching and Logging**
Caching (usually based on Redis) is common for improving application response times and cost, while tools like Weights & Biases, MLflow, PromptLayer, and Helicone are used for logging, tracking, and evaluating LLM outputs. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Validation and Security Tools**
Tools like Guardrails are being developed to validate LLM outputs, and tools like Rebuff are being developed to detect prompt injection attacks. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**Hosting LLM Apps: Standard and Emerging Options**
LLM apps are hosted using standard options like Vercel or major cloud providers, but startups like Steamship and companies like Anyscale and Modal are emerging with end-to-end hosting or model/code hosting solutions. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**AI Agents: Potential but Immature**
AI agent frameworks have the potential to solve complex problems, act on the outside world, and learn from experience, but most are still in the proof-of-concept phase and lack reliability. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**LLMs: A Major Architectural Change**
Pre-trained AI models represent a significant architectural shift in software, enabling individual developers to build powerful AI apps quickly. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]
---
**The LLM App Stack is Evolving**
The tools and patterns described are a starting point for integrating LLMs, and the architecture will likely evolve as major changes take place, such as a shift toward model training. — [Matt Bornstein and Rajko Radovanovic, Andreessen Horowitz]