Projeto Oficina -
Este projeto consiste em uma API para o gerenciamento de oficinas mecânicas, com foco em agendamento de serviços, controle de ordens de serviço e gestão de clientes. O sistema foi desenvolvido para modernizar processos operacionais, permitindo maior controle sobre o fluxo de trabalho e histórico de manutenções.

Funcionalidades
Gerenciamento de Clientes: Cadastro, edição e consulta de perfis de clientes.

Agendamento de Serviços: Sistema para solicitação e reserva de horários para manutenção.

Controle de Veículos: Registro de modelos vinculados a cada cliente, com foco em histórico técnico.

Ordens de Serviço (OS): Criação e acompanhamento do status de cada serviço realizado em tempo real.

Tecnologias Utilizadas
Linguagem: Python 

Framework: FastAPI 

Banco de Dados: PostgreSQL

Como Executar o Projeto
Pré-requisitos

Git instalado.

Passo a Passo
Clone o repositório:

Bash
git clone https://github.com/victorigarashi/projeto-oficina.git
cd projeto-oficina

Estrutura do Projeto
Plaintext
├── app/
│   ├── api/          # Endpoints da API
│   ├── core/         # Configurações globais e segurança
│   ├── models/       # Entidades e mapeamento de banco de dados
│   ├── schemas/      # Validação de dados e DTOs
│   └── services/     # Regras de negócio e lógica do sistema
└── requirements.txt
Desenvolvido por Victor Igarashi
