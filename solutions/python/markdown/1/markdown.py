import re

def parse_bold_text(text):
    bold_text = re.match('(.*)__(.*)__(.*)', text)
    if bold_text:
        text = bold_text.group(1) + '<strong>' + \
        bold_text.group(2) + '</strong>' + bold_text.group(3)
    return text

def parse_italic_text(text):
    italic_text = re.match('(.*)_(.*)_(.*)', text)
    if italic_text:
        text = italic_text.group(1) + '<em>' + italic_text.group(2) + \
        '</em>' + italic_text.group(3)
    return text



def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list , in_list_append = False , False
    
    for text in lines:
        if re.match('###### (.*)', text) is not None:
            text = '<h6>' + text[7:] + '</h6>'
        elif re.match('##### (.*)', text) is not None:
            text = '<h5>' + text[6:] + '</h5>'
        elif re.match('#### (.*)', text) is not None:
            text = '<h4>' + text[5:] + '</h4>'
        elif re.match('### (.*)', text) is not None:
            text = '<h3>' + text[4:] + '</h3>'
        elif re.match('## (.*)', text) is not None:
            text = '<h2>' + text[3:] + '</h2>'
        elif re.match('# (.*)', text) is not None:
            text = '<h1>' + text[2:] + '</h1>'

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
                text = '<ul><li>' + curr + '</li>'
            else:
                text = '<li>' + curr + '</li>'
                
        else:
            if in_list:
                in_list_append, in_list = True, False

        # Paragraph parsing
        is_listItem_or_heading = re.match('<h|<ul|<p|<li', text)
        # default to paragraph if its not a list item or heading
        if not is_listItem_or_heading:
            text = '<p>' + text + '</p>'
            
        text = parse_bold_text(text)
        text = parse_italic_text(text)
        
        if in_list_append:
            text = '</ul>' + text
            in_list_append = False
        res += text
        
    if in_list:
        res += '</ul>'
    return res
