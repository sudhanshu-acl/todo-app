# Contributing Guidelines

Thank you for your interest in contributing to this project!

## Branching Strategy

Our project uses the following Git branching model:

- **`main`**: Represents the stable, production-ready release.
- **`develop`**: The active development and integration branch.
- **Feature/Bugfix Branches**: Always branch off from `develop`. Use descriptive naming conventions:
  - `feature/<short-description>` (e.g., `feature/user-login`)
  - `bugfix/<short-description>` (e.g., `bugfix/fix-auth-token`)

## How to Contribute

1. **Find or Create an Issue**: Before writing code, ensure an issue exists for tracking the work.
2. **Checkout a Branch**:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```
3. **Write Code**: Follow standard practices and keep modules separated as described in the README schema.
4. **Commit Your Changes**: We recommend [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for refactoring
   
   *Example*: `feat: add database pagination`
5. **Run Tests & Lints**: Ensure your code passes locally before pushing. Our GitHub Actions CI will run automatically on your PR.
6. **Open a Pull Request**: Push your branch and open a PR against `develop`.
   ```bash
   git push origin feature/your-feature-name
   ```
   Link the associated issue in your PR description (e.g., `Closes #123`).
7. **Code Review**: Please wait for approval from another contributor before merging your code.

## Local Development Setup

Refer to the primary [README.md](README.md) for detailed instructions on installing requirements and running the application.
