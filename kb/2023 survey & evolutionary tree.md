# Research Notes: 2023 survey & evolutionary tree

**Source:** `2023 survey & evolutionary tree`  
**Processed:** research-kb

---

Okay, here are the notes extracted from the provided document, formatted as requested:

**LLMs Revolutionizing NLP**
Large Language Models (LLMs) have shown great potential in addressing a variety of NLP tasks, ranging from natural language understanding (NLU) to generation tasks, even paving the way to Artificial General Intelligence (AGI).

---

**LLMs vs. Fine-tuned Models: Definitions**
LLMs are huge language models pre-trained on large amounts of datasets without tuning on data for specific tasks; fine-tuned models are typically smaller language models pre-trained and then further tuned on a smaller, task-specific dataset.

---

**Key Finding: Decoder-Only Models Dominating LLM Development**
Decoder-only models have gradually dominated the development of LLMs, especially after the introduction of GPT-3 in 2021, while encoder-only models have begun to fade after BERT's initial growth. — Source: 2023 survey & evolutionary tree

---

**OpenAI Leading LLM Development**
OpenAI consistently maintains its leadership position in LLM, both currently and potentially in the future. Other companies and institutions are struggling to catch up with OpenAI in developing models comparable to GPT-3 and the current GPT-4.

---

**Meta's Contribution to Open-Source LLMs**
Meta contributes significantly to open-source LLMs and promotes research of LLMs. Meta stands out as one of the most generous commercial companies, as all the LLMs developed by Meta are open-sourced. — Source: 2023 survey & evolutionary tree

---

**LLMs Exhibiting a Tendency Towards Closed-Sourcing**
In the early stages of LLM development (before 2020), the majority of models were open-sourced. However, with the introduction of GPT-3, companies have increasingly opted to close-source their models. — Source: 2023 survey & evolutionary tree

---

**Encoder-Decoder Models Remain Promising**
Encoder-decoder models remain promising, as this type of architecture is still being actively explored, and most of them are open-sourced. Google has made substantial contributions to open-source encoder-decoder architectures. — Source: 2023 survey & evolutionary tree

---

**Key Capability: Generalization with Limited Data**
Employ the exceptional generalization ability of LLMs when facing out-of-distribution data or with very few training data.

---

**Key Capability: High-Quality Text Generation**
Utilize LLMs’ capabilities to create coherent, contextually relevant, and high-quality text for various applications.

---

**Key Capability: Leveraging Extensive Knowledge**
Leverage the extensive knowledge stored in LLMs for tasks requiring domain-specific expertise or general world knowledge.

---

**Key Capability: Reasoning Ability**
Understand and harness the reasoning capabilities of LLMs to improve decision-making and problem-solving in various contexts.

---

**LLMs Generalize Better with OOD Data**
LLMs generalize better than fine-tuned models in downstream tasks facing out-of-distribution data, such as adversarial examples and domain shifts.

---

**Data Availability and Model Choice**
LLMs are preferable to fine-tuned models when working with limited annotated data, and both can be reasonable choices when abundant annotated data is available, depending on specific task requirements.

---

**Importance of Pre-training Data Similarity**
It’s advisable to choose models pre-trained on fields of data that are similar to downstream tasks.

---

**Zero Annotated Data: Use LLMs**
In scenarios where annotated data is unavailable, utilizing LLMs in a zero-shot setting proves to be the most suitable approach.

---

**Few Annotated Data: Use LLMs with In-Context Learning**
With few annotated data, incorporate the few-shot examples directly in the input prompt of LLMs, which is named as in-context learning, and these examples can effectively guide LLMs to generalize to the task.

---

**Abundant Annotated Data: Consider Both LLMs and Fine-tuned Models**
With a substantial amount of annotated data for a particular task available, both fine-tuned models and LLMs can be considered, depending on desired performance, computational resources, and deployment constraints.

---

**Traditional NLU Tasks: Fine-tuned Models Often Better**
Fine-tuned models generally are a better choice than LLMs in traditional NLU tasks, but LLMs can provide help while requiring strong generalization ability.

---

**Traditional NLU Tasks: LLMs Struggle with Toxicity Detection**
All LLMs cannot perform well on toxicity detection, and on CivilComments even the best one is only better than random guessing.

---

**Traditional NLU Tasks: LLMs Not Widely Exploited in IR**
In information retrieval (IR) tasks, LLMs are not widely exploited yet, one major reason is that IR tasks are fundamentally different from others.

