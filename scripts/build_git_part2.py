# scripts/build_git_part2.py
"""
Builds 55 more Git / GitHub interview questions to reach 215 total.
"""

git_part2 = [
    (
        "What is `.gitattributes` and what is it commonly used for?",
        "`.gitattributes` assigns path-specific settings in a repository, most commonly used to standardize line endings (`* text=auto eol=lf`) across Windows, macOS, and Linux to prevent noisy diffs.",
        "Intermediate",
        "Concept",
        "* text=auto eol=lf\n*.png binary",
        "What does `binary` indicate in .gitattributes?"
    ),
    (
        "What is the `core.autocrlf` setting and what should it be set to on Windows?",
        "On Windows, `git config --global core.autocrlf true` converts LF to CRLF when checking out code, and converts CRLF back to LF when committing. On macOS/Linux, it should be set to `input`.",
        "Easy",
        "Practical",
        "git config --global core.autocrlf true",
        "Why do mismatched line endings cause entire files to appear modified in diffs?"
    ),
    (
        "What is `git worktree` and when is it useful?",
        "`git worktree` allows you to check out multiple branches simultaneously into different directories from a single local Git repository, eliminating the need to stash or switch branches.",
        "Advanced",
        "Concept",
        "git worktree add ../hotfix-dir hotfix/critical-bug",
        "How do you remove a worktree after completing work?"
    ),
    (
        "How do you debug which `.gitignore` rule is ignoring a specific file?",
        "Use `git check-ignore -v <filepath>`. It outputs the exact `.gitignore` file and line number responsible for ignoring the file.",
        "Easy",
        "Practical",
        "git check-ignore -v src/config.env\n# .gitignore:12:.env*  src/config.env",
        "What flag shows verbose rule details?"
    ),
    (
        "What is `git shortlog -sn` used for?",
        "It summarizes commit history grouped by author, sorted numerically (`-n`) showing total commit counts (`-s`).",
        "Easy",
        "Practical",
        "git shortlog -sn",
        "How do you view contributors for a specific time range?"
    ),
    (
        "What is `git rerere` (Reuse Recorded Resolution)?",
        "`git rerere` records how you resolved a merge conflict and automatically applies the exact same resolution if Git encounters that same conflict again in future merges or rebases.",
        "Advanced",
        "Concept",
        "git config --global rerere.enabled true",
        "When is rerere particularly helpful?"
    ),
    (
        "How do you export a clean ZIP or tarball of your project code without the `.git` folder?",
        "Use `git archive --format=zip HEAD -o project.zip`.",
        "Easy",
        "Practical",
        "git archive --format=zip HEAD -o release.zip",
        "What commit does `HEAD` export in this command?"
    ),
    (
        "What is `git describe` and what does it output?",
        "`git describe` finds the most recent reachable annotated tag from the current commit and appends the number of additional commits and the short SHA (e.g. `v1.2.0-4-g2a1b3c`).",
        "Intermediate",
        "Concept",
        "git describe --tags",
        "Where is git describe commonly used in software release versions?"
    ),
    (
        "What is `git fsck` used for?",
        "`git fsck` (File System Consistency Check) verifies the integrity of the Git object database, identifying dangling commits, corrupted blobs, or broken references.",
        "Advanced",
        "Practical",
        "git fsck --full",
        "What is a dangling commit?"
    ),
    (
        "What is a dangling commit in Git?",
        "A dangling commit is an orphaned commit that is no longer directly reachable by any branch, tag, or reference. It can be inspected using `git show <hash>` and is eventually cleaned by `git gc`.",
        "Intermediate",
        "Concept",
        "",
        "Can a dangling commit be recovered?"
    ),
    (
        "What is GitHub Dependabot?",
        "An automated security bot on GitHub that scans project dependency files (`package.json`, `pom.xml`, etc.) for known vulnerabilities and automatically opens Pull Requests with updated versions.",
        "Easy",
        "Concept",
        "",
        "Where is Dependabot configured in a repository?"
    ),
    (
        "What are GitHub Secrets in GitHub Actions?",
        "Encrypted environment variables stored securely in repository settings (e.g. API keys, database credentials, AWS access keys) that workflows can access without exposing secrets in code.",
        "Easy",
        "Concept",
        "env:\n  API_KEY: ${{ secrets.STRIPE_SECRET_KEY }}",
        "Can collaborators with read access view secret values in repository settings?"
    ),
    (
        "What is the difference between a Deploy Key and a Personal Access Token on GitHub?",
        "A Deploy Key is an SSH key that grants read/write access to a single specific repository, typically used on deployment servers. A PAT belongs to a user account and can access multiple repositories with user permissions.",
        "Intermediate",
        "Comparison",
        "",
        "Why is a Deploy Key safer on production servers than a personal account token?"
    ),
    (
        "What is a GitHub Release?",
        "A packaged deliverable of a specific version of your software based on a Git tag, containing release notes, changelogs, and binary downloadable assets (e.g. installer .exe, .tar.gz).",
        "Easy",
        "Concept",
        "",
        "Does creating a release automatically create a Git tag?"
    ),
    (
        "What is the GitHub Merge Queue feature?",
        "A feature for busy repositories with high merge frequency that sequences PRs into a queue, testing each PR combined with previously queued PRs before merging to main to prevent broken builds.",
        "Advanced",
        "Concept",
        "",
        "What problem does a merge queue solve?"
    ),
    (
        "What is the difference between `git checkout -- <file>` and modern `git restore <file>`?",
        "Both discard uncommitted changes in the working directory; `git restore` was introduced in Git 2.23 to separate file restoration from branch switching.",
        "Easy",
        "Comparison",
        "",
        "Which command is recommended in modern documentation?"
    ),
    (
        "What does `git log -n 5 --oneline` do?",
        "It limits the log output to the last 5 commits, formatting each commit as a single line with short SHA and message.",
        "Easy",
        "Practical",
        "git log -n 5 --oneline",
        "What does `-n 5` specify?"
    ),
    (
        "How do you format git log output with custom formatting (e.g. hash, date, author)?",
        "Use `git log --pretty=format:'%h - %an, %ar : %s'` where `%h` is short hash, `%an` author name, `%ar` relative date, and `%s` subject.",
        "Intermediate",
        "Practical",
        "git log --pretty=format:'%h - %an, %ar : %s'",
        "What does `%s` represent in the format string?"
    ),
    (
        "What does `git bundle` do?",
        "`git bundle create repo.bundle --all` packages Git objects and references into a single binary file that can be copied to offline air-gapped computers and cloned like a remote repository.",
        "Advanced",
        "Concept",
        "git bundle create backup.bundle --all\ngit clone backup.bundle my-repo",
        "Can you fetch from a bundle file?"
    ),
    (
        "What is `git notes` used for?",
        "`git notes add -m 'Reviewed by QA' <commit_hash>` adds extra notes and metadata to an existing commit without modifying the commit object or changing its SHA hash.",
        "Advanced",
        "Concept",
        "",
        "Are Git notes pushed to remote repositories automatically?"
    ),
    (
        "What happens if you run `git push origin main --force` on a branch where other developers are actively pushing?",
        "It overwrites the remote branch history with your local branch history, potentially deleting your teammates' commits permanently from the remote repository.",
        "Easy",
        "Scenario",
        "",
        "What safer flag should always be used instead?"
    ),
    (
        "What is the difference between `git merge --ff-only` and standard `git merge`?",
        "`--ff-only` will ONLY merge if a fast-forward merge is possible without creating a merge commit. If branches have diverged, it refuses to merge and exits with an error.",
        "Intermediate",
        "Concept",
        "git merge --ff-only feature-branch",
        "When is `--ff-only` commonly used?"
    ),
    (
        "Which command shows all local branches that have already been merged into `main`?",
        "Run `git branch --merged main`.",
        "Easy",
        "Practical",
        "git branch --merged main",
        "How do you list branches that have NOT been merged yet?"
    ),
    (
        "How do you list local branches that have NOT been merged into `main`?",
        "Run `git branch --no-merged main`.",
        "Easy",
        "Practical",
        "git branch --no-merged main",
        "Why is this helpful before running branch cleanups?"
    ),
    (
        "How do you revert a sequence of multiple commits in order?",
        "Use a commit range with `git revert`: `git revert --no-commit HEAD~3..HEAD` followed by a single commit, or revert commits one by one in reverse chronological order.",
        "Intermediate",
        "Practical",
        "git revert --no-commit HEAD~3..HEAD\ngit commit -m 'revert: roll back last 3 commits'",
        "Why must multiple commits be reverted in reverse order?"
    ),
    (
        "What does `git clean -Xf` do?",
        "`-X` deletes ONLY ignored files (matching `.gitignore`, like build outputs and node_modules), leaving untracked unignored files intact.",
        "Intermediate",
        "Practical",
        "git clean -Xfd",
        "How does `-X` differ from standard `-x`?"
    ),
    (
        "What does `git clean -xdf` do?",
        "`-x` deletes ALL untracked files including ignored files (e.g. node_modules, build directories, logs), restoring the repository to an immaculate clean state.",
        "Intermediate",
        "Practical",
        "git clean -xdf",
        "Why should you be very cautious when running `git clean -xdf`?"
    ),
    (
        "What is `git branch -r`?",
        "It lists all remote tracking branches (e.g. `origin/main`, `origin/feature`).",
        "Easy",
        "Practical",
        "git branch -r",
        "How do you check out a remote branch locally?"
    ),
    (
        "How do you check out and start working on a remote branch `origin/feature`?",
        "Run `git switch feature` (or `git checkout feature`). Git automatically creates a local tracking branch pointing to `origin/feature`.",
        "Easy",
        "Practical",
        "git switch feature",
        "What happens if two remotes have a branch with the same name?"
    ),
    (
        "What is `git remote rename <old_name> <new_name>`?",
        "It renames a remote alias (e.g. `git remote rename origin upstream`).",
        "Easy",
        "Practical",
        "git remote rename origin old-origin",
        "What happens to remote tracking branch names when a remote is renamed?"
    ),
    (
        "What is `git remote remove <name>`?",
        "It unlinks and removes a remote alias and deletes all associated remote-tracking branches from your local repository.",
        "Easy",
        "Practical",
        "git remote remove upstream",
        "Does this delete the remote repository on GitHub?"
    ),
    (
        "What is `git log --left-right <branch1>...<branch2>`?",
        "It shows symmetric difference between two branches with `<` indicating commits exclusive to branch1 and `>` indicating commits exclusive to branch2.",
        "Intermediate",
        "Practical",
        "git log --left-right --oneline main...feature",
        "What does the three-dot `...` notation mean in Git diff/log?"
    ),
    (
        "What is the difference between two-dot `..` and three-dot `...` in `git diff`?",
        "`git diff branchA..branchB` shows diff between the tips of both branches. `git diff branchA...branchB` shows changes on branchB since its common ancestor with branchA.",
        "Intermediate",
        "Comparison",
        "",
        "Which diff notation corresponds to the diff shown on a GitHub Pull Request?"
    ),
    (
        "Which diff notation (`..` or `...`) matches what GitHub displays in a Pull Request?",
        "Three-dot diff (`git diff main...feature`) because GitHub PRs display only the commits added on the feature branch since it diverged from main.",
        "Intermediate",
        "Concept",
        "",
        "Why would a two-dot diff be confusing on a PR?"
    ),
    (
        "What does `git rebase --abort` do?",
        "It completely stops an in-progress rebase and restores the branch to the exact state it was in before `git rebase` was executed.",
        "Easy",
        "Practical",
        "git rebase --abort",
        "What command continues a rebase after resolving a conflict?"
    ),
    (
        "What command continues a rebase after resolving conflicts and staging files?",
        "Run `git rebase --continue`.",
        "Easy",
        "Practical",
        "git add resolved-file.js\ngit rebase --continue",
        "Do you run `git commit` during a rebase continue?"
    ),
    (
        "Why should you NOT run `git commit` when resolving conflicts during a rebase?",
        "Running `git commit` creates an extra commit instead of updating the replayed commit. You should stage files with `git add` and run `git rebase --continue`.",
        "Intermediate",
        "Practical",
        "",
        "What happens if you accidentally run git commit during rebase?"
    ),
    (
        "What does `git rebase --skip` do?",
        "It skips the current conflicting commit entirely, ignoring its changes and continuing the rebase with the next commit.",
        "Intermediate",
        "Practical",
        "git rebase --skip",
        "When is `--skip` appropriate?"
    ),
    (
        "What is the output of `git branch --show-current` in modern Git?",
        "It prints only the name of the currently checked-out branch, useful for shell prompt customization and CI scripts.",
        "Easy",
        "Practical",
        "git branch --show-current",
        "What does it output in detached HEAD state?"
    ),
    (
        "What is the output of `git status` when working tree is clean?",
        "'nothing to commit, working tree clean'.",
        "Easy",
        "Output",
        "git status",
        "Does this mean your local branch is synchronized with remote?"
    ),
    (
        "What is GitHub Gist?",
        "A simple GitHub service for sharing single code snippets, notes, and small scripts with full Git version control without creating a full repository.",
        "Easy",
        "Concept",
        "",
        "Can a Gist be cloned locally with Git?"
    ),
    (
        "What is the purpose of `.github/workflows/` directory in a project?",
        "It stores YAML workflow files that define automated CI/CD jobs, tests, and deployment steps executed by GitHub Actions.",
        "Easy",
        "Concept",
        "",
        "What file extension must GitHub Actions workflow files use?"
    ),
    (
        "What is the default trigger event in a GitHub Actions workflow file?",
        "`on: [push, pull_request]` triggers the workflow whenever code is pushed or a PR is opened/updated.",
        "Easy",
        "Concept",
        "on:\n  push:\n    branches: [ main ]\n  pull_request:\n    branches: [ main ]",
        "Can workflows be scheduled using cron syntax?"
    ),
    (
        "Can GitHub Actions run on a scheduled cron trigger?",
        "Yes, using `on: schedule: - cron: '0 0 * * *'` to trigger recurring background jobs (e.g. nightly builds).",
        "Easy",
        "Concept",
        "",
        "What timezone does GitHub Actions cron use?"
    ),
    (
        "What is a runner in GitHub Actions?",
        "A virtual machine (Ubuntu, Windows, or macOS) or container hosted by GitHub (or self-hosted) that executes the steps of a workflow job.",
        "Easy",
        "Concept",
        "runs-on: ubuntu-latest",
        "What is the most commonly used runner image?"
    ),
    (
        "What does `actions/checkout@v4` do in a GitHub Actions workflow?",
        "It is the official GitHub Action that checks out your repository onto the runner VM so the workflow can access and test your code.",
        "Easy",
        "Concept",
        "- uses: actions/checkout@v4",
        "What happens if this step is omitted?"
    ),
    (
        "What is the difference between an issue and a pull request on GitHub?",
        "An Issue is a ticket used to track bugs, feature requests, or tasks. A Pull Request is a proposed code change containing actual Git commits that resolve an issue or add functionality.",
        "Easy",
        "Comparison",
        "",
        "How do you automatically close an issue when a PR is merged?"
    ),
    (
        "How do you automatically close issue #42 when a Pull Request is merged?",
        "Include keywords like `Closes #42`, `Fixes #42`, or `Resolves #42` in the Pull Request description or commit message.",
        "Easy",
        "Practical",
        "Fixes #42",
        "Which keywords are supported by GitHub for closing issues?"
    ),
    (
        "What is GitHub Markdown and what extra features does it offer over standard Markdown?",
        "GitHub Flavored Markdown (GFM) adds task lists `[x]`, tables, syntax-highlighted code blocks, autolinking issue numbers (`#123`), @mentions, and commit SHA links.",
        "Easy",
        "Concept",
        "- [x] Write unit tests\n- [ ] Update documentation",
        "How do you render a checked task list item?"
    ),
    (
        "What is the purpose of `LICENSE` file in an open-source repository?",
        "The license specifies the legal permissions, restrictions, and conditions under which others can use, copy, modify, and distribute your code (e.g. MIT, Apache 2.0, GPL).",
        "Easy",
        "Concept",
        "",
        "If a repository has no license file, is it open source?"
    ),
    (
        "What is the MIT License?",
        "A permissive open-source license that allows anyone to use, modify, and distribute the code for free, including for commercial purposes, with only an attribution requirement.",
        "Easy",
        "Concept",
        "",
        "What is the copyleft alternative to MIT?"
    ),
    (
        "What is the difference between `git diff` and `git diff --cached`?",
        "`git diff` shows unstaged working directory modifications. `git diff --cached` (synonym for `--staged`) shows modifications that are already staged for the next commit.",
        "Easy",
        "Comparison",
        "",
        "When would both commands return empty output?"
    ),
    (
        "What happens if you delete a tracked file manually with `rm` or File Explorer without using `git rm`?",
        "`git status` shows the file as 'deleted' under 'Changes not staged for commit'. Running `git add <file>` or `git rm <file>` will stage the deletion.",
        "Easy",
        "Practical",
        "",
        "How do you restore a file accidentally deleted from the working tree?"
    ),
    (
        "How do you discard a deleted file and restore it from the repository index?",
        "Run `git restore <file>`.",
        "Easy",
        "Practical",
        "git restore deleted-file.js",
        "What was the git checkout syntax for this?"
    ),
    (
        "What is a git alias and how do you create one?",
        "A shortcut for frequently used commands created via `git config --global alias.<shortcut> '<command>'` (e.g. `git config --global alias.co checkout`).",
        "Easy",
        "Practical",
        "git config --global alias.co checkout\ngit config --global alias.br branch\ngit config --global alias.ci commit\ngit config --global alias.st status",
        "Where are Git aliases stored?"
    )
]

print(f"Total Git Part 2 questions created: {len(git_part2)}")

with open('scripts/git_part2.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/git_part2.py\nSecond batch of fresher Git / GitHub interview questions.\n"""\n\n')
    f.write('git_part2_items = [\n')
    for item in git_part2:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/git_part2.py")
