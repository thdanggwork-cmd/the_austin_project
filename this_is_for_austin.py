# ================= INVALID RESPONSES =================
import random

invalid_messages = [
    "Booooo, you choose the invalid option.\n:P :P :P",
    "The cactus has rejected your application. 🌵",
    "Error 404: Common sense not found.",
    "You discovered a secret option.\nSadly, it contains nothing.",
    "AUSTINNNNNNNNNNNNNNNNNN!\n我知道你在亂按。😑",
    "Keep trying bro. Don't ask me how though.",
    "I have no idea what option that is.\nCongratulations on discovering new mathematics.",
    "Please enter a valid option.\nThe program is trying its best.",
    "Congratulations.\nYou have selected Optionn't.",
    "The option you're looking for is studying abroad.",
    "Task failed successfully.",
    "Please try again.\nPreferably with less innovation.",
    "This message has a 0.1% chance of appearing.\nI lied. But please type the correct value!",
    "Austin，這是請我喝珍珠奶茶的訊號。🧋",
    "WRONGGG.\nIf you're stuck, you gotta type exactly as it is! 1, 2 like that.",
    "Please enter a valid option before I book a flight to Taiwan pls."
]

not_Austin = [
    "Hmm... Not the one I expected. Bye :P",
    "Oh, I think you should remove the 'Lin'...",
    "小提示：只輸入名字就好 :P"
]
# ================= INVALID RESPONSES (END) =================


# ================= PAUSES =================
import time
def pause():
    input("\n[Press Enter to continue...]\n")
def menu():
    input("\n[Press Enter to return to main menu...]\n")
    print("Returning to main menu...\n")
    time.sleep(0.8)
# ================= PAUSES (END) =================


# ================= PART 6: GOODBYE =================
import sys
def goodbye():
    print("\nThank you for trying this_is_for_austin.exe.\n")
    time.sleep(1.4)
                
    print("""By the time you're reading this,
we're probably still thousands of kilometers apart.\n""")
    time.sleep(2.8)

    print("""But hopefully this program made
that distance a little smaller.\n""")
    time.sleep(2.8)
                
    print("""You'd probably know about:

- the cactus
- the photography
- the random projects (like this one)
- the MYANMAR dude you met at YMUNT 2024

And probably a few of my bugs too.\n""")
    time.sleep(4.4)
    print("So...")
    time.sleep(1.2)

    print("""到時見 👋
很期待見到你。\n""")
    time.sleep(2.4)
                      
    print("""See you at Purdue 👋
Looking forward to meeting you in person.\n""")
    time.sleep(2.4)

    print("Hopefully with fewer bugs than before :P\n")
    time.sleep(2)

    print("""- Jake (or Dang)

Going back to Austin's computer...
""")
    time.sleep(2.4)
    sys.exit()
# ================= PART 6: GOODBYE (END) =================


# ================= PART 5: FRIEND MANUAL =================
def reflective_question(
    num,
    text,
    jake_comp,
    explanation,
):
    while True:
        ans_comp = input(f"{num}. {text}\n> ")

        if ans_comp.lower() in ["a", "b", "c", "d", "e"]:
            break
        print(random.choice(invalid_messages))
        time.sleep(1.2)
        print("\nPlease choose a valid option.\n")
        time.sleep(1.2)

    print("\n-------- RESULT --------\n")
    time.sleep(0.8)

    print(f"Your answer: {ans_comp.upper()}")
    time.sleep(0.8)

    print(f"Jake's answer: {jake_comp.upper()}")
    time.sleep(0.8)
    
    print(explanation)
    pause()
def compatibility_question(
    num,
    text,
    jake_comp,
    explanation,
    valid_answers=None
):
    if valid_answers is None:
        valid_answers = [jake_comp.lower()]

    while True:
        ans_comp = input(f"{num}. {text}\n> ")

        if ans_comp.lower() in ["a", "b", "c", "d", "e"]:
            break

        print(random.choice(invalid_messages))
        time.sleep(1.2)
        print("\nPlease choose a valid option or this will go on forever.\n")
        time.sleep(1.2)

    print("\n-------- RESULT --------\n")
    time.sleep(0.8)

    print(f"Your answer: {ans_comp.upper()}")
    time.sleep(0.8)

    print(f"Jake's answer: {jake_comp.upper()}")
    time.sleep(0.8)

    if ans_comp.lower() in valid_answers:
        score += 1
        print("\n[✓] Compatibility point earned!\n")
    else:
        print("\n[X] No compatibility point this time.\n")

    time.sleep(1)

    print(explanation)
    pause()
    
