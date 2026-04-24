---
name: mmx-cli
description: >
  Generate text, images, video, speech, and music via the MiniMax AI platform.
  Covers text generation (MiniMax-M2.7 model), image generation (image-01),
  video generation (Hailuo-2.3), speech synthesis (speech-2.8-hd, 300+ voices),
  music generation (music-2.6 with lyrics, cover, and instrumental), and web search.
  Use when the user needs to create AI-generated multimedia content, produce
  narrated audio from text, compose music, or search the web through MiniMax AI services.
---

# mmx-cli Skill

Generate multimedia content (text, images, video, speech, music) via the
[MiniMax AI](https://github.com/MiniMax-AI/cli) platform.

## Install

```bash
npx skills add MiniMax-AI/cli@skill -g -y
```

Or manually:

```bash
npm install -g @minimax-ai/cli
```

Set your API key:

```bash
export MINIMAX_API_KEY=your_api_key_here
```

## Capabilities

| Capability | Command | Model |
|------------|---------|-------|
| Text generation | `mmx text generate` | MiniMax-M2.7 |
| Image generation | `mmx image generate` | image-01 |
| Video generation | `mmx video generate` | Hailuo-2.3 |
| Speech synthesis | `mmx speech generate` | speech-2.8-hd |
| Music generation | `mmx music generate` | music-2.6 |
| Web search | `mmx search` | — |

## Quick Examples

```bash
# Generate text
mmx text generate "Summarize the key benefits of reinforcement learning from human feedback"

# Generate an image
mmx image generate "A diagram of a RAG architecture with vector database"

# Generate a short video clip
mmx video generate "An AI engineer working at a laptop surrounded by floating neural network nodes"

# Synthesize speech from text
mmx speech generate --text "Welcome to AI Engineering." --voice Calm_Woman

# Generate music with lyrics
mmx music generate --lyrics "Code and data, night and day" --style "upbeat tech"

# Web search
mmx search "latest advances in LLM evaluation benchmarks"
```

## Gather from user before running

| Info | Required? | Notes |
|------|-----------|-------|
| MINIMAX_API_KEY | Yes | From [MiniMax platform](https://www.minimaxi.com/) |
| Prompt or text | Yes | Describe what to generate |
| Voice name | No | For speech; run `mmx speech list-voices` to browse 300+ options |
| Output path | No | Default saves to current directory |

## Tips

- Use `--output json` flag for structured output suitable for pipelines.
- Use `--non-interactive` and `--quiet` flags in automated / agent workflows.
- Run `mmx --help` or `mmx <subcommand> --help` to see all options.
- The [SKILL.md](https://github.com/MiniMax-AI/cli/blob/main/skill/SKILL.md)
  in the upstream repo is always up-to-date with the latest flags and models.
