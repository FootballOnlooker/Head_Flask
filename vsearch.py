def search4vowels(phrase:str)->set:
    """Возвращает гласные, найденные в указанной форме"""
    return set('aeiou').intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Возращает множество букв из letters, найденных в указанной форме"""
    return set(letters).intersection(set(phrase))