def manual():
    global score
    score = 0
    print("""
[✓] Friend manual selected!
Loading compatability test...""")
    time.sleep(1.2)

    print("""\nHere are some manuals of how to live with me.
Let's see if we're any compatible!
(P/s it doesn't matter that much tbh)""")
    pause()
    
    compatibility_question(
1,
"""Which type of movie sounds most appealing?

A. Action-packed movies
B. Thrillers, mysteries, and psychological games
C. Slow-paced documentaries and slice-of-life stories""",

"A and B",

"""I like movies that keep me engaged.
Explosions are cool.
Mysteries are cool.
Please don't make me watch paint dry for two hours.""",

["a", "b"]
)
    
    compatibility_question(
2,
"""Which type of game sounds most appealing?

A. Competitive multiplayer games
B. Sandbox / creative games
C. Story-driven adventures""",

"C",

"""I enjoy games with a direction.
Exploration is fun.
Knowing why I'm moving forward is even better.""",

["c"]
)
    
    compatibility_question(
3,
"""What kind of music do you listen to?

A. Pop
B. Instrumental
C. Rock
D. Classical
E. Other""",

"All of the above",

"""My music taste behaves more like a tourist
than a permanent resident.

If it sounds good, it enters the playlist.""",

["a","b","c","d","e"]
)
    compatibility_question(
4,
"""Which working style sounds more appealing?

A. Working alone
B. Working with a team""",

"B",

"""I enjoy teamwork more than people expect.

The challenge isn't teamwork.
It's finding a good team.""",

["b"]
)
    
    compatibility_question(
5,
"""What makes a friendship valuable?

A. Having fun together
B. Being there when needed
C. Trust and honesty
D. Shared experiences""",

"All of the above",

"""Friendships aren't optimization problems.

You don't maximize one variable.
They're all important.""",

["a","b","c","d"]
)
    compatibility_question(
6,
"""What would you most likely forget before a trip?

A. Phone
B. Charger
C. Money
D. ID Card
E. Airpods""",

"D",

"""I'm always telling myself that I prepared the IDs.
And then forgot it. And encountered 101 problems and criticisms.

Please remind me twice before going out anytime.
I'm working on it, I promise! I'll remind you too :D""",

["d"]
)
    reflective_question(
7,
"""If given unlimited time and resources,
what would you most likely create?

A. A successful, worldwide business
B. Useful projects and tools
C. Laughter stuff
D. Something personal""",

"???",

"""Honestly, I don't know yet.

I'm entering a new chapter of life,
and I haven't fully figured out what I want to do.

Maybe that's okay.

For now, I'm exploring the options I have.
You could also explore with me if you want to :P""",
)
    
    compatibility_question(
8,
"""You find two options. What would you choose?

A. More expensive but slightly better
B. Cheaper but still acceptable""",

"B",

"""I usually try to maximize value.
You could see me stretching my wallet like bubble gums.

It isn't always as sweet as bubble gums, though.""",

["b"]
)
    compatibility_question(
9,
"""What would a shared room with you probably look like?

A. Extremely organized
B. Organized chaos
C. Self-disaster only
D. Complete mess""",

"C",

"""I usually mess up my room a lot.

But I often try to keep that disorganization to myself.
I value public places :P
Yeah I'll keep the living room tidy.""",

["c"]
)
    compatibility_question(
10,
"""Which sounds most satisfying?

A. Solving a difficult problem
B. Creating something useful
C. Roast someone playfully
D. Eating good food""",

"All of the above",

"""This question is a free pass.

I genuinely enjoy all four.""",

["a","b","c","d"]
)
    time.sleep(1)
    print(f"Compatibility Score: {score}/9")

    if score <= 3:
        print("""
Interesting.

One of us may be an alien.
""")

    elif score <= 5:
        print("""
Not bad.

Further roommate testing recommended.
""")

    elif score <= 7:
        print("""
Pretty compatible.

We may survive Purdue.
""")

    else:
        print("""
Warning.

Possible duplicate Jake detected.
""")

    time.sleep(2)
    print("""[✓] Compatability test finished!
Thank you for participating in the
official Jake compatibility assessment.

I believe we both have some similarities and differences.
But let's try to live together peacefully and with lots of laughter :P
Happy Purdue, Austin!""")

    menu()
# ================= PART 5: FRIEND MANUAL (END) =================


