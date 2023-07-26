# 2023-07-25 dev env workshop

**Table of contents:**
- [2023-07-25 dev env workshop](#2023-07-25-dev-env-workshop)
- [Introduction](#introduction)
- [Main contents](#main-contents)
	- [Terminal](#terminal)
	- [VSCode/Python/Jupyter](#vscodepythonjupyter)
	- [Linter](#linter)
	- [VS code short-cut](#vs-code-short-cut)
	- [Formatter](#formatter)
	- [requirements](#requirements)
	- [Git](#git)
	- [Git VS github](#git-vs-github)
	- [branch](#branch)
	- [What's Fork and branching](#whats-fork-and-branching)
	- [Reference](#reference)


# Introduction

Go over some industry standard to make your life and your team life easier by Leon

# Main contents

## Terminal

Navigate in terminal is a must-have for any one want to do any dev work as DA, DS and DE. Some of the plug-ins will make your life easier

- terminal plugins:
	- [fzf](https://github.com/junegunn/fzf)
		- fuzzy match to locate your command
	- [autojump](https://github.com/wting/autojump)
		- make `cd` great again
	- autosuggestions
- Conda vs pip for package management
	- `conda` is popular among DS. it has multiple distribution: 
		- miniconda for minimalist. 500MB ish
		- anaconda so it has GUI. kinda big
	- `pip` is built-in with python, super light-weight. 
	- Comparison
		- conda's environment doesn't live with the project while pip's venv lives with the code. If you have an environment that you need to use for multiple similar project, you can try `conda` so i will not cluster your workspace

## VSCode/Python/Jupyter

## Linter
- linter
	- linter is a style and standard to write your code. For python, the most popular standard is  called [pep8](https://peps.python.org/pep-0008/). So we will have snake_case for python etc. We need some tools to enforce it every single time since it's hard to adhere to rules all the time. Therefore, you can select some linter for your python code. Popular ones are [black](https://pypi.org/project/black/) and [autopep8](https://pypi.org/project/autopep8/)
	- linter it typically built-in as one of the `pre-commit` process to ensure when every1 push their code for review.


## VS code short-cut

Leon introduced many short-cuts in VS code that will make our life easier. You can check out [VScode tech with tim](https://www.youtube.com/watch?v=phC-vKlNoaM&ab_channel=TechWithTim).

It's going to make our life easier!


## Formatter

Format your code on save in VS code
- `command + p` to bring up command pallete
- type settings and search for `save`

Check out the [following link](https://code.visualstudio.com/docs/python/editing) under the heading formatting for details and windows version.

## requirements

In terminal, we could export packages to a file `requirements.txt` for the following purpose
- more portable for other people to use to another machine

```python
pip freeze > requirements.txt
```


## Git 

Git is for version control and collaboration for multiple people. It manages:
- multiple developer to work on the same project
- control multiple version of the same code in a organized manner

It's a very long topic that you need to master, please go to reference to find resources to understand it thoroughly since it will be ur bread and butter.

## Git VS github

- `git` is a tool built for version control code  
- `github` is a service built on top of `git`. It serves as a remote server to store your code. It also provides more features and UI to make your experience with `git` easier. 

## branch
- branch
	- `dev branch`: for develop a feature or hot-fix a bug. 
	- `staging branch`: staging branch is "review-ready" branch. It sits in between your feature branch and main branch.
	- `main branch`: it's protected and used for production. You need a pull request to push your code.
- pull request
	- a way for developer to propose changes (personal work) to the codebase (collective work)

> Interestingly, pull request is not a feature of `git` but `github`/`gitlab` 

## What's Fork and branching

When you work on your side project,
- you create remote repo on github
- you add remote repo to link it up with your local repo. (`git remote add`)
- you develop on your local and push to it at the end of the day

You can push your work for your side project since you have the access and admin privilege to everything.

Fork is a process that for you to work with a open-source project that you don't have access. The normal process is to:
- fork it from [longchain-ai](https://github.com/langchain-ai/langchain). The process will create an instance of the project on your remote repo. You "borrowed" the code from longchain's remote repo to your remote repo.
- Now you clone it locally and work as normal.
- You push your code to YOUR REMOTE REPO instead of longchain's repo.
- You create a PR request to see whether they accept your proposed changes or not.


## Reference

- [git and git bash for windows user](https://www.youtube.com/watch?v=7BOrUHFu44A&ab_channel=HowTo)
- [VScode shortcut like a pro by tech with tim](https://www.youtube.com/watch?v=phC-vKlNoaM&ab_channel=TechWithTim)
- Youtuber David Mahle's series, solid free courses to master git, after this, you should be good to go. Do practice with it tho
	- [Introduction to Git - Core Concepts](https://www.youtube.com/watch?v=uR6G2v_WsRA&t=1504s)
	- [Introduction to Git - Branch and merging](https://www.youtube.com/watch?v=FyAAIHHClqI)
	- [Introduction to Git - Remotes](https://www.youtube.com/watch?v=Gg4bLk8cGNo&t=1331s)
