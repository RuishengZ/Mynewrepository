class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        # Set counters for both Cows and Bulls
        cow = 0
        bull = 0
        
        # check for Bulls
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                secret = secret.replace(secret[i], "#", 1)
                guess = guess.replace(guess[i], "#", 1)
                
        secret = secret.replace("#", "", bull)
        guess = guess.replace("#", "", bull)
        
        # check for Cows
        for i in range(len(secret)):
            if guess[i] in secret:
                cow += 1
                secret = secret.replace(guess[i], " ", 1)
        
        # Output the result
        return str(bull) + 'A' + str(cow) + 'B'
        