---

**Use Case for LLMs: Miscellaneous Text Classification**
One of the representative tasks is miscellaneous text classification, which deals with a diverse range of topics and categories that may not have a clear or strong relationship with one another.

---

**Use Case for LLMs: Adversarial NLI**
LLMs have shown superior performance on Adversarial NLI (ANLI), especially on the R3 and R2.

---

**Generation Tasks: LLMs Show Superiority**
Due to their strong generation ability and creativity, LLMs show superiority at most generation tasks.

---

**Summarization Tasks: Humans Prefer LLM Results**
Although LLMs do not have an obvious advantage over fine-tuned models under traditional automatic evaluation metrics, human evaluation results indicate that humans tend to prefer the results generated by LLMs.

---

**Machine Translation: LLMs Good at Low-Resource Languages**
LLMs are particularly good at translating some low-resource language texts to English texts, such as in the Romanian-English translation of WMT’16.

---

**Code Synthesis: LLMs are Remarkably Adept**
LLMs are remarkably adept at code synthesis as well. Either for text-code generation, such as HumanEval and MBPP, or for code repairing, such as DeepFix, LLMs can perform pretty well.

---

**Knowledge-Intensive Tasks: LLMs Excel**
LLMs excel at knowledge-intensive tasks due to their massive real-world knowledge.

---

**Closed-Book Question Answering: LLMs Perform Better**
Closed-book question-answering tasks require the model to answer a given question about factual knowledge without any external information, and LLMs perform better on nearly all datasets.

---

**Scaling and Reasoning: LLMs Benefit Greatly**
With the exponential increase of model scales, LLMs become especially capable of reasoning like arithmetic reasoning and commonsense reasoning.

---

**Emergent Abilities: Serendipity for LLM Uses**
Emergent abilities become serendipity for uses that arise as LLMs scale up, such as ability in word manipulation and logical ability.

---

**No-Use Cases: Performance Doesn't Always Improve with Scaling**
In many cases, performance does not steadily improve with scaling due to the limited understanding of how large language models’ abilities change as they scale up.

---

**Regression Tasks: LLMs Generally Struggle**
LLMs generally struggle with some tasks due to differences in objectives and training data, for example, ChatGPT’s performance on the GLUE STS-B dataset, which is a regression task evaluating sentence similarity, is inferior to a fine-tuned RoBERTa performance.

---

**LLMs: Excellent at Mimicking Humans**
LLMs are excellent at mimicking human, data annotation and generation. They can also be used for quality evaluation in NLP tasks and have bonuses like interpretability.

---

**LLMs: Good Annotators and Data Generators**
LLMs can both act as a good annotator and data generator for data augmentation. Some LLMs have been found as good as human annotators in some tasks.

---

**LLMs: Quality Assessment on NLG Tasks**
LLMs can also be used for quality assessment on some NLG tasks, such as summarization and translation.

---

**Real-World Scenarios: LLMs are Better Suited**
LLMs are better suited to handle real-world scenarios compared to fine-tuned models. However, evaluating the effectiveness of models in the real world is still an open problem.

---

**Cost Considerations: Light, Local Models May Be Better**
Light, local, fine-tuned models should be considered rather than LLMs, especially for those who are sensitive to the cost or have strict latency requirements.

---

**Parameter-Efficient Tuning: Viable Option**
Parameter-Efficient tuning can be a viable option for model deployment and delivery.

---

**Trustworthiness: Robustness and Calibration**
The zero-shot approach of LLMs prohibits the learning of shortcuts from task-specific datasets, which is prevalent in fine-tuned models. Nevertheless, LLMs still demonstrate a degree of shortcut learning issues.

---

**Trustworthiness: Safety Concerns**
Safety concerns associated with LLMs should be given utmost importance as the potentially harmful or biased outputs, and hallucinations from LLMs can result in severe consequences.

---

**Safety: Hallucinations**
The potential for LLMs to "hallucinate," or generate nonsensical or untruthful content, can have significant negative impacts on the quality and reliability of information in various applications.

---

**Safety: Harmful Content**
Due to the high coherence, quality, and plausibility of texts generated by LLMs, harmful contents from LLMs can cause significant harm, including hate speech, discrimination, incitement to violence, false narratives, and even social engineering attack.

---

**Safety: Privacy**
LLMs can face serious security issues, an example is the issue of user privacy.