\# AI Service — Tool-107 Risk Heatmap Export Service



\## Overview

Flask-based AI microservice using Groq LLaMA-3.3-70b-versatile model.

Provides risk description, recommendations, and report generation.



\---



\## Tech Stack

\- Python 3.11

\- Flask 3.0

\- Groq API (LLaMA-3.3-70b-versatile)

\- flask-limiter 30 req/min

\- sentence-transformers



\---



\## Setup Instructions



\### Prerequisites

\- Python 3.11

\- Groq API key from console.groq.com



\### Step 1 — Clone the repo

```bash

git clone https://github.com/kusumaau/risk-heatmap-export-service

cd risk-heatmap-export-service/ai-service

```



\### Step 2 — Create .env file

```bash

GROQ\_API\_KEY=gsk\_JCZlBJKEEWgmglP8N6W3WGdyb3FYdkeDRUlTDueSgRlVAWnVWdtx

```



\### Step 3 — Install dependencies

```bash

pip install -r requirements.txt

```



\### Step 4 — Run the service

```bash

python app.py

```

Service runs on http://localhost:5000



\---



\## API Endpoints



\### POST /describe

Input:

```json

{"text": "risk scenario description"}

```

Output: structured risk description with summary, likelihood, impact, score



\### POST /recommend

Input:

```json

{"text": "risk scenario description"}

```

Output: 3 recommendations as JSON array with action\_type, description, priority



\### POST /generate-report

Input:

```json

{"text": "risk scenario description"}

```

Output: full professional risk report



\### GET /health

Output: service status, model name, uptime



\---



\## Environment Variables

| Variable | Description |

|----------|-------------|

| GROQ\_API\_KEY | Your Groq API key from console.groq.com |



\---



\## Running with Docker

```bash

docker build -t ai-service .

docker run -p 5000:5000 --env-file ../.env ai-service

```



\---



\## Running Tests

```bash

pytest test\_unit.py -v

```

