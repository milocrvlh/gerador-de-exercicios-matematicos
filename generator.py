import random

latex_template = """
%%----------LaTeX template for teachers-----------------------------%%
%%----------Samuel S. Watson----------------------------------------%% 
%%----------January 2013--------------------------------------------%% 

\\documentclass[12pt]{{article}} % Especifica o tamanho da fonte

%%----------------PACOTES-------------------------------------------%%
\\usepackage[margin=1in]{{geometry}} % Define todas as margens em 1 polegada
\\usepackage[pdftex]{{graphicx}} % Permite a inclusão de arquivos de imagem
\\usepackage{{amssymb}} % Acesso a símbolos matemáticos extras
\\usepackage{{amsmath}} % Acesso a símbolos matemáticos extras
\\usepackage{{wrapfig}} % Permite o texto envolver figuras
\\usepackage{{calc}} % Dá acesso a uma calculadora básica 
%%-------------------------------------------------------------------%%

%%----------------COMANDOS-------------------------------------------%%
\\newcommand\\blank{{\\underline{{\\hspace{{2cm}}}}}} % Cria um espaço em branco 

\\newcounter{{prob}} % Um novo contador para o número do problema atual

\\setcounter{{prob}}{{1}} % Inicia o contador com o valor 1

\\newcommand\\itm{{
\\fbox{{\\textbf{{\\theprob}}}} \\refstepcounter{{prob}}
}} % Chama o número do problema


\\newcommand{{\\problem}}[1]{{\\makebox[0.5cm]{{\\itm}}   
  \\begin{{minipage}}[t]{{\\textwidth-0.5cm}} #1 \\end{{minipage}} 
}} % Um ambiente para uma declaração de problema em uma ou mais linhas


\\newcommand{{\\pairofprobs}}[2]{{
  \\begin{{minipage}}[t]{{0.5\\textwidth}}\\itm #1 \\end{{minipage}} 
  \\begin{{minipage}}[t]{{0.5\\textwidth}}\\itm #2 \\end{{minipage}} 
}} % Coloca dois problemas na mesma linha


\\newcommand{{\\threeprobs}}[3]{{
\\begin{{minipage}}[t]{{0.31\\textwidth}}\\itm #1 \\end{{minipage}} \\hfill
 \\begin{{minipage}}[t]{{0.31\\textwidth}}\\itm #2 \\end{{minipage}} \\hfill 
 \\begin{{minipage}}[t]{{0.31\\textwidth}}\\itm #3 \\end{{minipage}}
}} % Coloca três problemas na mesma linha


\\newcounter{{choice}} % Contador para problemas de múltipla escolha 

\\setcounter{{choice}}{{1}} % Inicia o contador com o valor 1


\\newcommand\\achoice{{
(\\alph{{choice}}) \\stepcounter{{choice}}
}} % Gera letra para opção de múltipla escolha


\\newcommand{{\\answers}}[5]{{\\vspace*{{-7mm}} 
  \\begin{{tabular}}{{l@{{\\hspace{{1mm}}}}p{{0.9\\textwidth}}}}
    \\achoice & #1 \\\\ \\achoice & #2 \\\\ \\achoice & #3 \\\\ 
    \\achoice & #4 \\\\ \\achoice & #5 \\end{{tabular}}
  \\setcounter{{choice}}{{1}}
}} % Cria opções de múltipla escolha 
%---------------------------------

% ARITMÉTICA (exemplos na próxima seção) 
% Quatro Operações


%% a divisão deve ser ajustada para o formato brasileiro

\\newcommand\\divi[2]{{
$\\begin{{array}}{{r|}}
\\hline #2 \\
\\end{{array}} \\! #1$
}}

\\newcommand\\mult[2]{{
$\\begin{{array}}{{rr}} 
 & #1 \\\\ 
 \\times & #2 \\\\ \\hline 
 \\end{{array}}$}}
 
\\newcommand\\addi[2]{{
  $\\begin{{array}}{{rr}} 
   &  #1 \\\\ 
    + & #2 \\\\ \\hline 
  \\end{{array}}$}}

\\newcommand\\subt[2]{{
  $\\begin{{array}}{{rr}}
    & #1 \\\\ 
    - & #2 \\\\ \\hline
  \\end{{array}}$}}

  
% Álgebra 
% Produtos Notáveis
\\newcommand\\triquadpftd[2]{{$
(#1a + #2b)^2 =
$}}

\\newcommand\\triquadpftf[3]{{$
#1a^2 + #3ab + #2b^2=
$}}

%%-------------------------------------------------------------------%%

%%-----------FORMATAÇÃO----------------------------------------------%%
\\pagestyle{{empty}} % Garante que nenhum número de página seja impresso
\\parskip = 0.2 in % Coloca um pouco de espaço entre parágrafos 
\\parindent = 0.0 in % Garante que não haja indentação para parágrafos
%%-------------------------------------------------------------------%%

%%-----------EXEMPLOS DE USO------------------------------------------%%
% Para tentar qualquer um dos exemplos abaixo, descomente-os e cole 
% abaixo do comando \\begin{{document}} na seção de CONTEÚDO. 

% Para configurar um problema de divisão como 93 dividido por 3:
% \\divi{{3}}{{93}}

% Para configurar um problema de multiplicação como 14 vezes 4:
% \\mult{{14}}{{4}}

% Para colocar dois problemas na mesma linha: 
% \\pairofprobs{{\\divi{{3}}{{93}}}}{{\\mult{{14}}{{4}}}} 

% Para incluir um espaço vertical de 3cm entre as questões 
% \\vspace{{3cm}} 

%%--------------------------------------------------------------------%%

%%-----------CABEÇALHO--------------------------------------------------%%
\\begin{{document}}

\\begin{{center}} 
  \\textsc{{Cálculo}} \\\\ 
  \\textsc{{Prof. Milo}}
\\end{{center}}

Nome:\\underline{{\\hspace*{{4cm}}}}
\\

Data:\\hspace*{{1cm}}/ \\hspace*{{0.5cm}}/\\hspace*{{0.5cm}} \\hfill Início: \\underline{{\\hspace*{{0.7cm}}}}: \\underline{{\\hspace*{{0.7cm}}}}. Término:  \\underline{{\\hspace*{{0.7cm}}}}: \\underline{{\\hspace*{{0.7cm}}}}

\\

\\fontsize{{14}}{{18pt}} \\selectfont % Aumenta o tamanho da fonte

%%-----------TEOREMAS-------------------------------------------%%
\\newtheorem{{axioma}}{{Axioma}}[section]
\\newtheorem{{teorema}}{{Teorema}}[section]

%%-----------CONTEÚDO--------------------------------------------%%
\\section{{Produtos Notáveis}}

\\begin{{axioma}}[Fator Comum em Evidência]
Sejam \\(x\\), \\(a\\), \\(b \\in \\mathbb{{R}}\\). Então:
\\[ 
x(a+b) = ax + bx 
\\]
\\end{{axioma}}

\\begin{{teorema}}[Trinômio Quadrado Perfeito]
Sejam \\(a\\), \\(b \\in \\mathbb{{R}}\\). Então:
\\[ 
(a + b)^2 = a^2 + 2ab + b^2 
\\]
\\end{{teorema}}

\\textit{{Direções:}} 
 do problema 1 a 80 desenvolva as expressões usando o Trinômio Quadrado Perfeito. Do problema 81 a 100, fatore as expressões usando o mesmo teorema.

{problems}

\\end{{document}} 
%%-------------------------------------------------------------------%%

"""

