# -*- coding: utf-8 -*-
"""Riverside cards for Video 1, "How to Change Jobs Without Starting Your Career Over".

Slide 01, the career-path card, is already uploaded and placed in Riverside, so
it is deliberately absent. These are the eight cards that accompany it, taken
from the completed states of the approved v2.4 deck. No progressive reveals, no
section-title cards, no em dashes.
"""
import layouts as L
from rdeck import Card

V1 = [
 dict(file="02_Riverside_Move_1_Three_Questions.png",
      draw=lambda c: L.numbered(c, "Move one",
          ["What problems do people trust me to solve?",
           "What decisions can I now make with better judgment?",
           "What could I do in another setting because of what I learned here?"],
          headline="Look underneath the title.", size=48),
      script="\"The first one is to look underneath your title.\" through the three "
             "questions that follow.",
      purpose="Holds all three questions in view so the viewer can answer them "
              "without rewinding.",
      display="Full screen", seconds="8 to 10 seconds",
      prompt="Show this slide when I start asking the three questions under Move "
             "One. Keep it full screen for all three, then cut back to me."),

 dict(file="03_Riverside_Employer_Language.png",
      draw=lambda c: L.duo(c, "Move two",
          "Explain what the work changed.",
          ("INTERNAL DESCRIPTION", "I led an onboarding redesign."),
          ("WHAT ANOTHER EMPLOYER CAN UNDERSTAND",
           "I led an onboarding redesign with my team. One measure of how well "
           "new hires felt integrated moved from 47 to 75."),
          foot="Somebody who was not there can hear what changed.", dark=True),
      script="\"I led an onboarding redesign.\" through to \"I led an onboarding "
             "redesign with my team, and one measure of how well new hires felt "
             "integrated moved from 47 to 75.\"",
      purpose="Shows the translation instead of describing it, which is the whole "
              "move.",
      display="Full screen", seconds="8 to 10 seconds",
      prompt="Bring this slide up when I read the internal version, and hold it "
             "through the version that carries so the viewer can compare them. Do "
             "not put captions over the right-hand text."),

 dict(file="04_Riverside_Result_47_to_75.png",
      draw=lambda c: L.bignumber(c, "One result",
          "One measure of new-hire integration",
          "47", "75", ("Before the redesign", "After the redesign"),
          foot="A team result from a redesign I led."),
      script="\"one measure of how well new hires felt integrated moved from 47 "
             "to 75.\"",
      purpose="Puts the one number in the video on screen, with the precision "
              "qualifier attached to it.",
      display="Full screen", seconds="5 to 7 seconds",
      prompt="Use this slide the moment I say the measure moved from 47 to 75. "
             "Full screen, long enough to read the line underneath, then back to me."),

 dict(file="05_Riverside_Complete_Evidence_Example.png",
      draw=lambda c: L.grid4(c, "Move three",
          "Keep evidence before you need it.",
          [("Situation", "New hires needed a stronger integration experience."),
           ("My role", "I led the onboarding redesign with my team."),
           ("What changed", "One measure of how well new hires felt integrated "
                            "moved from 47 to 75."),
           ("What this shows", "I can diagnose a weak point in the employee "
                               "experience and lead a redesign that improves it.")],
          dark=True),
      script="\"The four lines on screen are enough. The situation. Your role. "
             "What changed. And what this shows.\"",
      purpose="Shows the finished record in full, which is the template the viewer "
              "copies.",
      display="Full screen", seconds="10 to 12 seconds",
      prompt="Show this slide when I say the four lines on screen are enough, and "
             "keep it up while I explain each one and the honesty test on the last "
             "line. This one needs longer than the others."),

 dict(file="06_Riverside_Three_Moves_Summary.png",
      draw=lambda c: L.numbered(c, "Three things I learned to do",
          ["Look underneath the title",
           "Explain what the work changed",
           "Keep evidence before you need it"],
          foot="What helped me carry my experience forward."),
      script="\"So those are the three. Look underneath the title. Explain what the "
             "work changed. Keep evidence before you need it.\"",
      purpose="Summarizes the three moves in the order I say them.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Show this summary slide when I list the three practices together. A "
             "few seconds full screen, then back to me."),

 dict(file="07_Riverside_Before_Next_Move_Three_Questions.png",
      draw=lambda c: L.numbered(c, "Before your next move",
          ["What can I solve now that I could not solve two years ago?",
           "What result can I describe in language another employer would "
           "understand?",
           "What could I still do if the title, employer or industry changed?"],
          foot="Write your answers down. Pause here if you want to.",
          dark=True, size=50),
      script="\"So before your next move, sit with three questions.\" through to "
             "\"Pause here if you want to write them down.\"",
      purpose="Keeps all three questions on screen for the pause I invite.",
      display="Full screen", seconds="10 to 14 seconds",
      prompt="Bring this slide up when I say to sit with three questions, and leave "
             "it on screen through the pause so anybody who wants to write them "
             "down has time. This is the longest hold in the video."),

 dict(file="08_Riverside_Career_Evidence_Starter_CTA.png",
      draw=lambda c: L.cta(c, "Free Career Evidence Starter",
          "One accomplishment.\nOne portable proof line.",
          "About 10 to 15 focused minutes.",
          "temidayoafonja.com/career-evidence-starter"),
      script="\"If you want to try this on one real thing you have done, I made a "
             "free Career Evidence Starter.\"",
      purpose="Supports the CTA and puts the link on screen while I say it.",
      display="CTA", seconds="6 to 8 seconds",
      prompt="Show this CTA slide while I describe the Career Evidence Starter, "
             "through to it being linked below. Do not cover the web address."),

 dict(file="09_Riverside_Watch_Next.png",
      draw=lambda c: L.watch_next(c,
          "Is Your Job\nMaking You Less\nMarketable?"),
      script="\"Watch Is Your Job Making You Less Marketable? next.\"",
      purpose="Supports the Watch Next ending, with the right of the frame kept "
              "clear for the YouTube end screen.",
      display="Watch Next", seconds="6 to 10 seconds",
      prompt="Use this as the closing slide when I say to watch Is Your Job Making "
             "You Less Marketable? next. Keep the right side clear so the YouTube "
             "end screen can sit there."),
]


def build_cards_v1():
    out = []
    for spec in V1:
        c = Card(int(spec["file"][:2]), spec["file"])
        spec["draw"](c)
        c.notes = "%s\n\nScript match: %s\n\nPurpose: %s\nDisplay: %s\nScreen time: %s" % (
            spec["file"], spec["script"], spec["purpose"], spec["display"],
            spec["seconds"])
        out.append(c)
    return out
