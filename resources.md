# Resources
During the process of writing *AI Engineering*, I went through many papers, case studies, blog posts, repos, tools, etc. The book itself has 1200+ reference links and I've been tracking [1000+ generative AI GitHub repos](https://huyenchip.com/llama-police). This document contains the resources I found the most helpful to understand different areas.

If there are resources that you've found helpful but not yet included, feel free to open a PR.

- [ML Theory Fundamentals](#ml-theory-fundamentals)
- [Chapter 1. Planning Applications with Foundation Models](#chapter-1-planning-applications-with-foundation-models)
- [Chapter 2. Understanding Foundation Models](#chapter-2-understanding-foundation-models)
    - [Training large models](#training-large-models)
    - [Sampling](#sampling)
    - [Context length and context efficiency](#context-length-and-context-efficiency)
- [Chapters 3 + 4. Evaluation Methodology](#chapters-3--4-evaluation-methodology)
- [Chapter 5. Prompt Engineering](#chapter-5-prompt-engineering)
    - [Prompt engineering guides](#prompt-engineering-guides)
    - [Defensive prompt engineering](#defensive-prompt-engineering)
- [Chapter 6. RAG and Agents](#chapter-6-rag-and-agents)
    - [RAG](#rag)
    - [Agents](#agents)
- [Chapter 7. Finetuning](#chapter-7-finetuning)
- [Chapter 8. Dataset Engineering](#chapter-8-dataset-engineering)
    - [Public datasets](#public-datasets)
- [Chapter 9. Inference Optimization](#chapter-9-inference-optimization)
- [Chapter 10. AI Engineering Architecture and User Feedback](#chapter-10-ai-engineering-architecture-and-user-feedback)
- [Bonus: Organization engineering blogs](#bonus-organization-engineering-blogs)

## ML Theory Fundamentals
While you don't need an ML background to start building with foundation models, a rough understanding of how AI works under the hood is useful to prevent misuse. Familiarity with ML theory will make you much more effective.

1. [Lecture notes] [Stanford CS 321N](https://cs231n.github.io/): a longtime favorite introductory course on neural networks.
    
    - [Videos] I'd recommend watching lectures 1 to 7 from the 2017 course [video recordings](https://www.youtube.com/watch?v=vT1JzLTH4G4&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv). They cover the fundamentals that haven't changed.
    - [Videos] Andrej Karpathy's [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) is more hands-on where he shows how to implement several models from scratch.
2. [Book] [Machine Learning: A Probabilistic Perspective](https://probml.github.io/pml-book/book1.html) (Kevin P Murphy, 2012)
    
    Foundational, comprehensive, though a bit intense. This used to be many of my friends' go-to book when preparing for theory interviews for research positions.
3. [Aman's Math Primers](https://aman.ai/primers/math/)
    
    A good note that covers basic differential calculus and probability concepts.
4. I also made a list of resources for MLOps, which includes a section for [ML + engineering fundamentals](https://huyenchip.com/mlops/#ml_engineering_fundamentals).
5. I wrote a brief [1500-word note](https://github.com/chiphuyen/dmls-book/blob/main/basic-ml-review.md) on how an ML model learns and concepts like objective function and learning procedure.
6. *AI Engineering* also covers the important concepts immediately relevant to the discussion:
    
    - Transformer architecture (Chapter 2)
    - Embedding (Chapter 3)
    - Backpropagation and trainable parameters (Chapter 7)

## Chapter 1. Planning Applications with Foundation Models

1. [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130) (OpenAI, 2023) 
    
    OpenAI (2023) has excellent research on how exposed different occupations are to AI. They defined a task as exposed if AI and AI-powered software can reduce the time needed to complete this task by at least 50%. An occupation with 80% exposure means that 80% of this occupation tasks are considered exposed. According to the study, occupations with 100% or close to 100% exposure include interpreters and translators, tax preparers, web designers, and writers. Some of them are shown in Figure 1-5. Not unsurprisingly, occupations with no exposure to AI include cooks, stonemasons, and athletes. This study gives a good idea of what use cases AI is good for.
1. [Applied LLMs](https://applied-llms.org/) (Yan et al., 2024)
    
    Eugene Yan and co. shared their learnings from one year of deploying LLM applications. Many helpful tips!
1. [Musings on Building a Generative AI Product](https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product) (Juan Pablo Bottaro and Co-authored byKarthik Ramgopal, LinkedIn, 2024) 
    
    One of the best reports I've read on deploying LLM applications: what worked and what didn't. They discussed structured outputs, latency vs. throughput tradeoffs, the challenges of evaluation (they spent most of their time on creating annotation guidelines), and the last-mile challenge of building gen AI applications.
1. [Apple's human interface guideline](https://developer.apple.com/design/human-interface-guidelines/machine-learning) for designing ML applications
    
    Outlines how to think about the role of AI and human in your application, which influences the interface decisions.
1. [LocalLlama subreddit](https://www.reddit.com/r/LocalLLaMA/): useful to check from time to time to see what people are up to.
1. [State of AI Report](https://www.stateof.ai/) (updated yearly): very comprehensive. It's useful to skim through to see what you've missed.
1. [16 Changes to the Way Enterprises Are Building and Buying Generative AI](https://a16z.com/generative-ai-enterprise-2024/) (Andreessen Horowitz, 2024)
1. ["Like Having a Really Bad PA": The Gulf between User Expectation and Experience of Conversational Agents](https://dl.acm.org/doi/abs/10.1145/2858036.2858288) (Luger and Sellen, 2016)
    
    A solid, ahead-of-its-time paper on user experience with conversational agents. It makes a great case for the value of dialogue interfaces and what's needed to make them useful, featuring in-depth interviews with 14 users. "*It has been argued that the true value of dialogue interface systems over direct manipulation (GUI) can be found where task complexity is greatest.*"
1. [Stanford Webinar - How AI is Changing Coding and Education, Andrew Ng & Mehran Sahami](https://www.youtube.com/watch?v=J91_npj0Nfw&ab_channel=StanfordOnline) (2024) 
    
    A great discussion that shows how the Stanford's CS department thinks about what CS education will look like in the future.. My favorite quote: "CS is about systematic thinking, not writing code."
1. [Professional artists: how much has AI art affected your career? - 1 year later : r/ArtistLounge](https://www.reddit.com/r/ArtistLounge/comments/1ap0cm3/professional_artists_how_much_has_ai_art_affected/) 
    
    Many people share their experience on how AI impacted their work. E.g.:

    *"From time to time, I am sitting in meetings where managers dream of replacing coders, writers and visual artists with AI. I hate those meetings and try to avoid them, but I still get involved from time to time. All my life, I loved coding & art. But nowadays, I often feel this weird sadness in my heart."*

## Chapter 2. Understanding Foundation Models

### Training large models

Papers detailing the training process of important models are gold mines. I'd recommend reading all of them. But if you can only pick 3, I'd recommend Gopher, InstructGPT, and Llama 3.

1. [GPT-2] [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (OpenAI, 2019) 
2. [GPT-3] [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (OpenAI, 2020) 
3. [Gopher] [Scaling Language Models: Methods, Analysis & Insights from Training Gopher](https://arxiv.org/abs/2112.11446) (DeepMind, 2021) 
4. [InstructGPT] [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) (OpenAI, 2022)
5. [Chinchilla] [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) (DeepMind, 2022)
6. [Qwen technical report](https://arxiv.org/abs/2309.16609) (Alibaba, 2022)
7. [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) (Alibaba, 2024)
8. [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) (Anthropic, 2022)
9. [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) (Meta, 2023) 
10. [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) (Meta, 2023)
11. [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) (Meta, 2024)
    
    This paper is so good. The section on synthetic data generation and verification is especially important.
12. [Yi: Open Foundation Models by 01.AI](https://arxiv.org/abs/2403.04652) (01.AI, 2024)

**Scaling laws**

1. [From bare metal to high performance training: Infrastructure scripts and best practices - imbue](https://imbue.com/research/70b-infrastructure/)
    
    Discusses how to scale compute to train large models. It uses 4,092 H100 GPUs spread across 511 computers, 8 GPUs/computer
2. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) (OpenAI, 2020)
    
    Earlier scaling law. Only up to 1B non-embedding params and 1B tokens.
3. [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) (Hoffman et al., 2022)
    
    Known as Chinchilla scaling law, this might be the most well-known scaling law paper.
4. [Scaling Data-Constrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9d89448b63ce1e2e8dc7af72c984c196-Abstract-Conference.html) (Muennighoff et al., 2023) 
    
    *"We find that with constrained data for a fixed compute budget, training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data. However, with more repetition, the value of adding compute eventually decays to zero."*
5. [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416) (Chung et al., 2022)
    
    A very good paper that talks about the importance of diversity of instruction data.
6. [Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws](https://arxiv.org/abs/2401.00448) (Sardana et al., 2023) 
7. [AI models are devouring energy. Tools to reduce consumption are here, if data centers will adopt](https://www.ll.mit.edu/news/ai-models-are-devouring-energy-tools-reduce-consumption-are-here-if-data-centers-will-adopt) ( MIT Lincoln Laboratory, 2023)
8. [Will we run out of data? Limits of LLM scaling based on human-generated data](https://arxiv.org/abs/2211.04325) (Villalobos et al., 2022)

**Fun stuff**

1. [Evaluating feature steering: A case study in mitigating social biases](https://www.anthropic.com/research/evaluating-feature-steering) (Anthropic, 2024)
    
    This area of research is awesome. They focused on 29 [features related to social biases](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant-bias) and found that feature steering can influence specific social biases, but it may also produce unexpected ‘off-target effects'.
2. [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) (Anthropic, 2024)
3. [GitHub - ianand/spreadsheets-are-all-you-need](https://github.com/ianand/spreadsheets-are-all-you-need)

    *"Implements the forward pass of GPT2 (an ancestor of ChatGPT) entirely in Excel using standard spreadsheet functions."*
4. [BertViz: Visualize Attention in NLP Models (BERT, GPT2, BART, etc.)](https://github.com/jessevig/bertviz)
    
    A helpul visualization of multi-head attention in action, developed to show how BERT works. 

### Sampling

1. [A Guide to Structured Generation Using Constrained Decoding](https://www.aidancooper.co.uk/constrained-decoding/) (Aidan Cooper, 2024)

    An in-depth, detailed tutorial on generating structured outputs.
2. [Fast JSON Decoding for Local LLMs with Compressed Finite State Machine](https://lmsys.org/blog/2024-02-05-compressed-fsm/) (LMSYS, 2024)
3. [How fast can grammar-structured generation be?](https://blog.dottxt.co/how-fast-cfg.html) (Brandon T. Willard, 2024)

I also wrote a post on [sampling for text generation](https://huyenchip.com/2024/01/16/sampling.html) (2024).

### Context length and context efficiency

1. [Everything About Long Context Fine-tuning](https://huggingface.co/blog/wenbopan/long-context-fine-tuning) (Wenbo Pan, 2024)
2. [Data Engineering for Scaling Language Models to 128K Context](https://arxiv.org/abs/2402.10171v1) (Yu et al., 2024)
3. [The Secret Sauce behind 100K context window in LLMs: all tricks in one place](https://blog.gopenai.com/how-to-speed-up-llms-and-use-100k-context-window-all-tricks-in-one-place-ffd40577b4c) (Galina Alperovich, 2023)
4. [Extending Context is Hard…but not Impossible](https://kaiokendev.github.io/context) (kaioken, 2023)
5. [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) (Su et al., 2021)
    
    Introducing RoPE, a technique to handle positional embeddings that enables transformer-based models to handle longer context length.

## Chapters 3 + 4. Evaluation Methodology

1. [Challenges in evaluating AI systems](https://www.anthropic.com/news/evaluating-ai-systems) (Anthropic, 2023)
    
   Discusses the limitations of common AI benchmarks to show why evaluation is so hard.
2. [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) (Liang et al., Stanford 2022)
3. [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/abs/2206.04615) (Google, 2022) 
4. [Open-LLM performances are plateauing, let's make the leaderboard steep again](https://huggingface.co/spaces/open-llm-leaderboard/blog) (Hugging Face, 2024)
    
    Helpful explanation on why Hugging Face chose certain benchmarks for their leaderboard, which is a useful reference for selecting benchmarks for your personal leaderboard. 
5. [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) (Zheng et al., 2023)
6. [LLM Task-Specific Evals that Do & Don't Work](https://eugeneyan.com/writing/evals/) (Eugene Yan, 2024) 
7. [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) (Hamel Hussain, 2024) 
8. [Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks](https://arxiv.org/abs/2305.10160) (Google & AI2, May 2023)
9. [alopatenko/LLMEvaluation](https://github.com/alopatenko/LLMEvaluation) (Andrei Lopatenko)
    
    A large collection of evaluation resources. The [slide deck](https://github.com/alopatenko/LLMEvaluation/blob/main/LLMEvaluation.pdf) on eval has a lot of pointers too.
10. [Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251) (Perez et al., 2022)
    
    A fun paper that uses AI to discover novel AI behaviors. They use methods with various degrees of automation to generate evaluation sets for 154 diverse behaviors.
11. [Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://arxiv.org/abs/2309.01219) (Zhang et al., 2023)
12. OpenRouter's [LLM Rankings](https://openrouter.ai/rankings) shows the top open source models on their platform, ranked by their usage (token volume). This can help you evaluate open source models by popularity. I wish more inference services would publish statistics like this.

## Chapter 5. Prompt Engineering

### Prompt engineering guides

1. [Anthropic's Prompt Engineering Interactive Tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit#gid=1733615301)
    
    Practical, comprehensive, and fun. The Google Sheets-based interactive exercises make it easy to experiment with different prompts and see immediately what works and what doesn't. I'm surprised other model providers don't have similar interactive guides.
2. [Brex's prompt engineering guide](https://github.com/brexhq/prompt-engineering)
    
    Contains a list of example prompts that Brex uses internally.
3. [Meta's prompt engineering guide](https://llama.meta.com/docs/how-to-guides/prompting/)
4. [Google's Gemini prompt engineering guide](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)
5. [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) 
6. Collections of prompt examples from [OpenAI](https://platform.openai.com/examples), [Anthropic](https://docs.anthropic.com/en/prompt-library/library), and [Google](https://console.cloud.google.com/vertex-ai/generative/prompt-gallery).
7. [Larger language models do in-context learning differently
](https://arxiv.org/abs/2303.03846) (Wei et al., 2023)
8. [How I think about LLM prompt engineering](https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering) (Francois Chollet, 2023) 

### Defensive prompt engineering

1. [Offensive ML Playbook](https://wiki.offsecml.com/Welcome+to+the+Offensive+ML+Playbook)
    
    Has many resources on adversarial ML and how to defend your ML systems against attacks, including both text and image attacks
2. [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208) (OpenAI, 2024)
    
    A good paper on how OpenAI trained a model to imbue prompt hierarchy to protect a model from jailbreaking. 
3. [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) (Greshake et al., 2023) 
    
    Has a great list of examples of indirect prompt injections in the appendix.
4. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://arxiv.org/abs/2302.05733) (Kang et al., 2023)
5. [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035) (Nasr et al., 2023)
6. [How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs](https://arxiv.org/abs/2401.06373) (Zeng et al., 2024)
7. [LLM Security](https://llmsecurity.net/): A collection of LLM security papers.
8. Tools that help automate security probing include [PyRIT](https://github.com/Azure/PyRIT), [Garak](https://github.com/leondz/garak/), [persuasive_jailbreaker](https://github.com/CHATS-lab/persuasive_jailbreaker), [GPTFUZZER](https://arxiv.org/abs/2309.10253), and [MasterKey](https://arxiv.org/abs/2307.08715).
9. [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) (Meta, 2023)
10. [AI Security Overview](https://owaspai.org/docs/ai_security_overview/#threat-model) (AI Exchange)

## Chapter 6. RAG and Agents

### RAG

1. [Reading Wikipedia to Answer Open-Domain Questions](https://arxiv.org/abs/1704.00051) (Chen et al., 2017)
    
    Introduces the RAG pattern to help with knowledge-intensive tasks such as question answering.
2. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020) 
3. [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) (Gao et al., 2023)
4. [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) (Anthropic, 2024)
    
    An important topic not discussed nearly enough is how to prepare data for RAG system. This post discusses several techniques for preparing data for RAG and some very practical on when to use RAG and when to use long context.
5. Chunking tutorials from [Pinecone](https://www.pinecone.io/learn/chunking-strategies/) and [Langchain](https://js.langchain.com/v0.1/docs/modules/data_connection/document_transformers/)
6. [The 5 Levels Of Text Splitting For Retrieval](https://www.youtube.com/watch?v=8OJC21T2SL4) (Greg Kamradt, 2024)
7. [GPT-4 + Streaming Data = Real-Time Generative AI](https://www.confluent.io/blog/chatgpt-and-streaming-data-for-real-time-generative-ai/) (Confluent, 2023)
    
    A great post detailing the pattern of retrieving real-time data in RAG applications.
8. [Everything You Need to Know about Vector Index Basics](https://zilliz.com/learn/vector-index) (Zilliz, 2023)
    
    An excellent series on vector search and vector database.
9. [A deep dive into the world's smartest email AI](https://www.shortwave.com/blog/deep-dive-into-worlds-smartest-email-ai/) (Hiranya Jayathilaka, 2023)
    
    If you can ignore the title, the post is a detailed case study on using the RAG pattern to build an email assistant.
10. [Book] [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html) (Manning, Raghavan, and Schütze, 2008)
    
    Information retrieval is the backbone of RAG. This book is for those who want to dive really, really deep into different techniques for organizing and querying text data.

### Agents

1. [[2304.09842] Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.09842) (Lu et al., 2023)
    
    My favorite study on LLM planners, how they use tools, and their failure modes. An interesting finding is that different LLMs have different tool preferences. 
2. [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (Park et al., 2023)
3. [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Schick et al., 2023)
4. [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) and the paper [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) (Patil et al., 2023)
    
    The list of 4 common mistakes in function calling made by ChatGPT is interesting.
5. [THUDM/AgentBench: A Benchmark to Evaluate LLMs as Agents](https://github.com/THUDM/AgentBench)  (ICLR'24) 
6. [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) (Nakano et al., 2021)
7. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Yao et al., 2022)
8. [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023)
9. [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) (Wang et al., 2023)
10. [Book] [Artificial Intelligence: A Modern Approach](https://www.amazon.com/Artificial-Intelligence-A-Modern-Approach/dp/0134610997) (Russell and Norvig, 4th edition is in 2020)
    
    Planning is closely related to search, and this classic book has a several in-depth chapters on search.

## Chapter 7. Finetuning

1. [Best practices for fine-tuning GPT-3 to classify text](https://docs.google.com/document/d/1rqj7dkuvl7Byd5KQPUJRxc19BJt8wo0yHNwK84KfU3Q/edit) (OpenAI) 
    
    A draft from OpenAI. While this guide focuses on GPT-3 but many techniques are applicable to full finetuning in general. It explains how GPT-3 finetuning works, how to prepare training data, how to evaluate your model, and common mistakes
2. [Easily Train a Specialized LLM: PEFT, LoRA, QLoRA, LLaMA-Adapter, and More](https://cameronrwolfe.substack.com/p/easily-train-a-specialized-llm-peft) (Cameron R. Wolfe, 2023)
    
    For more general parameter-efficient finetuning, 's 7000-word, well-researched article on the evolution of adapter-based finetuning, why LoRA has is so popular and why it works
3. [Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs](https://arxiv.org/abs/2312.05934) (Ovadia et al., 2024) 
    
    Interesting results to help answering the question: finetune or RAG?
4. [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751) (Houlsby et al., 2019)
    
    The paper introducing the concept of PEFT.
5. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (Hu et al., 2021)
    
    A must-read.
6. [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) (Dettmers et al., 2023)
7. [Direct Preference Optimization with Synthetic Data on Anyscale](https://www.anyscale.com/blog/direct-preference-optimization-with-synthetic-data) (2024)
8. [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) (kipply, 2022)
9. [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) (EleutherAI, 2023): Memory footprint calculation, focusing more on training.
10. [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2303.15647) (Lialin et al., 2023)
    
    An comprehensive study of different finetuning methods. Not all techniques are relevant today, though.
11. [My experience on starting with fine tuning LLMs with custom data : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/14vnfh2/my_experience_on_starting_with_fine_tuning_llms/) (2023)
12. [Train With Mixed Precision](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html) (NVIDIA Docs)

## Chapter 8. Dataset Engineering
1. [Annotation Best Practices for Building High-Quality Datasets](https://www.grammarly.com/blog/engineering/annotation-best-practices/) (Grammarly, 2022) 
2. [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416) (Chung et al., 2022) 
3. [The Curse of Recursion: Training on Generated Data Makes Models Forget](https://arxiv.org/abs/2305.17493) (Shumailov et al., 2023)
4. [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) (Meta, 2024)
    
    The whole paper is good, but the section on synthetic data generation and verification is especially important.
5. [Instruction Tuning with GPT-4](https://arxiv.org/abs/2304.03277) (Peng et al., 2023)
    
    Use GPT-4 to generate instruction-following data for LLM finetuning.
6. [Best Practices and Lessons Learned on Synthetic Data for Language Models](https://arxiv.org/abs/2404.07503) (Liu et al., DeepMind 2024)
7. [UltraChat] [Enhancing Chat Language Models by Scaling High-quality Instructional Conversations](https://arxiv.org/abs/2305.14233) (Ding et al., 2023)
8. [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) (Lee et al., 2021)
9. [Can LLMs learn from a single example?](https://www.fast.ai/posts/2023-09-04-learning-jumps/) (Jeremy Howard and Jonathan Whitaker, 2023)
    
    Fun experiment to show that it's possible to see model improvement with just one training example.
10. [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) (Zhou et al., 2023)

### Public datasets

Here are a few resources where you can look for publicly available datasets. While you should take advantage of available data, you should never fully trust it. Data needs to be thoroughly inspected and validated.

Always check a dataset's license before using it. Try your best to understand where the data comes from. Even if a dataset has a license that allows commercial use, it's possible that part of it comes from a source that doesn't.

1. [Hugging Face](https://huggingface.co/datasets) and [Kaggle](https://www.kaggle.com/datasets?fileType=csv) each host hundreds of thousands of datasets.
2. Google has a wonderful and underrated [Dataset Search](https://datasetsearch.research.google.com/).
3. Governments are often great providers of open data. [Data.gov](https://data.gov) hosts approximately hundreds of thousands of datasets, and [data.gov.in](https://data.gov.in) hosts tens of thousands. 
4. University of Michigan's [Institute for Social Research](https://www.icpsr.umich.edu/web/pages/ICPSR/index.html) ICPSR has data from tens of thousands of social studies.
5. [UC Irvine's Machine Learning Repository](https://archive.ics.uci.edu/datasets) and [OpenML](https://www.openml.org/search?type=data&sort=runs&status=active) are two older dataset repositories, each hosting several thousands of datasets.
6. The [Open Data Network](https://www.opendatanetwork.com/) lets you search among tens of thousands of datasets.
7. Cloud service providers often host a small collection of open datasets;, the most notable one is [AWS's Open Data](https://registry.opendata.aws/).
8. ML frameworks often have small pre-built datasets that you can load while using the framework, such as [TensorFlow datasets](https://www.tensorflow.org/datasets/catalog/overview#all_datasets).
9. Some evaluation harness tools host evaluation benchmark datasets that are sufficiently large for PEFT finetuning. For example, Eleuther AI's [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) hosts 400+ benchmark datasets, averaging 2,000+ examples per dataset.
10. The [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/) is a great repository for graph datasets.


## Chapter 9. Inference Optimization

1. [Mastering LLM Techniques: Inference Optimization](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) (NVIDIA Technical Blog, 2023)
    
    A very good overview of different optimization techniques.
2. [Accelerating Generative AI with PyTorch II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/) (Pytorch, 2023)
    
    A good case study with the performance improvement achieved from different techniques.
3. [Efficiently Scaling Transformer Inference](https://arxiv.org/pdf/2211.05102) (Pope et al., 2022)
    
    A highly technical but really good paper on inference paper from Jeff Dean's team. My favorite is the section discussing what to focus for different tradeoffs (e.g. latency vs. cost).
4. [Optimizing AI Inference at Character.AI](https://research.character.ai/optimizing-inference/) (Character.AI, 2024)
    
    This is less of a technical paper and more of a "Look, I can do this" paper. It's pretty impressive what the Character.AI technical team was able to achieve. This post discusses attention design, cache optimization, and int8 training.
5. [Video] [GPU optimization workshop with OpenAI, NVIDIA, PyTorch, and Voltron Data](https://www.youtube.com/watch?v=v_q2JTIqE20&ab_channel=MLOpsLearners) 
6. [Video] [Essence VC Q1 Virtual Conference: LLM Inference](https://www.youtube.com/watch?v=XPArX12gXVE) (with vLLM, TVM, and Modal Labs)
7. [Techniques for KV Cache Optimization in Large Language Models](https://www.omrimallis.com/posts/techniques-for-kv-cache-optimization/) (Omri Mallis, 2024)
    
    An excellent post explaining KV cache optimization, one of the most memory-heavy parts of transformer inference.
    
    [João Lages](https://medium.com/@joaolages/kv-caching-explained-276520203249) has an excellent visualization of KV cache.

8. [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318) (DeepMind, 2023)
9. [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://arxiv.org/abs/2401.09670) (Zhong et al., 2024) 
10. [The Best GPUs for Deep Learning in 2023 — An In-depth Analysis](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/) (Tim Dettmers, 2023) 
    
    Stas Bekman also has some great [notes](https://github.com/stas00/ml-engineering/tree/master/compute/accelerator) on evaluating accelerators. 
11. [Analysis of Large-Scale Multi-Tenant GPU Clusters for DNN Training Workloads](https://www.usenix.org/system/files/atc19-jeon.pdf) (Jeon et al., 2019)
    
    A detailed study of GPU clusters used for training deep neural networks (DNNs) in a multi-tenant environment. The authors analyze a two-month-long trace from a GPU cluster at Microsoft, focusing on three key issues affecting cluster utilization: gang scheduling and locality constraints, GPU utilization, and job failures.
12. [AI Datacenter Energy Dilemma - Race for AI Datacenter Space](https://www.semianalysis.com/p/ai-datacenter-energy-dilemma-race) (SemiAnalysis, 2024)
    
    Great analysis on the business of data centers and their bottlenecks.

I also have an older post [A friendly introduction to machine learning compilers and optimizers](https://huyenchip.com/2021/09/07/a-friendly-introduction-to-machine-learning-compilers-and-optimizers.html) (Chip Huyen, 2018)


## Chapter 10. AI Engineering Architecture and User Feedback

1. [Chapter 4: Monitoring](https://sre.google/workbook/monitoring/) from Google SRE Book
2. [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) (Microsoft Research)
    
    Microsoft proposed 18 design guidelines for human-AI interaction, covering decisions before development, during development, when something goes wrong, and over time.
3. [Peering Through Preferences: Unraveling Feedback Acquisition for Aligning Large Language Models](https://arxiv.org/abs/2308.15812v3) (Bansal et al., 2023)
    
    A study on how the feedback protocol influences a model's training performance.
4. [Feedback-Based Self-Learning in Large-Scale Conversational AI Agents](https://arxiv.org/abs/1911.02557) (Ponnusamy et al., Amazon 2019)
5. [A scalable framework for learning from implicit user feedback to improve natural language understanding in large-scale conversational AI systems](https://arxiv.org/abs/2010.12251) (Park et al., Amazon 2020)

User feedback design for conversation AI is an under-researched area so there aren't many resources yet, but I hope to see that will soon change.


## Bonus: Organization engineering blogs

I enjoy reading good technical blogs. Here are some of my frequent go-to engineering blogs.

1. [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering)   
2. [Engineering Blog - DoorDash](https://careersatdoordash.com/engineering-blog/) 
3. [Engineering | Uber Blog](https://www.uber.com/en-US/blog/engineering/)
4. [The Unofficial Google Data Science Blog](https://www.unofficialgoogledatascience.com/)  
5. [Pinterest Engineering Blog – Medium](https://medium.com/pinterest-engineering)
6. [Netflix TechBlog](https://netflixtechblog.com/)
7. [Blog | LMSYS Org](https://lmsys.org/blog/) 
8. [Blog | Anyscale](https://www.anyscale.com/blog)
9. [Data Science and ML | Databricks Blog](https://www.databricks.com/blog/category/engineering/data-science-machine-learning)  
10. [Together Blog](https://www.together.ai/blog) 
11. [Duolingo Engineering](https://blog.duolingo.com/hub/engineering/) 
