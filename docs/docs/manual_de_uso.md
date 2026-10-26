# Manual de Uso do Sistema TechBairro

## 1. Como iniciar o sistema

1. Abra o projeto TechBairro no Visual Studio Code.
2. Verifique se os arquivos necessários para o funcionamento do sistema estão na pasta do projeto.
3. No menu superior, clique em **Terminal** e depois em **Novo Terminal**.
4. Digite o comando para executar o arquivo principal do sistema. Caso o arquivo utilizado seja `techbairro_v15.py`, digite `python techbairro_v15.py`.
5. Pressione Enter e aguarde a abertura da janela de cadastro de clientes.

## 2. Como cadastrar um cliente

1. Na janela principal, localize os campos destinados às informações do cliente.
2. Preencha o campo **Nome** com o nome completo da pessoa.
3. Informe o número de telefone no campo **Telefone**.
4. Digite o endereço de e-mail no campo **E-mail**.
5. Preencha o campo **Endereço** com o endereço do cliente.
6. Confira se todas as informações foram preenchidas corretamente.
7. Clique no botão de salvar para registrar o cadastro.
8. Verifique a mensagem apresentada pelo sistema para confirmar se o cadastro foi realizado ou se é necessário corrigir alguma informação.

## 3. Como consultar os clientes

1. Na janela principal, clique no botão **Consultar** ou na opção correspondente.
2. Aguarde a abertura da janela de consulta.
3. Observe a lista de clientes cadastrados.
4. Localize o cliente que deseja consultar.
5. Clique sobre o nome correspondente para selecionar o cadastro.
6. Confira as informações apresentadas na tela antes de realizar qualquer alteração.

## 4. Como editar um cadastro

1. Abra a janela de consulta e localize o cliente que deseja modificar.
2. Selecione o cadastro correto.
3. Clique no botão **Editar selecionado**.
4. Verifique se as informações do cliente foram carregadas no formulário.
5. Altere os campos necessários, como telefone, e-mail ou endereço.
6. Confira os dados atualizados e clique em **Salvar edição**.
7. Aguarde a mensagem de confirmação.
8. Consulte novamente o cadastro para verificar se as alterações foram salvas corretamente.

## 5. Como cancelar uma edição

1. Selecione o cliente que deseja editar e clique em **Editar selecionado**.
2. Faça as alterações necessárias no formulário.
3. Caso não queira continuar, clique no botão **Cancelar**.
4. Verifique a mensagem informando que a edição foi cancelada ou que o formulário foi limpo.
5. Consulte novamente o cadastro para confirmar que as alterações não foram salvas.

## 6. Como excluir um cliente

1. Abra a janela de consulta e localize o cliente que deseja excluir.
2. Selecione o cadastro correto.
3. Confira o nome do cliente selecionado para evitar excluir outra pessoa por engano.
4. Clique no botão **Excluir selecionado**.
5. Leia a mensagem de confirmação apresentada pelo sistema.
6. Se desejar concluir a exclusão, clique em **Sim**. Caso queira manter o cadastro, clique em **Não**.
7. Após confirmar a exclusão, verifique se o cliente foi removido da lista.
8. Se cancelar a operação, confirme que o cadastro continua disponível.

**Importante:** antes de confirmar uma exclusão, verifique cuidadosamente o nome do cliente selecionado, pois essa operação pode remover permanentemente o cadastro do banco de dados.

## 7. Como verificar se as operações foram realizadas corretamente

1. Após cadastrar, editar ou excluir um cliente, observe a mensagem apresentada pelo sistema.
2. Confira se a mensagem corresponde à operação realizada.
3. Abra a consulta para verificar se os dados estão atualizados.
4. Caso apareça uma mensagem de erro, leia as orientações apresentadas na tela.
5. Se necessário, consulte o terminal do Visual Studio Code para verificar se foram exibidas informações sobre o problema.

## 8. Como encerrar o sistema

1. Finalize as operações que estiver realizando.
2. Feche a janela de consulta, caso esteja aberta.
3. Feche a janela principal do TechBairro.
4. Certifique-se de que nenhuma operação esteja em andamento antes de encerrar o programa.

## 9. Armazenamento e segurança dos dados

O TechBairro utiliza o SQLite para armazenar os cadastros no arquivo `techbairro.db`. As informações permanecem salvas nesse arquivo para que possam ser consultadas novamente quando o sistema for aberto.

Para preservar os dados, recomenda-se realizar cópias de segurança regularmente. Antes de copiar o banco de dados, feche o sistema e armazene uma cópia do arquivo em um local seguro.

O arquivo do banco de dados não deve ser enviado ao GitHub quando contiver informações pessoais de clientes, pois esses dados precisam ser protegidos. Por esse motivo, o arquivo `techbairro.db` deve ser incluído no `.gitignore`.

## 10. Considerações finais

O TechBairro foi desenvolvido para facilitar o cadastro e a organização das informações dos clientes. Para utilizar o sistema corretamente, é importante preencher os campos com atenção, conferir os dados antes de salvar e verificar o cadastro selecionado antes de realizar alterações ou exclusões.