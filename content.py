# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/george/Desktop/playground/dash-merchant")
# Your mock repo
mock_repo = git.Repo("/Users/george/Desktop/projects/bitbucket")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['mwaniki.george@gmail.com', 'george.mwaniki@spektra.co'])
importer.import_repository()


