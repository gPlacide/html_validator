#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tags = _extract_tags(html)
    s = []
    balanced = True
    index = 0

    for index in range(len(tags)):
        html_tag = tags[index]

        if '/' not in html_tag:
            s.append(html_tag)
        else:
            if s == []:
                balanced = False
            else:
                top = s.pop()
                if top[1:] != html_tag[2:]:
                    balanced = False
    if balanced and s == []:
        return True
    else:
        return False


def _extract_tags(html):    
    '''
    This function returns a list of all the html tags contained in the input string, stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    
    for x in range(len(html)):
        if html[x] == '<':
            html_tag = ''
            i = x
            
            while html[i] != '>':
                html_tag += html[i]
                i += 1
            html_tag += '>'
            tags.append(html_tag)
            
    return tags

