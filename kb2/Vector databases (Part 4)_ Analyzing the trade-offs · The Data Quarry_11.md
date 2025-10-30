**Source:** `Vector databases (Part 4)_ Analyzing the trade-offs · The Data Quarry`

**Decision: In-Memory vs. On-Disk Vector Storage**
If your use case requires storing enough vectors that are larger than memory, consider databases that use memory-mapped files for vectors, utilizing the page cache's virtual address space on disk. — The Data Quarry
