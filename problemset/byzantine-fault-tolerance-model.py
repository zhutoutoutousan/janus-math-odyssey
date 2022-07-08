'''
# Byzantine Fault Tolerance Model
## Related papers:
- https://medium.com/loom-network/understanding-blockchain-fundamentals-part-1-byzantine-fault-tolerance-245f46fe8419
- https://sourcegraph.com/search?q=context:global+byzantine&patternType=literal
- https://lamport.azurewebsites.net/pubs/byz.pdf

# My thinking
## How to make a Byzantine Fault Tolerance Model 100% robust?
- Add credibility, robustness field to every general node. Create a sandbox to train it
'''
class byzantine_model:
    # 1. Create a sandbox to train the model
    # 2. Train the model
    # 3. Create a sandbox to test the model
    # 4. Test the model

    # __init__
    def __init__(self):
        self.generals = []
    
    def add_general(self, general):
        self.generals.append(general)

    def train(self):
        pass
    

