## Introduction
Welcome to the second post of WTF Python. Last time we made a pure python clone of 'ls' tool used in GNU/Linux distributions.Last articles focus was using git branches to add new features in our application.
Today we will make a pure python clone of tool 'cat' which stands for concatenate which is used to print contents of a file or concatenate contents of multiple files.

## Today's focus
Today we will discuss a lot of Test Driven Development.We will start using unittest and even use tool called coverage.py to find the coverage of our tests.

## Let's start
If you have not already create a directory called pycat(Our project name) and create a git repository inside it.Then create directory inside the original pycat directory called pycat and make it a module by creating a '\_\_init\_\_.py' file inside it.Then make '\_\_main\_\_.py' so that we can use our project as a python module.Ex
```sh
mkdir pycat
cd pycat
mkdir pycat
touch pycat/__init__.py
$EDITOR pycat/__main__.py
python -m pycat
```
## Approach and Milestones
This project's very easy. So easy that we need no more than one file.I will not be revealing any code but if you are stuck more than a hour then refer to my [*code*](https://github.com/pspiagicw/pycat).
There are some milestones that we will follow this breaks the project into small objectives .So that you can focus on one functionality only.
 - First one is that we should accept a list of files as arguments.We do not want to check if it's a valid file or not.Just print the list of files passed as arguments.If you don't already know ,you should look at argparse module.It's the best way to implement this feature.If you are stuck look at [*this*](https://realpython.com/command-line-interfaces-python-argparse/) or [*this*](https://docs.python.org/3/library/argparse.html).Be sure to not copy the code in the article and understand and implement it yourself.
```sh
python -m pycat file1 file2 file3
# Output>> ['file1','file2','file3']
```
 - The next objective would be that to read the contents of the given files and print it's content.If you are stuck at this part you should look at [*this*](https://realpython.com/working-with-files-in-python/) article.But again be sure to not copy the code in the article and simply understand the usage and implement it yourself.

## TDD
Now that we have somewhat working project we should write tests for it.Though according to TDD(Test Driven Development) we should write test even before writing the starter code.But I am letting this part go as this was my first time using TDD Development.
We will be using unittest module in the python standard library to write tests.If you want to use pytest or nose2 as a testing framework.You can do that after implementing unittest tests.
## Testing
For testing create a directory in our project root called tests.
```sh
mkdir tests
```
then create a file that has 'test_' as the first part of the file.As unittest requires it by default.You can configure unittest for other patterns but it depends on your coding style.
Refer to unittest's [*documentation*](https://docs.python.org/3/library/unittest.html) on doc.python.org or refer to a more [*friendly*](https://realpython.com/python-testing/) documentation.But refer to official documentation for the true reference.
If you are confused then look at my [*code*](https://github.com/pspiagicw/pycat).
After you have implemented basic tests for argument testing and whether it actually print's contents of a file.You can move to the next section

### Moving Forward
Before implementing the next feature.We would write it's test following TDD.The next feature will be numbering the lines.Write a test for it and run the test suite.It should fail.

### New feature.
Now that the tests fail we should write the feature out.And yes we will be doing in a git branch format.If you are uncomfortable with it.Just refer to my previous post.
It should be pretty easy and once finished run the test suite once it run's successfully then. We are done.Merge the feature branch with the master branch.

## Extensions.
Referring to manpage of cat.We do not have more features to implement that are cool.If you think about it please comment below.If you think you can do it, implement it and share it in the comments below.Your comments are the best thing about this series.

## Coverage.py
If are up to this task.Let's begin by explaining what is coverage.py .It's a tool that find's out how much of your code is tested.To use it install it will pip
```sh
pip install coverage
```
You can refer it's official documentation and without putting much effort you should know the coverage percentage of you project.See if you can make it into 100%.Share your percentage in the comments below.

## GoodBye
GoodBye fellas and meet in the next post.If are looking for something more like this. Then look at [*Robert Heaton's*](https://robertheaton.com/2018/12/08/programming-projects-for-advanced-beginners/) blog.His blog inspired me to write this series.Implement his project #7 as it would be used in the next post.

