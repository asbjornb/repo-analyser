import os
import src.core as core

#core
def test_analyzefile():
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData.testFile.py'
    output=core._analyzefile(filepath)
    assert output['extension']=='.py'
    assert output['number of lines']==7
    assert output['linelengths']==[17,7,7,9,12,0,12]
    assert output['number of methods']==1