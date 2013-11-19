Coding-Puzzles-Day
==================

Any LUG member, including officers, who has not seen the source for the exemplar solutions, is eligible to compete.

Language Guidelines:
--------------------
Puzzles may be solved in any language, with this caveat: If you want to compete for fastest solution to a given puzzle, you must specify what dependencies your language requires to run at the beginning of the hour. Timing tests will all be performed on a ThinkPad X230 running Ubuntu on the 3.5.0-17-generic kernel with a core i5 processor and 4GB of RAM. If you use an unusual language which takes more than an hour to set up on such a system, your solutions will not be eligible to compete for fastest time.

If the language you're considering doesn't run on Linux at all, you should ask yourself why you're bringing it to a LUG coding competition, and consider taking the opportunity to explore a more open alternative.

The "debug this code" problems in each category will be written in either C or Python, at the challenge organizers' discretion. 


How to win:
-----------

LUG members will have 1 hour to use however they see fit in solving puzzles. Rules will be read at 6pm, and problems will be distributed once any questions on the rules have been answered. The challenge inputs will be distributed 45 minutes after the competition starts, and solutions must include both the source code and the output when that code is run on the challenge input. Solutions must be submitted within 60 minutes to score. 

After 1 hour, each competitor will submit their source and solutions to the GitHub repo. If they have trouble with GitHub, they can save their files to a USB stick and a club officer who was not competing in the challenge will commit the code for them. 

The solutions will be compared to each problem's correct solution, and points will be awarded to those whose solutions match.

After  the winners are announced, we will have a discussion in which the exemplar code for each problem is projected onto the screen, and the room discusses the ways in which the problems were worded  ambiguously, the code was buggy, or other reasons that they should have  gotten more points. If the room can unanimously agree that  there was a bug in a "correct" solution and how to fix it, the solution  will be fixed, the correct solutions will be re-generated, and the  competitors' entries will be re-scored.

The prizes will be fame, glory, bragging rights (put it on your resume!), and probably pizza.


The rules about Wikipedia and StackOverflow and stuff:
------------------------------------------------------

Competitors should make every effort to avoid reading source code which solves any coding competiton problem during the competition. Reading outlines of algorithm solutions is fine; reading snippets of source which demonstrate individual techniques in your language is fine. Finding a pre-made solution and then claiming it as your own work is not.

Going out and pre-writing a solution to one of the problem between when these rules are posted and when the competion starts would violate the spirit of this rule. However, since we have no way to prove when you wrote what, this rule will be enforced only by your personal integrity.


The rules about teams or lack thereof: 
--------------------------------------

This competiton is designed to take the right amount of time for individual programmers at a variety of levels. Pair programming (where two people use the same computer to write one piece of code that solves a task) is acceptable; two people working in parallel then swapping code for solutions they didn't work on is not. As with the Wikipedia rule, giving advice or insight about the problem or about debugging strategies to another competitor is okay; giving them source code is not. Again, it's on the honor system.


How scoring works:
------------------

Each level has one problem to implement and one problem where you'll be given slightly broken code to debug. Each competitor may attempt as many problems, from as many different levels, as they wish. Only solutions whose outputs exactly match the correct outputs will gain points. Each working solution (ie  solution whose output matches the test output) will receive the number  of points specified. The implementation and debugging challenges have the same point value.

"Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it." --Brian Kernighan


Fast code bonus:
----------------

Each piece of code which successfully completes a challenge will be timed as specified above, and the fastest working solution will earn an extra 2 points. The speed challenge includes the code used to  generate the correct solutions, if none of the competitor-submitted  code is faster than the exemplar, no competitor gets the 2-point bonus  for that problem.


The Puzzles
-----------

Expert level: (7 points each)

    Implement: Traveling Salesman

    Debug: Sum of Subsets

Intermediate level: (5 points each)

    Implement: Anagram finder

    Debug: Tree traversal

Beginner level: (3 points each)

    Complete the code: A linked list implementation
    
    Debug: An in-place array sort
