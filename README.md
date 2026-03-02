# <span style='font-size:200px;'>&#80;</span><span style='font-size:200px;'>&#84;</span> 
# Calculadora Simples
## Objetivo
Criar uma calculadora que realize operações matemáticas básicas.
## Requisitos
<ul>
    <li>O programa deve apresentar um menu com as opções:
        <ul>
            <li>1 - Soma</li>
            <li>2 - Subtração</li>
            <li>3 - Multiplicação</li>
            <li>4 - Divisão</li>
            <li>5 - Sair</li>
        </ul>
    </li>
    <li>Solicitar ao utilizador que escolha uma operação.</li>
    <li>Pedir dois números ao utilizador.</li>
    <li>Realizar a operação escolhida e apresentar o resultado.</li>
    <li>Tratar o caso de divisão por zero (apresentar mensagem de erro).</li>
    <li>Após cada operação, perguntar se o utilizador deseja realizar outra operação.</li>
    <li>O programa só deve terminar quando o utilizador escolher a opção "Sair".</li>
</ul>

## Desafio Extra
<ul>
  <li>Adicionar operações de potência e raiz quadrada.</li>
</ul>

## Explicação
Este exercício está dividido em duas formas de resolução diferentes.

<ul>
   <li>
      <strong>Primeira Forma de Resolução (Sem utilizar bibliotecas):</strong>
      <ul>
        <li>
            Dois ficheiros:
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/main.py">main.py</a>
            e
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoes.py">funcoes.py</a>.
            Esta estrutura permite maior organização, legibilidade e simplicidade.
        </li>
        <li>
            Ficheiro
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/main.py">main.py</a>:
            <ul>
                <li>Enunciado do exercício.</li>
                <li>Estrutura principal do programa.</li>
            </ul>
        </li>
        <li>
            Ficheiro
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoes.py">funcoes.py</a>:
            <ul>
                <li>Funções do programa:
                    <ul>
                        <li><code>menu()</code></li>
                        <li><code>addition()</code></li>
                        <li><code>subtration()</code></li>
                        <li><code>multiplication()</code></li>
                        <li><code>division()</code></li>
                        <li><code>potentiation()</code></li>
                        <li><code>squareroot()</code></li>
                        <li><code>ask2numbers()</code></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</li>

<li>
    <strong>Segunda Forma de Resolução (A utilizar a biblioteca <code>math</code>):</strong>
    <ul>
        <li>
            Dois ficheiros:
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/mainBiblioteca.py">mainBiblioteca.py</a>
            e
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoesBiblioteca.py">funcoesBiblioteca.py</a>.
        </li>
        <li>
            Ficheiro
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/mainBiblioteca.py">mainBiblioteca.py</a>:
            <ul>
                <li>Enunciado do exercício.</li>
                <li>Estrutura principal do programa.</li>
            </ul>
        </li>
        <li>
            Ficheiro
            <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoesBiblioteca.py">funcoesBiblioteca.py</a>:
            <ul>
                <li>Funções do programa:
                    <ul>
                        <li><code>menu()</code></li>
                        <li><code>addition()</code></li>
                        <li><code>subtration()</code></li>
                        <li><code>multiplication()</code></li>
                        <li><code>division()</code></li>
                        <li><code>potentiation()</code></li>
                        <li><code>squareroot()</code></li>
                        <li><code>ask2numbers()</code></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</li>
</ul>
<hr>

# <span style='font-size:200px;'>&#69;</span><span style='font-size:200px;'>&#78;</span><span style='font-size:200px;'>&#71;</span>

# Simple Calculator
## Objective
Create a calculator capable of performing basic mathematical operations.
## Requirements
<ul>
    <li>The programme must display a menu with the following options:
        <ul>
            <li>1 - Addition</li>
            <li>2 - Subtraction</li>
            <li>3 - Multiplication</li>
            <li>4 - Division</li>
            <li>5 - Exit</li>
        </ul>
    </li>
    <li>Prompt the user to choose an operation.</li>
    <li>Request two numbers from the user.</li>
    <li>Perform the selected operation and display the result.</li>
    <li>Handle division by zero (display an error message).</li>
    <li>After each operation, ask the user whether they wish to perform another operation.</li>
    <li>The programme must only terminate when the user selects the "Exit" option.</li>
</ul>

## Additional Challenge
<ul>
    <li>Add exponentiation and square root operations.</li>
</ul>

## Explanation

This exercise is divided into two different solution approaches.

<ul>
    <li>
        <strong>First Solution Approach (Without Using Libraries):</strong>
        <ul>
            <li>
                Two files:
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/main.py">main.py</a>
                and
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoes.py">functions.py</a>.
                This structure allows for improved organisation, readability, and simplicity.
            </li>
            <li>
                File
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/main.py">main.py</a>:
                <ul>
                    <li>Exercise specification.</li>
                    <li>Main programme structure.</li>
                </ul>
            </li>
            <li>
                File
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoes.py">functions.py</a>:
                <ul>
                    <li>Programme functions:
                        <ul>
                            <li><code>menu()</code></li>
                            <li><code>addition()</code></li>
                            <li><code>subtraction()</code></li>
                            <li><code>multiplication()</code></li>
                            <li><code>division()</code></li>
                            <li><code>exponentiation()</code></li>
                            <li><code>squareRoot()</code></li>
                            <li><code>ask2Numbers()</code></li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <strong>Second Solution Approach (Using the <code>math</code> library):</strong>
        <ul>
            <li>
                Two files:
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/mainBiblioteca.py">mainBiblioteca.py</a>
                and
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoesBiblioteca.py">funcoesBiblioteca.py</a>.
            </li>
            <li>
                File
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/mainBiblioteca.py">mainBiblioteca.py</a>:
                <ul>
                    <li>Exercise specification.</li>
                    <li>Main programme structure.</li>
                </ul>
            </li>
            <li>
                File
                <a href="https://github.com/fabiensantos/Python/blob/Calculadora-Simples/funcoesBiblioteca.py">funcoesBiblioteca.py</a>:
                <ul>
                    <li>Programme functions:
                        <ul>
                            <li><code>menu()</code></li>
                            <li><code>addition()</code></li>
                            <li><code>subtraction()</code></li>
                            <li><code>multiplication()</code></li>
                            <li><code>division()</code></li>
                            <li><code>exponentiation()</code></li>
                            <li><code>squareRoot()</code></li>
                            <li><code>ask2Numbers()</code></li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
