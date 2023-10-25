# from matplotlib import pyplot as plt
import math

class APracticalExample():
    # Note that g stand for the gravity. You can use 9.81 for that.
    # Also, convert the frequency to a timestep (t). Frequency means "how many times in 1 second". So we di 1/frequency.
    def projectile_motion(self, angle, speed, frequency):
        x = []
        y = []
        t = 0
        y_point = speed * math.sin(angle) * t - 9.81 *t*t/ 2
        while True:
            x_point = speed * math.cos(math.radians(angle)) * t
            y_point = speed * math.sin(math.radians(angle)) * t - 9.81 * t * t * 0.5

            if y_point < 0:
                break
            x.append(x_point)
            y.append(y_point)

            t += 1/frequency

        return x, y


if __name__ == "__main__":
    apracticalexample = APracticalExample()
    print(apracticalexample.projectile_motion(30, 15, 100))