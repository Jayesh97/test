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
                stage('Cleanup'){
                    steps{
                        mail body: 'project build successful',
                        from: 'jayesh5397@gmail.com',
                        replyTo: 'sjbondu@ncsu.edu',
                        subject: 'project build successful',
                        to: 'shbondu@ncsu.edu'
                    }
                }
            }     
}