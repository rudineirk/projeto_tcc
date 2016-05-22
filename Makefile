LATEXMK = latexmk  -f -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make

.PHONY: all view clean

all : tcc.pdf

clean :
	rm -rf build/ *.aux *.bbl *.blg *.dvi *.lof *.log *.lot *.backup *.toc *.pdf *.brf *.ps

view :
	xdg-open tcc.pdf

tcc.pdf : tcc.tex
	$(LATEXMK) tcc.tex
