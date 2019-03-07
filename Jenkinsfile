pipeline {
    agent any 
            stages{
                stage('checkout'){
                    steps{
                            sh 'pip install pyyaml'
                    }
                }
                stage('Building'){
                    steps{
                            sh 'python merge_logic.py test4/dir1/dir2/dir3/dir4/input.yaml'
                    }
                }
                stage('Testing'){
                    steps{
                            sh 'python test_merge.py'
                    }
                }
            }     
}