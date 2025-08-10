'''
Class Assignment-3: Piglatin Word Generator, Data Encryption
Input: transfer one million dollars to the account six two two
Output: ransfertp neop illionmp ollarsdp otp hetp ccountap ixsp wotp wotp
'''
def pt(sentence):
    words = sentence.split()
    encrypted_words = []

    for word in words:
        if len(word) > 0:
            new_word = word[1:] + word[0] + 'p'
            encrypted_words.append(new_word)
        else:
            encrypted_words.append('')
    return ' '.join(encrypted_words)
input_sentence = "transfer one million dollars to the account six two two"
output = pt(input_sentence)
print(output)