#!/usr/bin/env python3

from typing import Tuple

EyePattern = Tuple[str, str, str, str, str]

EYE_PATTERN_1: EyePattern = (
  "/---\\",
  "|   |",
  "|-o-|",
  "|   |",
  "\\---/"
)

EYE_PATTERN_2: EyePattern = (
  "/---\\",
  "| | |",
  "| 0 |",
  "| | |",
  "\\---/"
)

EYE_PATTERN_3: EyePattern = (
  "/---\\",
  "| | |",
  "|-q-|",
  "| | |",
  "\\---/"
)

EYE_PATTERN_4: EyePattern = (
  "/---\\",
  "|\\ /|",
  "| w |",
  "|/ \\|",
  "\\---/"
)

all_eye_patterns = [EYE_PATTERN_1,
                    EYE_PATTERN_2,
                    EYE_PATTERN_3,
                    EYE_PATTERN_4]

def pattern_to_int(pattern):
    int_pattern = []
    for y in range(len(pattern)):
        int_pattern.append([])
        for x in range(len(pattern[y])):
            if pattern[y][x]==' ':
                int_pattern[y].append(0)
            else:
                int_pattern[y].append(1)

    return int_pattern
        
