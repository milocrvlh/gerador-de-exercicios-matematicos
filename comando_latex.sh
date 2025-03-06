#!/bin/bash

echo "Gerando Exercícios"
python gerador.py

echo "Parafernalha do Latex "
latex exercicios.tex
dvipdfm exercicios.dvi
