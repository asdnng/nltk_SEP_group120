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


### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Yujin Choi>

<Function 1 matchBrackets>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


![match coverage report](https://github.com/asdnng/nltk_SEP_group120/blob/main/images/match_results.png)

<Function 2 _get_pos>
![getpos_coverage report](https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getpos_results.png)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Yujin Choi>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>


![match coverage report](https://github.com/asdnng/nltk_SEP_group120/blob/main/images/match_results.png)
![match new coverage report](https://github.com/asdnng/nltk_SEP_group120/blob/main/images/match_enhanced.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>
 The main reason for the improved coverage is that I added test cases and improved existing test cases to extend them to test all conditional branches. Previously, only some branches were tested, but I added test cases that could handle all input conditions so that each branch could be executed. So, coverage of the previous version was 60%, after enhancement, I got 100% test coverage.

<Test 2>

![getpos_coverage report](https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getpos_results.png)
![getpos_new coverage report](https://github.com/asdnng/nltk_SEP_group120/blob/main/images/getpos_enhanced.png)
<State the coverage improvement with a number and elaborate on why the coverage is improved>
 This function also has 100% test coverage after enhancement after I added some test cases like the first one. Before the improvement, coverage of this function was 25%

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>



<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

Yujin Choi(2769224) : matchbracket funtion in lexicon.py & _get_pos function in wordnet.py
