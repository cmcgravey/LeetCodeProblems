class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]
        altitude = 0

        for delta in gain:
            altitude += delta
            altitudes.append(altitude)
        
        return max(altitudes)


def main():
    s = Solution()

    gain = [-5, 1, 5, 0, -7]
    output = s.largestAltitude(gain)
    assert(output == 1)

    gain = [-4, -3, -2, -1, 4, 3, 2]
    output = s.largestAltitude(gain)
    assert(output == 0)

if __name__ == "__main__":
    main()