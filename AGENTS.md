# AGENTS.md

# ADOS AI Agent Protocol

Version: 0.1.0

Status: Active

---

# Purpose

This document defines how every AI agent must work inside ADOS.

The repository is the single source of truth.

Never rely on previous chat history.

Always rely on repository documentation.

---

# Boot Procedure

Before changing anything, every AI must execute the following sequence.

1. Read MASTER_INDEX.md
2. Read AGENTS.md
3. Read ROADMAP.md
4. Read TODO.md
5. Read DECISIONS.md
6. Read CHANGELOG.md
7. Read BUGS.md
8. Read project specification
9. Read related source code
10. Analyze current state

Only after these steps may implementation begin.

---

# AI Responsibilities

Every AI must:

* understand existing architecture
* avoid duplicate implementation
* preserve project consistency
* follow ADOS standards
* update documentation
* update TODO status
* update CHANGELOG
* record architectural decisions when needed

---

# Development Workflow

Analyze

↓

Plan

↓

Implement

↓

Self Review

↓

Testing

↓

Documentation Update

↓

Git Commit

↓

Finish

---

# Documentation Rules

Documentation is mandatory.

A task is NOT complete until documentation has been updated.

Required updates:

* CHANGELOG.md
* TODO.md
* BUGS.md (if applicable)
* DECISIONS.md (if architecture changes)

---

# Coding Rules

Never rewrite unrelated modules.

Prefer small commits.

Keep functions focused.

Avoid unnecessary dependencies.

Maintain backward compatibility whenever possible.

---

# Architecture Rules

Do not change repository structure.

Do not rename folders without recording a decision.

Do not introduce new frameworks without updating DECISIONS.md.

---

# Communication Rules

Do not ask unnecessary questions.

If information exists inside the repository, use it.

Only ask for clarification when a business decision cannot be inferred.

---

# Definition of Done

A task is complete only if:

* implementation finished
* no obvious errors remain
* documentation updated
* TODO updated
* CHANGELOG updated
* code is consistent with standards

---

# Current Priority

1. Complete ADOS Foundation.
2. Build ADOS CLI.
3. Build Project Generator.
4. Build Knowledge Engine.
5. Build Aegis Trade Engine.
