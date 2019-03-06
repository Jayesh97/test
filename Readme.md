# Merging YAML

Required Libraries : Pyyaml, os, collection

Steps to Run:
Step1: After Downloading the repo, check the path to ensure the tree is as such

![](/Images/test_Case1_tree.PNG)

Step2: Consider a Test case1 with the tress structure as seen in the pic

Step3: Observe the input.yaml files before they merge to the directory

![](/Images/before_modify.PNG)

Compare the YAML files and the objective to merge these files present in the parent directory

Step4: Execute the scrpit with 

#### python merge_logic.py path_to_file

The output can be shown as below. Observe the following changes, at position 1 we can see the 

![](/Images/Modified_file.PNG)

Verify the ouput which is the desired merge operation!!!


# Bonus - Using Travis for Continous Integration

A senerio may arise where many teams are working on the same Base_code, so each team has to commit, pull, rebase and commit again - even though the changes are minute, the job/project has to be tested and builds are to be made to make them deliverable for Contionous Deployment at any point of time. Travis CI is used for Continous Integration 

Travis CI with Git-Hub hosted code

Step 1: Sign-up with GitHUb

Step 2: Authorize travis to access the account 

Step 3: Enable travis in the repo

Step 4: Once travis is activated, we have to push something to the repo to trigger the CI

Step 5: Create a .travis.yaml file. This file will tell travis what to do. Just like Docker File or Jenkins file

![](/Images/yml file.PNG)

Step 6: Then commit these changes and push it to the github

Step 7: Enable the setting of Travis CI to enable build on push 

![](/Images/build_options.PNG)

## Output

![](/Images/output.PNG)

## Step 8 : Debug Phase

Since the file path is relative to the local directory, we need to modify the directory to use native VM filesystem which will be running on the worker node.

Modify the .travis.yml file to take the proper path of the input.yaml file

![](/Images/debug_1.PNG)

We can see the builds which have failed because of the path of the input.yaml file

![](/Images/debug_2.PNG)

### Running a build in Debug mode

Private GitHub repos can be run in Debug mode to connect to the VM and troubleshoot

![](/Images/debug_2_1.PNG)

Using SSH to connect to the VM

![](/Images/debug_3.PNG)
