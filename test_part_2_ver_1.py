#! /usr/bin/env python3
# """
# Mocking input for testing.
#
# In this test file we will see a method of testing input by mocking out the
# built-in input() function, as well as capturing output. Additionally, we will
# parameterize the tests to run on multiple data sets.
#
# 1. mock input using monkeypatching
#     1a. understand generators
# 2. capturing output with capsys
# 3. parameterizing input to the tests
# 4. tesing for exceptions
#
# """
import pytest

from part_2 import do_division


@pytest.mark.parametrize(
    "dividend, divisor, quotient",
    [("1", "2", "0.5"), ("1", "4", "0.25"), ("3", "4", "0.75"), (1, 2, 0.5)],
)
def test_do_division(monkeypatch, capsys, dividend, divisor, quotient):
    # """
    # Test the do_division() function.

    # Parameters
    # ----------
    # monkeypatch : obj
    #     The monkeypatch object allows us to patch, at run time, the
    #     funcionality of a pre-existing object.
    # capsys : obj
    #     Captures any output to either stdout or stderr
    # dividend : str, int
    #     The value being divided for this test
    # divisor : str, int
    #     The value being divided by for this test
    # quitient : str, float
    #     The result of the division
    # """

    # create a generator object, inputs, that will return the values passed to
    # it one at a time
    inputs = args_generator(dividend, divisor)

    # monkeypatch the input() function to return only the input we want it to
    # by temporarily replace the "actual" input function with one of our own
    monkeypatch.setattr("builtins.input", lambda x: next(inputs))

    # call do_division(), it will get its input values from the monkeypatched
    # input()
    do_division()

    # capture all output to stdout and stderr produced by do_divison()
    captured = capsys.readouterr()

    # assert that the output to stdout is equal to what we were expecing
    # (note: we do nothing with stderr here)
    assert captured.out.strip() == f"{dividend}/{divisor} = {quotient}"


def args_generator(dividend, divisor):
    # """
    # Generate arguments for the do_division() test.
    #
    # Parameters
    # ----------
    # dividend : str
    #     the number we will be dividing into
    # divisor : str
    #     the number we are dividing by
    # """
    vals = dividend, divisor  # tuple packing at its finest
    for val in vals:
        yield val


def test_do_division_by_zero(monkeypatch, capsys):
    # """
    # Test the do_division() function.

    # Parameters
    # ----------
    # monkeypatch : obj
    #     The monkeypatch object allows us to patch, at run time, the
    #     funcionality of a pre-existing object.

    # capsys : obj
    #     Captures any output to either stdout or stderr
    # """

    # create a generator object, inputs, that will return the values passed to
    # it one at a time
    inputs = args_generator("5", "0")

    # monkeypatch the input() function to return only the input we want it to
    # by temporarily replace the "actual" input function with one of our own
    monkeypatch.setattr("builtins.input", lambda x: next(inputs))

    # call d0_division() and it will get its values from the labmda above
    with pytest.raises(ZeroDivisionError):
        do_division()
