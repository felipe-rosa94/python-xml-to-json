import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse('my_data.xml')

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    languages = doc.getElementsByTagName('languages')

    print('%d languages:' % languages.length)

    for skill in languages:
        print(skill.getAttribute('name'))

    skills = doc.getElementById('first')
    print(skills)


if __name__ == '__main__':
    main()
