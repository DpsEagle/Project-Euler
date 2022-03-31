def LetterAmount(x):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits10s = ["place holder", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen"]
    amount = 0
    if x > 99 and x<1000:
        amount += 10  # Word  "a hundred" has 7 letters and the word "and" has 3 letters do. Do -22 at the very end
        # amount calculation because numbers one hundred two hundred etc. would not have an and in addition a thousand
        # has 1 extra letter because it is 8 letters long unlike hundred which has 8

        WordNumber = str(x)
        FirstDigitOfNumber = WordNumber[0]
        IntOfFirstDigitOfNumber = int(FirstDigitOfNumber)
        FirstDigitOfNumberIndex = digits[IntOfFirstDigitOfNumber - 1]
        LengthOfFirstDigitWord = len(FirstDigitOfNumberIndex)
        amount += LengthOfFirstDigitWord

        SecondDigitOfNumber = WordNumber[1]
        IntOfSecondDigitOfNumber = int(SecondDigitOfNumber)
        if IntOfSecondDigitOfNumber > 1:
            SecondDigitOfNumberIndex = digits10s[IntOfSecondDigitOfNumber - 1]
            LengthOfSecondDigitWord = len(SecondDigitOfNumberIndex)
            amount += LengthOfSecondDigitWord
        elif IntOfSecondDigitOfNumber == 1:
            ThirdDigitOfNumber = WordNumber[2]
            IntOfThirdDigitOfNumber = int(ThirdDigitOfNumber)

            ThirdDigitOfNumberIndex = tens[IntOfThirdDigitOfNumber]
            LengthOfThirdDigitWord = len(ThirdDigitOfNumberIndex)
            amount += LengthOfThirdDigitWord
        ThirdDigitOfNumber = WordNumber[2]
        IntOfThirdDigitOfNumber = int(ThirdDigitOfNumber)
        if IntOfThirdDigitOfNumber > 0 and IntOfSecondDigitOfNumber != 1:
            ThirdDigitOfNumberIndex = digits[IntOfThirdDigitOfNumber - 1]
            LengthOfThirdDigitWord = len(ThirdDigitOfNumberIndex)
            amount += LengthOfThirdDigitWord
    elif x < 100 and x>9:
        WordNumber = str(x)
        FirstDigitOfNumber = WordNumber[0]
        IntOfFirstDigitNumber = int(FirstDigitOfNumber)
        if IntOfFirstDigitNumber == 1:
            SecondDigitOfNumber = WordNumber[1]
            IntOfSecondDigitOfNumber = int(SecondDigitOfNumber)
            SecondDigitOfNumberIndex = tens[IntOfSecondDigitOfNumber]
            #print(SecondDigitOfNumberIndex)
            LengthOfSecondDigitWord = len(SecondDigitOfNumberIndex)
            #print(LengthOfSecondDigitWord)
            amount += LengthOfSecondDigitWord
        if IntOfFirstDigitNumber>1:
            FirstDigitOfNumberIndex = digits10s[IntOfFirstDigitNumber - 1]
            LengthOfFirstDigitWord = len(FirstDigitOfNumberIndex)
            amount += LengthOfFirstDigitWord

        if IntOfFirstDigitNumber>1:
            SecondDigitOfNumber = WordNumber[1]
            IntOfSecondDigitOfNumber = int(SecondDigitOfNumber)
            if IntOfSecondDigitOfNumber>0:
                SecondDigitOfNumberIndex = digits[IntOfSecondDigitOfNumber - 1]
                LengthOfSecondDigitWord = len(SecondDigitOfNumberIndex)
                amount += LengthOfSecondDigitWord
    elif x >0 and x<10:
        WordNumber = str(x)
        FirstDigitOfNumber = WordNumber[0]
        IntOfFirstDigitOfNumber = int(FirstDigitOfNumber)
        FirstDigitOfNumberIndex = digits[IntOfFirstDigitOfNumber - 1]
        LengthOfFirstDigitWord = len(FirstDigitOfNumberIndex)
        amount += LengthOfFirstDigitWord
    return amount


total = 0
for x in range(1, 1001):
    amount = LetterAmount(x)
    total += amount

print(total-16) # - 27 for all the and statements added with one hundred two hundred three hundred etc and then -27 + 11 for letters in one thousand which is
