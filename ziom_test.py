import pytest
from ziom import *

def test_add_content():
    motif = Motif()
    motif.add_content("ATCGTGCGCAAAAAACGTGAGTAATTGGAA")
    assert motif.content == "ATCGTGCGCAAAAAACGTGAGTAATTGGAA"

def test_seek_process():
    motif = Motif()
    motif.add_content("ACTACT")
    motif.seek(3)
    result = motif.k_meres
    expected = ["ACT", "ACT"]
    assert result == expected

def test_seek_result():
    motif = Motif()
    motif.add_content("ACTACT")
    result = motif.seek(3)
    expected = "ACT"
    assert result == expected

def test_counting_test():
    motif = Motif()
    motif.k_meres = ['abc', 'cdc', 'cdc', 'cdc', 'abc']
    result = motif.counting()
    expected = 'cdc'
    assert result == expected

def test_k_mere_add():
    motif = Motif()
    motif.add_content("ACTGGGTCACTG")
    motif.seek(4)
    result = motif.k_meres
    expected = ["ACTG","GGTC", "ACTG"]
    assert result == expected