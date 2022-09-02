#!/usr/bin/env python3

import utils.comparator as cmp

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer

import utils.eye_pattern as ep

def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    # Convert eye patterns to int (0, 1)
    all_eye_patterns_int = []
    for p in range(len(ep.all_eye_patterns)):
        all_eye_patterns_int.append(ep.pattern_to_int(ep.all_eye_patterns[p]))

    # Search for patterns and correct red eyes
    for i in range(len(images)):
        comparator = cmp.RedEyeRemoval(images[i],
                                       all_eye_patterns_int,
                                       200,
                                       150)
        comparator.search()
        images[i] = comparator.image
    del ft
            
