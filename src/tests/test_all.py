import os
import pytest
import src.file_analyser as file_analyser

#core
def test_file_analyser_outputs_extension():
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile.py'
    output=file_analyser.analysefile(filepath)
    assert output['extension'] is not None
    #assert output['extension']=='.py'
    #assert output['number of lines']==7
    #assert output['linelengths']==[17,7,7,9,12,0,12]
    #assert output['number of methods']==1

def test_file_analyser_outputs_correct_extension_for_python():
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile.py'
    output=file_analyser.analysefile(filepath)
    assert output['extension']==".py"

def test_file_analyser_outputs_correct_extension_for_javascript():
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile.js'
    output=file_analyser.analysefile(filepath)
    assert output['extension']==".js"

def test_file_analyser_errors_on_non_existing_file():
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile2.cs'
    with pytest.raises(FileNotFoundError):
        assert file_analyser.analysefile(filepath)