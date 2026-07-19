# this_is_for_austin.py 🌵
## 🚀 Release Notes

### v1.1.0 — The "Data-Driven Overhaul" Edition!
This update completely rewrites the application architecture, separating execution logic from the text content to make the codebase professional, optimized, and incredibly easy to maintain.

#### 🛠️ Operational Overhauls (How I de-bugged my own code)
* **The "Data-Driven" Clutter Eviction:** Yanked over 100 lines of massive text walls, hobby descriptions, and emotional baggage out of my main loop and stuffed them into nicely organized dictionary warehouses (`COMP_QUESTIONS`, `BEHAVIOR_QUESTIONS`, `BUGS_DATA`, `HOBBIES_DATA`). The code is now clean; my room is next.
* **Wiping out Globals (State Encapsulation):** Banned risky `global` score trackers because letting functions blindly change things in the outside world is a debugging nightmare. Functions now act like miniature vending machines—they do their math locally and use `return` to drop exactly 1 or 0 points straight back into the tally engine.
* **The Anti-Austin Finger-Slip Shield:** Chained `.strip().lower()` to literally every single user input field. Now, if you accidentally hit the spacebar or panic-mash the Caps Lock key while trying to answer, the program silently fixes it instead of immediately roasting your typos. You're welcome.
* **`if/elif` Demolition:** Completely tore down those long, annoying multi-tiered conditional chains in the sub-menus. Instead of asking Python 50 times "is it choice A? is it choice B?", the script now uses elegant direct dictionary key lookups to grab your reactions instantly.
---
## Description
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
