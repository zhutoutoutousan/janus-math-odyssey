'''
Markov Chain

https://www.youtube.com/watch?v=WT6jI8UgROI

https://www.upgrad.com/blog/markov-chain-in-python-tutorial/
https://www.datacamp.com/tutorial/markov-chains-python-tutorial

'''

import random
import matplotlib.pyplot as plt

class markov_chain:
    '''
    Markov Chain
    '''
    def __init__(self, seed):
        '''
        Constructor
        '''
        self.seed = seed
        self.chain = {}
        self.build_chain()

    def build_chain(self):
        '''
        Builds the chain
        '''
        for i in range(len(self.seed) - 1):
            if self.seed[i] not in self.chain:
                self.chain[self.seed[i]] = {}
            if self.seed[i + 1] not in self.chain[self.seed[i]]:
                self.chain[self.seed[i]][self.seed[i + 1]] = 1
            else:
                self.chain[self.seed[i]][self.seed[i + 1]] += 1

    def generate_chain(self, length):
        '''
        Generates a chain
        '''
        chain = []
        chain.append(self.seed[0])
        for i in range(length - 1):
            chain.append(self.generate_next(chain[i]))
        return chain

    def generate_next(self, previous):
        '''
        Generates the next character
        '''
        if previous not in self.chain:
            return self.seed[0]
        total = 0
        for i in self.chain[previous]:
            total += self.chain[previous][i]
        random_number = random.randint(0, total)
        for i in self.chain[previous]:
            random_number -= self.chain[previous][i]
            if random_number <= 0:
                return i

    def generate_string(self, length):
        '''
        Generates a string
        '''
        string = ""
        string += self.seed[0]
        for i in range(length - 1):
            string += self.generate_next(string[i])
        return string

    def test(self):
        '''
        Tests the chain
        '''
        # Generate a chain
        chain = self.generate_chain(10)
        # Matplotlib
        plt.plot(chain)

if __name__ == "__main__":
    '''
    Main
    '''
    # Generate a seed
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Create a chain
    chain = markov_chain(seed)
    # Test the chain
    chain.test()
    # Generate a string
    string = chain.generate_string(10)
    # Print the string
    print(string)
    # Matplotlib
    plt.show()
    # Print the string
    print(string)
    # Print the seed
    print(seed)
    # Print the chain
    print(chain.chain)
    # Print the chain length
    print(len(chain.chain))
    