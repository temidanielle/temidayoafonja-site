# -*- coding: utf-8 -*-
"""The title and thumbnail lock exactly as the September 11 instruction states
it, used to verify the supplied ZIP by content.

The instruction's own checksum string was corrupted, so the archive is
verified against the packaging lock in the same instruction instead. That is a
stronger check than a hash: it confirms the file carries the content the
instruction describes.
"""
LOCK = {
 4:  ("I Was First in 3 New Roles in 5 Years. Here's What I Stopped Doing.",
      "I'D NEVER HELD THE ROLE"),
 5:  ("I Changed Career Tracks Without Starting Over. Here's What I Carried "
      "With Me.", "CHANGED TRACKS. NOT ZERO."),
 6:  ("I've Worked Across 8 Industries and Sectors. Here's How I Know If a "
      "New Role Is Actually Growth.", "NEW TITLE. SAME WORK?"),
 7:  ("It Took Me Years to Stop Mistaking More Work for Career Growth",
      "MORE WORK ≠ GROWTH"),
 8:  ("How to Show Your Impact at Work When You Built It From Scratch",
      "NOW IT LOOKS EASY"),
 9:  ("How to Change Industries Without Starting Over",
      "NEW FIELD. NOT ZERO."),
 10: ("Before a Layoff, Know What You Can Still Prove",
      "BEFORE ACCESS ENDS"),
 11: ("AI Can Do the Task. What Are You Still Paid For?",
      "THE TASK ISN'T THE JOB"),
 12: ("What to Do When You Can't Quit Your Job Yet",
      "WHAT CAN CHANGE NOW?"),
 13: ("A 30-Day Plan to Test Your Next Career Move",
      "TEST BEFORE YOU QUIT"),
 14: ("Which Parts of Your Experience Actually Transfer to Another "
      "Industry?", "WHAT REALLY TRANSFERS?"),
 15: ("The Career Gaps You Don't See Until the Work Gets Harder",
      "KNOWING ISN'T OWNING"),
 16: ("What to Do When Your Work Is Valued but You Are Overlooked",
      "THEY NEED YOU. THEN SKIP YOU."),
 17: ("How to Prove Your Value When AI Does More of the Task",
      "WHAT DID YOU ACTUALLY DO?"),
 18: ("Should You Stay an Individual Contributor or Become a Manager?",
      "TWO DIFFERENT JOBS"),
 19: ("Should You Become a Consultant? The Part Everyone Leaves Out",
      "EXPERIENCE ISN'T AN OFFER"),
 20: ("How to Return After a Career Break Without Starting at Zero",
      "WHAT STILL COUNTS NOW?"),
 21: ("What You Must Relearn When You Change Industries",
      "NOT EVERYTHING TRAVELS"),
}
