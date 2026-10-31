# Session Notes: APIs & Keys
**Date:** October 31, 2026  
**Curriculum:** AI Engineering from Scratch (Volume 1: Foundations)  
**Phase:** 00 (Setup & Tooling) — Lesson 04: APIs & Keys  
**Quiz Score:** 4 / 4 (100%)

---

````carousel
### Slide 1: The Client-Server Pattern for AI APIs

Every LLM API (Anthropic, OpenAI, Google Gemini) follows the standard HTTP client-server model:

```mermaid
sequenceDiagram
    participant C as Your Python Script (The Client)
    participant N as HTTPS Network Request
    participant S as AI Provider Server (Anthropic / OpenAI / Google)

    Note over C: 1. Package Payload (Prompt, Model Name, Max Tokens)
    C->>S: POST /v1/messages + Header: x-api-key / Bearer token
    Note over S: 2. Authenticate Key, Meter Billing, Run Inference on GPU Cluster
    S-->>C: 200 OK + JSON Response Body (Text + Token Usage)
    Note over C: 3. Extract generated text & display
```

#### Anatomy of an API Call:
1. **Endpoint (URL):** Where the request goes (e.g. `https://api.anthropic.com/v1/messages`).
2. **Authentication Header:** The secret API key identifying your account and billing.
3. **Request Body (JSON):** Model name (`claude-sonnet-5`), token limits, and message list.
4. **Response Body (JSON):** Model response, completion reason, and token usage breakdown.

<!-- slide -->
### Slide 2: Security 101 & Secret Management

Why API keys must be treated like debit cards with your PIN attached:

```mermaid
graph TD
    A["API Key Safety"] --> B["NEVER Hardcode in .py files\nBots scrape GitHub 24/7\nExposed keys can burn thousands of dollars"]
    A --> C["Safe: Environment Variables\nos.environ.get('KEY_NAME')\nStored in OS memory"]
    A --> D["Safe: Local .env File\nStored in plain file\nALWAYS added to .gitignore"]
```

#### Best Practices:
* **The Golden Rule:** Never put API keys directly in source code.
* **The `.env` workflow:**
  ```ini
  # .env file (excluded in .gitignore)
  ANTHROPIC_API_KEY=sk-ant-...
  GEMINI_API_KEY=AIzaSy...
  OPENAI_API_KEY=sk-...
  ```
* **Reading in Python:**
  ```python
  import os
  api_key = os.environ.get("ANTHROPIC_API_KEY")
  ```

<!-- slide -->
### Slide 3: SDK vs. Raw HTTP

Understanding what high-level libraries do under the hood:

```mermaid
graph LR
    A["Python Script"] -->|"Option A: SDK"| B["Anthropic / OpenAI SDK\n(Convenience wrapper)"]
    B --> C["HTTP POST Request\n(urllib / requests / httpx)"]
    A -->|"Option B: Raw HTTP"| C
    C --> D["Cloud API Gateway"]
```

#### Why Know Both?
* **SDK:** Clean, concise syntax, automatic retries, typed responses, built-in streaming.
* **Raw HTTP:** Eliminates dependencies, runs in constrained environments, and makes troubleshooting network failures straightforward.

<!-- slide -->
### Slide 4: HTTP Status Code Decoder (The Troubleshooter)

When an API call fails, the HTTP status code tells you exactly where to look:

| Status Code | Meaning | Root Cause | Engineering Solution |
| :--- | :--- | :--- | :--- |
| **`401 Unauthorized`** | Bad Auth | Missing, invalid, or mistyped API key | Check environment variable: `echo $ANTHROPIC_API_KEY` |
| **`403 Forbidden`** | Permission Denied | Key is valid, but account lacks model access | Verify billing plan or request model permissions |
| **`429 Too Many Requests`** | Rate Limited | Exceeded RPM (requests/min) or TPM (tokens/min) | Implement exponential backoff and retry logic |
| **`400 Bad Request`** | Invalid Request | Malformed JSON, misspelled model, missing fields | Verify parameter names and schema against documentation |
| **`500 / 503`** | Server Error | Outage or maintenance at the provider | Wait 1–2 minutes and retry with backoff |

<!-- slide -->
### Slide 5: What We Tested & Verified Today

1. **Graceful Failure Handling:**
   - Executed [`first_api_call.py`](file:///Users/ponti/Desktop/AI%20from%20scratch/ai-engineering-from-scratch/phases/00-setup-and-tooling/04-apis-and-keys/code/first_api_call.py) with missing dependencies and saw clean fallback messages.
2. **Simulated Authentication Failure:**
   - Exported a temporary test key: `export ANTHROPIC_API_KEY="sk-ant-fake-key-for-testing-12345"`.
   - Reached the live Anthropic API endpoint via raw HTTP (`urllib.request`).
   - Observed the real-world server response: `urllib.error.HTTPError: HTTP Error 401: Unauthorized`.
   - Cleaned the environment using `unset ANTHROPIC_API_KEY`.
3. **AI Pro Advantage:**
   - Identified Google AI Studio / Gemini access as a zero-cost option for upcoming modules (`AI-100` and `GEN-204`).

<!-- slide -->
### Slide 6: Session Wrap-Up & Milestone Summary

* **Date Completed:** October 31, 2026
* **Phase:** 00 (Setup & Tooling)
* **Lesson:** 04 (APIs & Keys) — **Complete ✅**
* **Quiz Result:** 4 / 4 (100%)
  - Q1: `B` (API key authenticates identity and authorizes requests)
  - Q2: `C` (Prevents accidental commits and public web scraper theft)
  - Q3: `A` (Store keys in `.env` and protect via `.gitignore`)
  - Q4: `C` (HTTP 429 indicates rate limit throttling)
* **Next Lesson:**
  > **Phase 00, Lesson 05: Jupyter Notebooks** (`phases/00-setup-and-tooling/05-jupyter-notebooks/docs/en.md`)
````
