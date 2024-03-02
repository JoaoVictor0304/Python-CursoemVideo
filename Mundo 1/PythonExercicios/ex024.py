cidade = str(input('Em que cidade você nasceu? ')).strip()

primeiro = cidade.split()

santo = primeiro[0].upper()

santo2 = 'SANTO' in santo

print(f'A cidade começa com Santo: {santo2}')