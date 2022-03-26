# More-Python-Projects
This is a collection of python programs related to NFA's, DFA's, etc.
- NFAtoDFA.py will convert a nondeterministic finite automata into a deterministic finite automata
- minimizeDFA.py will take a deterministic finite automata and minimize it to its optimal state
------------------------------------------------------------------------------
DFA refers to Deterministic Finite Automaton. A Finite Automata(FA) is said to be deterministic, if corresponding to an input symbol, there is single resultant state i.e. there is only one transition. A deterministic finite automata is set of five tuples and represented as, M = {Q, Σ, δ, q0, F} where, 
- Q: A non empty finite set of states present in the finite control(qo, q1, q2, …). 
- Σ: A non empty finite set of input symbols. 
- δ: It is a transition function that takes two arguments, a state and an input symbol, it returns a single state. 
- qo: It is starting state, one of the state in Q. 
- F: It is non-empty set of final states/ accepting states from the set belonging to Q. 
------------------------------------------------------------------------------
NFA refers to Nondeterministic Finite Automaton. A Finite Automata(FA) is said to be non deterministic, if there is more than one possible transition from one state on the same input symbol. A non deterministic finite automata is also set of five tuples and represented as, M = {Q, Σ, δ, q0, F} where, 
- Q: A set of non empty finite states. 
- Σ: A set of non empty finite input symbols. 
- : It is a transition function that takes a state from Q and an input symbol from and returns a subset of Q. 
- qo: Initial state of NFA and member of Q. 
- F: A non-empty set of final states and member of Q. 
------------------------------------------------------------------------------
DFA can be best described and understood as one machine. NFA is like multiple small machines that are performing computational activities at the same time. All DFAs are derived from NFAs. The main difference between DFA and NFA, the two classes handling the transition functions of finite automata/ finite automaton theory, impact their behaviour in many ways.
