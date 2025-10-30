# Research Notes: Best Practices for RAG pipelines

**Source:** `Best Practices for RAG pipelines`  
**Processed:** research-kb

---

**Typical RAG Workflow Steps**
A typical RAG (Retrieval-Augmented Generation) workflow includes query classification, retrieval, re-ranking, re-packing, and summarization. Each step plays a crucial role in generating accurate and concise answers.

---

**Query Classification Determines Retrieval Need**
Query classification checks if the user's question requires document retrieval, as LLMs have built-in knowledge that may suffice. Retrieval is needed when the answer is outside the model's knowledge.

---

**Document Chunking Improves Retrieval Accuracy**
Document chunking improves retrieval accuracy and helps handle length limitations in LLMs. Sentence-level chunking is often favored for its balance of meaning preservation and simplicity.

---

**Embedding Model Selection Balances Performance and Resources**
Choosing the right embedding model is key for balancing performance and resource use; LLM-Embedder offers a good balance of effectiveness and efficiency. Enhancing chunk blocks with metadata like titles and keywords can further improve retrieval.

---

**Milvus Excels as a Vector Database**
Among vector databases like Weaviate, Faiss, Chroma, and Qdrant, Milvus stands out for its superior performance and comprehensive feature set.

---

**HyDE + Hybrid Search for Optimal Retrieval**
Using HyDE (Pseudo-Document Generation) combined with hybrid search (integrating BM25 and LLM embeddings) is recommended as the default retrieval method for balanced performance and low latency.

---

**Re-Ranking Improves Document Relevance**
Re-ranking refines document relevance after initial retrieval, and its absence leads to a significant performance drop. MonoT5 is recommended for a balance of performance and efficiency in re-ranking.

---

**Re-Packing Optimizes Document Order for LLM Response**
The re-packing module optimizes document order after re-ranking to ensure effective LLM response generation. A reverse configuration, placing more relevant context closer to the query, yields better results.

---

**Summarization Reduces Redundancy and Prevents Long Prompts**
Summarization reduces redundancy and prevents long prompts from slowing down inference in LLMs. Recomp is the preferred summarization method, with LongLLMLingua as an alternative.

---

**Fine-Tuning with Mixed Contexts Improves Generator Performance**
Fine-tuning the generator with a mix of relevant and random documents (Mgr) shows the best performance with gold or mixed context.

---

**Query Classification Improves RAG Effectiveness and Efficiency**
Implementing a query classification module increases RAG effectiveness and efficiency, improving the average score from 0.428 to 0.443 and reducing latency from 16.41 seconds to 11.58 seconds.

---

**Hybrid Retrieval Balances Performance and Latency**
While "Hybrid with HyDE" achieves the highest RAG score (0.58), it has a high computational cost; using "Hybrid" or "Original" methods is recommended to balance performance and latency.

---

**Re-Ranking is Crucial for Relevance**
The absence of a re-ranking module leads to a significant performance drop, highlighting its importance for relevance. MonoT5 achieved the highest average score in re-ranking.

---

**Re-Packing with Reverse Configuration Improves Results**
The reverse configuration in the re-packing module, which places more relevant context closer to the query, achieved a RAG score of 0.560.

---

**Recomp is the Preferred Summarization Method**
Recomp demonstrated superior performance in summarization. Removing the summary module can yield comparable results with lower latency, but Recomp remains preferred for handling the generator's maximum length limitation.