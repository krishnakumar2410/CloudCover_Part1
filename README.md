# CloudCover_Part1_FrontEndAutomation

# Tools/Technology Used
- Selenium
- Python
- pytest: Unittest framework

1. Install Pycharm editor if not already installed
2. Go to filea and click on create new project> Import downloaded project

** Packages Required
- pytes
- pytest-html
- selenium
- webdriver-manager

For installation, go to File>Setting>Project:CloudCover>Python Interpreter > Add package

# Folder Structure
Project Name: CloudCover
>Logs: Execution logs getting stored here
>Reports : Html file gets generated here, which we can open and check execution results for __pass/fail__
>TestCases: test_part1 is the test case created to achive part 1 assignment
>Utilities : Here logger file created to print and store the logs for each execution


# Run Instructions
- Go to terminal tab of the pycharm
- Use below command to run

> pytest -s -v TestCases/test_Part1.py --html=./Reports/testresult1.html
