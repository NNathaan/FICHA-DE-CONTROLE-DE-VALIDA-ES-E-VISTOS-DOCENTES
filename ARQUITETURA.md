# Arquitetura do TechFlow Core (Python CLI)

## 1. O que é um CLI
CLI significa Command Line Interface (Interface de Linha de Comando).
Um programa CLI roda no terminal/prompt de comando, e o usuário interage
digitando comandos ou opções pelo teclado. No CLI a interação acontece por
texto, enquanto em programas gráficos o usuário clica em janelas, menus e
botões. Escolhi um CLI para o TechFlow Core porque é mais simples de
desenvolver, facilita o aprendizado da lógica de programação e funciona
no ambiente do laboratório sem precisar criar uma interface gráfica.

## 2. O caminho de uma ação
Quando o programa começa, o `while True` inicia um laço que se repete até
encontrar um `break`. Dentro do laço, o programa mostra o menu com as
opções Cadastrar, Listar e Sair. O `input()` espera o usuário digitar uma
opção e guarda o valor na variável `opcao` como string. Se o usuário digita
2, o programa compara com "1", não bate, compara com "2" e executa o
`print("em construção")`. Como o laço não terminou, o programa volta ao
início do `while True` e mostra o menu de novo. Se o usuário digita 3, o
programa mostra "Saindo do sistema..." e o `break` faz o programa sair do
laço.

## 3. O que usei e onde
- `print()` para mostrar texto e `input()` para ler o que o usuário digita.
- O laço `while`, que repete o menu e só para quando o `break` é executado.
- `if` e `elif` para escolher o que fazer conforme a opção digitada.
- A variável `opcao` guarda uma string (texto).
- O `else` trata opções inválidas, mostrando uma mensagem de erro quando o
  usuário digita algo diferente das opções disponíveis.

## 4. Decisões técnicas
**Decisão 1:** comparei a opção como texto ("1") em vez de converter com
`int()`. O `input()` já retorna string, então é mais simples comparar
direto, e isso evita erros se o usuário digitar letras ou símbolos.

**Decisão 2:** usei `while True` com `break` no menu. Sem isso, o programa
executaria uma vez e terminaria logo após o usuário escolher uma opção. Com
isso, o usuário usa o menu várias vezes seguidas, até decidir sair
digitando 3.
