# Diagramas de Sequência

# Caso de Uso: Criar Sessão

View
↓
Controller
↓
Service
↓
Repository
↓
SQLite

Fluxo:
1. Usuário solicita criação da sessão
2. Controller recebe os dados
3. Service valida regras de negócio
4. Repository salva no banco
5. SQLite persiste os dados
6. Sistema retorna confirmação

<img width="636" height="360" alt="image" src="https://github.com/user-attachments/assets/5db43afe-3626-4925-8e06-d6e80c6fbb83" />


---

# Caso de Uso: Registrar Público

View
↓
Controller
↓
Service
↓
Repository
↓
SQLite

Fluxo:
1. Usuário informa público
2. Controller recebe os dados
3. Service valida capacidade
4. Repository atualiza sessão
5. SQLite salva alterações
6. Sistema retorna confirmação


<img width="636" height="354" alt="image" src="https://github.com/user-attachments/assets/630eaeea-c168-4897-9243-e601ae0b7d11" />
