# Commit message format

Commits follow the Commitizen default format (`cz_conventional_commits`), as specified by [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/#specification).

```text
<type>(<scope>): <subject>

<body>

<footer>
```

## Header

- **Type** (required): choose one.

  | Type | Use for |
  |------|---------|
  | `feat` | A new feature |
  | `fix` | A bug fix |
  | `docs` | Documentation only |
  | `style` | Formatting with no change in meaning |
  | `refactor` | Code change that neither fixes a bug nor adds a feature |
  | `perf` | Performance improvement |
  | `test` | Adding or correcting tests |
  | `build` | Build system or dependencies, including `pyproject.toml` and `uv.lock` |
  | `ci` | CI configuration |
  | `chore` | Maintenance that fits no other type |
  | `revert` | Reverting an earlier commit |

- **Scope** (optional): one noun with no spaces, naming the area changed, such as `cli`, `templates`, or `adr`.
- **Subject** (required): imperative mood, lower case, no trailing period. Keep the whole header to 72 characters or fewer.

## Body and footer

- **Body** (optional): one blank line after the header. Explain what changed and why, not how.
- **Footer** (optional): one blank line after the body. Use `Token: value` or `Token #value`, with `-` in place of spaces in the token. For example, `Refs: #123` or `Closes #123`.

## Breaking changes

Mark every breaking change with both forms:

```text
feat(cli)!: rename the new command to forge

BREAKING CHANGE: `anvil new` no longer exists. Use `anvil forge`.
```

`BREAKING CHANGE` must be upper case.

## Generating a message

- Describe the staged diff only, not the wider conversation.
- If the staged changes need more than one type, propose splitting them into separate commits.