# ================= PART 4: CURRENT ISSUES =================
def scan():
    print("""
[✓] Current issues selected!
Scanning Jake.exe...\n""")
    time.sleep(1.2)
    
    for i in range(1, 11):
        bar = "█" * i + "░" * (10 - i)
        print(f"\rScanning user... [{bar}]", end="")
        time.sleep(0.4)

    print("""\n\nScan complete.
5 known bugs detected.

4.1. JUDGEMENT_FILTER.exe
4.2. THEORY_RESISTANCE.dll
4.3. OVERTHINKING.sys
4.4. FEATURE_CREEP.py
4.5. SELF_PRIORITY_ERROR.log""")
    while True:

        bug = input("\nChoose a bug from 4.1 - 4.5 to investigate, or press Enter to exit: ")

        if bug == "":
            print("""\nSome other bugs may be undetected.

If additional issues are discovered,
please submit bug reports directly to Jake.

Further supervision and support recommended.

Returning to main menu...\n""")
            time.sleep(0.8)
            break
        bugscan(bug)
        
def bugscan(bug):
    
    if bug == "4.1":
        print("""
⚠ Bug detected!

Name:
JUDGEMENT_FILTER.exe

Description:
System may hesitate before expressing thoughts in situations
involving uncertainty about social judgment.
Input is processed through an internal "what will people think?" filter, 
which can delay output or reduce clarity.

Symptoms:
- pausing before speaking or responding
- holding back ideas in group settings
- hesitating to ask questions or request help
- over-checking responses before sending

Severity:
Medium

Trigger Conditions:
- unfamiliar people or environments
- group discussions
- situations involving evaluation or comparison

Status:
Active.
User awareness increasing.
Gradual improvement observed.""")
         
    elif bug == "4.2":
        print("""
⚠ Bug detected!

Name:
THEORY_RESISTANCE.dll

Description:
System shows reduced efficiency when processing
abstract information without immediate context or application.
Pure theory input may fail to sustain
attention without practical linkage.

Symptoms:
- low engagement with textbook-style learning
- faster understanding when examples or projects are present
- decreased motivation during abstract-only explanations
- preference for hands-on exploration

Severity:
Medium

Trigger Conditions:
- long theoretical lectures
- memorization-heavy material
- lack of real-world application

Status:
Ongoing.
Workarounds (projects, examples) highly effective.""")

    elif bug == "4.3":
        print("""
⚠ Bug detected!

Name:
OVERTHINKING.sys

Description:
System may enter recursive analysis loops
after decisions or social events.
Minor inputs can expand into extended
internal simulations of alternative outcomes.

Symptoms:
- replaying past conversations
- analyzing small mistakes in detail
- difficulty finalizing decisions quickly
- prolonged internal debate after events

Severity:
Medium

Trigger Conditions:
- social interactions
- perceived mistakes
- unclear or ambiguous outcomes

Status:
Active.
Management strategies partially effective.""")

    elif bug == "4.4":
        print("""
⚠ Bug detected!

Name:
FEATURE_CREEP.py

Description:
System may expand simple tasks beyond original scope by continuously
adding new ideas, improvements, or extra layers of detail during execution.

Symptoms:
- projects growing beyond initial intention
- spontaneous addition of extra features or polish
- "just one more thing" loop during creation
- increased complexity without external requirement

Severity:
Low

Trigger Conditions:
- creative work
- coding sessions
- boredom combined with curiosity spikes

Status:
Stable but persistent.
No corrective action planned.""")
            
    elif bug == "4.5":
        print("""
⚠ Bug detected!

Name:
SELF_PRIORITY_ERROR.log

Description:
System frequently provides support to others.

Unexpected side effect:
Maintenance of local system may be delayed.

Additional symptoms:
- harsher self-evaluation
- difficulty accepting own progress
- tendency to notice flaws before successes

Severity:
Medium

Status:
Patch currently in development.

Developer Notes:
User has become aware of the issue.
Progress is slow but measurable.""")
    else:
        print(random.choice(invalid_messages))
        time.sleep(1.2)
# ================= PART 4: CURRENT ISSUES (END) =================


# ================= PART 3.1: BEHAVIORS GAME =================
def question(num, text, jake_answer, reaction_a, reaction_b, reaction_c):

    while True:
        ans = input(f"{num}. {text}\n> ")

        if ans.lower() in ["a", "b", "c"]:
            break

        print(random.choice(invalid_messages))
        time.sleep(1.2)
        print("\nPlease choose A, B, or C or this will go on forever.\n")
        time.sleep(1.2)

    print("\n----- COMPARISON -----\n")
    time.sleep(1)
    print(f"Your answer: {ans.upper()}")
    time.sleep(1)
    print(f"Jake's answer: {jake_answer}")

    if ans.lower() == "a":
        time.sleep(0.8)
        print(reaction_a)
        
    elif ans.lower() == "b":
        time.sleep(0.8)
        print(reaction_b)
    else:
        time.sleep(0.8)
        print(reaction_c)
