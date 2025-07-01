# Development Workflows and Standards

This file defines standardized workflows, processes, and templates for efficient software development.

## Git Workflows

### Conventional Commits

```
processes:
  apply_as_conventional_commits: |
    Separate changes into distinct Conventional Commits (e.g., `test()`, `feat()`, `fix()`), each with a clear purpose. Use `git status` and check against full task history. Apply each commit using `git`

    Guidelines:
    - ALWAYS use `git ... | cat` for any `git` command that produces output to FORCE no pager
    - Use the guidelines from the `write_commit_message` process
    - Line wrap at 88 characters
    - Wrap code references in backticks (e.g., `variable_name`, `function()`)

  write_commit_message: |
    ## Commit Message Format

    You are an assistant to help write git commit messages in "Conventional Commit" style using **imperative tense**.

    Please use the following format for the body of the commit message, placing greater emphasis on the reason for each change (i.e., the "why") more so than the "how":

    ```markdown
    Prior to this commit, ...

    In this commit, ...
    ```

    For example:

    ```markdown
    fix(config): reduce resource allocation to prevent service termination

    Prior to this commit, the `service-manager` was killed due to resource over utilization when
    both the `data-processor` Job _and_ the `api-client` process were running.

    In this commit, reduce the resource allocation in an effort to reduce resource
    usage. Note that after this change was made, the following jobs successfully ran in a
    service-manager in the cloud environment:

    1. `data-processor` Job to transform the `resource_data` view to the
       `processed.resource_data_json` topic.
    2. `api-client` job to read records from the `processed.resource_data_json` topic
       and convert them into the respective API calls.
    ```

    REMINDER: use IMPERATIVE TENSE!!!

    Guidelines:
    - Line wrap at 88 characters
    - Wrap code or filepath references in backticks (e.g., `variable_name`, `function()`)
```

### Commit Organization Guidelines

```
commit_organization: |
  ## Commit Organization Guidelines

  When applying changes as Conventional Commits, follow these organization principles:

  1. Separate changes by purpose:
     - Core functionality changes: `fix()` or `feat()`
     - Build/dependency changes: `build()` or `chore()`
     - Documentation updates: `docs()`
     - Code improvements: `refactor()` or `perf()`
     - Test additions/changes: `test()`

  2. Order commits logically:
     - Start with core functionality changes
     - Follow with supporting changes
     - End with documentation updates

  3. Use appropriate scopes:
     - Component name: `fix(component)`
     - Module name: `feat(module)`
     - System area: `chore(dependencies)`
     - Documentation area: `docs(memory-bank)`

  4. Keep commits focused:
     - Each commit should do ONE thing
     - Changes should be related to the commit type and scope
     - Split large changes into multiple commits when appropriate
```

### Branch Management

```
branch_management: |
  ## Branch Management

  1. Create a new branch from current main:
     ```
     git checkout -b fix/TICKET-XXX-brief-description
     ```

  2. Push the feature branch:
     ```
     git checkout fix/TICKET-XXX-brief-description
     git push -u origin fix/TICKET-XXX-brief-description
     ```
```

## Pull Request Workflows

### PR Description Format

```
write_pr_description: |
  ## PR Description Format

  You are an assistant to help write GitHub PR descriptions that clearly explain changes and link to relevant tickets.

  Please use the following format, focusing on the problem being solved and the approach taken:

  ```markdown
  # Title: Brief description of the change

  Prior to this PR, [describe the problem or limitation]

  In this PR, [describe the solution implemented]

  [Include any additional context, testing notes, or implementation details]
  ```

  Guidelines:
  - Use continuous paragraphs without line breaks
  - Wrap code references in backticks (e.g., `variable_name`, `function()`)
  - Include Markdown links to all referenced tickets
  - Use emoji(s) prefixed headings and lists for better readability when appropriate
```

## Documentation Standards

### Code and Documentation Style

```
code_and_docs_style: |
  ## Code and Documentation Style

  - Use backticks for inline code references: `variable`, `method()`, `config.setting`
  - Use triple backticks for code blocks with language specification
  - For configuration values, include both the parameter name and value in backticks
  - When referencing file paths, use consistent formatting: `path/to/file.ext`
```

## Memory Bank System

