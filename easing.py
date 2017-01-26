
class EasingInOutCubic:
    @staticmethod
    def get(t):
        t *= 2
        if t < 1:
            return 0.5 * t * t * t

        t -= 2
        return 0.5 * (t * t * t + 2)