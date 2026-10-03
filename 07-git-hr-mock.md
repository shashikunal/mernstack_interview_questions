# 07 - Git + HR + 2 Mock Rounds

## Git - Top 12 Scenarios (say commands)

1. **Daily flow?** `git pull --rebase origin main` -> branch `feat/x` -> commit -> `git push -u origin feat/x` -> PR -> squash merge.
2. **Merge vs rebase?** Merge preserves history (main), rebase linearizes feature (clean log). Never rebase shared main.
3. **Conflict resolve?** `git status` -> edit `<<<<` -> `git add .` -> `git rebase --continue`. Use `git mergetool` / VSCode.
4. **Undo?** `git restore file` (unstage), `git reset --soft HEAD~1` (keep changes), `git revert <sha>` (safe shared), `git reset --hard` (danger local only).
5. **Stash?** `git stash push -m "wip" --include-untracked` -> switch -> `git stash pop`.
6. **Cherry-pick?** `git cherry-pick <sha>` to copy hotfix to release.
7. **Amend?** `git commit --amend --no-edit` only local unpushed.
8. **.gitignore?** `node_modules/.env/dist` + `git rm -r --cached .` if committed by mistake.
9. **PR good?** Small, linked issue, screenshots, `feat: add cart` Conventional Commits.
10. **Tags/release?** `git tag v1.0.0 && git push --tags`.
11. **Submodule vs monorepo?** Submodule links repos, monorepo single + workspaces.
12. **Hooks/CI?** husky lint+test pre-push, GitHub Actions runs `npm ci && npm test`.

## HR / Project (STAR)
- **Tell me about yourself (60s):** Stack -> 2 projects with metric -> what you want next.
  e.g. "Full-stack MERN, built e-comm with 2k products, cut load 40% via virtualize+ISR, auth JWT+refresh. Looking for product team with scale."
- **Challenge?** "Cart race on stock -> added Postgres transaction + optimistic UI + idempotency key, zero oversell in test."
- **Conflict?** "Disagreed on Redux vs Context -> benchmarked re-renders, chose Zustand for simple + docced decision."
- **Why us?** Mention their stack/product + how you add value in 30-60-90.
- Questions to ask: team size? code review? on-call? definition of done? growth?

## Mock A (30 min): Product Listing Page
Task: Fetch `/api/products?q=&page=` with search debounce, filter, skeleton, pagination.
Expectation: `useDebounce`, AbortController, `useMemo` filter, virtualize note, error/empty states.
Follow-ups: How cache? (SWR) How SEO? (Next ISR) How test? (RTL mock fetch)

## Mock B (30 min): Auth API Design
Task: Design `POST /auth/login`, `POST /auth/refresh`, `GET /me`.
Expectation: bcrypt compare, sign JWT, HttpOnly refresh, auth middleware, rate-limit login 5/min, 401 vs 403. Draw DB users table + refresh_tokens table.
Follow-ups: Where store on frontend? How logout all devices? How OAuth add?

## Final Checklist Tonight
- [ ] Can whiteboard event loop, hooks flow, JWT, ACID, Big-O
- [ ] 2 STAR stories ready
- [ ] Laptop: Node/npm run, Git clean, portfolio link
- [ ] Sleep: no new topics after 10pm, revise this file only