```
memory_bank: |
  # Memory Bank

  I am an AI agent, an expert software engineer with a unique characteristic: my memory resets completely between sessions. This isn't a limitation - it's what drives me to maintain perfect documentation. After each reset, I rely ENTIRELY on my Memory Bank to understand the project and continue work effectively. I MUST read ALL memory bank files at the start of EVERY task - this is not optional.

  ## Memory Bank Location

  The Memory Bank is located in the `./memory-bank` directory of the project repository.

  ## Memory Bank Structure

  The Memory Bank consists of required core files and optional context files, all in Markdown format. Files build upon each other in a clear hierarchy:

  ```mermaid
  flowchart TD
      PB[projectbrief.md] --> PC[productContext.md]
      PB --> SP[systemPatterns.md]
      PB --> TC[techContext.md]

      PC --> AC[activeContext.md]
      SP --> AC
      TC --> AC

      AC --> P[progress.md]
  ```

  ### Core Files (Required)
  1. [`projectbrief.md`](./memory-bank/projectbrief.md)
     - Foundation document that shapes all other files
     - Created at project start if it doesn't exist
     - Defines core requirements and goals
     - Source of truth for project scope

  2. [`productContext.md`](./memory-bank/productContext.md)
     - Why this project exists
     - Problems it solves
     - How it should work
     - User experience goals

  3. [`activeContext.md`](./memory-bank/activeContext.md)
     - Current work focus
     - Recent changes
     - Next steps
     - Active decisions and considerations

  4. [`systemPatterns.md`](./memory-bank/systemPatterns.md)
     - System architecture
     - Key technical decisions
     - Design patterns in use
     - Component relationships

  5. [`techContext.md`](./memory-bank/techContext.md)
     - Technologies used
     - Development setup
     - Technical constraints
     - Dependencies

  6. [`progress.md`](./memory-bank/progress.md)
     - What works
     - What's left to build
     - Current status
     - Known issues

  ### Additional Context
  Create additional files/folders within [`memory-bank`](./memory-bank/) when they help organize:
  - Complex feature documentation
  - Integration specifications
  - API documentation
  - Testing strategies
  - Deployment procedures

  ## Core Workflows

  ### Plan Mode
  ```mermaid
  flowchart TD
      Start[Start] --> ReadFiles[Read Memory Bank]
      ReadFiles --> CheckFiles{Files Complete?}

      CheckFiles -->|No| Plan[Create Plan]
      Plan --> Document[Document in Chat]

      CheckFiles -->|Yes| Verify[Verify Context]
      Verify --> Strategy[Develop Strategy]
      Strategy --> Present[Present Approach]
  ```

  ### Act Mode
  ```mermaid
  flowchart TD
      Start[Start] --> Context[Check Memory Bank]
      Context --> Update[Update Documentation]
      Update --> Rules[Update ./AGENTS.md if needed]
      Rules --> Execute[Execute Task]
      Execute --> Document[Document Changes]
  ```

  ## Documentation Updates

  Memory Bank updates occur when:
  1. Discovering new project patterns
  2. After implementing significant changes
  3. When user requests with **update memory bank** (MUST review ALL files)
  4. When context needs clarification

  ```mermaid
  flowchart TD
      Start[Update Process]

      subgraph Process
          P1[Review ALL Files]
          P2[Document Current State]
          P3[Clarify Next Steps]
          P4[Update ./AGENTS.md]

          P1 --> P2 --> P3 --> P4
      end

      Start --> Process
  ```

  Note: When triggered by **update memory bank**, I MUST review every memory bank file, even if some don't require updates. Focus particularly on activeContext.md and progress.md as they track current state.

  ## Project Intelligence (./AGENTS.md)

  The ./AGENTS.md file is my learning journal for each project. It captures important patterns, preferences, and project intelligence that help me work more effectively. As I work with you and the project, I'll discover and document key insights that aren't obvious from the code alone.

  ```mermaid
  flowchart TD
      Start{Discover New Pattern}

      subgraph Learn [Learning Process]
          D1[Identify Pattern]
          D2[Validate with User]
          D3[Document in ./AGENTS.md]
      end

      subgraph Apply [Usage]
          A1[Read ./AGENTS.md]
          A2[Apply Learned Patterns]
          A3[Improve Future Work]
      end

      Start --> Learn
      Learn --> Apply
  ```

  ### What to Capture
  - Critical implementation paths
  - User preferences and workflow
  - Project-specific patterns
  - Known challenges
  - Evolution of project decisions
  - Tool usage patterns

  The format is flexible - focus on capturing valuable insights that help me work more effectively with you and the project. Think of ./AGENTS.md as a living document that grows smarter as we work together.

  REMEMBER: After every memory reset, I begin completely fresh. The Memory Bank is my only link to previous work. It must be maintained with precision and clarity, as my effectiveness depends entirely on its accuracy.

> **Note**: The Memory Bank is the sole source of continuity for the AI agent and must be meticulously maintained to ensure project effectiveness.
```

