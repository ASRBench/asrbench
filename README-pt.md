[:us: American English Version](./README.md)

# ASRBench
### Avalie, compare e encontre o melhor modelo para transcrição de áudio.

## Índice
- [ASRBench](#asrbench)
    - [Avalie, compare e encontre o melhor modelo para transcrição de áudio.](#avalie-compare-e-encontre-o-melhor-modelo-para-transcrição-de-áudio)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Instalação](#instalação)
  - [Uso](#uso)
  - [Contribuição](#contribuição)
  - [Sobre](#sobre)
  - [Licença](#licença)

## Introdução
ASRBench é um framework desenvolvido em Python para criar e executar benchmarks de sistemas para transcrição de áudio.
Ele permite que pesquisadores e desenvolvedores comparem diferentes sistemas de transcrição em termos de acurácia,
desempenho e utilização de recursos.

## Instalação
Para instalar o ASRBench, você só precisa do [Python 3.12+](https://www.python.org/downloads/) e do pip. Use o
comando abaixo para instalar a versão mais recente:

```sh
pip install asrbench
```

## Uso
O ASRBench permite configurar e executar o benchmark usando um arquivo de configuração YAML. Essa abordagem facilita o
processo de configuração do ambiente de benchmark, permitindo ao usuário definir os datasets, transcritores e parâmetros
de saída de forma simples e declarativa. Para mais detalhes sobre a estrutura do arquivo de configuração, acesse a
[documentação - en](https://asrbench.github.io/asrbench/configuration).

Abaixo está um exemplo de estrutura do arquivo de configuração:

```yaml
# configuração da saída de dados
output:
  type: "csv"
  dir: "./results"
  filename: "example_filename"

# configuração dos datasets
datasets:
  dataset1:
    audio_dir: "resources/common_voice_05/wav"
    reference_dir: "resources/common_voice_05/txt"

# configuração dos sistema de transcrição
transcribers:
  faster_whisper_medium_int8:
    asr: "faster_whisper"
    model: "medium"
    compute_type: "int8"
    device: "cpu"
    beam_size: 5
    language: "pt"  
```

Com o arquivo de configuração pronto, basta criar um script Python para ler o arquivo e montar o ambiente do benchmark.
Veja um exemplo abaixo:

```python
from asrbench.config_loader import ConfigLoader

loader = ConfigLoader("path/to/configfile.yml")
benchmark = loader.set_up_benchmark()
benchmark.run()
```

Se você também deseja gerar um relatório em PDF a partir dos dados gerados no benchmark, basta adicionar o seguinte
trecho de código:

```python
from asrbench.report.report_template import DefaultReport
from asrbench.report.input_ import CsvInput
...

output_path = benchmark.run()
report = DefaultReport(CsvInput(output_filepath))
report.generate_report()

```

Caso prefira uma solução mais direta e simplificada, você pode conferir a [asrbench-cli](https://github.com/ASRBench/asrbench-cli).

## Contribuição
Se você deseja contribuir para o ASRBench, consulte [CONTRIBUTING.md](./CONTRIBUTING.md) para informações sobre como 
configurar o ambiente de desenvolvimento e as dependências necessárias. As principais ferramentas de desenvolvimento 
estão definidas no arquivo [pyproject.toml](./pyproject.toml) e são gerenciadas com [Poetry](https://python-poetry.org/docs/#installation).

## Sobre
O ASRBench foi desenvolvido como parte de um Trabalho de Conclusão de Curso (TCC) para explorar e avaliar a eficiência
de modelos de transcrição de áudio. O projeto acadêmico oferece uma análise detalhada do desenvolvimento do framework,
além dos desafios e resultados obtidos ao longo da pesquisa. Para mais informações, consulte o [TCC](https://repositorio.animaeducacao.com.br/handle/ANIMA/48443).

## Licença
Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.

[Ir para o topo](#índice)
