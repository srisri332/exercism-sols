import re

def parse_bold_text(text):
    """ Takes in text, formats it to bold"""
    bold_text = re.match('(.*)__(.*)__(.*)', text)
    if bold_text:
        text = bold_text.group(1) + '<strong>' + \
        bold_text.group(2) + '</strong>' + bold_text.group(3)
    return text

def parse_italic_text(text):
    """ Takes in text, formats it to italic"""
    italic_text = re.match('(.*)_(.*)_(.*)', text)
    if italic_text:
        text = italic_text.group(1) + '<em>' + italic_text.group(2) + \
        '</em>' + italic_text.group(3)
    return text

def parse_heading_text(text):
    """ Takes in text, formats it to a heading if applicable """
    for level in range(6, 0, -1):
        match = re.match('#' * level + r' (.*)', text)
        if match:
            return f'<h{level}>{match.group(1)}</h{level}>'
    return text


def parse(markdown):
    """ Method used for parsing markdown """
    lines = markdown.split('\n')
    res = ''
    in_list , in_list_append = False , False
    
    for text in lines:
        line_html = parse_heading_text(text)
        # List parsing
        parse_list_items = re.match(r'\* (.*)', text)
        if parse_list_items:
            curr = parse_list_items.group(1)
            # parsing bold text in each list item
            curr = parse_bold_text(curr)
            # parsing italic text in each list item
            curr = parse_italic_text(curr)
            if not in_list:
                in_list = True
                line_html = '<ul><li>' + curr + '</li>'
            else:
                line_html = '<li>' + curr + '</li>'
                
        else:
            if in_list:
                in_list_append, in_list = True, False
        # Paragraph parsing
        is_listItem_or_heading = re.match('<h|<ul|<p|<li', line_html)
        # default to paragraph if its not a list item or heading
        if not is_listItem_or_heading:
            line_html = '<p>' + line_html + '</p>'
            
        line_html = parse_bold_text(line_html)
        line_html = parse_italic_text(line_html)
        
        if in_list_append:
            line_html = '</ul>' + line_html
            in_list_append = False
        res += line_html
        
    if in_list:
        res += '</ul>'
    return res