## Issue Tracking Templates

### Bug Template

```
ticket_templates: |
  ## Issue Tracking Templates

  ### Bug Template
  ```
  h2. Problem

  [Clear description of the issue]

  h2. Error Message

  {noformat}
  [Exact error message]
  {noformat}

  h2. Root Cause

  [Analysis of what caused the issue]

  h2. Solution

  [How the fix addresses the problem]

  h2. Implementation Details

  1. [Step 1]
  2. [Step 2]
  3. [Step 3]

  h2. Related Commits

  * {{commit-hash}} [commit message]

  h2. Documentation

  [Links to updated documentation]
  ```

  ### Story Template
  ```
  h2. User Story

  As a [type of user], I want [goal] so that [benefit/value].

  h2. Background

  [Provide context and background information about why this story is important]

  h2. Acceptance Criteria

  * [ ] [Criterion 1]
  * [ ] [Criterion 2]
  * [ ] [Criterion 3]

  h2. Technical Requirements

  * [Requirement 1]
  * [Requirement 2]
  * [Requirement 3]

  h2. Dependencies

  * [Dependency 1, e.g., other stories, external systems]
  * [Dependency 2]

  h2. Design/Mockups

  [Links to design documents or mockups if applicable]

  h2. Testing Considerations

  * [Test scenario 1]
  * [Test scenario 2]
  ```

  ### Task Template
  ```
  h2. Objective

  [Clear description of what needs to be accomplished]

  h2. Context

  [Background information and why this task is necessary]

  h2. Requirements

  * [Requirement 1]
  * [Requirement 2]
  * [Requirement 3]

  h2. Implementation Plan

  1. [Step 1]
  2. [Step 2]
  3. [Step 3]

  h2. Dependencies

  * [Dependency 1]
  * [Dependency 2]

  h2. Definition of Done

  * [ ] [Criterion 1]
  * [ ] [Criterion 2]
  * [ ] [Criterion 3]

  h2. Documentation Updates

  [Specify which documentation needs to be updated]
  ```

  ### Epic Template
  ```
  h2. Epic Goal

  [High-level description of the epic's objective]

  h2. Business Value

  [Explain the business value this epic delivers]

  h2. Background

  [Provide context and background information]

  h2. Scope

  [Define what is in and out of scope for this epic]

  h3. In Scope
  * [Item 1]
  * [Item 2]

  h3. Out of Scope
  * [Item 1]
  * [Item 2]

  h2. User Journeys

  [Describe the key user journeys this epic enables]

  h2. Technical Considerations

  * [Technical consideration 1]
  * [Technical consideration 2]

  h2. Dependencies

  * [Dependency 1]
  * [Dependency 2]

  h2. Success Metrics

  * [Metric 1]
  * [Metric 2]
  ```

  ### Spike Template
  ```
  h2. Investigation Goal

  [Clear description of what needs to be investigated]

  h2. Background

  [Context and why this investigation is necessary]

  h2. Questions to Answer

  * [Question 1]
  * [Question 2]
  * [Question 3]

  h2. Investigation Approach

  1. [Step 1]
  2. [Step 2]
  3. [Step 3]

  h2. Time Box

  [Maximum time allocated for this investigation]

  h2. Deliverables

  * [Deliverable 1, e.g., technical document, proof of concept]
  * [Deliverable 2]

  h2. Outcome Documentation

  [Where and how the findings will be documented]
  ```
```
