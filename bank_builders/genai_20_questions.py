# genai_20_questions.py
# 20 Genuine Generative AI Questions with practical web-dev examples and realistic MCQ distractor options

GENAI_20_QUESTIONS = [
    {
        "id": "ai_genai_01",
        "question": "What is Generative AI, and how does it fundamentally differ from traditional Predictive / Discriminative AI?",
        "topic": "2. Generative AI",
        "subtopic": "Core Principles",
        "difficulty": "Basic",
        "importance": "High",
        "answer": "Predictive AI models learn boundaries to classify or predict numeric labels (estimating P(Y|X), such as spam classification or churn prediction). In contrast, Generative AI models learn the joint probability distribution of data (estimating P(X, Y) or P(X)) to synthesize entirely new, coherent artifacts (text, code, images, audio) that resemble their training data.",
        "example": "Predictive AI: Classifies a pull request comment as 'constructive' vs 'hostile'. Generative AI: Automatically writes the unit tests and pull request summary.",
        "options": [
            "Predictive AI only runs in the cloud, while Generative AI runs exclusively in client-side WebAssembly",
            "Generative AI learns joint probability distributions to generate novel content, whereas predictive AI models classify or predict existing target labels",
            "Predictive AI requires neural networks, whereas Generative AI uses rule-based decision trees",
            "Generative AI can never make errors, whereas predictive AI has an error rate"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_02",
        "question": "Explain the architectural difference between generative models and discriminative models.",
        "topic": "2. Generative AI",
        "subtopic": "Model Architectures",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Discriminative models focus on finding a decision boundary between categories, modeling conditional probability P(Y|X). Generative models capture how the data itself is generated, modeling P(X|Y)P(Y) or P(X), which allows sampling and creating novel high-dimensional data points from latent representations.",
        "example": "A discriminative model determines whether a submitted code snippet is written in TypeScript or Python. A generative model writes a new TypeScript interface from scratch.",
        "options": [
            "Discriminative models output probabilities, whereas generative models can only output boolean true/false",
            "Generative models only work with image data, while discriminative models work with text",
            "Discriminative models model P(Y|X) to discriminate between classes, while generative models model P(X|Y) or P(X) to sample new data instances",
            "Generative models have zero trainable parameters"
        ],
        "correctIndex": 2
    },
    {
        "id": "ai_genai_03",
        "question": "What is a Foundation Model in Generative AI, and why is it considered a paradigm shift?",
        "topic": "2. Generative AI",
        "subtopic": "Foundation Models",
        "difficulty": "Basic",
        "importance": "High",
        "answer": "A Foundation Model is a large-scale neural network trained on vast, diverse datasets at scale (usually self-supervised) that exhibits emergent, general-purpose reasoning capabilities. Instead of building bespoke models for sentiment, translation, and code analysis, one foundation model can be adapted to all these downstream tasks via prompt engineering or fine-tuning.",
        "example": "Claude 3.5 Sonnet, GPT-4o, and Gemini 1.5 Pro serve as foundation models capable of coding, language translation, creative writing, and data extraction.",
        "options": [
            "A foundation model is a specialized CSS framework for building AI dashboard layouts",
            "A model pre-trained on broad data at scale that can be adapted to a wide variety of downstream tasks through prompting or lightweight fine-tuning",
            "A database schema designed specifically for storing machine learning vectors",
            "An open-source Python compiler designed for running neural networks"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_04",
        "question": "What is the difference between Pre-training, Fine-tuning, and In-Context Learning (Prompting)?",
        "topic": "2. Generative AI",
        "subtopic": "Model Adaptation",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Pre-training trains the base model from scratch on trillions of tokens (millions of dollars, updates all weights). Fine-tuning adapts model weights on a curated, domain-specific dataset (e.g., internal company API schemas). In-Context Learning leaves model weights frozen and instructs the model dynamically via the prompt with system instructions and few-shot examples.",
        "example": "In-context: Passing 3 examples of custom React hook patterns in the prompt. Fine-tuning: Updating Llama weights on 50,000 internal proprietary codebase PRs.",
        "options": [
            "Pre-training modifies no weights; fine-tuning modifies all weights; prompting deletes the model cache",
            "Pre-training learns general language from scratch; fine-tuning updates weights on domain data; in-context learning guides the frozen model entirely through prompt context",
            "In-context learning requires retraining the transformer on GPU clusters",
            "Fine-tuning can only be performed on frontend client browsers"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_05",
        "question": "What are Multimodal Foundation Models and how do they benefit full-stack web development?",
        "topic": "2. Generative AI",
        "subtopic": "Multimodal AI",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Multimodal models process and generate multiple modalities of data (e.g., text, vision, audio) within a unified latent space. In web development, developers can feed UI mockups (Figma screenshots), architecture diagrams, or UI bug screenshots directly into the model, which inspects the visual elements and generates matching HTML, Tailwind CSS, and React JSX.",
        "example": "Uploading a screenshot of a broken responsive header layout to Claude or GPT-4o and asking: 'Why is this flex item overflowing on mobile viewport?'",
        "options": [
            "Models that run simultaneously across multiple operating systems like Windows and Linux",
            "Models that can process and reason across multiple modalities (text, images, audio, video) within a shared representation space",
            "Models that can only speak multiple human languages but cannot parse images or code",
            "Multi-threaded CPU processes that handle Node.js child processes"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_06",
        "question": "What is a Diffusion Model, and how does the forward and reverse process work?",
        "topic": "2. Generative AI",
        "subtopic": "Image Generation",
        "difficulty": "Intermediate",
        "importance": "Medium",
        "answer": "Diffusion models generate data (such as images in Midjourney or Stable Diffusion) by first defining a forward diffusion process that gradually adds Gaussian noise to an image until it becomes pure static, and learning a reverse denoising process with a U-Net or DiT that iteratively removes noise conditioned on text embeddings to recover a clear image.",
        "example": "Generating placeholder hero graphics or app marketing banners via Stable Diffusion by guiding the denoising steps with text prompts.",
        "options": [
            "A model that spreads database queries across multiple replica nodes",
            "A generative framework that learns to reconstruct clean data by iteratively removing Gaussian noise added during a forward process",
            "A technique for minifying JavaScript bundles during Vite production build",
            "A neural network that computes CSS flexbox layouts"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_07",
        "question": "What is a Generative Adversarial Network (GAN) and how does the Generator vs Discriminator game function?",
        "topic": "2. Generative AI",
        "subtopic": "GANs",
        "difficulty": "Intermediate",
        "importance": "Medium",
        "answer": "A GAN consists of two competing sub-networks: a Generator that creates synthetic samples from random noise, and a Discriminator that attempts to distinguish between real training samples and generated fakes. They are trained in a minimax two-player game until the Generator creates artifacts indistinguishable from real data.",
        "example": "Generating photorealistic synthetic user profile avatars for mocking testing databases without infringing on real user privacy.",
        "options": [
            "A client-server WebSocket protocol for streaming LLM tokens",
            "Two neural networks trained in competition: the Generator creates synthetic data, while the Discriminator tries to detect fakes",
            "A load balancer algorithm that pits two backend servers against each other",
            "An encryption algorithm that prevents prompt injection"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_08",
        "question": "What is RLHF (Reinforcement Learning from Human Feedback) and why is it crucial for LLM alignment?",
        "topic": "2. Generative AI",
        "subtopic": "Alignment",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Raw pre-trained LLMs merely predict the next statistically likely token, often resulting in unhelpful, repetitive, or toxic completions. RLHF aligns the model with human preferences by training a Reward Model on human preference rankings and using Proximal Policy Optimization (PPO) to steer the model to be helpful, honest, and harmless.",
        "example": "If a user asks 'How do I bypass authentication?', a raw base model might autocomplete insecure scripts, while an RLHF-aligned model explains security protocols safely.",
        "options": [
            "A JavaScript testing framework that simulates human mouse clicks",
            "A fine-tuning methodology where human preference rankings train a reward model to steer LLM behavior toward helpfulness and safety",
            "A system where humans manually edit all model weight matrices one by one",
            "A reinforcement learning agent that plays video games"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_09",
        "question": "What is RLAIF (Reinforcement Learning from AI Feedback) and Constitutional AI?",
        "topic": "2. Generative AI",
        "subtopic": "Alignment",
        "difficulty": "Intermediate",
        "importance": "Medium",
        "answer": "RLAIF replaces expensive human evaluators with a powerful, constitution-guided AI model that critiques and scores model outputs according to a defined set of principles (a 'constitution'). This allows automated, highly scalable alignment and reduces human subjective bias and evaluation fatigue.",
        "example": "Anthropic's Constitutional AI uses critique and revision cycles guided by ethical principles before applying AI-supervised preference training.",
        "options": [
            "A legal framework requiring AI companies to register models with federal regulators",
            "An alignment approach where an AI model evaluates and critiques outputs according to explicit constitutional rules to replace manual human labeling",
            "A React state management library that enforces immutable constraints",
            "A hardware watchdog that throttles GPU cluster temperature"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_10",
        "question": "What does the Temperature parameter control in Generative AI text generation?",
        "topic": "2. Generative AI",
        "subtopic": "Hyperparameters",
        "difficulty": "Basic",
        "importance": "High",
        "answer": "Temperature scales the logits before the softmax function in next-token prediction. A low temperature (e.g., 0.0 to 0.2) sharpens the probability distribution, making the model deterministic and focused (ideal for code generation and JSON extraction). A high temperature (0.7 to 1.0+) flattens probabilities, encouraging creative diversity and varied vocabulary.",
        "example": "Use temperature=0 for generating strict TypeScript interfaces or SQL queries; use temperature=0.8 for brainstorming marketing copy or fictional dialogue.",
        "options": [
            "The physical heat dissipation limit of the GPU server rack",
            "A parameter that scales logits: lower values yield deterministic, focused outputs (ideal for code), while higher values increase randomness and creativity",
            "The execution timeout in milliseconds before an API call aborts",
            "The compression ratio of the token embedding vector"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_11",
        "question": "Explain the difference between Top-k and Top-p (nucleus sampling) decoding strategies.",
        "topic": "2. Generative AI",
        "subtopic": "Hyperparameters",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Top-k sampling restricts the candidate token pool to the fixed 'k' most probable tokens. Top-p (nucleus) sampling dynamically selects the smallest set of tokens whose cumulative probability exceeds the threshold 'p' (e.g., 0.9). Top-p is more adaptive because it expands the candidate pool when multiple tokens are plausible and narrows it when one token is overwhelmingly likely.",
        "example": "When predicting after 'const x =', if only 'true' or 'false' have high probability, Top-p will only consider those two, whereas Top-k=50 would force 48 improbable tokens into consideration.",
        "options": [
            "Top-k filters by keyword; Top-p filters by punctuation",
            "Top-k selects from a fixed number of top tokens, while Top-p selects from a dynamic pool whose cumulative probability reaches threshold p",
            "Top-k runs on CPU; Top-p runs on GPU",
            "Top-p determines the maximum context window size in kilotokens"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_12",
        "question": "What is Hallucination in Generative AI, and what are its primary causes?",
        "topic": "2. Generative AI",
        "subtopic": "Model Limitations",
        "difficulty": "Basic",
        "importance": "High",
        "answer": "Hallucination is when an LLM generates factually false, ungrounded, or non-existent assertions with high linguistic confidence. Root causes include: models are probabilistic next-token predictors (not knowledge databases); out-of-distribution training data; knowledge cutoffs; and prompts asking for information absent from their pre-training.",
        "example": "An LLM recommending an npm package 'react-super-fast-virtualizer-v5' that does not actually exist on npm, along with fake code examples for it.",
        "options": [
            "A memory leak caused by unclosed Node.js socket connections",
            "When an LLM produces confident-sounding statements that are factually inaccurate or entirely fabricated, caused by statistical token guessing without grounded facts",
            "When the model refuses to answer due to rate limit constraints",
            "A rendering glitch in React when rendering HTML dangerously"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_13",
        "question": "How do Frequency Penalty and Presence Penalty impact AI text generation?",
        "topic": "2. Generative AI",
        "subtopic": "Hyperparameters",
        "difficulty": "Intermediate",
        "importance": "Medium",
        "answer": "Frequency penalty penalizes tokens based on how many times they have already appeared in the output, directly discouraging repetition of the same words or loops. Presence penalty penalizes any token that has appeared at least once, encouraging the model to introduce fresh subjects and diverse vocabulary into the conversation.",
        "example": "Setting frequency_penalty=0.5 prevents a model from looping the phrase 'It is important to remember...' repeatedly across bullet points.",
        "options": [
            "They charge the developer extra billing fees for every API request",
            "Frequency penalty discourages repeating identical tokens proportionally to count; presence penalty discourages reusing any token already mentioned once to introduce new ideas",
            "They throttle network packet frequency over WebSockets",
            "They control the audio frequency in speech-to-text models"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_14",
        "question": "Why do Generative AI models operate on 'Tokens' rather than raw characters or full words?",
        "topic": "2. Generative AI",
        "subtopic": "Tokenization",
        "difficulty": "Basic",
        "importance": "High",
        "answer": "Character-level processing requires excessively deep sequences and struggles with semantic chunking. Word-level tokenization produces huge vocabulary matrices (millions of words) and fails on unseen words, misspellings, and code syntax. Subword tokenization (BPE, WordPiece) provides an optimal trade-off: efficient vocabulary size (~32k-128k tokens) that can represent any arbitrary text or code without out-of-vocabulary errors.",
        "example": "The word 'tokenization' might be split into ['token', 'ization'], preserving semantic sub-roots while representing rare programming terms flexibly.",
        "options": [
            "Because computers cannot understand letters without converting them to ASCII numbers first",
            "Subword tokens strike the optimal balance between sequence length and vocabulary size, allowing flexible handling of code, rare words, and multiple languages",
            "Tokens are mandatory legal units required by copyright regulatory authorities",
            "Characters cannot be stored in GPU VRAM memory"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_15",
        "question": "What is the strategic trade-off between Open-Weights models (e.g. Llama 3) and Proprietary APIs (e.g. Claude 3.5, GPT-4o)?",
        "topic": "2. Generative AI",
        "subtopic": "Deployment Architecture",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Proprietary APIs offer state-of-the-art frontier capabilities, zero infrastructure management, and instant scalability, but pose privacy concerns (data crossing third-party boundaries) and vendor lock-in. Open-weights models can be self-hosted on private VPCs/on-premise for strict compliance (HIPAA, GDPR), fine-tuned deeply on proprietary codebases, and incur fixed compute costs.",
        "example": "Using Claude 3.5 Sonnet API for complex code architecture reviews, and self-hosted Ollama Llama 3 8B for parsing confidential employee healthcare forms.",
        "options": [
            "Open-weights models cannot generate JavaScript, while proprietary APIs can only generate HTML",
            "Proprietary APIs offer cutting-edge intelligence with zero server ops, while open-weights provide complete data sovereignty, self-hosting control, and offline security",
            "Proprietary APIs are always 100% free of charge, whereas open-weights require monthly cloud licenses",
            "Open-weights models do not run on Linux servers"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_16",
        "question": "How do AI code-completion engines (e.g. Copilot, Cursor) deliver sub-second inline completions?",
        "topic": "2. Generative AI",
        "subtopic": "Code Generation",
        "difficulty": "Practical",
        "importance": "High",
        "answer": "They use Fill-In-The-Middle (FIM) trained models (such as StarCoder or lightweight fast inference models) hosted with speculative decoding and vLLM/TensorRT-LLM. They send prefix context (code before the cursor) and suffix context (code after the cursor), stream tokens over HTTP/2 or WebSockets, and cache surrounding AST definitions.",
        "example": "When typing 'function calculateTotal(items: CartItem[]): number {' the FIM engine infers the function body while taking into account the closing bracket immediately following.",
        "options": [
            "They download the entire GitHub repository database into browser localStorage",
            "They use specialized Fill-In-The-Middle (FIM) models with speculative decoding, streaming tokens over low-latency connections using nearby AST context",
            "They search StackOverflow via Google Search API on every single keystroke",
            "They run synchronous regular expression replacement scripts in the IDE background"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_17",
        "question": "What intellectual property (IP) and licensing concerns must developers consider when using AI-generated code?",
        "topic": "2. Generative AI",
        "subtopic": "Ethics & IP",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Developers must verify that the AI tool provides copyright indemnification and does not train on private customer prompts. They must also check for verbatim recitation of GPL/copyleft-licensed open-source code (using code attribution filters) to avoid contaminating proprietary closed-source enterprise software with viral licenses.",
        "example": "Enterprise GitHub Copilot settings allow administrators to block suggestions that match public GitHub code snippets longer than 150 characters.",
        "options": [
            "Any code written with AI is automatically owned by Microsoft and Google",
            "Developers must ensure private prompts are not used for public model training, enable verbatim code matching filters, and confirm enterprise IP indemnification",
            "Developers are prohibited from selling software that contains any AI-assisted lines of code",
            "AI-generated code requires paying royalties to the author of every npm package mentioned"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_18",
        "question": "What is Synthetic Data generation in Generative AI and why is it valuable for testing web apps?",
        "topic": "2. Generative AI",
        "subtopic": "Synthetic Data",
        "difficulty": "Intermediate",
        "importance": "Medium",
        "answer": "Synthetic data is programmatically or LLM-generated data that mimics the statistical properties, edge cases, and schema structure of real-world data without exposing real user PII (Personally Identifiable Information). In web testing, it enables populating databases with thousands of realistic edge-case mock records (e.g. unicode names, expired card numbers, massive payloads).",
        "example": "Generating 500 varied e-commerce orders with realistic international addresses and localized phone numbers to stress-test checkout form validation.",
        "options": [
            "Corrupted data caused by bad hard drive sectors",
            "Artificially generated data that mirrors realistic distributions and edge cases without containing real sensitive user PII, ideal for QA and load testing",
            "Fake CSS mockups created without HTML tags",
            "Encrypted session cookies stored on client devices"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_19",
        "question": "What is Catastrophic Forgetting in neural network fine-tuning and how is it mitigated?",
        "topic": "2. Generative AI",
        "subtopic": "Fine-Tuning",
        "difficulty": "Advanced",
        "importance": "Medium",
        "answer": "Catastrophic forgetting occurs when a neural network trained on a new specific task overwrites the weights that held its previously learned general capabilities, losing basic reasoning or multilingual skills. It is mitigated using Parameter-Efficient Fine-Tuning (PEFT/LoRA) which freezes base model weights and trains small adapter matrices, or by mixing general replay data into fine-tuning.",
        "example": "Fine-tuning an LLM exclusively on internal SQL schemas might cause it to forget how to write Python scripts unless LoRA adapters or mixed datasets are used.",
        "options": [
            "When a user forgets their account password and loses access to the API",
            "When fine-tuning on a specialized domain causes a model to lose its pre-trained general reasoning abilities, mitigated by using LoRA or rehearsal datasets",
            "When the context window buffer overflows and drops the oldest user message",
            "When an operating system runs out of swap space on disk"
        ],
        "correctIndex": 1
    },
    {
        "id": "ai_genai_20",
        "question": "What is Model Quantization (e.g. 4-bit, 8-bit GGUF/AWQ) and why is it vital for local AI development?",
        "topic": "2. Generative AI",
        "subtopic": "Optimization",
        "difficulty": "Intermediate",
        "importance": "High",
        "answer": "Quantization reduces the numerical precision of model weights from 16-bit floating point (FP16) to lower bit representations (e.g., INT8 or INT4). This drastically reduces VRAM requirements (e.g., reducing a 70B model from 140GB to ~40GB VRAM) and speeds up memory-bandwidth-bound inference with negligible loss in reasoning accuracy, allowing developers to run models locally on laptops.",
        "example": "Running Llama 3 8B locally inside VS Code or Ollama with a 4-bit GGUF quantization using only 5.5GB of RAM instead of 16GB VRAM.",
        "options": [
            "Compressing image assets using WebP image encoding before sending to an LLM",
            "Reducing numerical precision of weights from FP16 to 8-bit or 4-bit, drastically lowering RAM/VRAM footprints so models run efficiently on local hardware",
            "Splitting an API key into four encrypted parts for security",
            "Converting synchronous JavaScript code into asynchronous Web Workers"
        ],
        "correctIndex": 1
    }
]
