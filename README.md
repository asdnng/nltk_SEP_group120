# Report for Assignment 1

## Project chosen

Name:  Natural Language Toolkit (NLTK)

URL: https://github.com/nltk/nltk

Number of lines of code and the tool used to count it: Lizard

Programming language: Python

## Coverage measurement

### Existing tool
: Coverage.py
<Inform the name of the existing tool that was executed and how it was executed>

<Show the coverage results provided by the existing tool with a screenshot>
<img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/overall_coverage.PNG" alt="original_coverage">

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Yujin Choi>

<Function 1 matchBrackets>

matchBracket.py URL : https://github.com/asdnng/nltk_SEP_group120/blob/fb41395d8a649f54f2ded22d1bb11c9153a7039d/nltk/ccg/lexicon.py
<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/match_results.png" alt="match_coverage_report">
</div>

<Function 2 _get_pos>
_get_pos.py URL : https://github.com/asdnng/nltk_SEP_group120/blob/fb41395d8a649f54f2ded22d1bb11c9153a7039d/nltk/corpus/reader/wordnet.py
<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getpos_results.png" alt="getpos_coverage_report">
</div>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Yujin Choi>

<Test 1>

enhanced matchbracket.py URL : https://github.com/asdnng/nltk_SEP_group120/blob/main/nltk/ccg/lexicon.py

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/match_results.png" alt="match_coverage_report">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/match_enhanced.png" alt="match_enhahnced">
</div>

<State the coverage improvement with a number and elaborate on why the coverage is improved>
 The main reason for the improved coverage is that I added test cases and improved existing test cases to extend them to test all conditional branches. Previously, only some branches were tested, but I added test cases that could handle all input conditions so that each branch could be executed. So, coverage of the previous version was 60%, after enhancement, I got 100% test coverage.

<Test 2>

enhanced _get_pos.py URL : https://github.com/asdnng/nltk_SEP_group120/blob/main/nltk/corpus/reader/wordnet.py

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getpos_results.png" alt="getpos_coverage_report">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getpos_enhanced.png" alt="getpos_enhahnced">
</div>

 This function also has 100% test coverage after enhancement after I added some test cases like the first one. Before the improvement, coverage of this function was 25%
## Coverage measurement

### Your own coverage tool

<Niek>

<Token.str>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>
<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/branchgetstr-precoverage.png" alt="str-instrumentation">
</div>

<getinfo>
<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/branchgetinfo-precoverage.png" alt="getinfo_instrumentation">
</div>

<Provide the same kind of information provided for Function 1>



## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Niek>

<Test 1: test_str>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/branchgetstr-precoverage.png" alt="str-instrumentation">
</div>

<Provide a screenshot of the new coverage results>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getstr improved coverage.png" alt="str-improvement">
</div>

<State the coverage improvement with a number and elaborate on why the coverage is improved>
The coverage improved from 0% covered to 100% covered
Specific tests were written to check the output of the str method both with and without semantics. This ensures that all branches in the str method are exercised.

<Test 2: test_getinfo>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/branchgetinfo-precoverage.png" alt="getinfo_instrumentation">
</div>

<Provide a screenshot of the new coverage results>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getinfo improved coverage.png" alt="getinfo-improvement">
</div>

The coverage improved from 50% covered to 100% covered
Additional test cases were written to cover all possible branches in the getinfo    function. For example, tests were added to ensure that functions with variable arguments, keyword arguments, and closures are properly tested.
 

 ## Coverage measurement

 ### Your own coverage tool

 <Junhyeok Lee>

<rte_classifier>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/rte_classify_old_coverage.png">
</div>

<call_tadm>

<Provide the same kind of information provided for Function 1>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/call_tadm_old_coverage.png">
</div>

## Coverage improvement

### Individual tests

<Junhyeok Lee>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/rte_classify_old_coverage.png">
</div>

<"Provide a screenshot of the new coverage results">

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/test_rte_classify_new_coverage_1.png">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/test_rte_classify_new_coverage_2.png">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/test_rte_classify_new_coverage_3.png">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/test_rte_classify_new_coverage_4.png">
</div>

(these were all produced in one command but because function has other printouts, had to separate the screenshots)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

Initial coverage measurement i conducted resulted in hitting only 2 branch flags out of 5 branch flags and there was another test case existed
, which was “..without megam” and “..with megam” tests. These both existing tests eventually hit only 3 branch flags out of 5, so I made two extra test cases to cover all branch flags at least one resulting to enhance coverage up to 100%. Test cases include an accepting algorithm, whether the sample was none or not and an unsupported algorithm where it was a hidden else statement for some, thus by considering these results full 100% coverage improvement.

<Test 2>

<Provide the same kind of information provided for Test 1>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/call_tadm_old_coverage.png">
</div>

<"Provide a screenshot of the new coverage results">

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/test_call_tadm_new_coverage.png">
</div>

I started with random args where none of the flags was hit in the beginning. So I created a whole new test case to test out all 6 branches. This function required the destination of the directory to test some branches, so if needed I added a fake address in the test if the branch can be hit although the functionality of code won’t work as it's not existing directories. As the test name states, tested input such as ["hello"], “hello” and etc, eventually made each test case to hit each branch flag at least once resulting in 100% coverage improvement.

## Coverage measurement

### Your own coverage tool

<Juan Sebastian Dhanaharsa>

<Function 1: can_combine>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/can_combine%20hithit.png">
</div>

<Function 2: combine>
<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/combine%20hit.png">
</div>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Juan Sebastian Dhanaharsa>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/can_combine%20coverage.png">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/can_combine%20hit.png">
</div>

<State the coverage improvement with a number and elaborate on why the coverage is improved>
Since the initial of my implementation of tests for the can_combine method, I achieved 100% branch coverage from 0% without the need for further enhancements. But, I experienced some errors at first in my code which makes the test itself doesn't even run rather than a decrease in coverage percentage. 

<Test 2>

<div align="center">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/combine%20coverage.png">
  <img src="https://github.com/asdnng/nltk_SEP_group120/blob/main/images/combine%20hithit.png">
</div>

From the start of testing the combine function, I managed to secure 100% on my coverage testing from 0% without necessitating any additional modifications.

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>



<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

Yujin Choi(2769224) : made test printing function that all group members can use, selecting subject

Juan Sebastian Dhanaharsa(276575) : 

Junhyeok Lee (2777848) : In the beginning helped tracking down to install module specific in order to test out the functions (nltk data installation). Then further conducted my coverage measurement both by given tool and by my own method. Later created one new test case for call_tadm and enhanced existing rte_classifier test case by adding more cases, and eventually proved to improve by 100%. Later further contributed to the teammates when they struggled or had unclear instructions were found.
