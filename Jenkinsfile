pipeline {
    //Agent can also be a docker 
    agent any 
            stages{
                //Installing dependencies
                stage('checkout'){
                    steps{
                            sh 'pip install pyyaml'
                    }
                }
                //This stage takes input yamlfile and merges accordingly
                stage('Building'){
                    steps{
                            sh 'python merge_logic.py test4/dir1/dir2/dir3/dir4/input.yaml'
                    }
                }
                //This stage performs unittest on the given 3 test cases of the program
                stage('Testing'){
                    steps{
                            sh 'python test_merge.py'
                    }
                }
            }     
}