# ================= PART 3.1: BEHAVIORS GAME (END) =================


# ================= PART 3.2: BEHAVIORS =================
def behaviors():
    print("""
[✓] Behaviors selected!
Loading questions...""")
    time.sleep(1.2)

    print("""\nYou're gonna answers some questions about behaviors with me.
It'll be useful to get to know some of my basic human functions :D""")
    pause()
    question(
    1,
    """When learning something new, you usually:

A. Read theory and understand it first.
B. Start trying things immediately.
C. Alternate between theory and practice.""",
    "B",
    "-> Interesting. I usually get impatient if I stay in theory for too long 😭",
    "-> Yep, same. I like to try things first and figure things out along the way.",
    "-> Honestly, that's probably the healthiest approach."
                    )
    pause()
            
    question(
    2,
    """In a new group of people, you usually:

A. Observe first and speak when comfortable.
B. Start conversations and meet people quickly.
C. Depends on the group and the vibe.""",
    "C",
    "-> I can be like that too. Sometimes I need a bit of time to understand the vibe.",
    "-> That's braver than me 🤣 I don't usually walk into a room and start collecting friends.",
    "-> Same. My social mode changes a lot depending on who's around."
                    )
    pause()
            
    question(
    3,
    """Which type of behavior bothers you most?

A. Arrogance and looking down on others.
B. Constant negativity and complaining.
C. Dishonesty and talking behind people's backs.""",
    "A",
    "-> Same. People acting superior for no reason drains my battery surprisingly fast.",
    "-> I get that too. A little complaining is fine, but endless negativity gets exhausting.",
    "-> Yeah... Trust is really important in any friendship."
                    )
    pause()
            
    question(
    4,
    """What usually motivates you to do something?

A. A clear goal or achievement.
B. Curiosity and interest.
C. Responsibility to other people.""",
    "B",
    "-> Goals help, but they're usually not enough by themselves for me.",
    "-> Yep. Curiosity is ridiculously effective on me. \nOne random idea can consume my entire afternoon.",
    "-> Helping people is also motivating for me. I like feeling useful."
                    )
    pause()
            
    question(
    5,
    """When facing a difficult problem, you usually:

A. Keep trying different approaches.
B. Ask someone for help.
C. Take a break and return later.""",
    "A",
    "-> Same. I tend to poke problems with a stick until they reveal what they're hiding. 🤓",
    "-> I should probably do this more often. \nAsking for help isn't exactly my first instinct.",
    "-> Honestly, this works more often than people think. A reset can help a lot."
            )
    time.sleep(2)
    print("""\n[✓] Test finished!
Congratulations. You have successfully completed the behavior test.

I don't know what you answered, but since this is
a program to get to know me, it doesn't matter :P.

Oh, you can also try as many options as you want.
They have different responses :3""")
    
    menu()
# ================= PART 3.2: BEHAVIORS (END) =================


# ================= PART 2: HOBBIES =================
def hobbies():
    print("""
[✓] Hobbies selected!
Loading Jake's 101 random hobbies...""")
    time.sleep(1.2)
    print("""\nI like a lot of things. Pick one:

2.1 Photography
2.2 Cooking
2.3 Sleeping
2.4 Random projects
2.5 Chaos""")
    while True:
        
        choicehb = input("\nChoose a hobby from 2.1 - 2.5, or press Enter to exit: ")
        if choicehb == "":
            print("""
[✓] Oh you want to come back.

You could see me having 99+ more hobbies
when we live together. Prepare yourself.

Returning to main menu...\n""")
            time.sleep(2.4)
            break
        hobbydesc(choicehb)
def hobbydesc(choicehb):

        if choicehb == "2.1":
            print("""
[✓] Photography selected!

I enjoy taking photos, especially landscapes.
My walking speed decreases by approximately 90%
whenever the landscape becomes interesting.
Please be patient.""")
            time.sleep(2.4)
            
        elif choicehb == "2.2":
            print("""
[✓] Cooking selected!

I enjoy cooking when I choose to cook.
If someone urges me to cook, my motivation drops significantly.
If I choose to cook, I become 999% focused.
Scientists are still investigating why.""")
            time.sleep(2.4)
            
        elif choicehb == "2.3":
            print("""
[✓] Sleeping selected!
...
...
zzz...

Yes, I enjoy sleeping.
Unfortunately, sleep schedule and I are
currently in a long-distance relationship.""")
            time.sleep(2.4)
            
        elif choicehb == "2.4":
            print("""
[✓] Random projects selected!

I enjoy making random things:
- Python programs
- Photography projects
- Weird experiments
- Solving problems nobody asked for""")
            time.sleep(2.4)
            
        elif choicehb == "2.5":
            print("""
[✓] Chaos selected!

I own a talking cactus.
It repeats everything I say.

"I own a talking cac-"
I turned it off in time.

I also enjoy making people laugh.
Occasionally this is achieved through sarcasm.
Most of them are friendly.

Keyword: "Most".""")
            time.sleep(2.4)
        else:
            print(random.choice(invalid_messages))
            time.sleep(1.2)
