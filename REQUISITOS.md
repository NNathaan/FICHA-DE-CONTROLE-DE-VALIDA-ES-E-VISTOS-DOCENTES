Regra Nº	Ação (tema)	Pista para você completar
RF01	Criar	Registrar um novo chamado. Quais dados o usuário                    informa?
RF02	Listar	Ver todos os chamados cadastrados.
RF03	Buscar	Achar um chamado específico. Por qual campo?
RF04	Atualizar	Mudar algo num chamado que já existe (o status, por exemplo).
RF05	Remover	Apagar um chamado.
RF06	Consultar o CEP	Ao informar um CEP, o sistema descobre a cidade sozinho pela internet.
# REQUISITOS - TechFlow Core

## Requisitos Funcionais (RF)
RF01: O sistema deve registrar um novo chamado, com o usuário informando título, solicitante, prioridade e CEP.
RF02: O sistema deve exibir todos os chamados cadastrados.
RF03: O sistema deve buscar um chamado específico pelo id.
RF04: O sistema deve permitir alterar o status de um chamado existente.
RF05: O sistema deve permitir excluir um chamado pelo id.
RF06: O sistema deve consultar o cep informado e preencher automaticamente a cidade do chamado.

## Requisitos Não Funcionais (RNF)
RNF01: O sistema deve usar somente bibliotecas padrão do Python, sem instalar programas que exijam permissão de administrador.
RNF02: Se o usuário digitar um dado inválido, o sistema não deve travar, e sim mostrar uma mensagem de erro.
RNF03: O código deve ser dividido em módulos, para que cada parte possa ser reaproveitada e testada separadamente.
RNF04: O código deve seguir o padrão PEP 8, usando nomes de variáveis em snake_case.
RNF05: O sistema não deve pedir nem guardar dados sensíveis do usuário, como CPF ou senha, porque o chamado só precisa de título, solicitante, prioridade e CEP.