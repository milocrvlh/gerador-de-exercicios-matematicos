import random
from sympy import *

latex_template = """
%%----------LaTeX template for teachers-----------------------------%%
%%----------Samuel S. Watson----------------------------------------%% 
%%----------January 2013--------------------------------------------%% 

%% ATENÇÃO: Deve-se usar o dobro dos caracteres \\ e {{}} para que o código funcione em LaTeX %% 

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
\\newcommand\\blank{{\\underline{{\\hspace{{2cm}}}}}} % Cria um ___________ 

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

%% a divisão deve ser ajustada para o formato brasileiro %%

\\newcommand\\divi[2]{{
$\\begin{{array}}{{r|}}
\\hline #2 \\\\
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

  \\newcommand\\addim[3]{{
  $\\begin{{array}}{{rr}} 
        &#3 \\\\
        &#1 \\\\ 
    +   &#2 \\\\ \\hline 
  \\end{{array}}$}}


  \\newcommand\\addil[2]{{$
#1 + #2 =
$}}
  
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
#1a^2 + #3ab + #2b^2 
$}}

\\newcommand\\fatcomevum[1]{{$
#1
$}}

\\newcommand\\fatcomevdois[1]{{$
#1
$}}

\\newcommand\\fatcomevtres[1]{{$
#1
$}}

% Cálculo
\\newcommand\\polinomial[9]{{
\\begin{{align*}}
f(x) &= #1x^8 + #2x^7 + #3x^6 + #4x^5 + #5x^4 + #6x^3 + #7x^2 + #8x + #9 \\\\[0.5cm]
f'(x) &=
\\end{{align*}}
}}
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
  \\textsc{{Aritmética}} \\\\ 
  \\textsc{{Prof. Milo}}
\\end{{center}}

Nome:\\underline{{\\hspace*{{4cm}}}}
\\

Data:\\hspace*{{1cm}}/ \\hspace*{{0.5cm}}/\\hspace*{{0.5cm}} \\hfill Início: \\underline{{\\hspace*{{0.7cm}}}}: \\underline{{\\hspace*{{0.7cm}}}}. Término:  \\underline{{\\hspace*{{0.7cm}}}}: \\underline{{\\hspace*{{0.7cm}}}}

\\

\\fontsize{{14}}{{18pt}} \\selectfont % Aumenta o tamanho da fonte

%%-----------TEOREMAS-------------------------------------------%%

%%-----------CONTEÚDO--------------------------------------------%%
\\section*{{Adição e Tabuada}}

\\textit{{Direções:}} 
efetue as operações.

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
    weights = [1] + [60] * 5 + [39] * 4  # Probabilidades diferentes para cada coeficiente
    (a,b) = random.choices(range(0, 10), weights=weights, k=2)
    return f'\\addi{{{a}}}{{{b}}}'

def adicao_montada_3():
    weights = [1] + [60] * 5 + [39] * 4  # Probabilidades diferentes para cada coeficiente
    (a,b,c) = random.choices(range(0, 10), weights=weights, k=3)
    return f'\\addim{{{a}}}{{{b}}}{{{c}}}'

def adicao_linear():
    weights = [1] + [40] * 5 + [59] * 4  # Probabilidades diferentes para cada coeficiente
    (a,b) = random.choices(range(0, 10), weights=weights, k=2)
    return f'\\addil{{{a}}}{{{b}}}'


def multiplicacao_montada():
    weights = [1] + [5] + [94]*8  # Probabilidades diferentes para cada coeficiente
    (a,b) = random.choices(range(0, 10), weights=weights, k=2)    
    return f'\\mult{{{a}}}{{{b}}}'

def multiplicacao_nove():
    weights = [1] + [5] + [94]*8  # Probabilidades diferentes para cada coeficiente
    a = random.choices(range(0, 10), weights=weights, k=1)[0]
    return f'\\mult{{{9}}}{{{a}}}'

def multiplicacao_oito():
    weights = [1] + [5] + [94]*8  # Probabilidades diferentes para cada coeficiente
    a = random.choices(range(0, 10), weights=weights, k=1)[0]
    return f'\\mult{{{8}}}{{{a}}}'

def multiplicacao_selecionada():
    weights = [1] + [5] + [94]*8  # Probabilidades diferentes para cada coeficiente
    a = random.choices(range(8,10), k=1)[0]
    b = random.choices(range(0, 10), weights=weights, k=1)[0]

    return f'\\mult{{{a}}}{{{b}}}'

def adicao_montada_com_3():
    weights = [1] + [40] * 5 + [59] * 4  # Probabilidades diferentes para cada coeficiente
    (a,b, c) = random.choices(range(0, 10), weights=weights, k=3)
    return f'\\addim{{{a}}}{{{b}}}{{{c}}}'

# Existe um problema em que um número primo aparece para ser dividido por eles mesmos
# Melhorar para que isso não aconteça
def divisao_montada():
    a = random.choice(range(4, 101))
    b = random.choice(range(2, a+1))
    while a % b != 0:
        b = random.choice(range(2, a+1))
    return f'\\divi{{{a}}}{{{b}}}'

# Álgebra

def desenvolvimento_trinomio_quadrado_perfeito():
    weights = [50] * 3 + [30] * 2 + [15] * 5 + [5] * 5  # Probabilidades diferentes para cada coeficiente
    (a, b) = random.choices(range(1, 16), weights=weights, k=2)
    return f'\\triquadpftd{{{a}}}{{{b}}}'

def fatoracao_trinomio_quadrado_perfeito():
    weights = [80] * 3 + [10] * 2 + [8] * 5 + [2] * 2  # Probabilidades diferentes para cada coeficiente
    a = (random.choices(range(1, 13), weights=weights, k=1))[0]**2
    b = (random.choices(range(1, 13), weights=weights, k=1))[0]**2
    c = 2* int(a**(1/2))*int(b**(1/2))
    return f'\\triquadpftf{{{a}}}{{{b}}}{{{c}}}'

def fator_comum_em_evidência1():
    while True:
      a, b = random.randint(2, 30), random.randint(2, 30)
      if gcd(a, b) > 1:
          break
    x, y = random.sample(['x', 'y', 'z', 'a', 'b'], 2)
    expr_expandida = f"{a}{x} + {b}{y}"
    return f'\\fatcomevum{{{latex(expr_expandida)}}}'

def fator_comum_em_evidência2():
    vars = random.sample(['x', 'y', 'z'], 2)
    a, b = symbols('a b')
    var1, var2 = symbols(vars[0]), symbols(vars[1])  # Converte strings em símbolos
    grp1 = a * (var1 + var2)  # Ex: a*(x + y)
    grp2 = b * (var1 + var2)  # Ex: b*(x + y)
    expr_expandida = expand(grp1 + grp2)
    # Formata a expressão expandida em LaTeX corretamente
    return f'\\fatcomevdois{{{latex(expr_expandida)}}}'


## erro nessa função
def fator_comum_em_evidência3():
    common_factor = sympify(f"x + {random.randint(1,5)}")
    inner_expr = Add(*[symbols(c) for c in random.sample(['a', 'b', 'c'], 2)])
    expanded = expand(common_factor * inner_expr)
    return f'\\fatcomevtres{{{latex(expanded)}}}'

# Cálculo
def derivada_de_polinomio():
    coeficientes = [random.randint(1, 10) for num in range(11)]
    return f'\\polinomial{{{coeficientes[0]}}}{{{coeficientes[1]}}}{{{coeficientes[2]}}}{{{coeficientes[3]}}}{{{coeficientes[4]}}}{{{coeficientes[5]}}}{{{coeficientes[6]}}}{{{coeficientes[7]}}}{{{coeficientes[8]}}}'

def get_row_of_random_problems(exercise_type):
    if exercise_type == 'tipo_a':
        return f'\\pairofprobs{{{adicao_montada_com_3()}}}{{{adicao_montada_com_3()}}}'
    elif exercise_type == 'tipo_b':
        return f'\\threeprobs{{{multiplicacao_selecionada()}}}{{{multiplicacao_selecionada()}}}{{{multiplicacao_selecionada()}}}'
    elif exercise_type == 'tipo_c':
        return f'\\threeprobs{{{adicao_linear()}}}{{{adicao_linear()}}}{{{adicao_linear()}}}'
    # Add more types as needed

def get_rows_of_random_problems(n, exercise_type):
    rows = ""
    for i in range(n):
        rows += '\n\n\\vspace{2cm}\n\n' + get_row_of_random_problems(exercise_type)
    return rows

# Gerar seções de diferentes tipos de exercícios
problems_tipo_a = get_rows_of_random_problems(75, 'tipo_a')
problems_tipo_b = get_rows_of_random_problems(50, 'tipo_b')
problems_tipo_c = get_rows_of_random_problems(83, 'tipo_c')


# Para adicionar os problema do tipo b, basta usar '+ problems_tipo_b'
worksheet = latex_template.format(problems=problems_tipo_a +problems_tipo_b )
with open('exercicios.tex', 'w', encoding='utf-8') as f: 
    f.write(worksheet)

  

