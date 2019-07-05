# Given a bag of candies distribute them between two people and return the max number of differing cadies a person can have


class Distribute:
    def distrCandies(self, candies):
        return min(len(set(candies)), len(candies) // 2)


print(Distribute().distrCandies([505, 8, 951, 606, 475, 401, 451, 903, 618, 772, 760, 475, 310, 417, 728, 972, 646, 794, 648, 315, 353, 698, 55, 88, 503, 798, 297, 139, 879, 99, 917, 38, 554, 747, 561, 175, 956, 373, 672, 941, 267, 680, 89, 902, 127, 428, 545,
                                 914, 586, 349, 339, 152, 185, 340, 220, 547, 648, 364, 939, 641, 212, 422, 621, 512, 338, 826, 887, 813, 125, 955, 4, 874, 804, 868, 231, 939, 114, 237, 298, 606, 199, 965, 972, 141, 676, 90, 369, 289, 628, 12, 588, 236, 254, 370, 920, 298, 566, 888, 316, 173]))
