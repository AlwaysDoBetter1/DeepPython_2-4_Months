'''
Write a program using a recursive function that displays an image of an hourglass made up of the numbers 1, 2, 3, and 4:
1111111111111111 #16 times
  222222222222 #12times
    33333333 #8times
      4444 #4 times
    33333333#8times
  222222222222#12times
1111111111111111#16 times
'''


def rec():
    def fall(n):
        if n >= 4:
            print(" " * (4 - n // 4) * 2 + n * str(4 - (n - 4) // 4))
            fall(n - 4)
    fall(16)
    def growth(e):
        if e <= 16:
            print(" " * (4 - e // 4) * 2 + e * str(4 - (e - 4) // 4))
            growth(e + 4)
    growth(8)

rec()