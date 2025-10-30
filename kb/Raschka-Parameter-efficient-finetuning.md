# Research Notes: Raschka-Parameter-efficient-finetuning

**Source:** `Raschka-Parameter-efficient-finetuning`  
**Processed:** research-kb

---

**Parameter-Efficient Finetuning (PEFT) Overview**
Parameter-efficient finetuning techniques allow for adapting large language models (LLMs) to specific tasks while training only a small fraction of the total parameters. This reduces computational costs and enables training on devices with limited resources. — Raschka-Parameter-efficient-finetuning

---

**Key Finding: Finetuning Improves Performance**
Adapting and finetuning an LLM on a target task using data from the target domain generally yields better results than relying solely on in-context learning. — Raschka-Parameter-efficient-finetuning

---

**Three Conventional Finetuning Approaches**
The three conventional approaches to finetuning LLMs are: feature-based approach, updating the output layers (finetuning I), and updating all layers (finetuning II). — Raschka-Parameter-efficient-finetuning

---

**Feature-Based Approach**
The feature-based approach involves using a pre-trained LLM to generate output embeddings for a training set, which are then used as input features for a separate classification model. — Raschka-Parameter-efficient-finetuning

---

**Finetuning I: Updating Output Layers**
Finetuning I keeps the parameters of the pre-trained LLM frozen and only trains the newly added output layers, similar to training a classifier on embedded features. — Raschka-Parameter-efficient-finetuning

---

**Finetuning II: Updating All Layers**
Finetuning II updates all layers of the pre-trained LLM, typically resulting in superior modeling performance compared to only updating the output layers, but at a higher computational cost. — Raschka-Parameter-efficient-finetuning

---

**Performance vs. Cost Trade-off in Finetuning**
Finetuning more layers generally leads to better performance, but it also increases the computational cost. — Raschka-Parameter-efficient-finetuning

---

**Prefix Tuning**
Prefix tuning adds a trainable tensor to each transformer block, instead of only the input embeddings, to improve modeling performance on a target task. — Raschka-Parameter-efficient-finetuning

---

**Prefix Tuning Efficiency**
Prefix tuning can achieve comparable performance to finetuning all layers while only training a small percentage (e.g., 0.1%) of the parameters. — Raschka-Parameter-efficient-finetuning

---

**Adapters: Adding Layers to Transformer Blocks**
The adapter method adds adapter layers in two places within each transformer block, using bottleneck structures to achieve parameter efficiency. — Raschka-Parameter-efficient-finetuning

---

**Adapter Performance and Efficiency**
A BERT model trained with adapters can reach performance comparable to a fully finetuned BERT model while training only a small percentage (e.g., 3.6%) of the parameters. — Raschka-Parameter-efficient-finetuning

---

**LLaMA-Adapter: Combining Prefix Tuning and Adapters**
LLaMA-Adapter prepends tunable prompt tensors to the embedded inputs, similar to prefix tuning, but also introduces a zero-initialized attention mechanism and gating. — Raschka-Parameter-efficient-finetuning

---

**LLaMA-Adapter: Focus on Top Layers**
LLaMA-Adapter adds learnable adaption prompts only to the topmost transformer layers, enabling more effective tuning of language representations. — Raschka-Parameter-efficient-finetuning

---

**LLaMA-Adapter Training Stability**
LLaMA-Adapter uses a gating mechanism to stabilize training by mitigating the potential disruption of linguistic knowledge caused by randomly initialized tensors. — Raschka-Parameter-efficient-finetuning

---

**LLaMA-Adapter Performance and Efficiency**
A 7 billion parameter LLaMA model can be finetuned in one hour using eight A100 GPUs with LLaMA-Adapter, outperforming other models on question-answering tasks while only finetuning 1.2M parameters. — Raschka-Parameter-efficient-finetuning

---

**Key Capability: Selecting the Right Finetuning Method**
Buy-side firms need to evaluate the trade-offs between performance, computational cost, and data requirements when selecting a finetuning method (full finetuning, prefix tuning, adapters, LLaMA-Adapter). — Raschka-Parameter-efficient-finetuning

---

**Key Capability: Understanding Licensing Implications**
Firms must consider the licensing implications of different LLM implementations (e.g., GPL vs. Apache) when choosing a model and finetuning approach. — Raschka-Parameter-efficient-finetuning

---

**Best Practice: Tailoring LLMs to Specific Business Needs**
Finetuning pre-trained LLMs allows firms to tailor these models to suit specific business requirements and align them with target domain data. — Raschka-Parameter-efficient-finetuning