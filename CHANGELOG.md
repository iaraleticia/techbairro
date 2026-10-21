# CHANGELOG — TechBairro

## v3.3.0 (Aula 20)

### Adicionado
- Armazenamento temporário dos clientes em `clientes_na_tela`, mantendo a correspondência com os dados mostrados na Consulta.
- Criação da função `cliente_selecionado(acao)` para conferir se um cliente válido foi selecionado antes de executar uma ação.
- Notificação caso o cliente escolhido para exclusão não esteja mais cadastrado no banco de dados.
- Alteração do texto do botão para **Salvar edição** enquanto o usuário estiver modificando um cadastro.
- Opção de abrir os dados do cliente no formulário por meio de um duplo clique na Consulta.
- Mensagem informando claramente quando uma edição é cancelada.

### Corrigido
- As operações de editar e excluir utilizam os dados correspondentes à linha selecionada, evitando problemas causados por listas desatualizadas.
- A função de atualização agora confere o resultado de `atualizar()` antes de confirmar que a alteração foi realizada.
- A exclusão verifica o retorno de `remover()` e renova a lista quando o registro já não existe.
- As linhas usadas apenas para informar situações, como **Nenhum cliente cadastrado**, não são consideradas clientes selecionados.
- O botão retorna ao nome **Salvar** quando o formulário deixa de estar no modo de edição.