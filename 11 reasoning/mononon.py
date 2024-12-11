class MonotonicReasoning:
    def __init__(self):
        self.knowledge_base = set()
    
    def add_fact(self, fact):
        self.knowledge_base.add(fact)
        print(f"Added fact: {fact}")
    
    def query(self, fact):
        return fact in self.knowledge_base
    
class NonMonotonicReasoning:
    def __init__(self):
        self.facts = {}
        self.defaults = {}
    
    def add_fact(self, fact, truth_value=True):
        self.facts[fact] = truth_value
        print(f"Added fact: {fact} = {truth_value}")
    
    def add_default_rule(self, condition, conclusion):
        self.defaults[condition] = conclusion
        print(f"Added default rule: If {condition} then typically {conclusion}")
    
    def query(self, fact):
        # Check direct facts first
        if fact in self.facts:
            return self.facts[fact]
        
        # Check default rules
        for condition, conclusion in self.defaults.items():
            if condition in self.facts and self.facts[condition] and conclusion == fact:
                return True
        
        return False

# Example usage
def demonstrate_reasoning():
    print("Monotonic Reasoning Example:")
    mono = MonotonicReasoning()
    mono.add_fact("Socrates is human")
    mono.add_fact("All humans are mortal")
    print("Query: Is Socrates human?", mono.query("Socrates is human"))
    
    print("\nNonmonotonic Reasoning Example:")
    non_mono = NonMonotonicReasoning()
    non_mono.add_fact("bird")
    non_mono.add_default_rule("bird", "can_fly")
    print("Query: Can it fly?", non_mono.query("can_fly"))
    
    # Adding exception
    non_mono.add_fact("penguin")
    non_mono.add_fact("can_fly", False)  # Override previous default
    print("Query after exception: Can it fly?", non_mono.query("can_fly"))

if __name__ == "__main__":
    demonstrate_reasoning()