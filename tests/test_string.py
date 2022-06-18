from stringmethods.string_methods import add_comma


def test_strings_boris_romain_seb():
    """This method should return "boris, romain, seb" """
    assert add_comma("boris romain seb") == ("boris, romain, seb")
