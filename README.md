# Demo Backend

This project follows a modular architecture designed for maintainability, scalability, and clear separation of concerns.

## Module Division

The application code is organized within the `app` directory and is divided into three main areas:

### 1. `app/core/`
This directory contains application-wide configurations and setup code that are essential for the application to run but are not tied to any specific business domain.
- **Examples**: Database connections (`database.py`), general environment configuration (`config.py`), and documentation settings (`docs.py`).
- **Rule**: Core modules should not depend on feature modules.

### 2. `app/shared/`
This directory is meant for shared utilities, helper functions, cross-cutting concerns, and base classes that can be used by any feature module across the application.
- **Examples**: Common response schemas, base database models, pagination utilities, or shared middleware.

### 3. `app/modules/`
This is where the actual business logic resides. The backend is split into multiple feature-based domain modules. Each subdirectory under `app/modules` represents a specific domain.
- **Current Modules**: `auth`, `todos`.
- **Structure**: Each module is self-contained and typically includes its own:
  - `router.py`: API endpoint definitions
  - `schemas.py`: Pydantic models for request/response validation
  - `models.py`: Database models (SQLAlchemy)
  - `service.py` / `crud.py`: Core business logic and database interactions

---

## Management Ideas & Guidelines

To maintain a healthy codebase as the project scales, we follow these management principles:

1. **Self-Contained Domains (Domain-Driven Design concepts)**
   Each module inside `app/modules/` should encapsulate a single business capability. If a feature touches multiple domains, consider where the primary responsibility lies, or if a new orchestrating module is needed.

2. **Strict Dependency Rules**
   - `modules/` can depend on `core/` and `shared/`.
   - `core/` and `shared/` **must never** depend on anything inside `modules/`.
   - Cross-module dependencies (e.g., `todos` depending on `auth`) should be minimized. When necessary, rely on shared interfaces or ID references rather than heavily coupling the business logic between modules.

3. **Dependency Injection**
   Leverage FastAPI's dependency injection system (e.g., for database sessions, current user retrieval) to keep routing code clean and make services highly testable. 

4. **Scalability Path**
   By strictly maintaining this module division, the project is structured as a "Modular Monolith". If the application load or team size grows significantly, individual modules can be easily refactored and extracted into separate microservices.
