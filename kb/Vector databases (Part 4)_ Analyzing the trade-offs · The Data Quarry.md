# Research Notes: Vector databases (Part 4)_ Analyzing the trade-offs · The Data Quarry

**Source:** `Vector databases (Part 4)_ Analyzing the trade-offs · The Data Quarry`  
**Processed:** research-kb

---

**Key Finding: No One-Size-Fits-All Vector DB Solution**
The best way to choose a vector database stack is to first understand the requirements and constraints of your use case, and then test out different solutions on your own data. — The Data Quarry

---

**Critical Capability: Understanding Vector DB Trade-offs**
Buy-side firms need to understand the trade-offs between on-prem vs. cloud hosting, purpose-built vs. incumbent vendors, insertion speed vs. query speed, recall vs. latency, in-memory vs. on-disk storage, sparse vs. dense vectors, full-text vs. vector search, and filtering strategies. — The Data Quarry

---

**Decision: On-Prem vs. Cloud Hosting for Vector DBs**
Consider cloud-native (managed) + client-server, on-prem (self-hosted) + embedded, and cloud-native (managed) + embedded combinations when evaluating hosting options for cost-effectiveness. — The Data Quarry

---

**Supporting Fact: Embedded Vector DBs Offer Flexibility**
Embedded/serverless vector DBs offer freedom and flexibility to developers when connecting data layers to the application layer, especially when privacy and security are a concern. — The Data Quarry

---

**Decision: Cost Considerations for Cloud-Native Vector DBs**
Organizations with large in-house data infrastructure teams may find on-prem or embedded hosting more cost-effective than cloud-native, managed solutions that charge based on data stored and queries made. — The Data Quarry

---

**Decision: Purpose-Built vs. Incumbent Vendor for Vector Search**
If adding vector search to an existing application, first try the vector search capabilities of your existing database, but consider the cost implications and potential performance limitations before looking outward. — The Data Quarry

---

**Supporting Fact: Purpose-Built Vector DBs Offer Performance Advantages**
Purpose-built vector DB vendors have optimized their storage, indexing, and querying strategies for vector search, often using modern programming languages for massive scalability and performance. — The Data Quarry

---

**Supporting Fact: Incumbent Solutions May Have Limitations**
Elasticsearch has additional constraints on which clients can use their vector search offering, and MongoDB offers vector search only for their Atlas cloud deployment. — The Data Quarry

---

**Decision: Insertion Speed vs. Query Speed Trade-off**
For most organizations, querying speed is more important than insertion speed, as insertion and indexing are typically done infrequently compared to real-time querying. — The Data Quarry

---

**Key Capability: Optimizing for Recall and Latency**
Different vector database vendors make different trade-offs when optimizing for recall (percentage of relevant results) vs. latency (time to return results). — The Data Quarry

---

**Supporting Fact: Indexing Strategies Impact Recall and Latency**
Flat indexes are most accurate but slowest; IVF-Flat indexes are faster but sacrifice some accuracy; HNSW is popular and can be combined with Product Quantization (PQ) for better recall and memory efficiency; Vamana is optimized for on-disk performance. — The Data Quarry

---

**Decision: In-Memory vs. On-Disk Vector Storage**
If your use case requires storing enough vectors that are larger than memory, consider databases that use memory-mapped files for vectors, utilizing the page cache's virtual address space on disk. — The Data Quarry

---

**Supporting Fact: LanceDB's Disk-Based Approach**
LanceDB stands out because all supported indexes are disk-based, loading only relevant pages from the index file from disk and caching them in memory. — The Data Quarry

---

**Decision: Sparse vs. Dense Vector Storage**
If semantic search is very important, then dense vectors are the way to go; if latency and speed of indexing are critical, then sparse vectors might be worth looking at. — The Data Quarry

---

**Key Finding: Vector Search is Not a Panacea**
For enterprise-level applications, plain vector search is frequently the wrong solution and is often used as part of a broader information retrieval system. — The Data Quarry, citing Colin Harman

---

**Decision: Hybrid Search Strategy**
Consider a hybrid search strategy that combines full-text search with vector search to rank exact matches higher than semantically similar results. — The Data Quarry

---

**Best Practice: Hybrid Search Techniques**
Techniques include naive fallback, Reciprocal Rank Fusion (RRF), and cross-encoder reranking to improve the quality of search results. — The Data Quarry

---

**Decision: Filtering Strategy for Vector Search**
Consider how your database of choice handles pre/post filtering and how well the filtering strategy works on your data for the classes of queries you will be performing. — The Data Quarry

---

**Best Practice: Test Vector DB Solutions on Your Own Data**
The best way to choose a vector database stack is to first understand the requirements and constraints of your use case, and then test out the different solutions on your own data. — The Data Quarry

---

**Key Quote: Purpose-built solutions are the superior option**
"In my experience, purpose-built solutions are the superior option, because they have a wider of suite of functions, are able to implement cutting-edge solutions due to starting from a clean-slate, and they also contain a host of optimizations that incumbent vendors just can’t prioritize for." — The Data Quarry