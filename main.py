# The Tired Dark Lord: a 100-word villain monologue, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The villain: nine kingdoms conquered, a prophecy that says 'meh,
# eventually', minions unionised, a hero who is late again, a back that
# hurts, a drafty throne room -- and, before world domination, a nap.
# The tiredness lives in the deflections (soup, naps, cold tea, rehearsing
# the laugh) rather than in any plain statement of weariness.
import os

LINE = "Honestly? The ritual is at midnight, the minions unionised, and the ancient prophecy just says 'meh, eventually.' I've conquered nine kingdoms and I can't remember why — I think one of them had good soup. The hero is late again; I've rescheduled the final battle three times because my back hurts and the throne room is drafty. Do I still want to rule the world? Yes. But first, a nap. Then world domination, probably. Or soup. My evil laugh needs rehearsing, and the castle runs on cold tea. The dark lord rests now. Tell the bards to keep it down."

OUTPUT_PATH = "/output/entry.txt"

assert len(LINE.split()) == 100, "entry must be exactly 100 words"
assert 1 <= len(LINE) <= 600, "entry must be 1 to 600 characters"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the monologue, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the monologue: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
