# Pocket Monsters: Advanced Object-Oriented Programming & Algorithmic Design

Pocket Monsters is a Python implementation of a modular battle system inspired by complex turn-based games. It models teams of autonomous entities engaging in combat, with support for dynamic team management, type-effectiveness logic, and multi-mode battle simulations.

This project is engineered under strict constraints prohibiting Python built-in containers (lists, dictionaries, sets) to demonstrate advanced object-oriented design, abstraction, and custom data structures for deterministic performance.

## Features

This project implements a modular turn-based battle system with support for team management, type-effectiveness strategies, and multiple battle modes. It demonstrates disciplined engineering under strict constraints prohibiting Python built-in containers (lists, dicts, sets).

Key capabilities:  
- Dynamic team creation and regeneration with adjustable limits.  
- Battle mechanics adhering to turn-based logic with attack/special actions and speed-based priority resolution.  
- Level-up and evolution systems with stat scaling and transformation.  
- Support for Set, Rotating, and Optimised battle modes using custom ADTs.  
- Battle Tower feature for multi-team gauntlets with persistent state management.

---

## Architecture Highlights

- **Custom Abstract Data Types (ADTs):** Queue, Priority Queue, and Linked Lists tailored to enforce constraints and achieve deterministic time complexity.  
- **Modular Components:** Each module (e.g., `poke_team.py`, `battle.py`, `tower.py`) isolates responsibility for maintainability and extensibility.  
- **Battle Engine:** Implements multi-phase combat flow, including damage calculation with type multipliers and Pokedex completion bonuses.  
- **Data-Driven Design:** Type effectiveness matrix initialized from external CSV for flexible updates.  
- **Complexity Annotations:** All methods include formal Big-O analysis for best and worst cases, ensuring transparency of performance characteristics.