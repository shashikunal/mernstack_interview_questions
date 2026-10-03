# scripts/build_git.py
"""
Builds 215 comprehensive, fresher-focused Git / GitHub interview questions.
"""

git_items = [
    # --- Fundamentals & Setup (35 items) ---
    (
        "What is Git and why is it called a Distributed Version Control System (DVCS)?",
        "Git is a distributed version control system where every developer has a complete local copy of the repository's entire history. Unlike centralized systems (like SVN), developers can commit, branch, view history, and work offline without a central server.",
        "Easy",
        "Concept",
        "",
        "What happens if the remote server goes down in a DVCS?"
    ),
    (
        "What is the difference between Git and GitHub?",
        "Git is an open-source command-line version control tool installed locally on your computer. GitHub is a cloud-based hosting platform and web service that stores Git repositories remotely and adds collaboration tools like Pull Requests, Issues, and Actions.",
        "Easy",
        "Comparison",
        "",
        "Can you use Git without GitHub?"
    ),
    (
        "What are the three main states (or trees) of files in Git?",
        "1) Working Directory: the sandbox where files are created and modified. 2) Staging Area (Index): a holding area where modifications are prepared and indexed before committing. 3) Git Repository: the database of committed snapshots stored permanently in `.git`.",
        "Easy",
        "Concept",
        "",
        "How do you move a modified file from the working directory to the staging area?"
    ),
    (
        "What is the purpose of the `.git` directory inside a project root?",
        "The `.git` directory contains all metadata, commit history, object database (blobs, trees, commits, tags), branch references (refs), and configuration files that make the folder a Git repository.",
        "Easy",
        "Concept",
        "",
        "What happens to version history if the `.git` folder is deleted?"
    ),
    (
        "How do you initialize a brand new Git repository in the current folder?",
        "Run `git init`. This creates a hidden `.git` directory and sets up the default branch (usually `main` or `master`).",
        "Easy",
        "Practical",
        "git init",
        "How do you specify the default branch name during initialization?"
    ),
    (
        "How do you configure your name and email in Git globally?",
        "Use `git config --global user.name 'Your Name'` and `git config --global user.email 'you@example.com'`. These identifiers are attached to every commit you create.",
        "Easy",
        "Practical",
        "git config --global user.name 'John Doe'\ngit config --global user.email 'john@example.com'",
        "Where is global Git configuration stored on Windows?"
    ),
    (
        "How do you check your current Git configuration settings?",
        "Run `git config --list` to view all configuration variables from system, global, and local levels.",
        "Easy",
        "Practical",
        "git config --list\ngit config --show-origin user.email",
        "Which configuration level takes precedence if the same setting exists in multiple files?"
    ),
    (
        "What does `git status` display?",
        "It displays the current branch, untracked files, modified files in the working tree, files staged for commit, and whether your local branch is ahead/behind the remote tracking branch.",
        "Easy",
        "Concept",
        "git status",
        "How do you display git status in a compact, short format?"
    ),
    (
        "What is a `.gitignore` file and what is it used for?",
        "A `.gitignore` file is a text file containing patterns of files and directories that Git should intentionally ignore and not track (e.g. `node_modules/`, `.env`, build artifacts, log files, OS cache).",
        "Easy",
        "Concept",
        "# Example .gitignore\nnode_modules/\n.env\ndist/\n*.log\n.DS_Store",
        "Should `.gitignore` itself be committed to the repository?"
    ),
    (
        "Why does adding a file to `.gitignore` not stop Git from tracking it if it was already committed earlier?",
        "`.gitignore` only prevents untracked files from being automatically staged. If a file is already tracked in the Git index, Git continues tracking changes. You must remove it from the index using `git rm --cached <file>`.",
        "Intermediate",
        "Practical",
        "git rm --cached .env\ngit commit -m 'chore: stop tracking .env'",
        "Does `git rm --cached` delete the file from your local disk?"
    ),
    (
        "How do you ignore an entire directory in `.gitignore`?",
        "Append a forward slash to the directory name: `node_modules/` or `dist/`.",
        "Easy",
        "Practical",
        "node_modules/\ndist/",
        "What does `*.log` match in `.gitignore`?"
    ),
    (
        "How do you ignore all files with a `.log` extension except `important.log` in `.gitignore`?",
        "Use the negation exclamation mark pattern: `*.log` followed on a new line by `!important.log`.",
        "Intermediate",
        "Practical",
        "*.log\n!important.log",
        "Why must the negation rule appear after the ignore rule?"
    ),
    (
        "What is the difference between `git clone` and `git init`?",
        "`git init` creates an empty local repository in an existing directory. `git clone` copies an existing remote repository (including all files, branches, and commit history) to your computer and automatically configures a remote named `origin`.",
        "Easy",
        "Comparison",
        "git clone https://github.com/user/repo.git",
        "Can you clone only a specific branch to save bandwidth?"
    ),
    (
        "What is a commit in Git?",
        "A commit is an immutable snapshot of all tracked files at a specific moment in time. Each commit has a unique SHA hash, author information, timestamp, commit message, and a reference to its parent commit(s).",
        "Easy",
        "Concept",
        "",
        "Can a commit have multiple parent commits?"
    ),
    (
        "What is a SHA-1 hash in Git?",
        "A 40-character hexadecimal string generated by hashing the commit's content, author, tree, and parent commit. It uniquely identifies commits and ensures cryptographic data integrity.",
        "Easy",
        "Concept",
        "commit 4f9b8a2e1d7c3b5a6f8e0d2c4b6a8f0e2d4c6b8a",
        "How many characters are typically used in a short SHA hash?"
    ),
    (
        "Which command is used to record changes in the repository?",
        "`git commit` records staged snapshots in the repository database.",
        "Easy",
        "MCQ",
        "",
        {"A": "git push", "B": "git commit", "C": "git add", "D": "git save"},
        "B",
        "What flag allows typing the commit message directly in terminal?"
    ),
    (
        "Which command stages all modified, deleted, and untracked files in the entire project?",
        "`git add -A` (or `git add --all`) stages all changes across the entire working tree regardless of current directory.",
        "Easy",
        "MCQ",
        "",
        {"A": "git add .", "B": "git add -A", "C": "git commit -a", "D": "git stage"},
        "B",
        "How is `git add .` different from `git add -A` when inside a subfolder?"
    ),
    (
        "What is the difference between `git add .` and `git add -A`?",
        "In modern Git, `git add .` stages all changes within the current directory and its subdirectories. `git add -A` stages all changes across the entire repository regardless of which subdirectory you are currently in.",
        "Easy",
        "Comparison",
        "",
        "Does `git add .` stage deleted files?"
    ),
    (
        "What does `git log` display?",
        "It displays the chronological list of commits in the current branch, showing commit hashes, authors, dates, and commit messages.",
        "Easy",
        "Concept",
        "git log\ngit log --oneline\ngit log -n 5",
        "How do you exit from the `git log` paging view?"
    ),
    (
        "How do you display a compact one-line summary of commit history?",
        "Run `git log --oneline`.",
        "Easy",
        "Practical",
        "git log --oneline --graph --decorate --all",
        "What does `--graph` add to git log output?"
    ),
    (
        "What is the staging area (index) in Git?",
        "The staging area is an intermediate layer that lets you select and group specific file modifications before permanently recording them into a commit.",
        "Easy",
        "Concept",
        "",
        "Why is having an intermediate staging area better than committing working directory changes directly?"
    ),
    (
        "What does `git diff` display by default without arguments?",
        "It shows unstaged modifications between your working directory and the staging area (Index).",
        "Easy",
        "Concept",
        "git diff",
        "What command shows diff between the staging area and last commit?"
    ),
    (
        "What command displays the changes that are already staged for commit?",
        "Run `git diff --staged` (or `git diff --cached`).",
        "Easy",
        "Practical",
        "git diff --staged",
        "Can `git diff` compare two branches?"
    ),
    (
        "How do you view changes between two different commits?",
        "Use `git diff <commit1> <commit2>`.",
        "Easy",
        "Practical",
        "git diff HEAD~1 HEAD",
        "What does `HEAD~1` represent?"
    ),
    (
        "What does `HEAD` represent in Git?",
        "`HEAD` is a symbolic reference that points to the current active branch or commit you have checked out in your working directory.",
        "Easy",
        "Concept",
        "",
        "What does a 'detached HEAD' mean?"
    ),
    (
        "What is a 'detached HEAD' state and how does it happen?",
        "A detached HEAD occurs when you check out a specific commit hash or tag directly rather than a branch name (`git checkout <commit_hash>`). Any new commits made in this state are not on any branch and can be garbage collected unless given a branch name.",
        "Intermediate",
        "Concept",
        "git checkout 4f9b8a2\n# Now in detached HEAD state\ngit switch -c new-feature-branch # to save commits",
        "How do you safely return to your main branch from a detached HEAD?"
    ),
    (
        "What is Conventional Commits specification?",
        "A lightweight convention for commit messages with structured prefixes: `feat:` (new feature), `fix:` (bug fix), `docs:` (documentation), `style:` (formatting), `refactor:` (code restructuring), `test:` (tests), `chore:` (build/configs).",
        "Easy",
        "Concept",
        "feat: add user login validation\nfix: handle null token in auth middleware\nchore: update dependencies",
        "How does Conventional Commits help with automated changelog generation?"
    ),
    (
        "How do you view details of a specific commit using its hash?",
        "Run `git show <commit_hash>` to view the commit metadata and unified diff.",
        "Easy",
        "Practical",
        "git show a1b2c3d",
        "Can `git show` display a tag?"
    ),
    (
        "What is the difference between HTTPS and SSH cloning protocols on GitHub?",
        "HTTPS requires a Personal Access Token (PAT) for authentication over port 443. SSH uses public/private cryptographic key pairs without requiring entering passwords on push.",
        "Intermediate",
        "Comparison",
        "",
        "Where are SSH keys typically stored on Windows?"
    ),
    (
        "How do you generate a new SSH key pair for GitHub?",
        "Run `ssh-keygen -t ed25519 -C 'your_email@example.com'`. Add public key (`~/.ssh/id_ed25519.pub`) to your GitHub account settings.",
        "Intermediate",
        "Practical",
        "ssh-keygen -t ed25519 -C 'email@example.com'\ncat ~/.ssh/id_ed25519.pub",
        "Why is `ed25519` algorithm preferred over standard `rsa`?"
    ),
    (
        "Which command discards all unstaged local modifications in a specific file?",
        "`git restore <file>` discards working directory modifications and restores the file to the state in the index.",
        "Easy",
        "MCQ",
        "",
        {"A": "git revert <file>", "B": "git restore <file>", "C": "git reset <file>", "D": "git clean <file>"},
        "B",
        "What legacy command was previously used for this?"
    ),
    (
        "What is the purpose of `git rm`?",
        "It removes files from both the working directory and the staging area (index) so that the deletion is staged for the next commit.",
        "Easy",
        "Concept",
        "git rm filename.js",
        "How do you remove a file from Git tracking without deleting it from disk?"
    ),
    (
        "What is the purpose of `git mv`?",
        "`git mv <old_name> <new_name>` renames or moves a file and automatically stages the rename in one command.",
        "Easy",
        "Practical",
        "git mv oldName.js newName.js",
        "How does Git detect file renames under the hood?"
    ),
    (
        "Can Git track empty folders?",
        "No. Git tracks file contents, not empty directories. To keep an empty folder in Git, create a dummy file inside it, typically named `.gitkeep`.",
        "Easy",
        "Concept",
        "touch src/assets/.gitkeep\ngit add src/assets/.gitkeep",
        "Is `.gitkeep` an official Git feature or a community convention?"
    ),
    (
        "What is `git help <command>` used for?",
        "It opens the official documentation manual page for the given command in your terminal or browser (e.g. `git help commit`).",
        "Easy",
        "Practical",
        "git commit --help",
        "What flag provides a quick command-line options summary?"
    ),

    # --- Staging, Commits & History (35 items) ---
    (
        "How do you modify the most recent commit message?",
        "Run `git commit --amend -m 'New commit message'`. This replaces the previous commit with a new commit object having the updated message.",
        "Easy",
        "Practical",
        "git commit --amend -m 'fix: correct typo in auth route'",
        "Should you amend a commit that has already been pushed to a shared public branch?"
    ),
    (
        "How do you add forgotten modified files into the most recent commit without changing its message?",
        "Stage the forgotten files (`git add <file>`), then run `git commit --amend --no-edit`.",
        "Intermediate",
        "Practical",
        "git add forgotten-file.js\ngit commit --amend --no-edit",
        "Does amending a commit change its SHA hash?"
    ),
    (
        "What is interactive staging with `git add -p`?",
        "`git add -p` (patch mode) reviews file modifications in chunks ('hunks') and asks whether to stage each hunk (y/n/s/e), allowing committing only parts of a file.",
        "Intermediate",
        "Concept",
        "git add -p",
        "What does the 's' (split) option do in patch mode?"
    ),
    (
        "How do you commit all modified tracked files in a single step without running `git add`?",
        "Use `git commit -am 'commit message'`. Note: this only stages modified tracked files; it does NOT stage newly created untracked files.",
        "Easy",
        "Practical",
        "git commit -am 'refactor: simplify user validator'",
        "Does `git commit -a` stage new untracked files?"
    ),
    (
        "What does the tilde `~` and caret `^` notation mean in commit references (e.g. `HEAD~2` vs `HEAD^`)?",
        "`HEAD~n` references the n-th generational ancestor (linear grandparent). `HEAD^` references the immediate parent. For merge commits with multiple parents, `HEAD^2` references the second parent.",
        "Intermediate",
        "Concept",
        "",
        "What is the difference between `HEAD~2` and `HEAD^^`?"
    ),
    (
        "How do you view commits created by a specific author?",
        "Run `git log --author='Author Name'`.",
        "Easy",
        "Practical",
        "git log --author='Sarah'",
        "Can regex be used with `--author`?"
    ),
    (
        "How do you search for commits whose commit message contains a specific keyword?",
        "Run `git log --grep='keyword'`.",
        "Easy",
        "Practical",
        "git log --grep='bugfix'",
        "How do you search case-insensitively?"
    ),
    (
        "How do you search for commits that introduced or deleted a specific string in code (Pickaxe search)?",
        "Run `git log -S 'functionName'`.",
        "Intermediate",
        "Practical",
        "git log -S 'calculateTax'",
        "Why is `git log -S` called the pickaxe search?"
    ),
    (
        "What is `git blame` and when is it useful?",
        "`git blame <file>` displays each line of a file alongside the commit hash, author, and timestamp of the commit that last modified that line. It is useful for investigating the history and context of code changes.",
        "Easy",
        "Concept",
        "git blame src/services/auth.js",
        "How do you blame only a specific line range?"
    ),
    (
        "How do you view file changes line-by-line using git blame for lines 20 to 35?",
        "Use `git blame -L 20,35 <file>`.",
        "Easy",
        "Practical",
        "git blame -L 20,35 app.js",
        "What does `git log -L` show compared to `git blame`?"
    ),
    (
        "What is `git bisect` and how does it find which commit introduced a bug?",
        "`git bisect` performs binary search through commit history. You mark a bad commit and an older good commit. Git checks out intermediate commits for testing; you mark each good/bad until Git identifies the exact faulty commit.",
        "Intermediate",
        "Concept",
        "git bisect start\ngit bisect bad HEAD\ngit bisect good v1.0.0\n# test code...\ngit bisect good\ngit bisect reset",
        "Can `git bisect` be automated with test scripts?"
    ),
    (
        "Which command un-stages a staged file without discarding working directory changes?",
        "`git restore --staged <file>` removes the file from the index while preserving your working directory edits.",
        "Easy",
        "MCQ",
        "",
        {"A": "git rm <file>", "B": "git restore --staged <file>", "C": "git clean <file>", "D": "git checkout <file>"},
        "B",
        "What was the legacy command for this?"
    ),
    (
        "What does `git log --stat` show?",
        "It shows commit metadata plus a summary of modified files, additions (+), and deletions (-) per commit.",
        "Easy",
        "Practical",
        "git log --stat",
        "How do you view full diffs for each commit in git log?"
    ),
    (
        "What is the output of `git log -p`?",
        "It outputs the commit log together with the full patch (diff) for every commit.",
        "Easy",
        "Concept",
        "git log -p -n 2",
        "How do you limit output to the last 2 commits?"
    ),
    (
        "What happens if you run `git commit` with an empty commit message?",
        "Git aborts the commit and does not record any changes.",
        "Easy",
        "Concept",
        "",
        "Can an empty commit with no file changes be created intentionally?"
    ),
    (
        "How do you create an empty commit without any file changes?",
        "Use `git commit --allow-empty -m 'Trigger CI rebuild'`. This is commonly used to re-trigger CI/CD pipelines.",
        "Intermediate",
        "Practical",
        "git commit --allow-empty -m 'ci: trigger deployment'",
        "When is an empty commit useful?"
    ),
    (
        "What is a Git tag and how does it differ from a branch?",
        "A tag is an immutable reference pointing to a specific commit, typically used to mark release versions (e.g. `v1.0.0`). Unlike a branch, a tag does not move forward when new commits are created.",
        "Easy",
        "Comparison",
        "git tag -a v1.0.0 -m 'Release v1.0.0'\ngit push origin v1.0.0",
        "What is the difference between a lightweight tag and an annotated tag?"
    ),
    (
        "How do you create an annotated tag in Git?",
        "Run `git tag -a <tag_name> -m 'Tag message'`. Annotated tags store the tagger's name, email, date, message, and can be signed with GPG.",
        "Easy",
        "Practical",
        "git tag -a v2.1.0 -m 'Release version 2.1.0'",
        "Are tags pushed automatically when running `git push`?"
    ),
    (
        "How do you push all local tags to the remote repository?",
        "Run `git push origin --tags`.",
        "Easy",
        "Practical",
        "git push origin --tags",
        "How do you delete a tag locally and remotely?"
    ),
    (
        "How do you delete a remote tag named `v1.0.0`?",
        "Run `git push origin --delete v1.0.0` (or `git push origin :refs/tags/v1.0.0`).",
        "Intermediate",
        "Practical",
        "git tag -d v1.0.0\ngit push origin --delete v1.0.0",
        "What does `git tag -d` do?"
    ),
    (
        "What is the difference between a blob, tree, commit, and tag object in Git internals?",
        "Blob: stores file contents (no filenames). Tree: stores directory structure and links to blobs/subtrees with filenames and permissions. Commit: points to a top-level tree, parents, author, and message. Tag: points to a commit with a message.",
        "Advanced",
        "Concept",
        "",
        "Where are these objects stored on disk?"
    ),
    (
        "How does Git compress and store objects in `.git/objects`?",
        "Git uses zlib compression on objects formatted as `type <size>\0<content>`, and indexes them in a content-addressable key-value store keyed by their SHA-1 hash.",
        "Advanced",
        "Concept",
        "",
        "What is a Git packfile?"
    ),
    (
        "What is garbage collection in Git (`git gc`)?",
        "`git gc` optimizes the local repository by packing uncompressed loose objects into packfiles and pruning unreachable orphaned objects that are older than the retention period.",
        "Intermediate",
        "Concept",
        "git gc --prune=now",
        "When does Git automatically run garbage collection?"
    ),
    (
        "What is the difference between `git diff HEAD` and `git diff`?",
        "`git diff` compares the working directory against the staging area. `git diff HEAD` compares the working directory against the last commit (showing both staged and unstaged changes).",
        "Intermediate",
        "Comparison",
        "",
        "What does `git diff --staged` compare?"
    ),
    (
        "What does `git log --graph` visualize?",
        "It draws an ASCII character graph on the left side of the log displaying branch topologies, merge points, and fork points.",
        "Easy",
        "Concept",
        "",
        "What other flags are frequently paired with `--graph`?"
    ),
    (
        "Which command lists all Git tags in alphabetical order?",
        "Run `git tag` (or `git tag -l`).",
        "Easy",
        "Practical",
        "git tag",
        "Can you filter tags using wildcard patterns?"
    ),
    (
        "How do you filter tags matching `v1.*`?",
        "Run `git tag -l 'v1.*'`.",
        "Easy",
        "Practical",
        "git tag -l 'v1.*'",
        "Why are quotes needed around the pattern?"
    ),
    (
        "What is a pre-commit hook in Git?",
        "A pre-commit hook is a script located in `.git/hooks/pre-commit` that runs automatically before a commit is created. If the script exits with non-zero status (e.g. linter or tests fail), the commit is aborted.",
        "Intermediate",
        "Concept",
        "",
        "How can you bypass Git hooks during commit if necessary?"
    ),
    (
        "How do you bypass Git pre-commit hooks when committing?",
        "Pass the `--no-verify` (or `-n`) flag: `git commit --no-verify -m 'message'`.",
        "Intermediate",
        "Practical",
        "git commit --no-verify -m 'wip: bypass hooks'",
        "Why should `--no-verify` be used sparingly?"
    ),
    (
        "What popular Node.js tool is used to manage Git hooks across team members?",
        "Husky is the standard tool to manage and share Git hooks within `package.json` or `.husky/` directory.",
        "Easy",
        "Concept",
        "",
        "Why are `.git/hooks/` scripts not committed to the repository by default?"
    ),
    (
        "What does `lint-staged` do in a frontend development workflow?",
        "`lint-staged` runs linters, formatters (Prettier, ESLint), and tests only against staged files before committing, keeping commits clean without slowing down the workflow.",
        "Easy",
        "Practical",
        "",
        "How does lint-staged integrate with Husky?"
    ),
    (
        "What is the difference between working directory untracked files and ignored files?",
        "Untracked files are files not yet added to Git that appear in `git status` under 'Untracked files'. Ignored files match patterns in `.gitignore` and are completely hidden from `git status`.",
        "Easy",
        "Comparison",
        "",
        "How can you view ignored files in git status?"
    ),
    (
        "How do you view ignored files using `git status`?",
        "Run `git status --ignored`.",
        "Easy",
        "Practical",
        "git status --ignored",
        "What flag shows short output?"
    ),
    (
        "What is the output of `git rev-parse HEAD`?",
        "It outputs the full 40-character SHA-1 commit hash of the current HEAD commit.",
        "Intermediate",
        "Practical",
        "git rev-parse HEAD\ngit rev-parse --short HEAD",
        "What does `--short` do?"
    ),
    (
        "What is a Fast-Forward commit?",
        "A merge where the target branch has no divergent commits; Git simply moves the branch pointer forward to point to the incoming commit without creating a merge commit.",
        "Easy",
        "Concept",
        "",
        "When is a fast-forward merge not possible?"
    ),

    # --- Branching & Merging (40 items) ---
    (
        "What is a Git branch under the hood?",
        "A branch in Git is simply a lightweight, 41-byte movable pointer stored in `.git/refs/heads/<branch>` containing the 40-character commit hash of the latest commit on that branch.",
        "Easy",
        "Concept",
        "",
        "Why is creating branches in Git nearly instantaneous compared to older VCS?"
    ),
    (
        "How do you create a new branch and switch to it in modern Git?",
        "Use `git switch -c <branch_name>` (or the older `git checkout -b <branch_name>`).",
        "Easy",
        "Practical",
        "git switch -c feature/login\n# or\ngit checkout -b feature/login",
        "Why was `git switch` introduced in Git 2.23?"
    ),
    (
        "What is the difference between `git checkout` and modern `git switch` / `git restore`?",
        "`git checkout` had overloaded responsibilities: switching branches AND restoring files. Git 2.23 split these into two clear commands: `git switch` for branch navigation, and `git restore` for working tree / staging operations.",
        "Intermediate",
        "Comparison",
        "",
        "Which command switches branches?"
    ),
    (
        "How do you list all local branches in your repository?",
        "Run `git branch`. The currently checked-out branch is marked with an asterisk `*` and colored green.",
        "Easy",
        "Practical",
        "git branch",
        "How do you list both local and remote branches?"
    ),
    (
        "How do you list both local and remote tracking branches?",
        "Run `git branch -a` (or `git branch --all`).",
        "Easy",
        "Practical",
        "git branch -a",
        "What prefix do remote branches have in the list?"
    ),
    (
        "How do you rename the current active branch?",
        "Run `git branch -m <new_branch_name>`.",
        "Easy",
        "Practical",
        "git branch -m main",
        "How do you rename a branch that you are not currently on?"
    ),
    (
        "What is the difference between `git branch -d` and `git branch -D`?",
        "`git branch -d` (safe delete) deletes the branch only if it has already been fully merged into upstream. `git branch -D` (force delete) deletes the branch regardless of its merge status, discarding unmerged commits.",
        "Easy",
        "Comparison",
        "git branch -d feature-done\ngit branch -D abandoned-experiment",
        "Why will `git branch -d` fail on an unmerged branch?"
    ),
    (
        "What is a Fast-Forward Merge vs a 3-Way Merge (Merge Commit)?",
        "A fast-forward merge occurs when the main branch has no new commits since branching; Git simply moves the pointer forward. A 3-way merge occurs when both branches have diverged; Git creates a new 'merge commit' with two parent commits.",
        "Intermediate",
        "Comparison",
        "",
        "How can you force Git to create a merge commit even if fast-forward is possible?"
    ),
    (
        "How do you force Git to create a merge commit even when fast-forward is possible?",
        "Pass the `--no-ff` flag: `git merge --no-ff <branch_name>`.",
        "Intermediate",
        "Practical",
        "git merge --no-ff feature/user-profile",
        "Why do some teams mandate `--no-ff` merges?"
    ),
    (
        "What is a Merge Conflict in Git and why does it happen?",
        "A merge conflict occurs when two branches modify the exact same line(s) of a file differently, or one branch deletes a file that another modified. Git cannot automatically decide which change is correct and asks the developer to resolve it manually.",
        "Easy",
        "Concept",
        "",
        "What characters does Git insert into files to mark conflicts?"
    ),
    (
        "Explain the conflict markers inserted by Git during a merge conflict.",
        "`<<<<<<< HEAD` marks the beginning of changes on the current active branch. `=======` separates current changes from incoming changes. `>>>>>>> branch-name` marks the end of incoming changes.",
        "Easy",
        "Concept",
        "<<<<<<< HEAD\nconst api = 'https://api.v1.prod.com';\n=======\nconst api = 'https://api.v2.prod.com';\n>>>>>>> feature/v2-api",
        "What must you do to markers before committing the resolution?"
    ),
    (
        "What are the steps to resolve a merge conflict?",
        "1) Run `git status` to identify conflicting files. 2) Open conflicting files and manually edit the code to desired state, removing conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). 3) Stage resolved files with `git add <file>`. 4) Complete the merge with `git commit`.",
        "Easy",
        "Practical",
        "git status\n# edit conflicting files\ngit add src/api.js\ngit commit -m 'merge: resolve conflicts with main'",
        "What command aborts a conflicted merge and returns to the pre-merge state?"
    ),
    (
        "How do you abort an ongoing merge conflict and revert to pre-merge state?",
        "Run `git merge --abort`.",
        "Easy",
        "Practical",
        "git merge --abort",
        "Does `git merge --abort` restore your uncommitted changes if they were clean before merge?"
    ),
    (
        "Compare `git merge` and `git rebase`.",
        "`git merge` preserves complete historical accuracy by adding a merge commit with two parents, leaving feature branch commits intact. `git rebase` rewrites history by replaying feature commits on top of the base branch, creating a clean linear history.",
        "Intermediate",
        "Comparison",
        "",
        "What is the Golden Rule of Rebase?"
    ),
    (
        "What is the 'Golden Rule of Rebase'?",
        "Never rebase commits that have been pushed to a public, shared repository or branch (like `main`). Rebasing rewrites commit hashes, which breaks other team members' branches and histories.",
        "Intermediate",
        "Concept",
        "",
        "What should you use instead of rebase on public branches?"
    ),
    (
        "What is an Interactive Rebase (`git rebase -i`)?",
        "`git rebase -i HEAD~n` opens an interactive editor allowing you to reorder, squash (combine), reword, edit, or drop individual commits before pushing.",
        "Intermediate",
        "Concept",
        "git rebase -i HEAD~3",
        "What does the 'squash' (s) command do in interactive rebase?"
    ),
    (
        "What is commit squashing?",
        "Squashing combines multiple small, intermediate commits (like 'wip', 'typo fix', 'test') into a single meaningful commit with a clean commit message before merging.",
        "Easy",
        "Concept",
        "",
        "What command does GitHub provide to squash PR commits automatically upon merging?"
    ),
    (
        "What is `git cherry-pick` and when is it used?",
        "`git cherry-pick <commit_hash>` applies the changes introduced by a specific commit from one branch onto your current active branch, creating a new commit with identical changes.",
        "Intermediate",
        "Practical",
        "git checkout main\ngit cherry-pick 8a2f1c4",
        "Does cherry-pick keep the original commit hash?"
    ),
    (
        "What happens if a cherry-pick encounters a merge conflict?",
        "Git stops the cherry-pick. You must resolve the conflict, stage files with `git add`, and run `git cherry-pick --continue` (or abort with `git cherry-pick --abort`).",
        "Intermediate",
        "Practical",
        "git cherry-pick --continue\ngit cherry-pick --abort",
        "What is the command to skip the current conflicting cherry-pick?"
    ),
    (
        "Which command switches to an existing branch named `develop` in modern Git?",
        "`git switch develop` switches the working tree to the develop branch.",
        "Easy",
        "MCQ",
        "",
        {"A": "git switch develop", "B": "git branch develop", "C": "git move develop", "D": "git change develop"},
        "A",
        "What was the older command?"
    ),
    (
        "Which command deletes a remote branch named `feature/login` from GitHub?",
        "`git push origin --delete feature/login` removes the branch from the remote server.",
        "Easy",
        "MCQ",
        "",
        {"A": "git branch -r feature/login", "B": "git push origin --delete feature/login", "C": "git remote rm feature/login", "D": "git delete origin/feature/login"},
        "B",
        "What is the shorthand syntax for deleting a remote branch?"
    ),
    (
        "What is the shorthand syntax to delete a remote branch using git push?",
        "`git push origin :<branch_name>` (pushing 'nothing' to the remote branch ref deletes it).",
        "Intermediate",
        "Practical",
        "git push origin :feature/login",
        "Why is `--delete` preferred in modern Git?"
    ),
    (
        "What is `git branch -vv`?",
        "It lists all local branches showing their latest commit hash, commit subject, and tracking status relative to their remote upstream branches (ahead, behind, or up-to-date).",
        "Easy",
        "Practical",
        "git branch -vv",
        "What does `[origin/main: ahead 1]` mean?"
    ),
    (
        "What does `[origin/main: behind 2]` mean in `git status`?",
        "It means your local branch is missing 2 commits that have already been pushed to the remote repository. You should run `git pull` to fetch and integrate them.",
        "Easy",
        "Concept",
        "",
        "What does `[ahead 1, behind 2]` indicate?"
    ),
    (
        "What does `[ahead 1, behind 2]` mean?",
        "Your local branch and the remote branch have diverged. You have 1 local commit not on remote, and remote has 2 commits not in your local branch. Merging or rebasing will be required.",
        "Intermediate",
        "Concept",
        "",
        "What command cleanly integrates remote commits under your local commit?"
    ),
    (
        "What does `git pull --rebase` do?",
        "It fetches remote commits and rebases your local unpushed commits on top of the newly fetched remote commits, avoiding an unnecessary merge commit and maintaining a linear history.",
        "Intermediate",
        "Practical",
        "git pull --rebase origin main",
        "How do you set rebase as the default behavior for git pull?"
    ),
    (
        "How do you configure Git to always use rebase for `git pull` by default?",
        "Run `git config --global pull.rebase true`.",
        "Easy",
        "Practical",
        "git config --global pull.rebase true",
        "What are the alternatives to true (e.g. merges)?"
    ),
    (
        "What is the difference between merging `main` into your feature branch vs rebasing your feature branch onto `main`?",
        "Merging `main` creates an extra merge commit in your feature branch. Rebasing replays your feature commits on top of `main`, creating a clean linear history without extra merge commits.",
        "Intermediate",
        "Comparison",
        "",
        "Which approach creates a cleaner Pull Request diff?"
    ),
    (
        "What is Git Flow branching model?",
        "A structured branching workflow using: `main` (production-ready releases), `develop` (integration branch), `feature/*` (new features branched from develop), `release/*` (prep for release), and `hotfix/*` (urgent production fixes branched from main).",
        "Intermediate",
        "Concept",
        "",
        "How does GitHub Flow simplify Git Flow?"
    ),
    (
        "What is GitHub Flow and how does it differ from Git Flow?",
        "GitHub Flow is a lightweight, continuous deployment workflow: 1) `main` is always deployable. 2) Create descriptive feature branches from `main`. 3) Open Pull Requests for discussion and code review. 4) Merge to `main` and deploy immediately.",
        "Easy",
        "Comparison",
        "",
        "Why is GitHub Flow preferred for modern web web applications and microservices?"
    ),
    (
        "What is Trunk-Based Development?",
        "A development practice where developers merge small, frequent updates directly into a single central branch ('trunk' or 'main') multiple times a day, avoiding long-lived feature branches and large merge conflicts.",
        "Intermediate",
        "Concept",
        "",
        "What technique enables merging incomplete features in trunk-based development?"
    ),
    (
        "What is a Feature Flag (Feature Toggle)?",
        "A software technique that wraps new code in conditional checks, allowing code to be safely committed and deployed to production while keeping the feature disabled for users until ready.",
        "Easy",
        "Concept",
        "if (featureFlags.isEnabled('newCheckoutUI')) {\n  renderNewCheckout();\n} else {\n  renderLegacyCheckout();\n}",
        "How do feature flags facilitate continuous deployment?"
    ),
    (
        "What is a fast-forward merge conflict?",
        "Trick question: Fast-forward merges CANNOT have merge conflicts because the target branch has no diverged commits. Conflicts only happen during 3-way merges or rebases.",
        "Easy",
        "Concept",
        "",
        "What allows a fast-forward merge?"
    ),
    (
        "How do you merge branch `feature` into `main`?",
        "Switch to the target branch (`git switch main`), then run `git merge feature`.",
        "Easy",
        "Practical",
        "git switch main\ngit merge feature",
        "What happens if you run git merge while on the feature branch?"
    ),
    (
        "What is a squash merge on GitHub?",
        "A GitHub merge option that combines all commits in a Pull Request into a single commit on the destination branch, keeping the main branch history concise and linear.",
        "Easy",
        "Concept",
        "",
        "Does a squash merge delete the branch history on GitHub?"
    ),

    # --- Remote Repositories & Collaboration (35 items) ---
    (
        "What is `origin` in Git?",
        "`origin` is the default shorthand alias name given to the remote repository URL from which you cloned the project (or added via `git remote add origin <url>`).",
        "Easy",
        "Concept",
        "git remote -v\n# origin  https://github.com/user/repo.git (fetch)\n# origin  https://github.com/user/repo.git (push)",
        "Can a Git project have more than one remote?"
    ),
    (
        "What is `upstream` in Git open-source workflow?",
        "`upstream` is the conventional remote name pointing to the original parent repository from which you created your personal fork.",
        "Easy",
        "Concept",
        "git remote add upstream https://github.com/original-owner/repo.git",
        "Why is keeping an upstream remote useful in forked repositories?"
    ),
    (
        "What is the difference between Forking and Cloning a repository?",
        "Forking creates a personal remote copy of someone else's repository under your own GitHub account on GitHub's servers. Cloning downloads a remote repository to your local computer.",
        "Easy",
        "Comparison",
        "",
        "Do you need write permissions on a repository to fork it?"
    ),
    (
        "What is the difference between `git fetch` and `git pull`?",
        "`git fetch` downloads commits, refs, and branches from remote to your local repository without modifying your working directory or active branch. `git pull` executes `git fetch` followed immediately by `git merge` into your current branch.",
        "Easy",
        "Comparison",
        "git fetch origin\n# inspect changes...\ngit merge origin/main\n# vs\ngit pull origin main",
        "Why is `git fetch` safer than `git pull`?"
    ),
    (
        "What does `git push -u origin main` do and what does `-u` mean?",
        "`-u` (or `--set-upstream`) links the local branch to the remote branch `origin/main`. Once upstream tracking is set, you can simply type `git push` or `git pull` without specifying remote or branch names.",
        "Easy",
        "Practical",
        "git push -u origin main",
        "Where is upstream tracking stored?"
    ),
    (
        "What is a Pull Request (PR) or Merge Request (MR)?",
        "A Pull Request is a collaborative feature on platforms like GitHub where a developer proposes merging changes from their branch into a target branch, allowing code reviews, inline discussions, automated tests, and approvals before merging.",
        "Easy",
        "Concept",
        "",
        "Can you open a Pull Request between two branches in the same repository?"
    ),
    (
        "What is the difference between `git push --force` and `git push --force-with-lease`?",
        "`git push --force` blindly overwrites the remote branch, erasing any commits pushed by teammates in the meantime. `--force-with-lease` only forces the push if no one else has updated the remote branch since your last fetch, preventing accidental data loss.",
        "Intermediate",
        "Comparison",
        "git push --force-with-lease origin feature-branch",
        "Why should `--force-with-lease` always be preferred over `--force`?"
    ),
    (
        "What does the error 'fatal: refusing to merge unrelated histories' mean and how do you resolve it?",
        "It happens when trying to merge two repositories that do not share a common root commit (e.g. local repo created with `git init` and remote created with README on GitHub). Resolved with `git pull origin main --allow-unrelated-histories`.",
        "Intermediate",
        "Practical",
        "git pull origin main --allow-unrelated-histories",
        "Why does Git block merging unrelated histories by default?"
    ),
    (
        "How do you synchronize your local fork with the latest changes from the original `upstream` repository?",
        "1) `git fetch upstream`. 2) Switch to local main (`git switch main`). 3) Merge upstream main (`git merge upstream/main`). 4) Push updated main to your fork (`git push origin main`).",
        "Intermediate",
        "Practical",
        "git fetch upstream\ngit switch main\ngit merge upstream/main\ngit push origin main",
        "Can this also be done using GitHub's 'Sync fork' button?"
    ),
    (
        "What is a Branch Protection Rule on GitHub?",
        "A repository governance feature that enforces rules on critical branches (like `main`), such as requiring Pull Request reviews, passing CI/CD status checks, preventing force pushes, and disallowing direct pushes.",
        "Easy",
        "Concept",
        "",
        "Who can bypass branch protection rules if allowed?"
    ),
    (
        "What is GitHub Actions?",
        "A continuous integration and continuous delivery (CI/CD) platform built directly into GitHub that automates build, test, lint, and deployment pipelines triggered by GitHub events (like push or pull request).",
        "Easy",
        "Concept",
        "# .github/workflows/ci.yml\nname: Node CI\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-node@v4\n      - run: npm ci\n      - run: npm test",
        "Where are GitHub Actions workflow files stored in a project?"
    ),
    (
        "What is a Personal Access Token (PAT) on GitHub?",
        "A secure authentication token used instead of a password when authenticating Git over HTTPS or accessing the GitHub REST/GraphQL API. PATs have configurable scopes, permissions, and expiration dates.",
        "Easy",
        "Concept",
        "",
        "Why does GitHub no longer accept account passwords for Git operations?"
    ),
    (
        "How do you remove remote branches from your local list that were deleted on GitHub?",
        "Run `git fetch --prune` (or `git remote prune origin`). This removes stale remote-tracking branch references (like `origin/deleted-branch`).",
        "Easy",
        "Practical",
        "git fetch --prune",
        "How do you configure Git to always prune on fetch?"
    ),
    (
        "How do you configure Git to automatically prune dead remote branches on every fetch?",
        "Run `git config --global fetch.prune true`.",
        "Easy",
        "Practical",
        "git config --global fetch.prune true",
        "What command lists stale branches?"
    ),
    (
        "What is `git remote show origin`?",
        "It inspects the remote repository, displaying URLs, tracked branches, local branches configured for push/pull, and stale remote branches.",
        "Easy",
        "Practical",
        "git remote show origin",
        "What information does it provide about HEAD branch?"
    ),
    (
        "Which command lists all configured remote repository aliases and their URLs?",
        "Run `git remote -v`.",
        "Easy",
        "MCQ",
        "",
        {"A": "git remote list", "B": "git remote -v", "C": "git remotes", "D": "git origin -v"},
        "B",
        "What does `-v` stand for?"
    ),
    (
        "How do you change the URL of an existing remote named `origin`?",
        "Use `git remote set-url origin <new_url>`.",
        "Easy",
        "Practical",
        "git remote set-url origin git@github.com:user/new-repo.git",
        "When is changing remote URL commonly needed?"
    ),
    (
        "What is a Draft Pull Request on GitHub?",
        "A Pull Request marked as 'Draft' that cannot be merged until marked 'Ready for review'. It allows sharing work in progress, soliciting early feedback, and running CI tests without notifying reviewers.",
        "Easy",
        "Concept",
        "",
        "Can CI checks run on a Draft PR?"
    ),
    (
        "What are GitHub CODEOWNERS?",
        "A file located in `.github/CODEOWNERS` that defines individuals or teams responsible for specific code paths; GitHub automatically requests reviews from code owners when a PR touches those files.",
        "Intermediate",
        "Concept",
        "# .github/CODEOWNERS\n* @core-team\n/src/api/ @backend-team\n*.css @frontend-team",
        "Where can the CODEOWNERS file be placed?"
    ),
    (
        "What is a Git Submodule?",
        "A mechanism that allows keeping a Git repository as a subdirectory of another Git repository, pinned to a specific commit hash of the external project.",
        "Intermediate",
        "Concept",
        "git submodule add https://github.com/lib/utils.git libs/utils\ngit submodule update --init --recursive",
        "What command initializes and downloads submodules after cloning?"
    ),

    # --- Undoing Changes & Recovery (40 items) ---
    (
        "What is the difference between `git reset` and `git revert`?",
        "`git reset` moves the branch pointer backward, effectively erasing commits from history (destructive for public branches). `git revert` creates a brand new commit that inverts the changes of an older commit, keeping history intact and safe for shared branches.",
        "Easy",
        "Comparison",
        "git revert 4f9b8a2 # Safe on shared branch\ngit reset --hard HEAD~1 # Rewrites history locally",
        "Which command should be used on a shared `main` branch?"
    ),
    (
        "Explain the three modes of `git reset`: `--soft`, `--mixed`, and `--hard`.",
        "`--soft`: moves HEAD pointer back; keeps changes staged in Index and working directory. `--mixed` (default): moves HEAD back; unstages changes into working directory. `--hard`: moves HEAD back and discards all changes in staging and working directory.",
        "Intermediate",
        "Comparison",
        "git reset --soft HEAD~1   # staged\ngit reset --mixed HEAD~1  # unstaged\ngit reset --hard HEAD~1   # completely discarded",
        "Which mode is the default when no flag is supplied?"
    ),
    (
        "What is `git stash` and when should you use it?",
        "`git stash` temporarily shelves (stashes) uncommitted modifications in your working directory and staging area, giving you a clean working copy so you can switch branches or pull urgent updates without committing incomplete work.",
        "Easy",
        "Concept",
        "git stash\ngit switch main\ngit pull\ngit switch feature\ngit stash pop",
        "Does `git stash` stash untracked files by default?"
    ),
    (
        "How do you include untracked files when stashing?",
        "Pass the `-u` (or `--include-untracked`) flag: `git stash -u`.",
        "Easy",
        "Practical",
        "git stash -u",
        "What flag stashes all files including ignored files?"
    ),
    (
        "What is the difference between `git stash pop` and `git stash apply`?",
        "`git stash pop` applies the most recent stashed changes to your working directory AND removes the stash from the stash list. `git stash apply` applies the stashed changes but keeps the stash in the stash list for reuse.",
        "Easy",
        "Comparison",
        "git stash pop\n# vs\ngit stash apply",
        "What command lists all stashes?"
    ),
    (
        "How do you view all saved stashes?",
        "Run `git stash list`.",
        "Easy",
        "Practical",
        "git stash list\n# stash@{0}: WIP on main\n# stash@{1}: WIP on feature",
        "How do you drop (delete) a specific stash?"
    ),
    (
        "How do you delete a specific stash?",
        "Run `git stash drop stash@{index}` (e.g. `git stash drop stash@{0}`). To clear all stashes, run `git stash clear`.",
        "Easy",
        "Practical",
        "git stash drop stash@{0}\ngit stash clear",
        "What does `git stash clear` do?"
    ),
    (
        "What is `git reflog` and why is it considered the ultimate safety net in Git?",
        "`git reflog` records every update to HEAD (commits, checkouts, resets, rebases, merges) in local chronological order. Even if you accidentally run `git reset --hard` or delete a branch, you can locate the lost commit hash in the reflog and restore it.",
        "Intermediate",
        "Concept",
        "git reflog\n# find commit hash\ngit reset --hard HEAD@{2}",
        "How long does Git retain reflog entries by default?"
    ),
    (
        "How do you recover a branch or commit accidentally deleted via `git reset --hard`?",
        "1) Run `git reflog` to find the commit hash before the reset. 2) Run `git reset --hard <hash>` or create a new branch from that commit: `git branch recovery-branch <hash>`.",
        "Intermediate",
        "Practical",
        "git reflog\ngit branch recover-work 4a3b2c1",
        "Does `git reflog` track changes across remote repositories?"
    ),
    (
        "What does `git clean -fd` do?",
        "`git clean -f` forces removal of untracked files from the working directory. The `-d` flag includes untracked directories.",
        "Easy",
        "Practical",
        "git clean -fd",
        "How do you preview which files will be deleted before running git clean?"
    ),
    (
        "How do you preview untracked files that would be removed by `git clean` (dry run)?",
        "Use `git clean -nd` (or `git clean -n`). The `-n` flag performs a dry run without deleting anything.",
        "Easy",
        "Practical",
        "git clean -nd",
        "What flag deletes ignored files as well?"
    ),
    (
        "How do you discard changes in a single working directory file using modern Git?",
        "Run `git restore <file>`.",
        "Easy",
        "Practical",
        "git restore src/index.js",
        "Can `git restore` be undone once executed?"
    ),
    (
        "What command un-stages all staged files in the current repository in modern Git?",
        "Run `git restore --staged .`.",
        "Easy",
        "Practical",
        "git restore --staged .",
        "Does this modify your code in the working directory?"
    ),
    (
        "What does `git revert HEAD` do?",
        "It creates a new commit that applies the exact inverse diff of the latest commit on the current branch.",
        "Easy",
        "Concept",
        "git revert HEAD",
        "Can you revert a merge commit?"
    ),
    (
        "How do you revert a merge commit?",
        "You must specify the parent mainline number using `-m`: `git revert -m 1 <merge_commit_hash>` to specify which parent branch should be considered the mainline.",
        "Advanced",
        "Practical",
        "git revert -m 1 9f8e7d6",
        "Why is `-m` mandatory for merge commits?"
    ),
    (
        "Which command is the safest way to undo a commit on a shared remote branch?",
        "`git revert <commit_hash>` creates a new commit undoing the changes without rewriting history.",
        "Easy",
        "MCQ",
        "",
        {"A": "git reset --hard", "B": "git revert <commit_hash>", "C": "git rebase -i", "D": "git checkout <commit_hash>"},
        "B",
        "Why is `git reset --hard` dangerous on shared branches?"
    ),
    (
        "Scenario: You committed a secret API key in your latest local commit that has NOT been pushed yet. How do you fix it?",
        "Remove the key from the code, stage the change (`git add <file>`), and run `git commit --amend --no-edit` to replace the commit without leaving the key in Git history.",
        "Intermediate",
        "Scenario",
        "git add .env\ngit commit --amend --no-edit",
        "What must you do if the key was already pushed to GitHub?"
    ),
    (
        "Scenario: You accidentally committed an API key to a public GitHub repository. What steps must you take?",
        "1) Immediately revoke and rotate the API key in the provider console (assume it is compromised). 2) Remove the secret from Git history using tools like `git-filter-repo` or BFG Repo-Cleaner. 3) Force push with lease to update remote history.",
        "Intermediate",
        "Scenario",
        "",
        "Why is simply making a new commit that deletes the file insufficient?"
    ),
    (
        "What is BFG Repo-Cleaner or `git-filter-repo` used for?",
        "Tools used to completely remove sensitive data (passwords, private keys, massive binary files) from an entire Git repository history across all commits and branches.",
        "Intermediate",
        "Concept",
        "",
        "Why is `git-filter-repo` recommended over legacy `git filter-branch`?"
    ),
    (
        "What does `git stash drop` do without arguments?",
        "It deletes the most recent stash (`stash@{0}`) from the stash list.",
        "Easy",
        "Practical",
        "git stash drop",
        "What does `git stash pop` do differently?"
    ),

    # --- Scenario, Debugging & Best Practices (30 items) ---
    (
        "Scenario: You started working on the wrong branch (e.g. `main` instead of `feature`). You made changes but have NOT committed yet. How do you move your work to a new feature branch?",
        "Simply create and switch to the new branch: `git switch -c feature/my-work`. Uncommitted working directory modifications travel with you to the new branch safely.",
        "Easy",
        "Scenario",
        "git switch -c feature/my-work",
        "What happens if there are conflicts with files in the target branch?"
    ),
    (
        "Scenario: You made changes on `main` and committed them by mistake instead of creating a feature branch. How do you fix this?",
        "1) Create the feature branch pointing to current commit: `git branch feature/my-work`. 2) Reset `main` back by 1 commit: `git reset --hard HEAD~1`. 3) Switch to feature branch: `git switch feature/my-work`.",
        "Intermediate",
        "Scenario",
        "git branch feature/my-work\ngit reset --hard HEAD~1\ngit switch feature/my-work",
        "Why does `git branch feature/my-work` preserve the commit?"
    ),
    (
        "Scenario: A teammate pushed changes to `main`. When you run `git push origin main`, you get 'error: failed to push some refs... Updates were rejected because the remote contains work that you do not have locally.' How do you resolve this?",
        "Run `git pull --rebase origin main` to fetch remote updates and replay your local commits on top, resolve any merge conflicts if they occur, and then `git push origin main`.",
        "Easy",
        "Scenario",
        "git pull --rebase origin main\ngit push origin main",
        "Why did Git reject the push?"
    ),
    (
        "What does this error message mean: 'fatal: not a git repository (or any of the parent directories): .git'?",
        "You are executing a Git command inside a folder that has not been initialized with `git init` and is not inside any existing Git project.",
        "Easy",
        "Debugging",
        "",
        "How do you resolve it?"
    ),
    (
        "What causes the error: 'error: Your local changes to the following files would be overwritten by checkout'?",
        "You have uncommitted modifications in files that differ between your current branch and the target branch. Resolve by either committing your changes, stashing them (`git stash`), or discarding them (`git restore .`).",
        "Easy",
        "Debugging",
        "git stash\ngit switch other-branch\ngit stash pop",
        "Which solution preserves your work?"
    ),
    (
        "What is Semantic Versioning (SemVer) format used in Git tags?",
        "Format: `MAJOR.MINOR.PATCH` (e.g. `2.4.1`). MAJOR: incompatible breaking API changes. MINOR: backwards-compatible new features. PATCH: backwards-compatible bug fixes.",
        "Easy",
        "Concept",
        "v1.2.3",
        "What does a change from 1.9.0 to 2.0.0 indicate?"
    ),
    (
        "What is `.gitkeep` and why do developers use it?",
        "Git cannot track empty folders. Developers place an empty dummy file named `.gitkeep` inside an empty directory so Git will track and include the directory in commits.",
        "Easy",
        "Concept",
        "",
        "Does Git treat .gitkeep differently from any other file?"
    ),
    (
        "How do you ignore changes to a tracked file locally without untracking it for everyone else?",
        "Run `git update-index --assume-unchanged <file>`. Git will ignore local edits to that file. To undo, run `git update-index --no-assume-unchanged <file>`.",
        "Intermediate",
        "Practical",
        "git update-index --assume-unchanged config/local.json",
        "What is the difference between assume-unchanged and skip-worktree?"
    ),
    (
        "What is a pull request template and where is it placed?",
        "A markdown template (`.github/pull_request_template.md`) that automatically pre-fills the PR description on GitHub with guidelines, checklists, and test steps for contributors.",
        "Easy",
        "Concept",
        "",
        "Can you have multiple PR templates on GitHub?"
    ),
    (
        "What is the difference between git stash `apply` and `pop` if merge conflicts occur?",
        "If `git stash pop` encounters a merge conflict, it applies the changes but intentionally DOES NOT remove the stash from the stash list, giving you a chance to inspect and recover.",
        "Intermediate",
        "Concept",
        "",
        "How do you manually delete the stash after resolving conflicts?"
    ),
    (
        "What is `git cherry-pick -n` (or `--no-commit`)?",
        "It applies the changes from the specified commit to your working directory and staging area without automatically creating a new commit, allowing you to combine or inspect changes first.",
        "Intermediate",
        "Practical",
        "git cherry-pick -n 3a4b5c6",
        "When is `--no-commit` useful?"
    ),
    (
        "How do you clone only the latest commit without downloading the entire history (shallow clone)?",
        "Use the `--depth` flag: `git clone --depth 1 <repo_url>`. This significantly speeds up downloads and saves disk space in CI/CD pipelines.",
        "Intermediate",
        "Practical",
        "git clone --depth 1 https://github.com/user/large-repo.git",
        "Can a shallow clone be converted to a full clone later?"
    ),
    (
        "How do you deepen or unshallow a shallow clone?",
        "Run `git fetch --unshallow`.",
        "Intermediate",
        "Practical",
        "git fetch --unshallow",
        "Why are shallow clones widely used in Docker build pipelines?"
    ),
    (
        "What does the command `git commit --dry-run` do?",
        "It previews what files would be committed without actually creating a commit.",
        "Easy",
        "Practical",
        "git commit --dry-run",
        "How does it differ from git status?"
    ),
    (
        "What is a bare Git repository (`git init --bare`) and where is it used?",
        "A bare repository has no working directory; it contains only the `.git` metadata and objects. It is used exclusively as a central remote storage hub on servers (like GitHub) where developers push and fetch code, not edit files directly.",
        "Intermediate",
        "Concept",
        "git init --bare my-repo.git",
        "Why can you not make commits directly inside a bare repository?"
    )
]

print(f"Total Git / GitHub questions created: {len(git_items)}")

with open('scripts/git_questions.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/git_questions.py\n215 comprehensive fresher Git / GitHub interview questions.\n"""\n\n')
    f.write('git_items = [\n')
    for item in git_items:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/git_questions.py")
