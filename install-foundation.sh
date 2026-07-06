#!/data/data/com.termux/files/usr/bin/bash

set -e

ROOT="$(pwd)"

echo ""
echo "==============================================="
echo " ADOS Foundation Pack v0.1"
echo "==============================================="
echo ""

############################################
# Folder
############################################

mkdir -p docs/adr
mkdir -p knowledge
mkdir -p agents
mkdir -p templates/project
mkdir -p .github/workflows

############################################
# .gitignore
############################################

cat > .gitignore <<'GIT'
logs/
cache/
tmp/
workspace/
*.log
*.tmp
*.swp
*.bak
.env
.env.*
__pycache__/
*.pyc
node_modules/
dist/
build/
GIT

############################################
# CONTRIBUTING
############################################

cat > CONTRIBUTING.md <<'CONTRIB'
# Contributing

## Workflow

1. Create Feature Branch
2. Implement
3. Test
4. Update Documentation
5. Commit
6. Pull Request

Every feature must update:

- CHANGELOG
- TODO
- Documentation

CONTRIB

############################################
# SECURITY
############################################

cat > SECURITY.md <<'SEC'
# Security Policy

Report security issues privately.

Never commit:

- API Keys
- Passwords
- Tokens
- Secrets

SEC

############################################
# CODE OF CONDUCT
############################################

cat > CODE_OF_CONDUCT.md <<'CODE'
# Code of Conduct

Be respectful.

Focus on engineering quality.

Document every important decision.

CODE

############################################
# ADR
############################################

cat > docs/adr/ADR-0001.md <<'ADR'
# ADR-0001

Title

Freeze Repository Architecture

Status

Accepted

Decision

Repository structure is frozen for version 0.1.

Reason

Reduce unnecessary refactoring.

ADR

############################################
# Knowledge
############################################

cat > knowledge/README.md <<'KNOW'
# Knowledge Engine

This directory stores reusable engineering knowledge.

Modules

- Python
- PHP
- JavaScript
- HTML
- CSS
- Linux
- Docker
- Git
- Trading
- MT5
- SMC

KNOW

############################################
# Agent Architect
############################################

cat > agents/architect.md <<'ARCH'
# Architect Agent

Responsibilities

- Architecture
- Design Decisions
- Repository Structure
- Standards
- Reviews

ARCH

############################################
# Agent Backend
############################################

cat > agents/backend.md <<'BACK'
# Backend Agent

Responsibilities

- APIs
- Database
- Services
- Business Logic
- Testing

BACK

############################################
# Agent Frontend
############################################

cat > agents/frontend.md <<'FRONT'
# Frontend Agent

Responsibilities

- UI
- UX
- Components
- Accessibility

FRONT

############################################
# Project Template
############################################

cat > templates/project/README.md <<'TEMP'
# Project Template

Generated project structure.

Includes:

- Documentation
- Backend
- Frontend
- Tests
- GitHub Workflow

TEMP

############################################
# GitHub Action
############################################

cat > .github/workflows/foundation-check.yml <<'YML'
name: Foundation Check

on:
  push:
  pull_request:

jobs:
  verify:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Check Required Files
        run: |
          test -f README.md
          test -f MASTER_INDEX.md
          test -f AGENTS.md
          test -f ROADMAP.md
          test -f TODO.md
          test -f VERSION
          test -f .gitignore
YML

############################################
# Finish
############################################

echo "Foundation Pack Installed."

echo ""

tree -L 2

echo ""
echo "Next:"
echo "git status"
echo "git add ."
echo "git commit -m 'foundation: install foundation pack'"
echo "git push origin main"
echo ""

