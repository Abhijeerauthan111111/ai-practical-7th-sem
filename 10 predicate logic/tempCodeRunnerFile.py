class Predicate:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return f"{self.name}({', '.join(self.arguments)})"

class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, predicate):
        self.facts.append(predicate)

    def add_rule(self, conclusion, conditions):
        self.rules.append((conclusion, conditions))

    def query(self, predicate):
        # Check if the predicate matches any fact directly
        for fact in self.facts:
            if self._match_predicates(predicate, fact):
                return True

        # Check if the predicate can be proven using rules
        for rule in self.rules:
            conclusion, conditions = rule
            if self._match_predicates(predicate, conclusion):
                all_conditions_true = all(self.query(cond) for cond in conditions)
                if all_conditions_true:
                    return True
        return False

    def _match_predicates(self, pred1, pred2):
        return (pred1.name == pred2.name and 
                len(pred1.arguments) == len(pred2.arguments) and 
                all(arg1 == arg2 for arg1, arg2 in zip(pred1.arguments, pred2.arguments)))

# Example usage
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Adding facts
    kb.add_fact(Predicate("human", ["Socrates"]))
    kb.add_fact(Predicate("human", ["Plato"]))
    kb.add_fact(Predicate("mortal", ["Plato"]))

    # Adding rule: All humans are mortal
    rule_conclusion = Predicate("mortal", ["X"])
    rule_conditions = [Predicate("human", ["X"])]
    kb.add_rule(rule_conclusion, rule_conditions)

    # Testing queries
    print("\nKnowledge Base Queries:")
    print("Is Socrates human?", kb.query(Predicate("human", ["Socrates"])))
    print("Is Socrates mortal?", kb.query(Predicate("mortal", ["Socrates"])))
    print("Is Plato human?", kb.query(Predicate("human", ["Plato"])))
    print("Is Plato mortal?", kb.query(Predicate("mortal", ["Plato"])))
    print("Is Zeus human?", kb.query(Predicate("human", ["Zeus"])))