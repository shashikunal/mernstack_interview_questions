"""
Question Bank Part 1:
- 1. AI Fundamentals (30 questions)
- 2. Generative AI (20 questions)
- 3. LLM Fundamentals (25 questions)
Total: 75 Questions
"""

# Re-use the 30 AI Fundamentals and 20 Gen AI questions from generate_ai_vibe_curriculum
from generate_ai_vibe_curriculum import generate_curriculum

raw_fund_and_genai = generate_curriculum()

# Add 25 LLM Fundamentals Questions
llm_questions = [
    ("What is an LLM and how does autoregressive generation work?",
     "A Large Language Model is an autoregressive neural network that generates text sequentially one token at a time. It takes the preceding prompt and previously generated tokens, calculates probability distributions across its vocabulary (e.g. 100k tokens), samples the next token, and appends it to the sequence until it emits an end-of-sequence token.",
     "LLMs do not produce entire paragraphs at once; they run a continuous next-token prediction loop.",
     "// Conceptual loop:\nwhile (token !== '<EOS>') {\n  token = model.predictNext(textSoFar);\n  textSoFar += token;\n  yield token; // Streams to client\n}",
     "Basic", "Concept", "High", "Why does generating 500 output tokens take longer than processing 500 input tokens?"),

    ("What is Tokenization and how does Byte-Pair Encoding (BPE) work?",
     "Tokenization is the process of converting raw character strings into integer token IDs that neural networks can process. Byte-Pair Encoding (BPE) starts with individual characters and iteratively merges the most frequent adjacent pairs into subwords. This balances vocabulary size with handling rare or misspelled words without out-of-vocabulary errors.",
     "Tokenization splits text into common subword chunks and punctuation.",
     "// 'async function' -> ['async', ' function'] (2 tokens)\n// 'unconstitutional' -> ['un', 'constitut', 'ional'] (3 tokens)",
     "Basic", "Concept", "High", "Why does code typically consume more tokens per word than English prose?"),

    ("Input Tokens vs Output Tokens: Why is there an architectural and pricing difference?",
     "Input tokens are processed in parallel in a single forward pass through the GPU matrix, making prompt processing fast and inexpensive. Output tokens must be generated sequentially one-by-one (each new token requires a complete forward pass), which takes more time and GPU compute. Therefore, output tokens cost 3x-4x more than input tokens.",
     "Input = Parallel processing (fast, cheaper). Output = Sequential generation (slower, expensive).",
     "// Pricing difference reflects GPU compute:\n// Input: $0.15 / 1M tokens | Output: $0.60 / 1M tokens",
     "Basic", "Economics", "High", "How does limiting `max_tokens` protect application budgets?"),

    ("What is the Context Window and what determines its limit?",
     "The Context Window is the maximum number of tokens an LLM can hold in memory and compute attention across in a single request. It is determined by model architecture and GPU VRAM capacity. Modern context windows range from 8k (GPT-3.5) to 128k (GPT-4o) and up to 2 million tokens (Gemini 1.5 Pro).",
     "Context window defines the working memory capacity for a single prompt interaction.",
     "// Input tokens + conversation history + output tokens <= context_window_limit",
     "Basic", "Concept", "High", "What happens when an API call exceeds the context window?"),

    ("What are the fundamentals of the Transformer architecture?",
     "The Transformer (introduced in 2017) discarded recurrence (RNNs) in favor of the Self-Attention mechanism. It consists of an Encoder (processes input sequences in parallel) and/or a Decoder (generates output sequences autoregressively). Most modern LLMs (GPT, LLaMA, Claude) are decoder-only transformers optimized for next-token generation.",
     "Transformers process all words in parallel, allowing massive scaling on GPU clusters.",
     "// Encoder: Reads & understands context (e.g. BERT)\n// Decoder: Generates text autoregressively (e.g. GPT-4, LLaMA)",
     "Intermediate", "Concept", "High", "Why did decoder-only architectures dominate over encoder-decoder models for LLMs?"),

    ("What is the Self-Attention mechanism and why was it revolutionary?",
     "Self-Attention allows a model to calculate mathematical relevance scores between every pair of words in a sentence simultaneously. In traditional RNNs, earlier words faded as sentences grew long. Self-Attention allows 'it' in 'The server rejected the connection because it was overloaded' to directly attend to 'server' with high weight, preserving semantic context across long distances.",
     "Self-attention dynamically connects related words across long texts regardless of distance.",
     "// Attention Matrix connects 'it' -> 'server' (0.85 weight)",
     "Intermediate", "Concept", "High", "What is the computational complexity of standard self-attention? (O(N^2))"),

    ("What are Query, Key, and Value vectors in Multi-Head Attention?",
     "In self-attention, each token embedding is projected into three vectors: 1) Query (what this token is looking for), 2) Key (what this token contains/offers), and 3) Value (the actual content representation). The attention score is calculated as `softmax(Q * K^T / sqrt(d_k)) * V`, similar to a database index lookup in vector space.",
     "Query = Search query. Key = Database index tags. Value = The actual row data retrieved.",
     "// Attention formula: Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V",
     "Intermediate", "Concept", "Medium", "Why do models use Multi-Head attention instead of a single attention head?"),

    ("How does Model Inference compute next-token probabilities?",
     "During inference, input token embeddings pass through transformer layers (self-attention + feed-forward networks). The final layer outputs raw logits (unnormalized scores) across the entire vocabulary. A `softmax` function converts logits into probabilities (summing to 1.0). The model then samples the next token based on Temperature and Top-p.",
     "Logits -> Softmax -> Probabilities -> Temperature/Top-p Sampling -> Next Token.",
     "// Logit for 'React': 8.5 -> Softmax prob: 72%\n// Logit for 'Vue': 6.2 -> Softmax prob: 18%",
     "Intermediate", "Concept", "High", "What happens to the probabilities when Temperature is set to 0? (Argmax / Greedy decoding)"),

    ("Explain the System Message role in Chat Completions.",
     "The System Message sets the global personality, operational rules, safety guardrails, and formatting constraints for the assistant (e.g. 'You are an expert TypeScript tutor. Only output valid JSX'). It persists across the session and guides how the model interprets all subsequent user inputs.",
     "System Message = The developer's immutable instructions and guardrails.",
     "const messages = [{ role: 'system', content: 'You are an API documentation bot. Output Markdown only.' }];",
     "Basic", "Concept", "High", "Can a user prompt override system prompt instructions? (Prompt Injection)"),

    ("Explain the User Message role in Chat Completions.",
     "The User Message represents the actual prompt, command, question, or data provided by the human user or external client application. In multi-turn conversations, new user messages are appended to the history array on each turn.",
     "User Message = The end-user's dynamic input to the model.",
     "messages.push({ role: 'user', content: 'How do I center a div in Tailwind CSS?' });",
     "Basic", "Concept", "High", "Why should user messages be sanitized before sending to an LLM?"),

    ("Explain the Assistant Message role in Chat Completions.",
     "The Assistant Message represents the text previously generated by the model. Including past assistant messages alongside user messages in the array allows the model to have conversational memory across stateless HTTP requests.",
     "Assistant Message = The model's past responses included for multi-turn conversational context.",
     "messages.push({ role: 'assistant', content: 'You can use flex items-center justify-center.' });",
     "Basic", "Concept", "High", "How does omitting past assistant messages cause context amnesia?"),

    ("How do you manage Conversation History without running out of tokens?",
     "Because HTTP is stateless, the frontend or backend resends history on each turn. To prevent context overflow and ballooning costs: 1) Sliding Window: Retain only the last N messages (e.g. last 6-8 messages), 2) Conversation Summarization: Periodically summarize older messages into a 2-sentence context recap, and 3) Prune system messages to avoid redundancy.",
     "Never send unbounded conversation history. Use a sliding window of the last 6 messages.",
     "// Sliding window of last 6 messages:\nconst trimmedHistory = allMessages.slice(-6);",
     "Intermediate", "Architecture", "High", "What is the trade-off between sliding window history and conversational memory?"),

    ("How does Streaming work under the hood in LLM APIs?",
     "When `stream: true` is set, the API does not wait for full text generation. Instead, it leaves the HTTP connection open using chunked transfer encoding (`Transfer-Encoding: chunked`) and emits Server-Sent Events (SSE) containing token deltas as they are generated. The web server forwards these chunks directly to the browser.",
     "Streaming turns sequential token generation into an incremental real-time network stream.",
     "// Each SSE chunk:\n// data: {\"choices\":[{\"delta\":{\"content\":\"Hello\"}}]}",
     "Intermediate", "Architecture", "High", "Why does streaming drastically improve perceived performance for web users?"),

    ("What is Structured Output and how do modern LLMs enforce JSON schemas?",
     "Structured Output forces the model's token sampling to adhere strictly to a predefined JSON schema or grammar. During inference, tokens that would violate the JSON schema or field types are masked out with zero probability, guaranteeing that the generated string is 100% valid, parseable JSON without markdown backticks.",
     "Structured Outputs eliminate JSON parsing errors and markdown extraction regexes.",
     "const completion = await openai.beta.chat.completions.parse({\n  model: 'gpt-4o-mini',\n  messages: [...],\n  response_format: zodResponseFormat(UserSchema, 'user_data')\n});",
     "Intermediate", "Code", "High", "How does constrained decoding prevent invalid JSON at the token level?"),

    ("What is the difference between JSON Mode and Structured Outputs with Zod?",
     "JSON Mode (`response_format: { type: 'json_object' }`) only guarantees that the output is syntactically valid JSON, but the model might omit keys or invent extra fields. Structured Outputs (with Zod or JSON Schema) guarantees both valid JSON AND exact adherence to your defined schema, keys, and types.",
     "JSON Mode = Valid JSON syntax. Structured Outputs = Valid JSON syntax + Exact Schema compliance.",
     "// Structured Outputs guarantees required fields are never omitted by the model.",
     "Intermediate", "Comparison", "High", "When would you prefer Structured Outputs over basic JSON Mode?"),

    ("What is Function Calling / Tool Calling in LLMs?",
     "Function Calling allows an LLM to interact with external systems by detecting when an external function is needed and outputting structured JSON arguments for it. Crucially, the LLM does not execute the function; your backend executes the code and sends the result back to the model.",
     "The LLM is an intelligent router and argument parser; your backend executes the real API.",
     "// LLM outputs: { name: 'getWeather', arguments: { city: 'Tokyo' } }\n// Backend executes: await fetchWeather('Tokyo')\n// Backend returns result to LLM.",
     "Intermediate", "Architecture", "High", "How does tool calling turn an LLM into an autonomous agent?"),

    ("How does Parallel Tool Calling work in modern models?",
     "Parallel Tool Calling allows an LLM to generate multiple tool calls simultaneously in a single turn. For example, if a user asks 'What is the weather in Paris, Tokyo, and New York?', the model returns 3 distinct tool call objects in one response. Your backend executes all 3 API calls concurrently using `Promise.all()`, saving latency.",
     "Parallel tool calling executes multiple API calls concurrently via `Promise.all()`.",
     "const toolCalls = res.choices[0].message.tool_calls;\nconst results = await Promise.all(toolCalls.map(call => executeTool(call)));",
     "Intermediate", "Code", "High", "How does parallel tool calling reduce multi-turn latency?"),

    ("What is the difference between Pre-training, Fine-Tuning, and RLHF?",
     "1) Pre-training: Self-supervised training on trillions of text tokens to predict next tokens (creates base model). 2) Instruction Fine-Tuning (SFT): Supervised training on curated question-answer pairs to teach the model to follow instructions. 3) RLHF (Reinforcement Learning from Human Feedback): Aligning the model with human preferences for safety, helpfulness, and harmlessness.",
     "Pre-training teaches language and facts; Fine-tuning teaches instruction-following; RLHF aligns behavior.",
     "// Base Model (Pre-trained) -> Instruction Tuned (SFT) -> Aligned Model (RLHF / DPO)",
     "Intermediate", "Concept", "High", "Why does a raw pre-trained base model often repeat prompts instead of answering?"),

    ("What is Quantization in LLMs (e.g. 4-bit, 8-bit)?",
     "Quantization is the technique of reducing the numerical precision of model weights from 16-bit floating point (FP16) to 8-bit or 4-bit integers (INT8, INT4). This reduces VRAM requirements by 50% to 75% with minimal accuracy loss, allowing 8B and 70B models to run on consumer laptops and low-cost cloud GPUs.",
     "Quantization shrinks model size so larger models fit into smaller, cheaper GPU memory.",
     "// A 70B model in FP16 requires 140GB VRAM. In 4-bit (AWQ/GGUF), it fits into ~40GB VRAM!",
     "Intermediate", "Concept", "Medium", "What is the trade-off between 4-bit quantization and model perplexity?"),

    ("What is the 'Lost in the Middle' problem in long context LLMs?",
     "Research shows that LLMs recall information positioned at the very beginning (primacy effect) and very end (recency effect) of long context windows much better than information buried in the middle. When feeding 50,000+ tokens of context, critical facts in the middle may be overlooked by self-attention layers.",
     "LLMs remember the start and end of long prompts much better than the middle.",
     "// Optimization: Place critical instructions and retrieved facts at the very top or bottom of the prompt.",
     "Intermediate", "Concept", "High", "How does document reranking solve the lost in the middle problem in RAG?"),

    ("Practical: How do you implement tool calling with OpenAI SDK in Express?",
     "1) Define tools array with JSON schema. 2) Call `chat.completions.create({ tools, ... })`. 3) Check if `message.tool_calls` exists. 4) If yes, parse arguments, execute local function (e.g. database query). 5) Append assistant message and tool response message (`role: 'tool'`). 6) Make a second API call to let the model generate the final natural answer.",
     "Complete loop: Prompt -> Model tool call -> Server execution -> Second model call -> Final answer.",
     "const runner = await openai.beta.chat.completions.runTools({ model: 'gpt-4o-mini', messages, tools });\nconst finalContent = await runner.finalContent();",
     "Practical", "Code", "High", "What happens if your local tool function throws an error?"),

    ("Practical: How do you structure a multi-turn chat payload with sliding window in React?",
     "Maintain an array of `{ role, content }` objects in React state or database. When sending to the backend, slice the array to the last 6 messages and prepend the static system prompt: `const payload = [systemMessage, ...messages.slice(-6)]`. This bounds prompt tokens while maintaining recent conversational context.",
     "Sliding window keeps token count predictable across indefinite chat sessions.",
     "const payload = [{ role: 'system', content: sysPrompt }, ...chatHistory.slice(-6)];",
     "Practical", "Code", "High", "How do you preserve user name or critical facts across sliding window truncations?"),

    ("Scenario: Your model calls an external tool with hallucinated, invalid parameters. How do you prevent this?",
     "1) Provide strict JSON schemas with exact enums for allowed parameters. 2) In your backend tool handler, validate incoming arguments using Zod before executing any logic. 3) If validation fails, return an error message to the model in the tool response (`{ error: 'Invalid parameter. Allowed values are...' }`), allowing the model to self-correct on the next turn.",
     "Always validate tool arguments with Zod; return error strings to let the model self-correct.",
     "const parsed = ParamsSchema.safeParse(JSON.parse(toolCall.function.arguments));\nif (!parsed.success) return { error: parsed.error.message };",
     "Scenario", "Security", "Critical", "Why should you never pass raw LLM tool arguments directly to `child_process.exec()`?"),

    ("Scenario: Your LLM streaming stops mid-sentence in production. What are the common causes?",
     "1) Context or output limit reached: Check `finish_reason` in the stream chunk. If `finish_reason === 'length'`, the model hit `max_tokens`. 2) Network timeout: Backend or client closed the connection prematurely. 3) Content policy trigger: The stream was aborted due to safety filters. 4) Unhandled exception in the server SSE loop.",
     "Check `finish_reason`: 'stop' = completed normally; 'length' = max_tokens exceeded.",
     "if (chunk.choices[0]?.finish_reason === 'length') {\n  console.warn('Response truncated by max_tokens limit');\n}",
     "Scenario", "Debugging", "High", "How do you prompt the model to continue from where it was cut off?"),

    ("Scenario: How do you implement a Stop Generation button in a React streaming chat UI?",
     "Create an `AbortController` instance before calling `fetch('/api/chat', { signal: controller.signal })`. Store the controller in a React `useRef`. When the user clicks 'Stop', call `controller.abort()`. In the backend, listen to `req.on('close')` to cancel the upstream OpenAI stream and immediately halt token consumption.",
     "Use `AbortController` in React and listen to `req.on('close')` in Express to stop token waste.",
     "// React:\nconst abortControllerRef = useRef<AbortController | null>(null);\nconst handleStop = () => abortControllerRef.current?.abort();",
     "Scenario", "Code", "High", "Why is aborting upstream requests critical for API cost management?")
]

# Convert items to dicts
def get_part1_questions():
    all_q = []
    # add existing 50
    for q in raw_fund_and_genai:
        all_q.append(q)
    # add 25 LLM
    for item in llm_questions:
        idx = len(all_q) + 1
        all_q.append({
            "id": f"q-aivibe-{idx}",
            "num": idx,
            "subject": "AI & Generative AI",
            "topic": "3. LLM Fundamentals",
            "subTopic": "Architecture & Mechanics",
            "question": item[0],
            "answer": item[1],
            "shortExplanation": item[2],
            "codeExample": item[3],
            "difficulty": item[4],
            "questionType": item[5],
            "interviewImportance": item[6],
            "interviewRound": "Technical Round" if item[4] != "Scenario" else "System Design",
            "frequency": "High",
            "references": "Transformer & Attention Research",
            "followUpQuestions": item[7],
            "addedAt": idx,
            "globalId": 5478 + idx
        })
    return all_q

if __name__ == "__main__":
    qs = get_part1_questions()
    print(f"Part 1 questions total: {len(qs)}")
