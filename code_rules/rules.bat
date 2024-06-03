@echo off
cd ..
flake8 --config=code_rules/.flake8

pylint * --rcfile=./code_rules/.pylintrc

black --config ./code_rules/black.toml .
