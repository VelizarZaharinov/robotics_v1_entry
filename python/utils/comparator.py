class RedEyeRemoval:
    def __init__(self, image, pattern, threshold, correction):
        self.image = image
        self.pattern = pattern
        self.threshold = threshold
        self.correction = correction

        self.pattern_bbox = self.calc_pattern_bbox(self.pattern)

    # Find the rectangular area's dimensions inside which the pattern is.
    # The given patterns are 5x5 but for feature expansion in maind this
    # is not hard coded.
    def calc_pattern_bbox(self, pattern):
        pattern_width = len(pattern[0])
        pattern_height = len(pattern)

        for h in range(1, pattern_height):
            if pattern_width<len(pattern[h]):
                pattern_width = len(pattern[h])

        pattern_bbox = [pattern_width,
                        pattern_height]

        return pattern_bbox

    # Not making assumptions based on the given 4 patterns,
    # in order for the solution to work with the addition of new patterns.
    def match(self, pixel_index):
        for y in range(self.pattern_bbox[1]):
            for x in range(self.pattern_bbox[0]):
                if (self.image.pixels_red[pixel_index+x]<self.threshold) and self.pattern[y][x]:
                    return False
                elif (self.image.pixels_red[pixel_index+x]>=self.threshold) and (not self.pattern[y][x]):
                    return False
            pixel_index += self.image.resolution.width

        return True

    def apply_correction(self, pixel_index):
        for y in range(self.pattern_bbox[1]):
            for x in range(self.pattern_bbox[0]):
                if self.pattern[y][x]:
                    self.image.pixels_red[pixel_index+x] -= self.correction
            pixel_index += self.image.resolution.width

    def search(self):
        pixel_index = 0
        for y in range(self.image.resolution.height-self.pattern_bbox[1]+1):
            for x in range(self.image.resolution.width-self.pattern_bbox[0]+1):
                # The following line breaks the generality and robustness of the solution,
                # but accelerates it ~4.5 times! Remove for a general (slower, too) and robust solution!
                # Assumption: there is a pixel in the upper left corner of all paterns.
                if self.image.pixels_red[pixel_index]>=self.threshold:
                    if self.match(pixel_index):
                        self.apply_correction(pixel_index)
                        pixel_index += self.pattern_bbox[0]
                pixel_index += 1
            pixel_index += self.pattern_bbox[0] - 1
