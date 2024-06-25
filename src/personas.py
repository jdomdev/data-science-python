def lectura_txt():
    lista_dic = []
    idt = 'id'
    nombre = 'nombre'
    apellido = 'apellido'
    nacimiento = 'nacimiento'
    with open('../files/personas.txt', encoding='utf-8') as fich_pers:
        linea = fich_pers.readline()
        while linea:
            lista_linea = linea.split(';')
            for i, palabra in lista_linea:
                                
                #lista_dic.append({idt:})