# 🧮 Gerador e Validador de CPF em Python

Projeto desenvolvido em **Python**, utilizando apenas conceitos fundamentais da linguagem como:

- ✅ Variáveis  
- ✅ Estruturas condicionais (`if / else`)  
- ✅ Laços de repetição (`for`, `while`)  
- ✅ Listas  
- ✅ Manipulação de strings  
- ✅ Operadores matemáticos  

---

## 📌 Sobre o Projeto

Este projeto contém dois scripts:

📂 **Gerador_CPF.py**  
Gera um CPF aleatório e válido automaticamente, calculando corretamente os dois dígitos verificadores.

📂 **Validador_CPF.py**  
Valida um CPF informado pelo usuário, verificando:
- Se não é uma sequência repetida (ex: 11111111111)
- Se os dígitos verificadores estão corretos

---

## 🧠 Como Funciona o Algoritmo

O cálculo do CPF segue as regras oficiais:

1. Geração dos 9 primeiros dígitos aleatórios (no gerador)
2. Cálculo do 1º dígito verificador:
   - Multiplicação regressiva (10 → 2)
   - Soma dos resultados
   - `(soma × 10) % 11`
3. Cálculo do 2º dígito verificador:
   - Multiplicação regressiva (11 → 2)
   - Mesmo processo matemático

Se o resto for maior que 9, o dígito é definido como **0**.

---

## 🎯 Objetivo

Projeto criado com foco em **praticar lógica de programação e fundamentos do Python**, sem uso de bibliotecas externas ou funções avançadas.

---

## 🚀 Possíveis Melhorias Futuras

- Transformar em funções reutilizáveis
- Criar interface gráfica
- Criar API com Flask/FastAPI
- Adicionar testes automatizados
- Transformar em pacote instalável

---

## 👨‍💻 Guilherme Ribeiro Amorim

