## Manual de uso da TechBairro

## A tela principal
A janela principal do sistema TechBairro permite cadastrar, consultar, alterar e excluir clientes. Nela, aparecem os campos para preencher o nome, telefone, e-mail e endereço do cliente, além dos botões para salvar os dados e realizar outras operações. A tela também apresenta mensagens de orientação e um contador que informa a quantidade de clientes cadastrados.

## Cadastrar um cliente
1. Abra o sistema TechBairro.
2. Preencha os campos com o nome, telefone, e-mail e endereço do cliente.
3. Confira se todas as informações foram preenchidas corretamente.
4. Clique no botão Salvar para registrar o cliente.
5. Verifique a mensagem exibida na tela para confirmar se o cadastro foi realizado com sucesso.
6. Observe se o contador de clientes cadastrados foi atualizado.

## Consultar os clientes cadastrados
1. Na tela principal, clique no botão Consultar clientes para abrir a janela de consulta.
2. Observe a lista de clientes cadastrados no sistema.
3. Localize o cliente desejado pelo nome e selecione sua linha na lista.
4. Confira os dados apresentados para identificar o cadastro correto.
5. Abra novamente a consulta, quando necessário, para verificar os registros disponíveis.

## Alterar os dados de um cliente
1. Abra a janela de consulta dos clientes cadastrados.
2. Selecione na lista o cliente que deseja alterar.
3. Clique no botão Editar selecionado para carregar os dados no formulário principal.
4. Modifique as informações necessárias, como nome, telefone, e-mail ou endereço.
5. Observe que o botão Salvar será alterado para Salvar edição, indicando que o sistema está no modo de edição.
6. Confira os dados e clique em Salvar edição para confirmar as alterações.
7. Verifique a mensagem exibida na tela para confirmar se a atualização foi realizada corretamente.
8. Caso não queira continuar, clique em Cancelar antes de salvar as mudanças.

## Excluir um cliente
1. Abra a janela de consulta dos clientes cadastrados.
2. Localize e selecione o cliente que deseja excluir.
3. Clique no botão Excluir selecionado.
4. Leia a mensagem de confirmação e confira o nome do cliente que será excluído.
5. Se desejar continuar, clique em Sim. Caso contrário, clique em Não para cancelar a operação.
6. Verifique a mensagem apresentada pelo sistema.
7. Confira se o cliente foi removido da lista e se o contador foi atualizado.

## Regras de preenchimento
Campo	Obrigatório?	Regra
Nome	 Sim	        Informe o nome completo do cliente, utilizando letras e espaços.
Telefone Sim	        Informe um número de telefone válido para contato.
E-mail	 Sim	        Informe um endereço de e-mail válido, com nome de usuário, @ e domínio.
Endereço Sim	        Informe o endereço do cliente, incluindo rua, número e outras informações necessárias.

## Mensagens do sistema
Mensagem	                               O que significa	                                                O que fazer
Cliente cadastrado com sucesso!	           cadastro foi realizado corretamente.                             Confira os dados e verifique o contador de clientes.
Cliente atualizado com sucesso!	           As alterações foram salvas.	                                    Confira se as informações foram atualizadas corretamente.
Cliente excluído com sucesso!	           O cadastro foi removido do sistema.	                            Verifique se o cliente não aparece mais na lista.
Nenhum cliente cadastrado ainda.           Não há clientes registrados no sistema.	                        Cadastre um cliente para começar a utilizar o sistema.
Cliente não encontrado para atualização.   O sistema não encontrou o cadastro que deveria ser alterado. 	Consulte novamente os clientes e confira se o registro ainda existe.
Selecione um cliente.	                   Nenhum cliente foi selecionado para a operação.	                Selecione um cliente na lista antes de editar ou excluir.

## Observação: 
## Dúvidas frequentes
## O que fazer quando não consigo cadastrar um cliente?

Confira se todos os campos obrigatórios foram preenchidos corretamente e corrija as informações, caso necessário. Depois, tente salvar novamente.

Como faço para alterar um cadastro?

Abra a consulta, selecione o cliente desejado e clique em Editar selecionado. Faça as alterações e clique em Salvar edição.

É possível cancelar uma alteração?

Sim. Clique em Cancelar antes de salvar as mudanças para interromper a edição sem confirmar as alterações.

Como evitar excluir o cliente errado?

Selecione o cliente correto e confira o nome apresentado na mensagem de confirmação antes de clicar em Sim.

O que acontece quando clico em Não na confirmação de exclusão?

A exclusão é cancelada, e o cadastro do cliente deve permanecer no sistema.

Os clientes continuam cadastrados quando fecho o programa?

Sim. Os dados são armazenados em um banco de dados SQLite, permitindo que os cadastros sejam recuperados quando o sistema for aberto novamente, desde que o banco de dados seja mantido no local correto.

Importante: antes de alterar ou excluir um cadastro, confira se selecionou o cliente correto. Isso ajuda a evitar modificações ou exclusões indevidas.