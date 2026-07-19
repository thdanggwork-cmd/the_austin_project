# this_is_for_austin.py 🌵
## 🚀 Release Notes

### v1.1.0 — The "Data-Driven Overhaul" Edition
This update completely rewrites the application architecture, separating execution logic from the text content to make the codebase professional, optimized, and incredibly easy to maintain.

#### 🛠️ Architectural Improvements
* **Data-Driven Design:** Extracted over 100 lines of hardcoded question prompts, hobby descriptions, and system bugs out of sequential logic and grouped them into clean dictionary data structures (`COMP_QUESTIONS`, `BEHAVIOR_QUESTIONS`, `BUGS_DATA`, `HOBBIES_DATA`).
* **State Encapsulation:** Eliminated risky `global` variable tracking for game scores. Functions now utilize localized scope and explicit `return` pipes to safely pass point updates directly to math operators.
* **Input Sanitization Layer:** Chained `.strip().lower()` validation mechanics across all terminal prompts, creating a safety layer that catches accidental whitespace or casing errors without throwing runtime glitches.
* **Streamlined Control Flow:** Replaced multi-tiered `if/elif/else` conditional chains in sub-menus with elegant direct dictionary key lookups.
---
An interactive, terminal-based CLI application engineered to introduce myself (Jake) to my roommate Austin. Intended to bypass awkward remote roommate small talk, streamline boarding logistics, and stress-test the user's input boundaries.

> **"thoughtful project"**
> — ★★★★★ Austin (Verified Roommate)
---

## 🚀 Quick Start (Deployment)

To launch this high-performance roommate introduction system, run the script via your local terminal:

```bash
python this_is_for_austin.py

```

Note: Unauthorized launch attempts by non-Austins will trigger defensive error protocols.

---
## 👨‍🦲 User Registration:
When the program asks for your name, type Austin, or austin, or whatever aUStiN case formatting. You just need to be Austin (you only have two lives for this!), then proceed with the manual from the code itself!

## 🎮 User Manual: Menu Navigation

Once verified, you will navigate through a modular, menu-driven interface. The recommended sequence of execution is **1 → 2 → 3 → 4 → 5 → 6**:

### `[1]` Background 📖

Loads Jake’s core history, detailing the 12-year academic survival campaign, photography side quests, and a current ceasefire agreement with college Calculus.

### `[2]` Hobbies 🍳

Explores 101 highly random hobby scripts, including landscape photography, hyper-focused cooking, and the mechanics of a talking desktop cactus.

### `[3]` Behaviors 🧠

An interactive behavioral assessment module where your choices are immediately benchmarked against Jake's operational profile.

### `[4]` Current Issues (System Diagnostics) 🛠️

Runs a live diagnostic scan on `Jake.exe` to isolate and investigate known developer bugs.


### `[5]` Friend Manual (The Compatibility Engine) 🤝

An advanced, 10-question compatibility scoring program utilizing conditional logic, string validation, and dynamic score evaluation matrixes to determine if we will survive Purdue housing.

### `[6]` Exit Protocol 🚪

Gracefully terminates `this_is_for_austin.exe` and releases control of your machine.

---

## 🛡️ Input Validation & Defensive Coding

This application features a robust **Defensive Input Validation Engine**. If you attempt to break the code with "creative" inputs, you will encounter the `invalid_messages` database, resulting in roastful system notifications.

---

## 📄 License

This project is licensed under the **Malware-Free, Roommate-Approved License (MF-RAL)**. Any replication of these bugs in real life is purely intentional.