# ================= PART 2: HOBBIES (END) =================


# ================= PART 1: BACKGROUND =================
def background():
    print("""
[✓] Background selected!
Loading Jake's background info...""")
    time.sleep(1.2)

    print("""Hello! My name is Dang (also known as Jake).

After surviving:
- 12 years of school,
- Several clubs,
- Photography duties,
- Leadership positions,
- Regional English competitions,
- Approximately 47 million forms and essays,

I somehow ended up at Purdue University studying Data Science.
Nobody is entirely sure how. Not even me.

I was originally pushed toward STEM by my parents.
Meanwhile, I spent a suspicious amount of time carrying cameras, taking photos
and wondering whether I should secretly become a filmmaker.

Eventually I discovered that statistics, probability, logic
and asking "but why?" are actually pretty fun.

Calculus and I maintain a ceasefire (for now). Please don't question.""")

    menu()
# ================= PART 1: BACKGROUND (END) =================


# ================= MENU NAVIGATION =================
def info():
    while True:

        print("""What would you like to know about Jake?

1. Background
2. Hobbies
3. Behaviors
4. Current issues
5. Friend manual
6. Exit
""")

        choice2 = input("Option: ")
            
        if choice2 == "1":
                background()
                
        elif choice2 == "2":
                hobbies()
            
        elif choice2 == "3":
                behaviors()
                
        elif choice2 == "4":
                scan()
                
        elif choice2 == "5":
                manual()
                
        elif choice2 == "6":
                goodbye()

        else:
            print(random.choice(invalid_messages))
            time.sleep(1.2)
            menu()
# ================= MENU NAVIGATION (END) =================


# ================= LOADING SCREEN =================
def startup():
    print("""
Yay!
Estimated completion time: 5-10 minutes.
Estimated probability of boredom: Unknown.
""")
    time.sleep(1.4)
    print("User verified!")
    time.sleep(0.8)
    print("Malware check passed!")
    time.sleep(0.8)
    print("Loading personality data...")
    time.sleep(0.8)
    print("Preparing awkward self-introduction...(please don't laugh...)")
    time.sleep(0.8)

    print("""\nLet's start with some random facts about me :3

Recommended sequence:
1 → 2 → 3 → 4 → 5 → 6

(Or ignore it completely.
I can't stop you anyways.)\n""")
    info()


def loading():
    choice1 = input("Type y to continue!\n")
    if choice1.lower() != "y":
        print(random.choice(invalid_messages))

        choice1 = input("\nType y AGAIN to continue!\n")
        if choice1.lower() != "y":
            print("\nYou have lost all your lives :P :P :P.\nPlease run the program again.")
            time.sleep(2.4)
            sys.exit()
    startup()
# ================= LOADING SCREEN (END) =================


# ================= GREETINGS =================
def greetings():
    print("\nScanning user...")
    time.sleep(0.8)
    print("User identified: Austin")
    time.sleep(0.8)
    print("Threat level: Unknown")
    time.sleep(0.8)
    print("Loading Jake.exe...")
    time.sleep(0.8)

    print("""
你好 Austin!
Hello Austin! This is Dang (or Jake), your roommate.
I know it's pretty hard to get to know each other if we're this far away,
so I made this tiny program to introduce myself.
Believe me this is not malware T-T
(Right???)

So if you're ready...""")
    loading()

def verify_user():
    name = input("Please type your name: ")

    if name.lower() != "austin":
        print(random.choice(not_Austin))

        name_again = input("\nPlease type your name AGAIN: ")

        if name_again.lower() != "austin":
            print("\nMr. Lin please cooperate.\nPlease run the program again.")
            time.sleep(2.4)
            sys.exit()

    greetings()
# ================= GREETINGS (END) =================


# ================= START THE GAME! =================
print("""================================
歡迎來到 this_is_for_austin.exe!
Welcome to this_is_for_austin.exe!

Version 1.0 - Definitely Not Malware Edition
================================\n""")
verify_user()
