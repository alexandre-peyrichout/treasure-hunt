import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

from src.game import Game


def test_example_from_email():
    dir = "example_from_email"
    new_game = Game(f"./tests/{dir}/input.txt", f"./tests/{dir}/output.txt")
    new_game.play()

    output_file = open(f"./tests/{dir}/output.txt", "r")
    expected_output_file = open(f"./tests/{dir}/expected_output.txt", "r")
    assert output_file.read() == expected_output_file.read()