### Aritmética

def subtracao_montada():
    a = random.choice(range(10,20))
    b = random.choice(range(3,a+1))
    return f'\\subt{{{a}}}{{{b}}}'

def adicao_montada():
    (a,b) = random.choices(range(5, 10), k=2)
    return f'\\addi{{{a}}}{{{b}}}'

def multiplicacao_montada():
    (a,b) = random.choices(range(2,10), k=2)
    return f'\\mult{{{a}}}{{{b}}}'


# Existe um problema em que um número primo aparece para ser dividido por eles mesmos
# Melhorar para que isso não aconteça
def divisao_montada():
    a = random.choice(range(4, 101))
    b = random.choice(range(2, a+1))
    while a % b != 0:
        b = random.choice(range(2, a+1))
    return f'\\divi{{{a}}}{{{b}}}'

# Álgebra

def trinomio_quadrado_perfeito_des():
    weights = [80] * 3 + [10] * 2 + [8] * 5 + [2] * 5  # Probabilidades diferentes para cada os exercícios
    (a, b) = random.choices(range(1, 16), weights=weights, k=2)
    return f'\\triquadpftd{{{a}}}{{{b}}}'

def trinomio_quadrado_perfeito_fat():
    weights = [80] * 3 + [10] * 2 + [8] * 5 + [2] * 2  # Probabilidades diferentes para cada os exercícios
    a = (random.choices(range(1, 13), weights=weights, k=1))[0]**2
    b = (random.choices(range(1, 13), weights=weights, k=1))[0]**2
    c = 2*a*b
    return f'\\triquadpftf{{{a}}}{{{b}}}{{{c}}}'


def fator_comum_evidência():
    pass 

def get_row_of_random_problems(exercise_type):
    if exercise_type == 'tipo_a':
        return f'\\pairofprobs{{{trinomio_quadrado_perfeito_des()}}}{{{trinomio_quadrado_perfeito_des()}}}'
    elif exercise_type == 'tipo_b':
        return f'\\pairofprobs{{{trinomio_quadrado_perfeito_fat()}}}{{{trinomio_quadrado_perfeito_fat()}}}'
    # Add more types as needed

def get_rows_of_random_problems(n, exercise_type):
    rows = ""
    for i in range(n):
        rows += '\n\n\\vspace{2cm}\n\n' + get_row_of_random_problems(exercise_type)
    return rows

# Generate sections for different types of exercises
problems_tipo_a = get_rows_of_random_problems(40, 'tipo_a')
problems_tipo_b = get_rows_of_random_problems(10, 'tipo_b')

worksheet = latex_template.format(problems=problems_tipo_a + problems_tipo_b)

with open('exercicios.tex', 'w', encoding='utf-8') as f: 
    f.write(worksheet)
