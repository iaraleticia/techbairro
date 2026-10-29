# TechBairro

O TechBairro é um sistema de cadastro de clientes desenvolvido em Python com Tkinter e SQLite. Ele permite cadastrar, consultar, editar e excluir clientes, facilitando a organização das informações.

**Versão atual:** 3.3.2· Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastro de clientes com nome, telefone, e-mail e endereço.
- Consulta, edição e exclusão de clientes com confirmação e validação dos dados.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows |
| Python | Python 3 (versão testada: 3.3.2 ) |
| Tkinter | Necessário para a interface gráfica |
| Bibliotecas externas | Nenhuma além das dependências instaladas no projeto |
| Internet | Necessária para baixar o projeto, não para utilizar o sistema localmente |

## Instalação

1. Baixe ou clone o repositório do TechBairro.
2. Abra o terminal na pasta principal do projeto.
3. Execute o arquivo Python principal para iniciar o sistema.

## Configuração do banco de dados

O banco de dados `techbairro.db` é criado automaticamente pelo sistema quando necessário. O caminho do banco pode ser conferido no código ou na mensagem exibida no terminal, caso esteja habilitada. Esse arquivo não deve ser enviado ao GitHub porque pode armazenar dados pessoais dos clientes. Para fazer uma cópia de segurança, feche o sistema e copie o arquivo `techbairro.db` para um local seguro.

## Como usar
O passo a passo está no [Manual de uso](docs/manual_de_uso.md).


## Estrutura do projeto

- `__pycache__/`: armazena arquivos temporários gerados pelo Python.
- `dist/`: pasta destinada aos arquivos de distribuição do sistema.
- `docs/`: reúne a documentação, os registros das aulas, a modelagem do banco de dados, os testes e as verificações.
- `scripts/`: contém scripts auxiliares p.ara gerar pacotes, importar planilhas e verificar o banco de dados.
- `scripts/gerar_pacote.py`: gera o pacote de distribuição do projeto.
- `scripts/importar_planilha_aba...`: script relacionado à importação de dados de planilhas.
- `scripts/techbairro.db`: arquivo de banco de dados presente na pasta de scripts.
- `scripts/travar_banco.py`: script de teste relacionado ao bloqueio do banco de dados.
- `scripts/verificar_banco.py`: verifica o banco de dados.
- `.gitignore`: define os arquivos e pastas que não devem ser enviados ao Git.
- `CHANGELOG.md`: registra as mudanças realizadas nas versões do sistema.
- `cliente.py`: contém a classe que representa os clientes.
- `COMO_EXECUTAR.txt`: apresenta instruções para executar o sistema.
- `README.md`: apresenta as informações gerais e as instruções do projeto.
- `TechBairro_3.3.1...`: arquivo relacionado à versão ou ao pacote do sistema.
- `TechBairro_backup_3...`: arquivo de backup do projeto.
- `techbairro_v15.py`: arquivo principal do sistema.
- `techbairro.db`: banco de dados local dos clientes.
- `testar_validacao.py`: executa testes das regras de validação.
- `validacao.py`: contém a classe `ValidadorCliente`, responsável por validar os dados dos clientes.


## Autor

Nome: Iara Letícia  
Curso: Téccnico em Desenvolvimento de Sistemas  
Instituição: Senac Ennius Muniz - Setor Comercial Sul .
