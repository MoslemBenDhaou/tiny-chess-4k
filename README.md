# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/MoslemBenDhaou/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/MoslemBenDhaou/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4,096 bytes of plain Python 3.13 (stdlib only), written by an AI coding agent.

- 10x12 mailbox board, always seen from the side to move
- Piece-square tables from formulas, blended between middlegame and endgame by material
- Iterative deepening PVS with a transposition table, null-move pruning, late-move
  reductions, futility and reverse futility pruning, killer moves and quiescence search
- Repetition-aware; searches a fixed 200,000 nodes a move (no clock), so it is deterministic

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3.13 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
