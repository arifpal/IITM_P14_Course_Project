class CheckPalindrome:

    def is_palindrome(self, text):
        
        text = text.lower().replace(" ", "")
        reversed_text = text[::-1]
        return text == reversed_text


# example usage
pc = CheckPalindrome()
print(pc.is_palindrome("Madam"))  # output: True
print(pc.is_palindrome("Hello world"))  # output: False

