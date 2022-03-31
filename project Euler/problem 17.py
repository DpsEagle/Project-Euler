def letter_amount(number: object) -> object:
    """

    :rtype: object
    """
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits10s = ["place holder", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen"]
    ValueOfWord = 0
    if 99 < number < 1000:
        ValueOfWord += 10  # Word  "a hundred" has 7 letters and the word "and" has 3 letters do. Do -22 at the very end
        # amount calculation because numbers one hundred two hundred etc. would not have an and in addition a thousand
        # has 1 extra letter because it is 8 letters long unlike hundred which has 8

        word_number = str(number)
        first_digit_of_number = word_number[0]
        int_of_first_digit_of_number = int(first_digit_of_number)
        first_digit_of_number_index = digits[int_of_first_digit_of_number - 1]
        length_of_first_digit_word = len(first_digit_of_number_index)
        ValueOfWord += length_of_first_digit_word

        second_digit_of_number = word_number[1]
        int_of_second_digit_of_number = int(second_digit_of_number)
        if int_of_second_digit_of_number > 1:
            second_digit_of_number_index = digits10s[int_of_second_digit_of_number - 1]
            length_of_second_digit_word = len(second_digit_of_number_index)
            ValueOfWord += length_of_second_digit_word
        elif int_of_second_digit_of_number == 1:
            third_digit_of_number = word_number[2]
            int_of_third_digit_of_number = int(third_digit_of_number)

            third_digit_of_number_index = tens[int_of_third_digit_of_number]
            length_of_third_digit_word = len(third_digit_of_number_index)
            ValueOfWord += length_of_third_digit_word
        third_digit_of_number = word_number[2]
        int_of_third_digit_of_number = int(third_digit_of_number)
        if int_of_third_digit_of_number > 0 and int_of_second_digit_of_number != 1:
            third_digit_of_number_index = digits[int_of_third_digit_of_number - 1]
            length_of_third_digit_word = len(third_digit_of_number_index)
            ValueOfWord += length_of_third_digit_word
    elif 9 < number < 100:
        word_number = str(number)
        first_digit_of_number = word_number[0]
        int_of_first_digit_number = int(first_digit_of_number)
        if int_of_first_digit_number == 1:
            second_digit_of_number = word_number[1]
            int_of_second_digit_of_number = int(second_digit_of_number)
            second_digit_of_number_index = tens[int_of_second_digit_of_number]
            length_of_second_digit_word = len(second_digit_of_number_index)
            ValueOfWord += length_of_second_digit_word
        if int_of_first_digit_number > 1:
            first_digit_of_number_index = digits10s[int_of_first_digit_number - 1]
            length_of_first_digit_word = len(first_digit_of_number_index)
            ValueOfWord += length_of_first_digit_word

        if int_of_first_digit_number > 1:
            second_digit_of_number = word_number[1]
            int_of_second_digit_of_number = int(second_digit_of_number)
            if int_of_second_digit_of_number > 0:
                second_digit_of_number_index = digits[int_of_second_digit_of_number - 1]
                length_of_second_digit_word = len(second_digit_of_number_index)
                ValueOfWord += length_of_second_digit_word
    elif 0 < number < 10:
        word_number = str(number)
        first_digit_of_number = word_number[0]
        int_of_first_digit_of_number = int(first_digit_of_number)
        first_digit_of_number_index = digits[int_of_first_digit_of_number - 1]
        length_of_first_digit_word = len(first_digit_of_number_index)
        ValueOfWord += length_of_first_digit_word
    return ValueOfWord


total = 0
for x in range(1, 1001):
    amount = letter_amount(x)
    total += amount

print(
    total - 16)  # - 27 for all the and statements added with one hundred two hundred three hundred etc and then -27
# + 11 for letters in one thousand which is
