# Exercise 9
import numpy as np
from numpy.random import default_rng
from warnings import warn

# Data from Table 1.1 as booleans
x_raw = np.array([[True, True, False, False, True],
                  [True, True, False, True, False],
                  [True, True, False, True, False],
                  [True, True, True, False, True],
                  [True, False, True, True, False],
                  [False, True, True, False, True]])

y = np.array([[0], [0], [0], [1], [1], [1]])  # indicates class 0 or 1 NOT true or false


# Need to include negated literals
def neg(x):
    new = []
    for ex in x:
        temp = [not l for l in ex]
        new.append(temp)
    return np.array(new)


x_neg = neg(x_raw)
x = np.concatenate((x_raw, x_neg), axis=1)


class Rule:
    def __init__(self, depth, num_features, assigned_class, rng=None, seed=None):  # for now add rng
        self._depth = depth
        self._num_features = num_features
        self._class = assigned_class

        if rng is None:
            if seed is not None:
                self.rng = default_rng(seed)
                self._seed = seed
            else:
                self.rng = default_rng()
        else:
            self.rng = rng

        self.idx = []
        self.memory = [-1 for i in range(self._num_features)]

    def update_rule(self):
        self.idx = []
        for i in range(len(self.memory)):
            if self.memory[i] >= 0:
                self.idx.append(i)


def evaluate_rule(rule, example, y=None, return_class_match=False):  # check if rule evaluates to True
    # for this implementation, rules objects with a list of indeces of the literals
    if len(rule.idx) == 0:
        if return_class_match and (y is not None):
            class_truth = rule._class == y  # hmmm
            return True, class_truth
        else:
            return True

    curr = True
    for i in rule.idx:
        curr = curr and example[i]
        if curr == False:
            break

    if return_class_match == False:
        if y is not None:
            warn("{a} is not used unless return_class_match = True".format(a=y))  # hmmm
            return curr
    else:
        class_truth = rule._class == y  # hmmm
        return curr, class_truth


def recognize_feedback(rule, example,
                       mem_rate):  # To recognize feedback, each literal's position in the memorize-forget curve is incre/decre-mented
    for i in range(len(rule.memory)):
        prob_val = rule.rng.uniform()
        if example[i] == True:
            if prob_val <= mem_rate:
                if rule.memory[i] < rule._depth:
                    rule.memory[i] += 1

        elif prob_val >= mem_rate:
            if rule.memory[i] > -1 * rule._depth:
                rule.memory[i] -= 1
    rule.update_rule()


def erase_feedback(rule, example, mem_rate):  # do I need example here?
    for i in range(len(rule.memory)):
        prob = rule.rng.uniform()
        if rule.memory[i] > -1 * rule._depth:
            if prob >= mem_rate:
                rule.memory[i] -= 1
    rule.update_rule()


if __name__ == "__main__":
    # Make a new rule!
    rng = default_rng(seed=1066)

    memory_depth = 10
    memorize_value = 0.5

    first_rule = Rule(memory_depth, len(x[0]), 0, rng=rng)

    for i in range(len(x)):
        print("After {i} examples the Rule is: ".format(i=i), first_rule.idx)
        rule_truth, class_truth = evaluate_rule(first_rule, x[i], y[i], True)
        if class_truth:
            if rule_truth:
                recognize_feedback(first_rule, x[i], memorize_value)
            else:
                erase_feedback(first_rule, x[i], memorize_value)
        else:
            if rule_truth:
                print('reject feedback not yet implemented')
