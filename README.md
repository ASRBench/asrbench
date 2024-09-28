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

Para rodar o módulo de benchmark principal, utilize o Poetry para garantir que as dependências corretas sejam usadas:

```shell
poetry shell
poetry run python main.py
```

## 📁 Estrutura do Projeto

- **benchmark** - Pkg para executar os benchmarks.
- **benchmark/resources/audios** - Diretório dos arquivos de áudio de teste.
- **benchmark/resources/references** - Diretório dos arquivos de texto de referência (transcrições esperadas).
- **main_dataset_benchmark.py** - Módulo de benchmark principal que executa a transcrição de áudio.
