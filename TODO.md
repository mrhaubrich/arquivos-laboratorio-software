# Funcionalidades

1. leitura de arquivo
2. extrair dados de cliente para a classe Cliente
3. extrair dados de pagamentos para a classe Pagamento
4. filtrar os lançamentos não pagos
5. fltrar dívidas
6. agrupar dívidas por cliente
7. apresentar clientes e suas dívidas
8. Apresentar o valor já pago pelos clientes além do valor não pago

# Definição
- Pagamentos marcados como false (f) são valores devidos pelo cliente;
- Pagamentos marcados como true (t) são valores já pagos pelo cliente (MUST NOT).

# Histórias:
1. Leitura do arquivo:
   1. Começamos lendo o arquivo de clientes para a memória da aplicação.
   2. Em seguida, lemos o arquivo de pagamentos para a memória da aplicação.
2. Extrair dados de cliente para classe
   1. Usamos os dados de clientes já em memória para instanciar objetos que representam o cliente.
3. Extrair dados de pagamentos para classe
   1. Usamos os dados de pagamentos já em memória para instanciar objetos que representam o pagamento.
4. Filtrar os lançamentos não pagos
   1. Usamos os dados de pagamentos já em memória para filtrar os lançamentos não pagos.
5. Filtrar dívidas
   1. Usamos os dados de lançamentos não pagos para filtrar as dívidas.
   2. Relacionamos as dívidas com os clientes.
6. Agrupar dívidas por cliente
   1. Usamos os dados de dívidas já em memória para agrupar as dívidas por cliente.
7. Apresentar clientes e suas dívidas
   1. Usamos os dados de clientes e pagamentos já em memória para apresentar clientes e suas dívidas.
8. Apresentar o valor já pago pelos clientes além do valor não pago
   1. Usamos os dados de clientes e pagamentos já em memória para apresentar o valor já pago pelos clientes além do valor não pago.

# Testes de aceitação
1. Leitura do arquivo:
   1. Dado que o arquivo não existe, então a aplicação deve retornar um erro.
   2. Dado que o arquivo existe, então a aplicação deve retornar sucesso.
2. Extrair dados de cliente para classe
   1. Dado que os dados de clientes estão corretos, então a aplicação deve instanciar objetos que representam o cliente.
   2. Dado que os dados de clientes estão incorretos, então a aplicação deve retornar um erro.
   3. Dado que os dados de clientes estão vazios, então a aplicação deve retornar um erro.
   4. Dado que os dados de clientes estão nulos, então a aplicação deve retornar um erro.
3. Extrair dados de pagamentos para classe
   1. Dado que os dados de pagamentos estão corretos, então a aplicação deve instanciar objetos que representam o pagamento.
   2. Dado que os dados de pagamentos estão incorretos, então a aplicação deve retornar um erro.
   3. Dado que os dados de pagamentos estão vazios, então a aplicação deve retornar um erro.
   4. Dado que os dados de pagamentos estão nulos, então a aplicação deve retornar um erro.
   5. Dado que a data do pagamento está incorreta, então a aplicação deve retornar um erro.
   6. Dado que o cliente do pagamento não existe, então a aplicação deve retornar um erro.
4. Filtrar os lançamentos não pagos
   1. Dado que os dados de pagamentos estão vazio, a funcionalidade deve retornar uma lista vazia.
   2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
   3. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos não pagos.
5. Filtrar cliente pelo ID
   1. Dado que o ID do cliente não existe, a funcionalidade deve retornar um erro.
   2. Dado que o ID do cliente existe, a funcionalidade deve retornar o cliente.
   3. Dado que o ID do cliente está vazio, a funcionalidade deve retornar um erro.
   4. Dado que o ID do cliente está nulo, a funcionalidade deve retornar um erro.
6. Filtrar dívidas
   1. Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia.
   2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
   3. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de dívidas.
7. Agrupar dívidas por cliente
   1. Dado que os dados de dívidas estão vazios, a funcionalidade deve retornar uma lista vazia.
   2. Dado que os dados de dívidas estão nulos, a funcionalidade deve retornar um erro.
   3. Dado que os dados de dívidas estão corretos, a funcionalidade deve retornar uma lista de dívidas agrupadas por cliente.
8. Filtrar pagamentos já pagos além do valor não pago
   1. Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia.
   2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
   3. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos já pagos além do valor não pago.

# Sprint
0. Implementar testes de aceitação
   - Complexidade 40
   - TED: 2 horas
1. Leitura do arquivo
   - Complexidade 0.5
   - TED: 10 minutos
2. Extrair dados de cliente para classe
   - Complexidade 13
   - TED: 15 minutos
3. Extrair dados de pagamentos para classe
   - Complexidade 13
   - TED: 15 minutos
4. Filtrar os lançamentos não pagos
   - Complexidade 3
   - TED: 1 minuto
5. Filtrar dividas
   - Complexidade 3
   - TED: 1 minuto
6. Agrupar dividas por cliente
   - Complexidade 20
   - TED: 5 minutos
7. Apresentar clientes e suas dívidas
   - Complexidade 3
   - TED: 1 minuto
8. Apresentar o valor já pago pelos clientes além do valor não pago
   - Complexidade 3
   - TED: 1 minuto e 30 segundos e 28 milissegundos
