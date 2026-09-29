# Root files
touch README.md .env.example .gitignore docker-compose.yml Makefile LICENSE

# Backend files
touch backend/Dockerfile backend/requirements.txt
touch backend/app/main.py backend/app/config.py
touch backend/app/api/routes/chat.py
touch backend/app/api/routes/documents.py
touch backend/app/api/routes/health.py
touch backend/app/core/rag_chain.py
touch backend/app/core/embeddings.py
touch backend/app/core/vectorstore.py
touch backend/app/core/loader.py
touch backend/app/core/llm.py
touch backend/app/models/schemas.py
touch backend/app/utils/logger.py

# Frontend files
touch frontend/Dockerfile frontend/package.json frontend/next.config.mjs
touch frontend/tailwind.config.ts frontend/postcss.config.mjs frontend/tsconfig.json
touch frontend/src/app/layout.tsx frontend/src/app/page.tsx frontend/src/app/globals.css
touch frontend/src/components/ChatInterface.tsx
touch frontend/src/components/MessageBubble.tsx
touch frontend/src/components/Sidebar.tsx
touch frontend/src/components/DocumentUpload.tsx
touch frontend/src/components/SourceCard.tsx
touch frontend/src/components/ui/button.tsx
touch frontend/src/components/ui/input.tsx
touch frontend/src/lib/api.ts frontend/src/lib/utils.ts
touch frontend/src/types/index.ts

# Docs
touch docs/architecture.md
