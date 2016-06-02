LATEXMK = latexmk  -f -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make

.PHONY: all view clean

all : tcc.pdf

clean :
	find . \
		-iregex '.*\.\(aux\|bbl\|blg\|dvi\|lof\|loq\|log\|lot\|backup\|toc\|pdf\|brf\|ps\|fdb_latexmk\|fls\|glo\|idx\|ilg\|ind\|out\)' \
		! -path '*/dist*'\
		! -path '*/referencias*' \
		! -path '*/.git*' \
		-exec rm -rf {} +

view :
	xdg-open tcc.pdf

tcc.pdf : tcc.tex
	$(LATEXMK) tcc.tex
