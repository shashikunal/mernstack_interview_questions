# 00 - What 1 YOE Candidates Are Judged On

## Expectation vs Senior
- Senior: design scale, tradeoffs, lead. 1 YOE: can code CRUD cleanly, debug, explain basics, learn fast.
- You WIN by: clear fundamentals + 1-2 projects explained deeply + live coding without panic + honest "I don't know but I'd try...".

## What to Skip / Just 1-Liner (for 1 YOE)
- Skip: Redux-Saga complex flows, microservices, K8s deep, Serializable isolation theory, Nest interceptors deep.
- Just say: "Heard of X, used Y in tutorial, would use Y for [simple reason]." e.g. "Used Saga in tutorial, used Thunk at work for simple fetch."

## Project Story Template (memorize 2)
"Built [e-comm/todo/HR portal] with [React+Node+Mongo]. I did [auth + listing + pagination]. Challenge: [search lag / CORS / token expire]. Fixed by [debounce+abort / cors allowlist / refresh rotation]. Result: [400ms faster / zero 401 complaints]. Stack: [list]."

Fill tonight:
1. Project 1: ___ My part: ___ Tough bug: ___ Fix: ___
2. Project 2: ___ My part: ___ Tough bug: ___ Fix: ___

## Tomorrow Question Filter
If asked advanced (e.g. "design 10M users"), say: "At my scale [X users], I'd do [simple LB+stateless+managed DB+cache]. For 10M I'd add [read replica+CDN+queue] - haven't done at scale but approach is..."

## 1-YOE Live Coding Checklist
- Clarify: inputs? empty? large?
- Brute then optimal, say Big-O
- Handle edge: [], null, dup
- Test with 2 examples aloud

## Quick Self-Score (do tonight)
Can you without notes? [ ] debounce [ ] useEffect fetch+abort [ ] slice+thunk [ ] Express auth middleware [ ] JOIN + index [ ] Two Sum + Valid Paren [ ] git rebase + stash + conflict fix
If 5/7 yes, you're ready. Revise only the missing.
