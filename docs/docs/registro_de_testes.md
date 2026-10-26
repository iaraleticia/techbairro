## Registro de testes da TechBairro
## Versão testada: 3.3.1 · Data: 26/10/2026 · Responsável: Iara

Sistema operacional e versão do Python: Windows · versão do Python a confirmar no computador

## ID	    Requisito	Passos e dados	                                           	                                                                  
CT01	    RF01	    Cadastrar um cliente com todos os campos certos.	                        
CT02	    RF01	    Salvar com Nome e Endereço vazios.	    	
CT03	    RF02	    Informar o telefone 61 9999 0000, com espaços.	         
CT04	    RF03	    Informar o e-mail ana@email, sem ponto no domínio.	     
CT05	    RF05	    Editar um cliente, trocar o telefone e salvar.	         
CT06	    RF06	    Excluir um cliente: responder Não e depois Sim.	


## Esperado               

Cliente cadastrado com sucesso e contador atualizado.
O sistema deve impedir o cadastro e informar que os campos obrigatórios precisam ser preenchidos.
O sistema deve validar o telefone conforme as regras definidas no projeto.
O sistema deve rejeitar o e-mail inválido e orientar o usuário.
O telefone deve ser atualizado e uma mensagem de sucesso deve ser exibida.
Ao responder Não, o cadastro deve permanecer. Ao responder Sim, o cliente deve ser excluído.

## Obtido
Cliente cadastrado com sucesso e contador atualizado.
Mensagem exibida: 'Preencha o (s) campo (s): Nome, Endereço' 
Mensagem exibida: 'Telefone inválido: use somente números.'
Mensagem exibida: 'E-mail inválido: use o formato nome@dominio.com'
Mensagem exibida: 'Cliente 'nome' atualizado com sucesso.'	
Cliente excluído da lista de consulta.

## Status 
Feito 
Feito
Feito
Feito
Feito
Feito

## Testes automáticos
Saída do `python testar_validacao.py`: ____

## Defeitos encontrados
Aparentemente nenhum defeito encontrado nos testes. (o que falhou, como foi corrigido e em qual commit; ou "nenhum")
