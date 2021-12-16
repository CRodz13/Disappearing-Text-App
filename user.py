class User:
    def __init__(self):
        self.typed_words = 0
        """
        Has user typed anything yet?
        """
        self.typed = False
        self.reset_words_count()

    def increment_words_count(self):
        """
        Increments 1 to total amount of words
        """
        self.typed_words += 1

    def reset_words_count(self):
        """
        Resets the total amount of words typed
        """
        self.typed_words = 0
