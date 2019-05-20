# Testing Demos

You may remember in class today I was having difficulty with vscode's test runner not showing the results of running my tests despite them being run and the results being available in the output pane. After some experimenting it seems that the test runner was not happy with my having docstrings in the test file. After commenting them out test runner behaved as expected. I will continue to examine the issue and, if necessary, report the bug to the maintainers. Regardless, the tests are now running and test runner is showing their status as expected.

## Files in this repo

- **iter_demo.py:** This file is the result of our _brief_ exploration of writing an iterator and comparing them to generators
- **part_2.py:** This file is unchanged from the version that was given as part of the starter set for the lab. In retrospect, the calls to `int()` should have been calls to `float()` as that would have made more sense and would have made the program, such as it is, more flexible.
- **test_part_2_ver_1.py:** This is the version of the test we built in class today. It uses a [lambda function](https://dbader.org/blog/python-lambda-functions) to get values from the generator and provide input to `do_division()`.
- **test_part_2_ver_2.py:** This is a second version of the test I built which replaces the lambda function with an inner function that performs the same task. While the effect and output are identical, some people may prefer having an actual function to call instead of the lambda. It may also be instructional to compare the two versions to contrast them against each other.

## Notes

The files presented here are a good start in writing more advanced tests which mock I/O for the functions being tested.

We see a single example of testing for an exception. There is a lot of work to do to ensure that the code being tested is bulletproof, however.

For example, it would make a lot of sense to wrap the code in the function in a `try/catch` block and handle the error more elegantly there. What do you suppose the tests for that would look like? How would you go about testing for "accidental" bad input from the user?
