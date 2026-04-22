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

---

## Contribution & Branching Strategy

We follow a structured workflow to maintain code quality and stability.

### Branching Model

This project uses a standard branching flow:
- `main`: Represents the production-ready state. Only stable, tested features are merged here.
- `develop`: The primary integration branch. All feature branches are merged into `develop` for testing before a release.
- **Feature Branches**: Branch off from `develop` and name the branch descriptively (e.g., `feature/add-user-login`, `bugfix/auth-header`).

### Development Workflow

1. **Create an Issue**: Before starting work, ensure there is an issue tracking the feature or bug.
2. **Branch Out**: Create a branch off `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```
3. **Commit Messages**: Write clear, descriptive commit messages. We recommend using the [Conventional Commits](https://www.conventionalcommits.org/) format (e.g., `feat: API documentation updates`, `fix: database connection string`).
4. **Pull Request**: Push your branch and open a Pull Request against the `develop` branch.
5. **Code Review**: Ensure at least one teammate reviews your PR. Address any feedback before merging.
6. **Merge**: Once approved and all tests pass, merge your code.

### Pull Request Guidelines

- Keep PRs focused. Do not mix unrelated changes in a single Pull Request.
- Ensure all automated checks (linting, tests) pass.
- Link the related issue in the PR description (e.g., `Closes #123`).
