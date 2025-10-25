# Sistema de Agendamento de Consultas

## Configuração do Ambiente de Testes

### 1. Criar e Ativar Ambiente Virtual
```bash

python -m venv env

# Ativando ambiente virtual (Windows)
.\env\Scripts\activate
```

### 2. Instalar Dependências
```bash
# Instalar pytest e pytest-cov
pip install pytest pytest-cov
```

### 3. Estrutura do Projeto


### 4. Comandos para Executar Testes

#### Executar todos os testes
```bash
python -m pytest
```

#### Executar testes com relatório de cobertura
```bash
pytest --cov=src --cov-report=term-missing
```

#### Executar testes específicos
```bash
# Executar um arquivo de teste específico
pytest tests/test_paciente.py

# Executar um teste específico
pytest tests/test_paciente.py::test_criacao_paciente_valido
```

### 5. Verificar Versões
```bash
# Verificar versão do pytest
pytest --version

# Verificar todas as dependências instaladas
pip list
```

### 6. Configuração VS Code
1. Instale a extensão "Python" da Microsoft
2. Selecione o interpretador Python correto (do ambiente virtual)
3. Configure o Test Explorer para usar pytest

### Notas
- O arquivo `pytest.ini` já está configurado com as opções básicas
- A flag `-q` reduz a verbosidade da saída
- `--cov=src` indica a pasta para análise de cobertura
- `--cov-report=term-missing` mostra linhas não cobertas pelos testes