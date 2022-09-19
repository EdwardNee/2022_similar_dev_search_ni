# from repo_processing.code_parser.tree_sitter_parser import go_parse
import go_parse


py_names_entries = [
    {"code": bytes(""" class A():
ss = 5
a1 = a1 """, "utf8"), "expected_names": ["A", "ss", "a1"]},
    {"code": bytes(
        """ class A():
def foo():
    vall = 5
    if bar:
        baz()""", "utf8"), "expected_names": ["foo", "vall"]},
    {"code": bytes(""" class A():
class B():
class C(): """, "utf8"), "expected_names": ["foo", "vall"]}
]

py_imports_entries = [
    {"code": bytes(""" import sys1
from a import * """, "utf8"), "expected_imports": ["sys1", "a"]},
    {"code": bytes(""" from s import sys
from . import b """, "utf8"), "expected_imports": ["s", "sys", "b"]},
    {"code": bytes(""" import a2, b2
import b1.c as d
import a1.b.c """, "utf8"),
     "expected_imports": ["a2", "b2", "b1.c", "a1.b.c"]}
]


@pytest.mark.parametrize("code, expected_names", [(py_names_entries[0]["code"], py_names_entries[0]["expected_names"]),
                                                  (py_names_entries[1]["code"], py_names_entries[1]["expected_names"])])
def test_python_variables(code, expected_names):
    assert go_parse("python", code)["names"] == expected_names


@pytest.mark.parametrize("code, expected_imports",
                         [(py_imports_entries[0]["code"], py_imports_entries[0]["expected_imports"]),
                          (py_imports_entries[1]["code"], py_imports_entries[1]["expected_imports"]),
                          (py_imports_entries[2]["code"], py_imports_entries[2]["expected_imports"])])
def test_python_imports(code, expected_imports):
    assert go_parse("python", code)["imports"] == expected_imports


@pytest.mark.parametrize("code, expected_names", [(py_names_entries[0]["code"], py_names_entries[0]["expected_names"]),
                                                  (py_names_entries[1]["code"], py_names_entries[1]["expected_names"])])
def test_java_variables(code, expected_names):
    assert go_parse("java", code)["names"] == expected_names
