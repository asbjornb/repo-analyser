import os
import pytest
import src.file_analyser as file_analyser

#fixtures
@pytest.fixture
def testfile_py_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile.py'

@pytest.fixture
def testfile_js_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile.js'

#tests
def test_file_analyser_outputs_extension(testfile_py_path):
    output=file_analyser.analyse_from_filepath(testfile_py_path)
    assert output['extension'] is not None
    #assert output['number of methods']==1

def test_file_analyser_outputs_correct_extension_for_python(testfile_py_path):
    output=file_analyser.analyse_from_filepath(testfile_py_path)
    assert output['extension']==".py"

def test_file_analyser_outputs_correct_extension_for_javascript(testfile_js_path):
    output=file_analyser.analyse_from_filepath(testfile_js_path)
    assert output['extension']==".js"

def test_file_analyser_errors_on_non_existing_file():
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__)))+r'\sampleData\testFile2.cs'
    with pytest.raises(FileNotFoundError):
        assert file_analyser.analyse_from_filepath(filepath)

def test_file_analyser_outputs_linecount(testfile_py_path):
    output=file_analyser.analyse_from_filepath(testfile_py_path)
    assert output['line_count']==7

def test_file_analyser_outputs_linecount_js_file(testfile_js_path):
    output=file_analyser.analyse_from_filepath(testfile_js_path)
    assert output['line_count']==3

def test_file_analyser_outputs_line_lengths(testfile_py_path):
    output=file_analyser.analyse_from_filepath(testfile_py_path)
    assert output['line_lengths']==[18,8,8,10,13,1,12]

def test_file_analyser_outputs_line_lengths_js_file(testfile_js_path):
    output=file_analyser.analyse_from_filepath(testfile_js_path)
    assert output['line_lengths']==[46,28,25]
