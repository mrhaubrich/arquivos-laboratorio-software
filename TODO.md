# Funcionalidades

1. leitura de arquivo
2. extrair dados de cliente para a classe Cliente
3. extrair dados de pagamentos para a classe Pagamento
4. filtrar os lançamentos não pagos
5. apresentar clientes e suas dívidas

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
5. Apresentar clientes e suas dívidas
   1. Usamos os dados de clientes e pagamentos já em memória para apresentar clientes e suas dívidas.

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
4. Filtrar os lançamentos não pagos
   1. Dado que os dados de pagamentos estão vazio, a funcionalidade deve retornar uma lista vazia.
   2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
   3. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos não pagos.
5. Apresentar clientes e suas dívidas
   1. Dado que os dados de clientes e pagamentos estão vazios, a funcionalidade deve printar uma mensagem dizendo que não há clientes e pagamentos.
   2. Dado que os dados de clientes estão vazios e os pagamentos estão corretos, a funcionalidade deve printar uma mensagem dizendo que não há clientes.
   3. Dado que os dados de clientes estão corretos e os pagamentos estão vazios, a funcionalidade deve printar uma mensagem dizendo que não há pagamentos.
   4. Dado que os dados de clientes e pagamentos estão corretos, a funcionalidade deve printar os clientes e suas dívidas.

# Sprint
0. Implementar testes de aceitação
   - Complexidade 3
   - TED: 2 horas
1. Leitura do arquivo
   - Complexidade 1
   - TED: 10 minutos
2. Extrair dados de cliente para classe
   - Complexidade 5
   - TED: 15 minutos
3. Extrair dados de pagamentos para classe
   - Complexidade 5
   - TED: 15 minutos
4. Filtrar os lançamentos não pagos
   - Complexidade 2
   - TED: 1 minuto
5. Apresentar clientes e suas dívidas
   - Complexidade 1
   - TED: 1 minuto
