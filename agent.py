import json
import random
from datetime import datetime

with open("memory.json", "r") as f:
    memory = json.load(f)

with open("trends.json", "r") as f:
    trends = json.load(f)

available = [t for t in trends if t not in memory["used_topics"]]

if not available:
    memory["used_topics"] = []
    available = trends

trend = random.choice(available)

hooks = [
    "Your brain lies to you every day.",
    "No one explains this about your mind.",
    "This is why you feel stuck.",
    "Your attention span isn’t broken — it’s trained.",
    "You were never meant to focus like this."
]

available_hooks = [h for h in hooks if h not in memory["used_hooks"]]
hook = random.choice(available_hooks or hooks)

script = f"""
HOOK (0–3s):
{hook}

MAIN (3–50s):
Most people don’t realize that {trend.lower()}.
Your brain filters reality to save energy.
That means it deletes details, distorts time,
and prioritizes comfort over truth.
This isn’t a flaw — it’s survival.

CTA (last 5s):
Once you see this, you can’t unsee it.
"""

captions = [
    hook,
    "Your brain edits reality",
    "To save energy",
    "Once you notice it",
    "You can't ignore it"
]

post_caption = f"{hook} #psychology #mind #didyouknow #shorts"

timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
output = {
    "trend": trend,
    "hook": hook,
    "script": script.strip(),
    "captions": captions,
    "post_caption": post_caption
}

import os
os.makedirs("outputs", exist_ok=True)

with open(f"outputs/{timestamp}.json", "w") as f:
    json.dump(output, f, indent=2)

memory["used_topics"].append(trend)
memory["used_hooks"].append(hook)

with open("memory.json", "w") as f:
    json.dump(memory, f, indent=2)

print("Generated:", timestamp)