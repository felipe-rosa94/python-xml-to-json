import xmltodict

def main():
    ## lendo o documento xml.
    with open('my_data.xml') as fd:
        doc = xmltodict.parse(fd.read())

    ## pegando dados com nome da tag.
    first_name = doc['archive']['fname']
    last_name = doc['archive']['lname']
    profession = doc['archive']['profession']

    print('Nome:', first_name, last_name)
    print('Profissão: ', profession)

    languages = ''

    ## percorendo dentro de doc['archive']['languages'] que retonar um list.
    for i in doc['archive']['languages']:
        ## buscando dentro da tag
        languages += i['@name'] + ', '

    ## printando liguagens e removendo os 2 ultimos caracteris.
    print('Linguagens:', languages[:-2])

if __name__ == '__main__':
    main()