# Backend
mkdir -p backend/app/api/routes
mkdir -p backend/app/core
mkdir -p backend/app/models
mkdir -p backend/app/utils
mkdir -p backend/tests

# Frontend
mkdir -p frontend/src/app
mkdir -p frontend/src/components/ui
mkdir -p frontend/src/lib
mkdir -p frontend/src/types

# Data & docs
mkdir -p data
mkdir -p docs/screenshots

# Touch placeholder files so git tracks empty dirs
touch data/.gitkeep
touch backend/app/__init__.py
touch backend/app/api/__init__.py
touch backend/app/api/routes/__init__.py
touch backend/app/core/__init__.py
touch backend/app/models/__init__.py
touch backend/app/utils/__init__.py
