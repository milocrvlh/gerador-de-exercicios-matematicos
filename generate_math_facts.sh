#!/bin/bash

echo "Gerando Exercícios"
python generator.py

echo "Parafernalha do Latex "
latex exercicios.tex
dvipdfm exercicios.dvi
