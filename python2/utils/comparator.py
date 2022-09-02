class RedEyeRemoval:
    def __init__(self, image, all_patterns, threshold, correction):
        self.image = image
        self.all_patterns = all_patterns
        self.threshold = threshold
        self.correction = correction

    # Making a lot of assumptions, breaking generality and robustness,
    # but going for a lot of speed (this won't work with images that have
    # shapes with red values >= 200, that are not part of the given eye patterns).
    def match(self, pixel_index):
        match = -1

        if self.image.pixels_red[pixel_index+self.image.resolution.width+1]>=self.threshold:
            match = 3
        elif self.image.pixels_red[pixel_index+self.image.resolution.width+2]>=self.threshold:
            if self.image.pixels_red[pixel_index+2*self.image.resolution.width+1]>=self.threshold:
                match = 2
            else:
                match = 1
        else:
            match = 0        

        return match

    def apply_correction(self, pixel_index, pattern_number):
        for y in range(5):
            for x in range(5):
                if self.all_patterns[pattern_number][y][x]:
                    self.image.pixels_red[pixel_index+x] -= self.correction
            pixel_index += self.image.resolution.width

    def search(self):
        pixel_index = 0
        for y in range(self.image.resolution.height-4):
            for x in range(self.image.resolution.width-4):
                # The following line breaks the generality and robustness of the solution, too.
                # Assumption: there is a pixel in the upper left corner of all paterns.
                if self.image.pixels_red[pixel_index]>=self.threshold:
                    pattern_number = self.match(pixel_index)
                    if pattern_number>-1:
                        self.apply_correction(pixel_index,
                                              pattern_number)
                pixel_index += 1
            pixel_index += 4
