nome = input("Olá, Qual é o seu nome? ")
categorias = [
    "Wordpress",
    "Criação de Site",
    "E-commerce",
    "Marketing Digital",
    "Vendas",
    "Google Ads",
    "Design",
    "Negócios",
    "Youtube",
    "Criação de Conteúdo",
    "Programação",
]

for i in range(len(categorias)):
    print(f"{i}. {categorias[i]}")

num_das_categorias = input(
    "Digite o número das categorias desejadas (use vírgulas): \n"
)

num_das_categorias = num_das_categorias.split(",")
ncategorias = []
for elemento in num_das_categorias:
    numero = int(elemento.strip())
    ncategorias.append(numero)

tempo = int(input("Quanto tempo gostaria de estudar (min)?\n"))

mostrar_premium = input("Mostrar apenas cursos Premium (S/N)?\n")

if mostrar_premium == "N" or mostrar_premium == "n":
    mostrar_premium = False
elif mostrar_premium == "S" or mostrar_premium == "s":
    mostrar_premium = True

print()
print(f"Nome: {nome}")
print(f"ID das Categorias: {ncategorias}")
print(f"Tempo: {tempo} min")
print(f"Apenas Premium?: {mostrar_premium}")

# Colunas da tabela em forma de listas
cursos = [
    "Introdução ao Wordpress",
    "Criador de Sites",
    "Introdução ao WooCommerce",
    "Afiliado de Sucesso",
    "Venda mais com WhatsApp Business e Google Meu Negócio",
    "Introdução ao Google Ads",
    "E-commerce e Vendas Online",
    "Canva: Design Fácil para Empreendedores",
    "Youtube para Iniciantes: como criar e crescer o seu canal",
    "Rede de Display e Youtube",
    "Desenvolvimento de Plugins para WordPress",
]

tempos = [95, 25, 35, 85, 75, 150, 140, 120, 85, 335, 160]

categorias_do_curso = [
    ['wordpress', 'criação de sites'],
    ['criação de sites'],
    ['e-commerce', 'criação de sites', 'wordpress'],
    ['marketing digital', 'vendas'],
    ['marketing digital', 'vendas', 'google ads', 'negócios'],
    ['marketing digital', 'google ads'],
    ['e-commerce', 'vendas', 'negócios'],
    ['design', 'negócios'],
    ['youtube', 'criação de conteúdo'],
    ['marketing digital', 'google ads', 'youtube'],
    ['programação', 'wordpress'],
]

gratuidade = [
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
]

categorias_selecionadas = []
for n in ncategorias:
    categorias_selecionadas.append(categorias[n].upper())

print()
print(
    f"Olá, {nome}, com base no seu perfil, achamos que você iria gostar dos seguintes cursos:"
)

for cat in categorias_selecionadas:
    print(f"{cat}:")
    for linha in range(len(cursos)):
        if gratuidade[linha] or mostrar_premium:
            if (
                cat.lower() in categorias_do_curso[linha]
                and tempos[linha] <= tempo
            ):
                print(f"-{cursos[linha]} ({tempos[linha]} min)")
