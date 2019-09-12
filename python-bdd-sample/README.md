conda create -n pytest python pytest coverage
conda env create -f environment.yml
conda activate pytest

coverage run my_program.py
coverage report