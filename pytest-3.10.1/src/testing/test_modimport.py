import subprocess
import sys

import py

import _pytest
import pytest

MODSET = [
    x
    for x in py.path.local(_pytest.__file__).dirpath().visit("*.py")
    if x.purebasename != "__init__"
]


@pytest.mark.parametrize("modfile", MODSET, ids=lambda x: x.purebasename)
def test_fileimport(modfile):
    # this test ensures all internal packages can import
    # without needing the pytest namespace being set
    # this is critical for the initialization of xdist

    p = subprocess.Popen(
        [
            sys.executable,
            "-c",
            "import sys, py; py.path.local(sys.argv[1]).pyimport()",
            modfile.strpath,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (out, err) = p.communicate()
    if p.returncode != 0:
        pytest.fail(
            "importing %s failed (exitcode %d): out=%r, err=%r"
            % (modfile, p.returncode, out, err)
        )
