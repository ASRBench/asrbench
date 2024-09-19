# 🎤 Benchmarks de Transcrição de Áudio para Texto

Este projeto faz parte de um TCC e é um protótipo para testar a transcrição de áudio para texto utilizando modelos de IA.

## 🛠️ Pré-requisitos

- 🐍 [Python ^3.12.5](https://www.python.org/downloads/)
- 📦 [Poetry](https://python-poetry.org/docs/#installation) (para gerenciar as dependências)

## ⚙️ Configuração do Projeto

Siga as instruções abaixo para configurar e executar o projeto localmente:

### 🔶 Clonar o Repositório

Primeiro, clone este repositório:

```shell
git clone https://github.com/usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 📥 Instalar as Dependências

Instale todas as dependências necessárias usando o Poetry:

```shell
poetry install
```

Isso criará um ambiente virtual e instalará todas as bibliotecas necessárias.

### 🚀 Executar o Projeto

Para rodar o script principal, utilize o Poetry para garantir que as dependências corretas sejam usadas:

```shell
poetry shell
poetry run python src/benchmark/main.py
```

A saida esperada seria algo como:

```
Lang: pt                Lang Accuracy: 93.0%
IA: FasterWhisper       Model Size: FasterWhisperSizeModels.Medium
Device: cpu             Compute Type: int8
Wer: 0.33               Accuracy: 67.0%
```

## 📁 Estrutura do Projeto

- **src/benchmark** - Pkg para executar os benchmarks.
- **src/benchmark/resources/audios** - Diretório dos arquivos de áudio de teste.
- **src/benchmark/resources/references** - Diretório dos arquivos de texto de referência (transcrições esperadas).
- **src/benchmark/main.py** - Script de benchmark principal que executa a transcrição de áudio.

- **src/report** - Pkg para a gereção de relatórios dos benchmarks.
- **src/report/templates** - Diretório dos templates html para gerar os relatórios.
