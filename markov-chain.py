'''
Markov Chain
'''

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