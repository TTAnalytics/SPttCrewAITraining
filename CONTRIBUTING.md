# Contribution and Branching Workflow Guidelines

This document outlines the branching and development workflow for the project. These guidelines ensure consistency, encourage collaboration, and maintain the stability of the codebase.

---

## Table of Contents
1. [Branching Strategy](#branching-strategy)
2. [Workflow Overview](#workflow-overview)
3. [Branch Naming Conventions](#branch-naming-conventions)
4. [Merge Rules](#merge-rules)
5. [Testing and CI/CD](#testing-and-cicd)
6. [JIRA Integration](#jira-integration)
7. [Handling Hotfixes](#handling-hotfixes)
8. [Updating These Guidelines](#updating-these-guidelines)

---

## Branching Strategy

Our repository follows a structured branching model:

- **`main`**: Contains stable, deployed, and productive code. This branch is always deployable.
- **`develop`**: Contains all changes that are ready for the next release but not yet deployed. This is the main working branch for ongoing development.
- **Feature branches**: Used for implementing new features or minor changes. Feature branches are merged into `develop` after review and approval.
- **Release branches**: Created during a sprint to consolidate and test all features. Once testing is complete, release branches are merged into both `develop` and `main`.
- **Hotfix branches**: For critical fixes to `main`. Hotfixes are merged into both `main` and `develop` to keep branches in sync.

---

## Workflow Overview

1. **Start a Feature**:
   - Create a feature branch from `develop`.
   - Name the branch based on the related JIRA ticket (e.g., `feature/JIRA-ID-description`).

2. **Develop and Commit**:
   - Commit code changes to the feature branch.
   - Follow the [Branch Naming Conventions](#branch-naming-conventions).

3. **Merge into `develop`**:
   - Create a pull request (PR) from the feature branch to `develop`.
   - Request reviews and ensure all checks (e.g., CI tests) pass before merging.

4. **Create a Release Branch**:
   - At the designated sprint point, create a release branch from `develop`.
   - Test the release branch thoroughly in a staging environment.

5. **Finalize and Deploy**:
   - After testing, merge the release branch into `develop` and `main`.
   - Tag the release commit in `main` (e.g., `v1.0.0`).

---

## Branch Naming Conventions

Consistent branch names improve clarity and traceability. Use the following patterns:

- **Feature branches**: `feature/JIRA-ID-description`
- **Bugfix branches**: `bugfix/JIRA-ID-description`
- **Hotfix branches**: `hotfix/JIRA-ID-description`
- **Release branches**: `release/YYYY-MM-DD` or `release/sprint-X`

Examples:
- `feature/PROJ-123-new-login-page`
- `bugfix/PROJ-456-fix-null-pointer`
- `release/2025-02-01`

---

## Merge Rules

- **Feature branches**:
  - Must be reviewed by at least one team member before merging.
  - All CI checks must pass before merging.
- **Release branches**:
  - Should only include completed and tested feature branches.
  - Must pass integration tests before merging into `main` and `develop`.
- **Main branch**:
  - Protected to prevent direct pushes.
  - Merges into `main` must be tagged for release.

---

## Testing and CI/CD

- **Feature branches**: Run unit tests automatically through the CI pipeline. (Coming soon)
- **Release branches**: Run full integration and regression tests in the staging environment. (Coming soon)
- **Main branch**: Deploy to production automatically after successful testing. (Coming soon)

---

## JIRA Integration

- Branches must be named after their corresponding JIRA tickets for traceability.
- Use commit messages that reference JIRA IDs (e.g., `PROJ-123: Implement new login page`).
- Ensure JIRA tickets are updated as development progresses.

---

## Handling Hotfixes

1. Create a hotfix branch from `main` (e.g., `hotfix/JIRA-ID-critical-issue`).
2. Implement and test the fix.
3. Merge the hotfix branch into both `main` and `develop`.
4. Tag the `main` branch with the hotfix release (e.g., `v1.0.1`).

---

## Updating These Guidelines

Propose updates to this document by:
1. Creating a feature branch (e.g., `feature/update-contribution-guidelines`).
2. Submitting a pull request for review.
3. Ensuring team consensus before merging updates.

---

This workflow provides a structured, collaborative approach to development. Adherence to these guidelines ensures a stable codebase and efficient project management.