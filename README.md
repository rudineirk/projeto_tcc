# Projeto de TCC de Rudinei Goi Roecker

Versões pré-compiladas do projeto são mantidas em [dist/](dist).

Para compilar a partir dos fontes, é necessário a instalação do LaTeX.

Para instalar no Ubuntu e derivados use o comando abaixo:

```sh
sudo apt-get install texlive-full latexmk make
```

Para instalar no Fedora use o comando abaixo:

```sh
sudo dnf install texlive-scheme-full latexmk make
# ou
sudo yum install texlive-scheme-full latexmk make
```

depois rode o script de compilação

```sh
make clean
make
```

Para visualizar use o comando abaixo:

```sh
make view
```
