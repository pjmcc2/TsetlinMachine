Work realted to O. Granmo's textbook



**Exercise 1**:

*What is the structure of a Tsetlin Machine rule?*

A TM rule takes the form of a sequence of logical propositions, e.g. not blue and has four wheels and does not have wings therefore car

-------------------------------------------------------------------------------

**Exercise 2:**

*How are data features prepared as input to a Tsetlin Machine?*

Data are transformed into Booleans. For example, a simple feature may already be in Boolean form, like whether the sample has wings or not. However, things get a little more complicated with continuous features like height. From what I have seen so far, it looks like one chooses a slice of the continuous space for to create as a new feature, i.e. 0-2, 2-4, etc. From there the feature becomes a Boolean expression: Has wings, and is not 0-2 inches tall, and is 2-4 inches tall.


-------------------------------------------------------------------------------

**Exercise 3:**

*What are the three learning steps for a Tsetlin Machine?*


The three learning steps for a Tsetlin Machine are:

1.) Rule Evaluation

    The rule (each rule) is tested on a given input.

2.) Recognize Feedback

    If the rule evaluates to True (i.e. the literals of the example match the rule)
    this step is performed. The literals (individual boolean features) that are
    True of the object are incremented up towards maximally memorized. Likewise
    the features that are False are decremented towards maximally forgotten. 

3.) Erase Feedback

    If the rule evaluates to False (the literals of the example do not match the rule), this step is performed. Each literal regardless of its truth value is 
    decremented towards forgotten.

Note: There is also optional added randomness. This is included with the Memorize/Forget Value, a probability in which at any given increment, or decrement respectively, actually be performed. To my understanding this helps prevent over/under fitting by randomly over/under emphasising random features. In the average long run the features that matter will be learned, but with higher variance. 

4.) Reject Feedback

    If the rule evaluates to True (literals match rule) but the example belongs
    to the wrong class, this step triggers and instead of 2 and 3.
    All False AND forgotten literals are memorized WITHOUT randomness.

--------------------------------------------------------------------------------

**Exercise 4:**

*When and why are False and Forgotten literals memorized?*

False literals are incremented towards maximally memorized in step 4 other wise known as Reject Feedback or Type II feedback. This occurs when the rule evaluates to True but the class is incorrect. The effect is stated above.

--------------------------------------------------------------------------------

**Exercise 5:**

*What part of Tsetlin machine learning coordinates the learning of
multiple rules and how is the coordination done?*

The Vote Margin coordinates learning multiple rules at once. The margin works as follows: given a vote margin hyperparameter M := 2, count all True-evaluated rules (literals match the rule) and sum the votes for the class. If sum is greater than M or lesser than  -M clip to +-M. Finally input into formula 
(M - clip(sum))/2M. This creates a probability for which each rule is given feedback. This gradually shifts the characteristics of each rule towards supporting the voting margin. In other words, the rules are given feedback more when the vote sums to far from the margin, and given feedback less often when near to the margin. The effect pushes the rules towards that dynamic. 

--------------------------------------------------------------------------------

**Exercise 6:**

*When is Recognize Feedback triggered and how is this feedback related to the Tsetlin machine learning steps?*

See step 2. This step is triggered when the given rule evaluates to True (literals match the rule) and the class matches the training class. In a machine with multiple rules, if the rule evaluates to True, and majority vote matches the correct class, the given rule will trigger Recognize Feedback with probability (VoteMargin - Clip(VoteSum))/(2*VoteMargin). 

This feedback memorizes True literals and forgets false literals (with probability as a hyperparameter). This is the "pattern learning" process, as the rule increments closer to the True pattern (in the long run).

--------------------------------------------------------------------------------

**Exercise 7:**

*When is Reject Feedback triggered and how is this feedback related
to the Tsetlin machine learning steps?*

See Step 4. This step is triggered when the rule evaluates to True, but the class does not match. The False AND forgotten literals are all incremented towards memorized. This in essence pushes all of the "unused" features towards being used to discriminate between classes. For example, if the rule is if Blue and Transports people then car, but the example which is both blue and transports people is a plane, then the reject feedback step is triggered. Features that are forgetten (everthing except is blue and transports people) and that are False, (for example has 4 wheels is false for a plane) would be incremented. If a few more examples like this were shown to the rule, perhaps the new rule would become if Blue and has four wheels and Transports people then Car would no longer evaluate to True in the case of the Plane example. 

--------------------------------------------------------------------------------

**Exercise 8:**

*What happens if we set the Forget Value closer to 0.0?*

The Forget value is 1-Memory Value. It is the probability in which a decrement in Type Ia and Ib (steps 2 and 3) or Recognize/Erase feedback is actually performed. If the value is close to 0, it means that both increments in step 2 are more frequent and decrements in step 2 and 3 are less frequent. This means rules maintain their clauses more often, and become more complicated (more literals are included). This means the rules are more selective (biased) and more powerful (e.g. squiggly line instead of straight line in a regression).

--------------------------------------------------------------------------------
